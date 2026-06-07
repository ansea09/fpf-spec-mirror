---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability"
section_id: "A.2.2:5"
section_title: "Clear distinctions (litmus tests managers can apply)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__006_clear-distinctions-litmus-tests-managers-can-apply.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "A.2.2 — U.Capability"
  - "A.2.2:5 — Clear distinctions (litmus tests managers can apply)"
line_start: 2359
line_end: 2374
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.3"
  - "U.BoundedContext"
  - "U.Dynamics"
  - "U.PromiseContent"
  - "U.RoleAssignment"
keywords:
  - "ability"
  - "action"
  - "measures"
  - "performance"
  - "skill"
  - "work scope"
---

### A.2.2:5 - Clear distinctions (litmus tests managers can apply)

| If you are talking about…                  | Use                     | Litmus test                                                                                  |
| ------------------------------------------ | ----------------------- | -------------------------------------------------------------------------------------------- |
| **assignment** (who is being what, where) | **Role → Role assignment** | Can you reassign to another holder without changing the system’s composition? If yes → Role. |
| **Ability** (can do within bounds)         | **Capability**          | Would you still say “can do” even if not currently assigned? If yes → Capability.           |
| **Recipe** (how‑to)                        | **Method or MethodDescription** | Recover whether the text means the abstract way of doing or the episteme that describes it; has inputs and outputs and steps but no date/time. |
| **Execution** (what happened)              | **Work**                | Has a start/end, consumed resources, left a log.                                             |
| **External promise**                       | **Promise content (service promise clause)** | Framed as “we provide/guarantee to others.”                                                  |
| **Law/model of change**                    | **Dynamics**            | Describes state evolution, not an ability of one system.                                     |

**Two useful corollaries**

* A step in a Method may **require** a Role; **optionally** it may also stipulate a **capability threshold** (e.g., precision ≤ 0.2 mm). assignment and ability are checked separately.
* A promise content clause depends on **having** the needed capabilities **and** being **assigned/committed** to deliver under the clause’s context (bind as `U.Commitment` when it is an obligation).

