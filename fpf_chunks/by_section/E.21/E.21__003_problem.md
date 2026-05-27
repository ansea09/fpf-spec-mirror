---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern Quality Characteristic Space"
section_id: "E.21:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__003_problem.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "E.21 — FPF Pattern Quality Characteristic Space"
  - "E.21:2 — Problem"
line_start: 64176
line_end: 64190
dependencies:
  - "A.17-A.19"
  - "A.6.P"
  - "A.6.Q"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.11"
  - "E.17.AUD"
  - "E.19"
  - "E.8"
  - "F.18"
  - "J.4"
keywords:
  - "Goodhart/proxy substitution"
  - "Pareto/front comparison"
  - "PatternQualityCharacteristicSpace"
  - "PatternQualityQBundle"
  - "activation-normalized coordinates"
  - "and admissibility predicates are not written as duties"
  - "bounded non-use"
  - "coordinate evidence"
  - "definitions"
  - "eligibility filters"
  - "first move"
  - "invariants"
  - "pattern quality"
  - "state agent obligations only"
  - "stop condition"
  - "typing rules"
---

### E.21:2 - Problem

FPF needs a way to evaluate pattern quality without creating a fake scalar. A single score is attractive because it is easy to compare, but it is false for this object. A pattern can be excellent in SoTA support and still unreadable; precise in ontology and still too heavy for ordinary use; concise and still wrong about neighbours.

The recurring failures are:

1. **Hidden scalarization.** Different coordinates such as recognition, ontology, SoTA, evidence, and reader cost are averaged or ranked as if they had one common unit.
2. **Template-only maturity.** Canonical headings are present, but the first working situation, first admissible move, boundary, and practical payoff remain missing.
3. **Checklist substitution.** The conformance checklist replaces the `Solution` instead of testing it.
4. **Ontology-light review.** Wording is polished while kind, relation, support, evidence, measurement, assurance, and neighbouring-pattern authority remain unstable.
5. **Decorative SoTA.** Sources are cited, but they do not change the `Solution`, conformance checks, boundaries, examples, or relations.
6. **Apparatus bloat.** A draft accumulates fields, manifests, gates, and companion files that increase author and reader cost without improving admissible use.
7. **Coordinate Goodharting.** A draft is optimized for the declared coordinates until it becomes harder to use, costlier to maintain, or less faithful to the practical value the coordinates were meant to protect.
8. **Endless improvement.** Authors keep polishing because there is no declared stop condition and no visible distinction between material improvement and cosmetic movement.

