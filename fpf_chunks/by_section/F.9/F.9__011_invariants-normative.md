---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:9"
section_title: "Invariants (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__011_invariants-normative.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:9 — Invariants (normative)"
line_start: 63330
line_end: 63345
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "A.6.Q"
  - "B.3"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
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

### F.9:9 - Invariants (normative)


1. **Locality first.** A Bridge relates **SenseCells**, never Contexts or strings.
2. **senseFamily discipline.** **Substitution Bridges must be senseFamily-preserving**. **Interpretation Bridges** may cross senseFamilies but **never** support substitution.
3. **Direction clarity.** If the kind is directional, state direction explicitly.
4. **CL honesty.** Assign **CL** only if you can state at least one **counter-example** for `CL <= 2` or explain its absence with invariants for `CL = 3`.
5. **Loss visibility.** Every Bridge carries **Loss Notes** (even “none”).
6. **Row dependence.** A Concept-Set row’s **scope** is **bounded by the weakest CL** among its participating Bridges (F.7/F.8).
7. **No senseFamily jump by stealth.** You **must not** use an Interpretation Bridge to justify a **row** or **substitution**.
8. **Time DesignRunTag honesty.** If a Context fixes **DesignRunTag**, the Bridge must respect that distinction or explicitly declare a bridge such as `Design-spec -> Run-trace`.
9. **Kernel restraint.** Bridges **cannot** be used to promote ad-hoc sameness into a new **U.Type**; A.11 applies.
10. **Non-inheritance of Contexts.** Bridges **do not** imply -is-a- between Contexts (E.10.D1).
11. **Coarsened-note restraint.** A lighter cross-context note, comparative aid, redacted view, or surrogate **SHALL NOT** be treated as a Bridge Card or as bridge or substitution support by convenience. If bridge-bearing use is still wanted, the source-bearing episteme or source publication needed for bridge support must be reopened and the bridge must be declared explicitly with kind, direction, `CL`, and loss notes.


