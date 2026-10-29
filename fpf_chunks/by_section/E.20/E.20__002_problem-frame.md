---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol: Introduce or Revise FPF Mechanisms"
section_id: "E.20:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__002_problem-frame.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "E.20 — Mechanism Introduction Protocol: Introduce or Revise FPF Mechanisms"
  - "E.20:1 — Problem frame"
line_start: 112660
line_end: 112693
dependencies:
  - "A.15.3"
  - "A.6.1"
  - "A.6.7"
  - "E.10"
  - "E.15"
  - "E.18"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.18"
  - "G.2"
  - "G.Core"
  - "G.x"
keywords:
  - "MIP-run manifest"
  - "alias docking"
  - "authoring protocol"
  - "declaration-local operation members"
  - "governing-definition assignment"
  - "mechanism introduction"
  - "planned baseline"
  - "resolvable MechanismDefinitionRef"
  - "suite boundary"
  - "trigger triage"
  - "wiring"
---

### E.20:1 - Problem frame

FPF is intentionally **open-ended**: new `U.Mechanism` definitions, suite compositions, and SoTA-driven wiring modules can be added over time. This flexibility creates a recurrent authoring problem: introducing a new mechanism (or revising an existing one) tends to touch multiple subject patterns, specification loci, and extension blocks across Parts A/E/F/G and can easily create drift:

* semantics appear in the wrong governing locus (e.g., Part G wiring starts carrying mechanism meaning),
* suites degrade into “meta‑mechanisms” or hidden gates,
* planned baselines in exact `U.WorkPlan` content are conflated with dated performed Work,
* token drift breaks public references, or
* the corpus accumulates dangling references and non-normative drafting commitments without a governing definition.

This pattern provides a **repeatable, governing-definition assignment protocol** for introducing mechanisms. It preserves kernel coherence by keeping extension points and governing definitions explicit.

**Use this when.** Use E.20 when a proposed FPF change introduces or revises mechanism meaning, suite denotation, suite closure, suite obligations, suite pins, suite protocol semantics, planned-baseline pins, wiring semantics, governing-definition assignment, or what a citeable token denotes.

**First useful move.** Classify the edit with MIP trigger triage: `MIP not triggered`, `local wording or alias-docking only`, or `MIP-run manifest required`. If a manifest is required, name exactly one governing definition for each changed item before writing the pattern text.

**Same problem, different question under repair.** For a mechanism-adjacent transformation-flow problem, use `E.18` for transformation-flow structure, paths, valuations, and crossings, `A.20` for internal step validity, `A.21` for a gate profile application and decision, and `E.20` for mechanism-meaning placement; do not open the other three until their own claim is present.

**Semantic repair return.** When E.20 blocks a misleading word, face, alias, or source label, the repair must return to the enabled authoring move: name the governing definition, canonical location, alias-docking relation, or non-trigger stop that remains available under E.20. Do not stop at a classification of vocabulary or publication faces.

**Subject and relation separation.** Keep the selected transformation-flow structure, paths and crossings (`E.18`), its mathematical description (`E.18.2`), MVPK publication faces (`E.17`), internal CV status and witness (`A.20`), gate profile application and decision (`A.21`), evidence or provenance relation (`A.10`/`G.6`), work plan or work occurrence (`A.15`), and mechanism-definition assignment (`E.20`) distinct. An MVPK face, `DecisionLog`, evidence value, provenance reference, MIP manifest, or work witness does not supply another subject's project-side value unless an exact dependent-use assertion and its defining or constraining `ClaimGraph` establish that relation.

**Smallest affected locus.** Localize the change to the smallest current locus: `PathSlice` or crossing in `E.18`, CV step in `A.20`, the profile application and bounded action decided in `A.21`, or mechanism-governing definition in `E.20`. Do not widen to a whole flow or unrelated claim, locus, or EntityOfConcern when that locus is enough.

**Do not merge these pairs.** Keep `CV.Status` distinct from `GateDecision`, `E.18` `Check` locus distinct from `GateCheckKind`, MIP manifest distinct from `DecisionLog`, `ViewpointMap` distinct from graph semantics, `PathSlice` distinct from a work run, and `GateProfile=Lite` distinct from `PublishMode=Lite`.

**Anti-Goodhart guard.** A complete MIP-run manifest is not a substitute for the governed mechanism result. The cited `U.Mechanism` episteme must recover `<content, EntityOfConcernRef, effectiveReferenceScheme>` and the A.6.1 content needed by the receiving use. Realization, refinement, bridge, evaluation, evidence-use, and publication relations remain neighboring claims under their direct patterns.

**What goes wrong if missed.** A suite can start defining mechanism meaning, declaration-local WorkPlan rows can start carrying enactment witnesses or gate decisions, a wiring module can carry kernel semantics, or a token rename can break citations while looking like harmless cleanup.

**What this buys.** E.20 gives the reader one current authoring move: assign the change to the right governing definition and keep mechanism, suite, planning, wiring, and lexical continuity distinct.

**Not this pattern when.** If the edit is only pure currentness, typo, reference, or old-label cleanup and changes no semantics or citeable-token denotation, record the current governing locus and stop. If the question under repair is runtime gate passage, gate decision, approval, suite-as-mechanism, plan-as-enactment, or performed work, use the applicable gate, suite, planning, or Work pattern for that question. A MIP-run manifest is not a runtime gate, gate passage, approval packet, or binary pass/fail decision.

