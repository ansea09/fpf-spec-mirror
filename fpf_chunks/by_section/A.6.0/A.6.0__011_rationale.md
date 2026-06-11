---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law‑governed declaration for a SubjectKind on a BaseType"
section_id: "A.6.0:9"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__011_rationale.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.6.0 — U.Signature - Universal, law‑governed declaration for a SubjectKind on a BaseType"
  - "A.6.0:9 — Rationale"
line_start: 9243
line_end: 9256
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

### A.6.0:9 - Rationale

**Why “SubjectBlock”?** A.6.1 showed that making the **ranged-over type explicit** (here: *BaseType*) avoids category mistakes when moving between domains (e.g., *set‑algebra on context slices* vs *equivalence‑classes of normalisations*). A.6.0 lifts this to the kernel so every signature can declare **what it is about** before saying **what it provides**.
**Why one universal Block?** Experience with extension and mechanism signatures shows the value of a single canonical shape for Vocabulary, Laws, Applicability, and Alignment; A.6.0 factors that universal core so other families can add headers and views without fragmenting the Kernel.

**Informative echoes (post‑2015 SoTA).**
— **Algebraic effects and handlers** (OCaml 5, Koka, Effekt, Links): *operation signatures and handler laws* mirror **Vocabulary and Laws** while keeping implementations separate.
— **Session and behavioural types** (2016–2024): protocol and admissibility laws parallel the **Laws** row (at mechanism level).
— **Graded and row-polymorphic effects** (Granule, row-effects): inform the **EffectDiscipline** vocabulary and equational laws.

**Profiles rationale (informative).**
— **`profile=FormalSubstrate` signature profile.** Captures *mathematical language, inference kinds, and effect signatures* in the **conceptual declaration context**, ensuring the calculus stays independent from handler and realization choices; consuming mechanisms (A.6.1) provide **EffectRealization** only by reference.
— **PrincipleFrame.** Captures *postulates and invariants plus measurability intent (CHR binding)* without committing to **units, planes, or Transport**, which are declared centrally in **UNM** so that comparisons remain lawful and edition‑pinned.

