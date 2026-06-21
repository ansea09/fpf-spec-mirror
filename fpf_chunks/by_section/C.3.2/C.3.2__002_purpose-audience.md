---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "KindSignature (+F) & Extension/MemberOf"
section_id: "C.3.2:1"
section_title: "Purpose & Audience"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__002_purpose-audience.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "C.3.2 — KindSignature (+F) & Extension/MemberOf"
  - "C.3.2:1 — Purpose & Audience"
line_start: 40057
line_end: 40066
dependencies:
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
keywords:
  - "Formality F"
  - "KindSignature"
  - "MemberOf"
  - "determinism"
  - "extension"
  - "intension"
---

### C.3.2:1 - Purpose & Audience

This pattern makes **entityOfConcern testable** in a Context:

* Authors get a place to write **what defines a kind** (`KindSignature`) and at **what rigor (F)**.
* Reviewers can ask **deterministic** questions: *“Given this `TargetSlice`, which entities are in `k`?”*
* Managers can plan **ΔF** (raise signature rigor) and **ΔR** (evidence over members) **without** changing **G** (applicability).

**No tooling assumption.** The pattern is **conceptual** and notation‑neutral (no OWL/SHACL/type‑system requirement); it specifies reviewer‑checkable obligations that managers can read in plain language.

