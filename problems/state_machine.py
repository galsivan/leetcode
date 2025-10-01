from dataclasses import dataclass
from enum import Enum
from typing import Protocol

class ResultKind(Enum): SUCCESS=1; TRANSIENT=2; PERMANENT=3

class StepState(str, Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    SUCCESS = 'success'
    TRANSIENT = 'transient'
    PERMANENT = 'permanent'
    CANCELED = 'canceled'

@dataclass
class StepSpec:
    id: str
    deps: list[str]
    retries: int = 0
    timeout_ms: int = 5000
    initial_state: StepState = StepState.PENDING

class RunFn(Protocol):
    def __call__(self, step_id: str) -> tuple[ResultKind, dict]:
        return ResultKind.SUCCESS, {'output': 'ok'}

class Engine:
    def __init__(self, run_fns: dict[str, RunFn], max_workers: int = 4):
        self.run_fns = run_fns
        self.max_workers = max_workers
        self.workflows = {}  # wf_id -> {step_id -> state}
        
    def submit(self, wf_id: str, steps: list[StepSpec]) -> None:
        self.workflows[wf_id] = {step.id: StepState.PENDING for step in steps}

    def tick(self) -> None:  # advance state machine one scheduling cycle
        for wf_id, states in self.workflows.items():
            for step_id, state in states.items():
                if state == StepState.PENDING:
                    result = self.run_fns[step_id](step_id)
                    self.workflows[wf_id][step_id] = result

    def get_workflow(self, wf_id: str) -> dict:  # states per step + overall
        return self.workflows.get(wf_id, {})

    def cancel(self, wf_id: str) -> None:
        self.workflows.pop(wf_id, None)

