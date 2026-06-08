---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "U.RoleStateGraph: The Named State Space of a Role"
section_id: "A.2.5:5"
section_title: "What an RSG is not (guardrails)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__006_what-an-rsg-is-not-guardrails.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "A.2.5 — U.RoleStateGraph: The Named State Space of a Role"
  - "A.2.5:5 — What an RSG is not (guardrails)"
line_start: 3437
line_end: 3444
dependencies:
  - "A.15"
  - "A.2.1"
  - "A.2.3"
  - "B.3"
  - "E.10.D1"
  - "F.9"
  - "U.RoleAssignment"
  - "U.RoleDescription"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:5 - What an RSG is **not** (guardrails)

* **Not a task-order description.** RSG transitions do **not** encode method order; they encode **eligibility changes** of the *role*.
* **Not a capability list.** RSG is **authorization/readiness over time**, distinct from `U.Capability` (ability).
* **Not a global status set.** RSG lives **inside one Context**; the label *Ready* in another Context is **a different state** unless bridged (F.9).
* **Not a log.** RSG is not a history. Histories are **StateAssertions** over Windows; **`U.Work`** is the record of enactments.
* **Not a document-state sequence.** Epistemic role RSGs can *look like* document-state sequences, but they remain **role‑status graphs**; carrier history and carrier replacement stay separate (A.7, `U.Carrier`).

