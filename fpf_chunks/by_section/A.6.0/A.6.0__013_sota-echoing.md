---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
section_id: "A.6.0:9.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__013_sota-echoing.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "A.6.0 — U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
  - "A.6.0:9.1 — SoTA-Echoing"
line_start: 10250
line_end: 10258
dependencies:
  - "A.2.6"
  - "A.6.1"
  - "A.6.5"
  - "D.CTX"
  - "E.10"
  - "E.10.D1"
  - "E.5.3"
  - "E.8"
  - "U.Mechanism"
  - "U.RelationSlotDiscipline"
keywords:
  - "RFC 2119"
  - "applicability"
  - "bounded context"
  - "laws"
  - "signature"
  - "vocabulary"
---

### A.6.0:9.1 - SoTA-Echoing
— **Algebraic effects and handlers** (OCaml 5, Koka, Effekt, Links): *operation signatures and handler laws* mirror **Vocabulary and Laws** while keeping implementations separate.
— **Session and behavioural types** (2016–2024): protocol and admissibility laws parallel the **Laws** row (at mechanism level).
— **Graded and row-polymorphic effects** (Granule, row-effects): inform the **EffectDiscipline** vocabulary and equational laws.

**Profiles rationale (informative).**
— **`profile=FormalSubstrate` signature profile.** Captures *mathematical language, inference kinds, and effect signatures* in the **conceptual declaration context**, ensuring the calculus stays independent from handler and realization choices; consuming mechanisms (A.6.1) provide **EffectRealization** only by reference.
— **PrincipleFrame.** Captures *postulates and invariants plus measurability intent (CHR binding)* without committing to **units, planes, or Transport**, which are declared centrally in **UNM** so that comparisons remain lawful and edition‑pinned.

