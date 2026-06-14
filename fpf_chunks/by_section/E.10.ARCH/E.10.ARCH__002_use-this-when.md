---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__002_use-this-when.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:0 — Use this when"
line_start: 61708
line_end: 61736
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.SPR"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.F"
  - "A.6.P"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.25"
  - "C.27"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.P"
  - "C.30.STRAT"
  - "E.10"
  - "E.11"
  - "E.18"
  - "E.19"
  - "E.2"
  - "E.20"
  - "E.21"
  - "E.24"
  - "E.8"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

### E.10.ARCH:0 - Use this when

Use this pattern when a recurring FPF-governed wording-use problem cannot be closed by one local `E.10` rewrite because the wording hides a stable primary-EntityOfConcern use field set, a stable recovery apparatus, and a useful remaining reader move.

Use it especially when a subject or adequacy pattern contains repeated first-stage repair prose such as:

- architecture-vs-diagram, model, graph, ADR, dashboard, view, layer, level, tier, stack, block, expert, cache, router, or gate triage before the architecture, structure, control, module-interface, flow, scale, publication, or gate pattern can start;
- axis, dimension, feature, property, metric, indicator, score, strong, weak, robust, level, coordinate, threshold, or scalar-quality triage before a characteristic or scale pattern can start;
- quality-term repair that decides between relation construction, quality characterization, evaluative characterization, Q-bundle use, pattern-quality coordinate use, action invitation, bridge, or governing pattern;
- state-family wording such as state, status, posture, readiness, stance, or currentness before the bearer, state frame, value set, admissible use, or governing pattern is recovered;
- admissibility-like, legal, lawful, authority, validity, readiness, pass-looking, fail-looking, or conformance wording before bearer, claim kind, source relation, value frame, bounded use, and direct governing pattern are recovered;
- method, algorithm, program, proof, solver, workflow, process, procedure, access path, query plan, control strategy, or programming-paradigm wording before its slot or use-position is recovered as method, method description, formal substrate, mathematical-lens use, mechanism, work plan, dated work, evidence relation, or quote-only source wording;
- graph, path, query, table, dashboard, checklist predicate, publication face, evidence path, or pattern-relation wording overread as a route, call, dispatch, invocation, work sequence, permission, release, evidence result, or pattern application;
- source, publication, carrier, face, `PublicationUnit`, dashboard, documentation, or source-return wording whose project-side use is not yet recovered;
- relation-like, function-like, evidence-like, assurance-like, gate-like, work-like, decision-like, causal-use, release, or naming wording whose governing pattern is already known or must be recovered before the sentence is admitted.

**What goes wrong if missed.** FPF accumulates many small local trigger lists. One pattern says "architecture is not a diagram", another says "metric is not proof", another says "quality is not one scalar", another says "a path is not a route", and a reviewer cannot tell which pattern carries the repair. The text looks more precise, but the reader does not get a stable first move.

**What this buys.** `E.10.ARCH` gives one architecture for distributing wording-use repair: `E.10` catches; `E.10.ARCH` selects the row and extraction criterion; a realization pattern or governing neighboring pattern recovers the ontology; the subject pattern returns to its own primary `EntityOfConcern` and first useful move.

**First useful move.** Decide whether the wording can close locally under `E.10`, already has a governing pattern, or needs one applicability row with stable `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, `ontologicalNeighborhood`, recovery apparatus, and remaining reader move.

**Not this pattern when.**

- If a sentence is repaired locally under `E.10`, stop there.
- If the governing pattern and primary `EntityOfConcern`, relation record, or claim record are already recoverable by value, use that governing pattern directly.
- If the kind under repair is evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens use, grounded architecture adequacy, structural-view adequacy, characteristic-space construction, Q-bundle construction, pattern-quality evaluation, method, mechanism, method description, formal substrate, graph path, evidence path, publication face, or another FPF kind named by value, the governing pattern governs its own invariant. `E.10.ARCH` only governs the wording-use restoration distribution.
- If the wording problem is phrase-level apparatus around an already recoverable kind, use `F.19` rather than creating a new wording-use restoration row.

