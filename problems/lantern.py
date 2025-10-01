from enum import Enum, auto
from dataclasses import dataclass
import logging
from typing import Callable, Iterable, Optional

logger = logging.getLogger(__name__)

# ---------- Exceptions ----------
class InvalidTransition(Exception):
    pass

class Forbidden(Exception):
    pass

# `require` lives ONLY here and is used ONLY inside _transition()
def require(cond: bool, exc: Exception):
    if not cond:
        raise exc

# ---------- Roles ----------
class Role(Enum):
    AUTHOR = auto()
    REVIEWER = auto()
    APPROVER = auto()

@dataclass  # roles mutable if you need promotions
class User:
    user_id: str
    name: str
    role: Role

# ---------- States ----------
class State(Enum):
    DRAFT = auto()
    SUBMITTED = auto()
    UNDER_REVIEW = auto()
    APPROVED = auto()
    REJECTED = auto()

# ---------- Actions ----------
class Action(Enum):
    SUBMIT = auto()
    START_REVIEW = auto()
    REQUEST_CHANGES = auto()  # sends doc back to DRAFT
    APPROVE = auto()
    REJECT = auto()
    COMMENT = auto()          # no state change

# A transition spec declares who can do what from which states to which next state
Guard = Callable[["Document", User], bool]

@dataclass(frozen=True)
class TransitionSpec:
    from_states: frozenset[State]
    to_state: Optional[State]            # None = no state change (e.g., COMMENT)
    roles: frozenset[Role]
    guard: Optional[Guard] = None        # extra predicate (e.g., "only the author")

# ---------- Document ----------
class Document:
    def __init__(self, *, author: User, state: State = State.DRAFT, approvers = []):
        if author.role != Role.AUTHOR:
            raise Forbidden("only authors can create documents")
        self.author_id = author.user_id
        self.state = state
        self.comments: list[tuple[str, str]] = []  # (user_id, text)
        self.approver_ind = 0
        self.approvers = approvers

    # central transition: validates role + state + guard using `require`
    def _transition(self, *, action: Action, user: User, comment_text: str | None = None):
        spec = TRANSITIONS.get(action)
        require(spec is not None, InvalidTransition(f"unknown action {action}"))

        require(self.state in spec.from_states,
                InvalidTransition(f"{action.name} not allowed from {self.state.name}"))

        require(user.role in spec.roles,
                Forbidden(f"{action.name.lower()} requires roles {sorted(r.name for r in spec.roles)}"))

        if spec.guard is not None:
            require(spec.guard(self, user), Forbidden(f"{action.name.lower()} failed guard"))

        # side effect for comments
        if action is Action.COMMENT and comment_text:
            self.comments.append((user.user_id, comment_text))

        # move state if needed
        if spec.to_state is not None:
            logger.info("Transition: %s --%s--> %s", self.state.name, action.name, spec.to_state.name)
            self.state = spec.to_state
        else:
            logger.info("Action without state change: %s on %s", action.name, self.state.name)

    # thin action wrappers that do no checks themselves
    def submit(self, user: User):
        self._transition(action=Action.SUBMIT, user=user)

    def start_review(self, user: User):
        self._transition(action=Action.START_REVIEW, user=user)

    def request_changes(self, user: User, comment: str | None = None):
        self._transition(action=Action.REQUEST_CHANGES, user=user, comment_text=comment)

    def approve(self, user: User):
        self._transition(action=Action.APPROVE, user=user)

    def reject(self, user: User):
        self._transition(action=Action.REJECT, user=user)

    def comment(self, user: User, text: str):
        self._transition(action=Action.COMMENT, user=user, comment_text=text)

    def __repr__(self):
        return f"<Document state={self.state.name} comments={len(self.comments)}>"

# ---------- Transition table ----------
def _is_author(doc: Document, user: User) -> bool:
    return user.user_id == doc.author_id

def _is_approved(doc: Document, user: User) -> bool:
    return doc.approver_ind < len(doc.approvers)


TRANSITIONS: dict[Action, TransitionSpec] = {
    Action.SUBMIT: TransitionSpec(
        from_states=frozenset({State.DRAFT}),
        to_state=State.SUBMITTED,
        roles=frozenset({Role.AUTHOR}),
        guard=_is_author,  # only the creating author may submit
    ),
    Action.START_REVIEW: TransitionSpec(
        from_states=frozenset({State.SUBMITTED}),
        to_state=State.UNDER_REVIEW,
        roles=frozenset({Role.REVIEWER}),
    ),
    Action.REQUEST_CHANGES: TransitionSpec(
        from_states=frozenset({State.UNDER_REVIEW}),
        to_state=State.DRAFT,  # back to DRAFT per your instruction
        roles=frozenset({Role.REVIEWER}),
    ),
    Action.APPROVE: TransitionSpec(
        from_states=frozenset({State.UNDER_REVIEW}),
        to_state=State.APPROVED,
        roles=frozenset({Role.APPROVER}),
        guard=_is_approved,
    ),
    Action.SINGLE_APPROVER: TransitionSpec(
        from_states=frozenset({State.UNDER_REVIEW}),
        to_state=State.UNDER_REVIEW,
        roles=frozenset({Role.APPROVER})
    ),
    Action.REJECT: TransitionSpec(
        from_states=frozenset({State.SUBMITTED, State.UNDER_REVIEW}),
        to_state=State.REJECTED,
        roles=frozenset({Role.APPROVER}),
        # check that only the person who is supposed to be reviewing can reject
    ),
    Action.COMMENT: TransitionSpec(
        from_states=frozenset({State.SUBMITTED, State.UNDER_REVIEW}),
        to_state=None,  # no state change
        roles=frozenset({Role.REVIEWER}),
    ),
}

# ---------- demo ----------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")

    author = User("u1", "Alice", Role.AUTHOR)
    reviewer = User("u2", "Ravi", Role.REVIEWER)
    approver = User("u3", "Ava", Role.APPROVER)

    doc = Document(author=author)            # DRAFT
    doc.submit(author)                       # SUBMITTED
    doc.start_review(reviewer)               # UNDER_REVIEW
    doc.comment(reviewer, "nit: fix header")
    doc.request_changes(reviewer, "add summary")  # -> DRAFT
    doc.submit(author)                       # SUBMITTED
    doc.start_review(reviewer)               # UNDER_REVIEW
    doc.approve(approver)                    # APPROVED

    # negative path samples
    try:
        doc2 = Document(author=author)
        doc2.approve(approver)
    except InvalidTransition:
        logger.exception("Invalid transition caught")

    try:
        doc3 = Document(author=author)
        doc3.submit(reviewer)                # wrong role
    except Forbidden:
        logger.exception("Forbidden action caught")