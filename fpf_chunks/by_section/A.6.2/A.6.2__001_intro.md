---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "Effect-free episteme morphing"
section_id: "A.6.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__001_intro.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "A.6.2 — Effect-free episteme morphing"
  - "A.6.2:intro — Intro"
line_start: 13005
line_end: 13028
dependencies:
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

## A.6.2 - Effect-free episteme morphing
> **Status:** Stable
> **Type:** Definitional pattern

**One-line summary.** Effect-free episteme morphing (EFEM) is a local mathematical discipline for law-constrained arrows between exact epistemes. It compares what the source and receiving epistemes say, what they concern, and the schemes that make their claims interpretable, then states the allowed ClaimGraph difference. If its rule needs grounding, representation, conformance, or another separately obtaining relation, it names and reads that occurrence without changing it. The declaration, arrow, use claim, operation application, and performed Work remain distinct.

**Use this pattern when** a project needs to state and reuse a law-constrained mathematical relation between two exact epistemes while keeping that arrow distinct from a claim that it suits one use, an operation application, publication, and performed Work.

**What goes wrong if missed.** A view, retargeting, refinement, representation change, publication rendering, mechanism application, or work occurrence is treated as the same operation, so the project can no longer tell whether the EntityOfConcern changed or only the episteme changed.

**What this buys.** EFEM gives one law-constrained episteme-to-episteme morphism discipline with explicit preserve/retarget mode, clear boundaries among actual values, declaration-local participant meanings, and references, plus conservativity and composition conditions.

**Placement.** After **A.6.1 `U.Mechanism`** and before the A.6.3 epistemic-viewing and A.6.4 EntityOfConcern-retargeting branches.

**Builds on.**
A.6.0 `U.Signature` for subject, vocabulary, laws, and applicability; A.6.1 `U.Mechanism`; A.6.5 for declaration-local SlotSpecs; C.2.1 for `U.Episteme` identity and direct constitution, empirical-grounding, and edition relations; E.10.D2 for the EntityOfConcern, Description-episteme, describing-use, and specification-use boundary; and C.3 plus F.9 for kind-level and exact cross-local reasoning.

**Used by.**
A.6.3 epistemic viewing; A.6.4 EntityOfConcern retargeting; E.17.0 multi-view describing; E.17 (MVPK); and E.18 structural reinterpretation over transformation-flow structure.

**EntityOfConcern change-mode discipline.** EFEM uses `EntityOfConcernChangeMode` for the preserve/retarget characteristic over the exact C.2.1 EntityOfConcern designated by `entityOfConcernRef`. Earlier source-side spellings must be normalized to the EntityOfConcern family before conformant use and do not define a second EntityOfConcern ontology.

**Object settlement.** EFEM and `EpMorphism` are local mathematical classes under C.29, not admitted durable U-kinds. `U.Episteme` is reused from C.2.1. An A.6.0 FormalSubstrate signature that declares EFEM vocabulary and laws is a separate episteme; one arrow, one use-specific assertion about that arrow, any operation application, performed Work, and publication remain separate objects under their direct governors.

