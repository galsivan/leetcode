# copilot-instructions for leetcode repository

This repository contains many individual LeetCode problem folders. Each folder typically includes:
- a `README.md` describing the problem and examples
- one or more solution files (`*.py`) that define either `class Solution` or small helper classes (e.g. `MinStack`)

Quick big-picture
- The project is a collection of independent problem solutions — there's no central application or build system.
- Solutions are standalone Python snippets. Tests are not present; running is usually done by copying code into LeetCode or running small ad-hoc scripts.

What to do as an AI coding agent
- Make minimal, local, single-file edits unless a change clearly affects multiple problems.
- Preserve the pattern: top-level `class Solution` with typed method signatures. Many files omit imports (e.g. `List`, `Optional`, `collections`) — only add imports when needed for local execution or clarity.
- Use the folder `README.md` as canonical problem description and examples. Refer to it when writing or verifying examples.

Examples from this repo
- `1-two-sum/two-sum.py`: returns indices using a hash map, defined inside `class Solution`.
- `102-binary-tree-level-order-traversal/binary-tree-level-order-traversal.py`: uses commented `TreeNode` definition pattern and `collections.deque`.

Conventions discovered
- Prefer simple, idiomatic Python (lists, dicts, deques). Keep solutions concise and LeetCode-style.
- When a file uses types like `List`, `Optional`, or `TreeNode` without imports, assume they match LeetCode's environment; add `from typing import ...` only if you need to run the file locally.

Developer workflows (how to run locally)
- There is no project-level test runner. To run a specific solution locally:
  1. Add missing imports at top (e.g. `from typing import List, Optional`, `import collections`).
  2. Add a small `if __name__ == "__main__":` block that constructs inputs and calls the class/method.
Example quick-run (add to a file):
```
from typing import List
if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15], 9))
```

Scope and limits for edits
- Avoid introducing project-wide tools (CI, test frameworks) unless requested. Keep changes low-risk and localized.
- Don't invent external integrations. The repo has no dependency manifest (`requirements.txt` / `pyproject.toml`) — add one only when you add external packages.

References (important files)
- Root `README.md` — repo title
- Per-problem `README.md` — canonical problem statement (e.g. `1-two-sum/README.md`)
- Representative solution files: `1-two-sum/two-sum.py`, `102-binary-tree-level-order-traversal/binary-tree-level-order-traversal.py`, `155-min-stack/min-stack.py`

When in doubt
- Follow existing file structure and naming. Prefer minimal, readable fixes. If you need to run code, add imports and a `__main__` guard rather than changing APIs.

If you want me to expand or merge content from another guidance file, point me to it and I'll integrate.
