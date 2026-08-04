---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol"
section_id: "E.20:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__002_problem-frame.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "E.20 — Mechanism Introduction Protocol"
  - "E.20:1 — Problem frame"
line_start: 85844
line_end: 85893
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
  - "P2W seam"
  - "PQG profiles"
  - "SlotKind lexicon discipline"
  - "alias docking"
  - "authoring protocol"
  - "canonical card-first"
  - "governing-definition assignment"
  - "mechanism introduction"
  - "no dangling …IntensionRef"
  - "regression envelope"
  - "suite boundary hygiene"
  - "typed RSCR triggers"
---

### E.20:1 - Problem frame

FPF is intentionally **open-ended**: new `U.Mechanism` definitions, suite compositions, and SoTA-driven wiring modules can be added over time. This flexibility creates a recurrent authoring problem: introducing a new mechanism (or revising an existing one) tends to touch multiple governing patterns, specification loci, and extension blocks across Parts A/E/F/G and can easily create drift:

* semantics appear in the wrong governing locus (e.g., Part G wiring starts carrying mechanism meaning),
* suites degrade into “meta‑mechanisms” or hidden gates,
* planned baselines (WorkPlanning) are conflated with execution witnesses (WorkEnactment),
* token drift breaks public references, or
* the corpus accumulates dangling references and non-normative drafting commitments without a governing definition.

This pattern provides a **repeatable, governing-definition assignment protocol** for introducing mechanisms. It preserves kernel coherence by keeping extension points and governing definitions explicit.

**Use this when.** Use E.20 when a proposed FPF change introduces or revises mechanism meaning, suite denotation, suite closure, suite obligations, suite pins, suite protocol semantics, planned-baseline pins, wiring semantics, governing-definition assignment, or what a citeable token denotes.

**First useful move.** Classify the edit with MIP trigger triage: `MIP not triggered`, `local wording or alias-docking only`, or `MIP-run manifest required`. If a manifest is required, name exactly one governing definition for each changed item before writing the pattern text.

**Smallest sufficient governing-definition assignment guidance.** Use the lightest governing-definition assignment guidance that preserves the next bounded reader use. Add MIP-run manifest fields, canonical mechanism card stubs, suite fields, planned-baseline pins, wiring refs, RSCR triggers, PQG coverage, or deprecation-continuity material only when the current mechanism-definition or citeable-token claim would otherwise become false, unsafe, non-replayable, or lack a named governing-definition locus.

**Minimum sufficient MIP result.** If the edit does not change citeable-token denotation, mechanism meaning, suite denotation, suite closure, suite obligations, suite pins, suite protocol semantics, planned-baseline pins, wiring semantics, or governing-definition assignment, a MIP-run manifest is not opened; name the current governing locus or alias-docking relation and stop.

**Do not escalate when.** Do not create a MIP-run manifest when alias docking or local wording repair preserves denotation. Do not treat a suite, plan, wiring module, or lexical cleanup as mechanism meaning unless the changed item needs a new or revised governing definition.

**Same problem, different question under repair.** For a mechanism-adjacent transformation-flow problem, use `E.18` for transformation-flow structure, graph/path, valuation, or crossing claims, `A.20` for internal step validity, `A.21` for gate-decision publication, and `E.20` for mechanism-meaning placement; do not open the other three until their own claim is present.

**Semantic repair return.** When E.20 blocks a misleading word, face, alias, or source label, the repair must return to the enabled authoring move: name the governing definition, canonical location, alias-docking relation, or non-trigger stop that remains available under E.20. Do not stop at a classification of vocabulary or publication faces.

**Governed-object and relation separation.** Keep the graph object and path or crossing relation (`E.18`), MVPK publication faces (`E.17`), internal CV status and witness (`A.20`), gate decision and `DecisionLog` (`A.21`), evidence or provenance relation (`A.10`/`G.6`), work plan or work occurrence (`A.15`), and mechanism-governing definition assignment (`E.20`) distinct. An MVPK face, `DecisionLog`, evidence value, provenance reference, MIP manifest, or work witness does not supply another pattern's project-side value unless that governing pattern consumes it for that relation.

**Smallest affected locus.** Localize the change to the smallest current locus: `PathSlice` or crossing in `E.18`, CV step in `A.20`, `GateDecision` equivalence class in `A.21`, or mechanism-governing definition in `E.20`. Do not widen to a whole flow or unrelated claim, locus, or EntityOfConcern when that locus is enough.

**Ordinary success.** For ordinary E.20 use, success is that the edit is classified, the current governing locus or alias-docking relation is named, and no MIP-run manifest is opened unless denotation, mechanism meaning, suite denotation, suite closure, suite obligations, suite pins, suite protocol semantics, planning pins, wiring semantics, or governing-definition assignment actually changes.

**Locality asymmetry.** `E.18` is graph-local, `A.20` is step-local, `A.21` is gate-local, and `E.20` is trigger-local. Do not normalize the four patterns into one assurance regime.

**Do not merge these pairs.** Keep `CV.Status` distinct from `GateDecision`, `E.18` `Check` locus distinct from `GateCheckKind`, MIP manifest distinct from `DecisionLog`, `ViewpointMap` distinct from graph semantics, `PathSlice` distinct from a work run, and `GateProfile=Lite` distinct from `PublishMode=Lite`.

**Field applicability.** Always core for E.20: trigger triage and the current governing locus or alias-docking relation. Conditional fields: MIP-run manifest fields, canonical mechanism card stubs, suite fields, planned-baseline pins, wiring refs, RSCR triggers, PQG coverage, and deprecation continuity; open them only when the corresponding denotation, mechanism-meaning, suite, planning, wiring, lexical, refresh, review, or retirement claim is present.

**Retrieval trap guard.** When excerpted alone, E.20 manifest language must not be read as requiring a full MIP-run for every mechanism-adjacent edit. Pure currentness cleanup, alias docking, optional suite-member citation of an already-defined mechanism, and local wording repair stop at the current governing locus unless denotation, mechanism meaning, suite closure, suite obligations, suite pins, suite protocol semantics, planning pins, wiring semantics, or governing-definition assignment changes.

**Anti-Goodhart guard.** A complete MIP-run manifest is not a substitute for the governed mechanism result: the mechanism-governing definition must still carry the operation, law, admissibility, slot, transport, applicability, and audit meaning needed for the claim.

**Generative side.** E.20 preserves open-ended action by allowing new mechanism definitions, suite variants, wiring, and citeable tokens to enter FPF with a named governing definition; the discipline prevents semantic drift so new work can be added rather than merely blocked.

**What goes wrong if missed.** A suite can start defining mechanism meaning, a plan item can start carrying enactment witnesses or gate decisions, a wiring module can carry kernel semantics, or a token rename can break citations while looking like harmless cleanup.

**What this buys.** E.20 gives the reader one current authoring move: assign the change to the right governing definition and keep mechanism, suite, planning, wiring, and lexical continuity distinct.

**Not this pattern when.** If the edit is only pure currentness, typo, reference, or old-label cleanup and changes no semantics or citeable-token denotation, record the current governing locus and stop. If the question under repair is runtime gate passage, gate decision, approval, suite-as-mechanism, plan-as-enactment, or performed work, use the gate, suite, planning, or work loci that own that question. A MIP-run manifest is not a runtime gate, gate passage, approval packet, or binary pass/fail decision.

