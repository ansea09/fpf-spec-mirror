---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics"
section_id: "A.3.3:1"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__002_context.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.3.3 — U.Dynamics"
  - "A.3.3:1 — Context"
line_start: 6448
line_end: 6467
dependencies:
  - "A.19"
  - "B.4"
keywords:
  - "model"
  - "simulation"
  - "state evolution"
  - "state space"
---

### A.3.3:1 - Context

Teams need one place to say **how a thing changes**. Physicists call this “dynamics” (equations of motion, state‑transition maps). In IT and enterprise change, we often talk about **evolution of characteristics** (latency, cost, reliability, compliance, architectural fitness) across time. In knowledge work, **KD‑CAL** (knowledge dynamics) reasons about how the **status of claims** shifts as evidence arrives. All these are *the same modeling need*: a context‑local description of **state space** and **allowed transitions**.

FPF already separates:

* **what a holon is** (structure, PBS/SBS),
* **how we act** (Method or MethodDescription, Work),
* **what we promise** (Service).

What is missing without `U.Dynamics` is the **law of change**—the model that tells us how states evolve **with or without** our interventions.

> Intuition: **Method** tells an agent what to do; **Dynamics** tells everyone how the world (or a model of it) changes when something happens (or even when nothing happens).

**Lexical note.** Terms like *process* and *thermodynamic process* are mapped by **L‑PROC**:

* the **recipe** is `U.Method or U.MethodDescription`,
* the **dated run** is `U.Work`,
* the **law/trajectory model** is `U.Dynamics`.

