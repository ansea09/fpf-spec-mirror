---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__002_use-this-when.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:0 — Use this when"
line_start: 58236
line_end: 58260
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.22"
  - "A.6.3.CSC"
  - "A.6.F"
  - "A.6.P"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.P"
  - "C.25"
  - "C.27"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.P"
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.21"
  - "E.8"
  - "F.18"
  - "J.4"
keywords:
---

### E.10.ARCH:0 - Use this when

Use this pattern when a recurring FPF-facing wording-use problem cannot be closed by one local `E.10` rewrite because the wording hides a stable governed-object-kind/use field set, a stable recovery apparatus, and a useful remaining reader move.

Use it especially when a subject or adequacy pattern contains repeated first-stage repair prose such as:

- architecture-vs-diagram, model, graph, ADR, dashboard, view, or layer triage before the architecture pattern can start;
- axis, dimension, feature, property, metric, indicator, score, strong, weak, robust, level, coordinate, threshold, or scalar-quality triage before a characteristic or scale pattern can start;
- quality-term repair that decides between relation construction, quality/evaluative characterization, Q-bundle use, pattern-quality coordinate use, action invitation, bridge, or exact receiving pattern;
- source, publication, carrier, face, `PublicationUnit`, dashboard, documentation, or source-return wording whose project-side use is not yet recovered;
- relation-like, function-like, evidence-like, assurance-like, gate-like, work-like, decision-like, causal-use, release, or naming wording whose exact receiving pattern is already known or must be recovered before the sentence is admitted.

**What goes wrong if missed.** FPF accumulates many small local trigger lists. One pattern says "architecture is not a diagram", another says "metric is not proof", another says "quality is not one scalar", and a reviewer cannot tell which pattern owns the repair. The text looks more precise, but the reader does not get a stable first move.

**What this buys.** `E.10.ARCH` gives one architecture for distributing wording-use repair: `E.10` catches; `E.10.ARCH` selects the row and extraction criterion; a realization pattern or exact neighbor recovers the ontology; the subject pattern returns to its own governed object.

**First useful move.** Decide whether the wording can close locally under `E.10`, already has an exact receiving pattern, or needs one applicability row with a stable `ontologicalNeighborhood`, recovery apparatus, and remaining reader move.


**Not this pattern when.**

- If a sentence is repaired locally under `E.10`, stop there.
- If the exact receiving pattern and governed object are already recoverable by value, use that receiving pattern directly.
- If the live object is evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens adequacy, architecture-description adequacy, structural-view adequacy, characteristic-space construction, Q-bundle construction, pattern-quality evaluation, or another exact FPF object, the exact receiving pattern governs its own invariant. `E.10.ARCH` only governs the wording-use restoration distribution.

