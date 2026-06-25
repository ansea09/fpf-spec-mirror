---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
section_id: "A.6.0:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__007_archetypal-grounding-tell-show-show.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "A.6.0 — U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
  - "A.6.0:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 10170
line_end: 10188
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

### A.6.0:5 - Archetypal Grounding (Tell–Show–Show)

| quartet Element | `U.System` Example — **Grammar of Motions** | `U.Episteme` Example — **Normalization Family** |
| --- | --- | --- |
| **SubjectBlock** | **Subject:** SubjectKind=`MotionGrammar`; RangedValueKind=`U.System:TrajectorySpace`. **Quantification:** SliceSet=`ContextSliceSet`; ExtentRule=`admissible motion words per slice (kinematics and domain restrictions)`; ResultKind?=`Language[Segment]`. | **Subject:** SubjectKind=`NormalizationMethod-Class`; RangedValueKind=`U.Episteme:ChartFamily` (one `U.BoundedContext`). **Quantification:** SliceSet=`ContextSliceSet`; ExtentRule=`admissible method instances per slice (edition and validity)`; ResultKind?=`NormalizedChart`. |
| **Vocabulary** | Types: `Pose`, `Segment`; Operators: `concat`, `reverse`, `sample` (any Γ‑like aggregator is published outside the Signature Block, typically as a Mechanism‑level operator namespaced under the Signature id). | Operators: `apply(method)`, `compose`, `quotient(≡)`. |
| **Laws (Invariants and Constraints)** | Closure of `concat`; associativity; time-monotone sampling; **`reverse` is declared only for holonomic arms (domain restriction)**. | Ratio→positive-scalar; Interval→affine; Ordinal→monotone; Nominal→categorical; LUT(+uncertainty). |
| **Applicability (Scope and Context)** | Context: *industrial robotics*; stance: design; time notion: discrete ticks. Cross-context transport not declared. | Context: *clinical metrics*; stance: analysis; validity windows declared; cross-context transport via Bridge (concept only; details per A.6.1). Numeric comparability bound to CHR and CG-Spec. |

*Why these two?* E.8 requires pairs from **U.System** and **U.Episteme** to demonstrate trans‑disciplinary universality.

#### A.6.0:5.1 - Near-miss and anti-cases

**Near-miss: handler hidden in a `U.Signature(profile=FormalSubstrate)` declaration.** A `U.Signature(profile=FormalSubstrate)` declaration for an algebraic-effects calculus may list operation symbols, inference kinds, and equational laws. If the same block says how a database handler commits transactions, the text has crossed into A.6.1 `U.Mechanism`: keep the operation and effect signature in A.6.0, and publish the handler realization as a mechanism that cites this signature.

**Near-miss: measurement comparison hidden in a principle frame.** A `PrincipleFrame` may state that a physical model preserves a heat-flow invariant and that observability must be recoverable through CHR. It must not declare units, reference planes, comparator legality, or transport loss as if they were signature laws. Those belong to CHR, UNM, bridge, comparator, and measurement patterns that cite the principle frame.

**Anti-case: implementation manual called a signature.** A document that names build steps, CI checks, tool vendors, or work authorization before it states `SubjectBlock`, `Vocabulary`, `Laws`, and `Applicability` is not a conformant `U.Signature`. Rewrite the declaration first; then place realization, work, evidence, or tooling claims in their governing patterns.

