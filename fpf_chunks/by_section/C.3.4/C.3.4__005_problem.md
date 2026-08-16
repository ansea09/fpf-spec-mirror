---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:3"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__005_problem.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:3 — Problem"
line_start: 45339
line_end: 45345
dependencies:
  - "A.2.6"
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
  - "F.9"
keywords:
  - "base KindSignature"
  - "candidate-feature constraint"
  - "correspondence declaration"
  - "kind-use adaptation declaration"
  - "three-valued judgment"
  - "vocabulary binding"
---

### C.3.4:3 - Problem

1. **Kind sprawl.** Teams mint near-duplicate kinds such as `Account_PCI` and `Account_Ledger`, and alignment decays.
2. **Hidden constraints.** Informal “we only accept …” statements leak into prose, so guards cannot check them deterministically.
3. **Scope conflation.** Jurisdiction, API version, or another context condition is smuggled into type talk, blurring Scope and Kind.
4. **Cross-context fragility.** Local declarations do not travel safely unless differences in constraints and bindings are stated explicitly.

