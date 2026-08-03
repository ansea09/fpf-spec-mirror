---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:6.1"
section_title: "Bias-Annotation (per E.8 SG-bias slot)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__008_bias-annotation-per-e-8-sg-bias-slot.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:6.1 — Bias-Annotation (per E.8 SG-bias slot)"
line_start: 83353
line_end: 83362
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.18.NET"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.18:6.1 - Bias-Annotation (per E.8 SG-bias slot)

* **Acyclic-bias risk.** Tooling accustomed to DAGs may discourage admissible feedback loops; E.18 explicitly permits loops with budget and sentinel controls (CC-E18-13, -18).
* **Scalarization-bias risk.** Cultural defaults to single-score rankings can suppress Pareto fronts and QD archives; E.18 keeps declared order relations and return sets visible (CC-E18-10, CC-E18-12).
* **Interop-dominance risk.** File and format ecosystems (CWL, RO-Crate, and lineage) can be mistaken for semantic sources; E.18 places them in **InteropCard** and keeps governing semantics in loci and gates.
* **Over-formalization risk.** Category-theoretic formalisms can obscure operational guard-rails; E.18 grounds crossings in exact positions, changed state bindings, direct governors, one A.21 gate, and a replayable `CrossingRef` (CC-E18-11, -23).
* **Retrospective rewrite risk.** Global rewrites break replay; E.18 confines them to edition bumps and slice-local refresh (CC-E18-16).

**Mitigations.** Profile-gated publication, audit of `DecisionLog`, mandatory edition pins, Lean-to-Core upgrade conditions, and conformance tests tied to PathSlice replay.

