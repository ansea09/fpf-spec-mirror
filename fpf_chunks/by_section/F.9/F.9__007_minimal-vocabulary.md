---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:5"
section_title: "Minimal vocabulary"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__007_minimal-vocabulary.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:5 — Minimal vocabulary"
line_start: 84731
line_end: 84743
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.10.D1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:5 - Minimal vocabulary

* **Context** - shorthand for `U.BoundedContext` per E.10.D1.
* **SenseCell** - the pair `(Context, Local-Sense)` from F.3.
* **Bridge** - a declared relation between two `SenseCells` with kind, direction, `CL`, Loss Notes, and admitted use.
* **CL (Congruence Level)** - ordinal congruence class `0..3` for one Bridge.
* **Admitted use** - what the Bridge lets a downstream claim do without overclaim.
* **Naming-only** - cross-context prose label or Concept-Set row label only.
* **Role-description naming** - a row or label may inform a `RoleDescription` name for one local `U.Role`; it does not assign that role and does not attribute performed work.
* **Type-structure** - structural inference across contexts; admissible only at `CL = 3` with named invariants.
* **Explanation-only** - interpretation relation across sense families; no row substitution and no direct role, status, work, evidence, gate, or decision effect.
* **senseFamily** - the local meaning family used by Part F, such as Role, Status, Measurement, Type-structure, Method, Work occurrence, Evidence-use, or Policy-use. A `senseFamily` label is not a durable U-kind by itself.

