---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Task Typing and TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__001_intro.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.22 — Task Typing and TaskSignature Assignment (Problem-CHR)"
  - "C.22:intro — Intro"
line_start: 49584
line_end: 49597
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

## C.22 - Task Typing and TaskSignature Assignment (Problem-CHR)
> **Status:** Stable
> **Type:** Calculus (C)

**Purpose.** Give FPF an admissible, minimal, and portable `TaskSignature` declaration for selector-facing use after the problem-side episteme is stable enough for Principles-to-Work, eligibility, acceptance, or policy-governed choice. `C.22.2` carries the first problem-framing episteme for a messy signal. C.22 constitutes one CHR-grounded `U.Signature` and, when a receiving use is current, relates the exact problem-side episteme to that signature through `TaskSignatureAssignmentRelation`. Typed characteristics and unknowns stay visible. The declaration includes scope and only those basis, currentness, evidence-use, or crossing relations on which the receiving use relies; none adds a generic setting, carrier, or organization as a participant.

**Body-level kind boundary.** `TaskSignature` is a C.2.1 episteme and a species of existing `U.Signature`, conformant to A.6.0 direct declaration fields, Vocabulary, Laws, and Applicability. It is not a record format and introduces no new root U-kind. `TaskSignatureAssignmentRelation` is a separate obtaining relation among one exact problem-side episteme, one exact TaskSignature episteme, and one exact use episteme. `ProblemCard` is the C.22.2 problem-side episteme used before that assignment. `KindSet` contains C.3 `U.Kind` values for selected entities. Descriptor maps, telemetry hooks, policy ids, and selector fields remain signature vocabulary or projections unless an exact admission predicate and current subject assertion establish another kind.

**Primary EntityOfConcern.** This pattern defines or constrains one `TaskSignature` episteme. Inside it, `EntityOfConcernRef` identifies the exact task or work target declared for the receiving use; it does not identify the signature, `TaskKind`, carrier, organization, or publication. `TaskKind`, optional `TaskFamilyRef`, `KindSet`, characteristic bindings, and scope relations are declaration content. A later `SelectorOutcome` remains a downstream result.

**Placement.** Part C (Kernel Extensions Specifications) -> Cluster C.I (Core CHRs and CALs).
**Depends on:** **C.16 MM-CHR** (measurement admissibility), **G.5** (selector S2 and S3), **G.0** (CG-Spec invariants).
**Coordinates with:** **G.4** (Acceptance and Evidence profiles), **C.23** (MethodFamily admissibility and maturity), **C.18 NQD-CAL** (QD and illumination), **C.19 E/E-LOG** (emitters and policies), **E.10** (LEX).

