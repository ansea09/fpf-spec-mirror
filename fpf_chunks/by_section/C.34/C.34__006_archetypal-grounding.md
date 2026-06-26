---
chunk_kind: "child"
pattern_id: "C.34"
pattern_title: "Structural Correspondence, Equivalence, and Morphism Adequacy"
section_id: "C.34:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.34/C.34__006_archetypal-grounding.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "C.34 — Structural Correspondence, Equivalence, and Morphism Adequacy"
  - "C.34:5 — Archetypal Grounding"
line_start: 61640
line_end: 61651
dependencies:
  - "A.22"
  - "A.6.M"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ADR"
  - "C.32.PAD"
  - "E.18"
  - "F.15"
  - "F.9"
keywords:
  - "directionality"
  - "equivalence"
  - "lost structure"
  - "mapping mode"
  - "morphism"
  - "preserved structure"
  - "scope"
  - "structural correspondence"
---

### C.34:5 - Archetypal Grounding

Tell: C.34 is the pattern for a declared architecture preservation claim. It is used when a practitioner says that one structure-bearing object is the same enough as another for a specific architecture use. The pattern does not ask for the strongest possible proof. It asks for the weakest adequate mapping mode, preserved structure, lost structure, directionality, scope, admissible use, and receiving owner.

Show - view and description case. Two architecture diagrams are edge-isomorphic. In one diagram an edge means data dependency; in the other it means control authority. C.34 records mapping mode `nearSameness`, preserved node partition, lost relation-type semantics, and non-admissible use "control separation decision." The repair is to recover relation semantics through `C.30.ASV`, `C.30.TFS-REL`, or `C.30.LCA` before using the mapping for architecture work.

Show - source model and generated graph case. A code-agent dependency graph matches module names in a source model but marks several edges inferred and several regions unexplored. C.34 records source observation class, directionality, preserved dependency hints, lost dynamic wiring, and non-admissible use "safe-change authority." The graph may help inspect candidate dependencies, but it cannot prove release readiness.

Show - candidate and realized structure case. A candidate architecture promises that a service split preserves interface substitutability, but the realized structure adds shared storage and a hidden orchestration dependency. C.34 records preserved interface signatures, lost runtime independence, changed coupling, and source return to `A.6.M`, `C.31`, `C.30`, and `C.32.PAD` before the decision is reused.

Show - neural substitution case. A candidate replaces an attention block with an SSM block. C.34 asks which selected structures are preserved: sequence dataflow, routing interface, memory access, latency envelope, training resource boundary, or inference resource boundary. Shape sameness or benchmark improvement does not by itself preserve the architecture relation needed by the next claim.

