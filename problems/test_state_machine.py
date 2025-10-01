import os
import sys
import pytest

ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from problems.state_machine import Engine, StepSpec, ResultKind, StepState


def test_happy_path_and_run_results():
    called = []
    def run_fn(step_id: str):
        called.append(step_id)
        return (ResultKind.SUCCESS, {"output": step_id + "-done"})

    run_fns = {"s1": run_fn, "s2": run_fn}
    engine = Engine(run_fns)

    steps = [StepSpec(id="s1", deps=[]), StepSpec(id="s2", deps=[])]
    engine.submit("wf1", steps)

    assert engine.get_workflow("wf1") == {"s1": StepState.PENDING, "s2": StepState.PENDING}

    engine.tick()

    wf = engine.get_workflow("wf1")
    # after one tick, each step should have been executed and replaced by tuple result
    assert isinstance(wf["s1"], tuple)
    assert wf["s1"][0] == ResultKind.SUCCESS
    assert wf["s1"][1]["output"] == "s1-done"
    assert wf["s2"][1]["output"] == "s2-done"
    assert set(called) == {"s1", "s2"}


def test_cancel_removes_workflow():
    def run_fn(step_id: str):
        return (ResultKind.TRANSIENT, {})

    run_fns = {"a": run_fn}
    engine = Engine(run_fns)
    engine.submit("wf2", [StepSpec(id="a", deps=[])])
    wf = engine.get_workflow("wf2")
    assert "a" in wf and wf["a"] == StepState.PENDING
    engine.cancel("wf2")
    assert engine.get_workflow("wf2") == {}


def test_resubmit_overwrites():
    def run_fn1(step_id: str):
        return (ResultKind.SUCCESS, {"v": 1})
    def run_fn2(step_id: str):
        return (ResultKind.PERMANENT, {"v": 2})

    engine = Engine({"x": run_fn1})
    engine.submit("wf3", [StepSpec(id="x", deps=[])])
    engine.tick()
    assert engine.get_workflow("wf3")["x"][1]["v"] == 1

    # replace run function and resubmit same wf id
    engine.run_fns["x"] = run_fn2
    engine.submit("wf3", [StepSpec(id="x", deps=[])])
    # after resubmit it's pending again
    assert engine.get_workflow("wf3")["x"] == "pending"
    engine.tick()
    assert engine.get_workflow("wf3")["x"][0] == ResultKind.PERMANENT


if __name__ == '__main__':
    pytest.main([__file__])
