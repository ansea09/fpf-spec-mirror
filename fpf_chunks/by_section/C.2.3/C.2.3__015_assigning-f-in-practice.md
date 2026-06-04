---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Unified Formality Characteristic F"
section_id: "C.2.3:14"
section_title: "Assigning F in Practice"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__015_assigning-f-in-practice.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "C.2.3 — Unified Formality Characteristic F"
  - "C.2.3:14 — Assigning F in Practice"
line_start: 35718
line_end: 35750
dependencies:
  - "A.16"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.2"
  - "C.2.2"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "F.9"
keywords:
  - "F-scale"
  - "F0-F9"
  - "Formality"
  - "language-state separation"
  - "proof"
  - "rigor"
  - "specification"
---

### C.2.3:14 - Assigning `F` in Practice

#### C.2.3:14.1 - First-pass questions

1. **Can a competent reader misread the claim materially?**
   If yes, the expression is likely at `F0-F2`; if not, it may be `F3` or above.
2. **Are the critical claims visible as explicit predicates or invariants?**
   If yes, the expression is at least `F4`.
3. **Does the expression have declared executable semantics?**
   If yes, it is likely in the `F5-F6` region.
4. **Would a logic kernel or type checker reject an incorrect change to a core claim?**
   If yes, the expression is likely `F7-F8`, or `F9` if higher-equality machinery is essential.

#### C.2.3:14.2 - Quick rubric

- No full structure -> `F0-F1`
- Full structure but mostly placeholder criteria -> `F2`
- Controlled prose with one stable reading -> `F3`
- Explicit predicates / invariants -> `F4`
- Declared executable semantics -> `F5`
- Hybrid / layered formal obligations -> `F6`
- Machine-checked proof core -> `F7`
- Dependent proof-carrying core -> `F8`
- Higher-equality foundations are essential -> `F9`

#### C.2.3:14.3 - Typical delta-`F` moves

- `F2 -> F3`: replace loose prose with controlled phrasing and explicit acceptance statements.
- `F3 -> F4`: recast acceptance into typed predicates or invariants.
- `F4 -> F5`: give the expression declared executable semantics.
- `F5 -> F6`: make multi-layer obligations explicit.
- `F6 -> F7/F8`: move critical claims into machine-checked proof or dependent-type form.

