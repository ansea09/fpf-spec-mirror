---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:10"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__012_invariants.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:10 — Invariants"
line_start: 82618
line_end: 82631
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

### F.9:10 - Invariants

1. **Locality first.** A Bridge relates `SenseCells`, never contexts as wholes and never strings alone.
2. **senseFamily discipline.** Substitution Bridges preserve `senseFamily`. Interpretation Bridges may cross `senseFamily` boundaries but remain Explanation-only.
3. **Direction clarity.** Directional kinds state direction explicitly.
4. **CL honesty.** `CL <= 2` needs at least one counter-example or boundary case. `CL = 3` needs invariant evidence.
5. **Loss visibility.** Every Bridge carries Loss Notes, even when the note is "none" at `CL = 3`.
6. **Weakest-link row discipline.** A Concept-Set row's admitted use is bounded by the weakest participating Bridge.
7. **No role-assignment by bridge.** A Bridge may inform RoleDescription naming or comparison; `U.RoleAssignment`, required-role satisfaction, and performed-work attribution remain with A.2.1, F.6, and A.15.1.
8. **No interpretation bridge substitution.** Interpretation Bridges cannot justify substitution rows.
9. **Design-run honesty.** If a context fixes a design-run distinction, the Bridge respects it or explicitly uses a design-spec-to-run-occurrence interpretation bridge.
10. **Kernel restraint.** Bridges do not promote ad hoc sameness into a durable U-kind; E.24.UK, A.11, and F.8 govern that decision.
11. **Non-inheritance of contexts.** Bridges do not imply is-a relations between contexts.

