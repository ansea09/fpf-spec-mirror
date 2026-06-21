---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:13"
section_title: "Bias-Annotation (per E.8 SG-bias slot)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__008_bias-annotation-per-e-8-sg-bias-slot.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:13 — Bias-Annotation (per E.8 SG-bias slot)"
line_start: 69919
line_end: 69928
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "P2W support"
  - "composition"
  - "crossings"
  - "flow valuation"
  - "guards"
  - "selected transformations"
  - "transformation flow structure"
---

### E.18:13 - Bias-Annotation (per E.8 SG-bias slot)

* **Acyclic-bias risk.** Tooling accustomed to DAGs may discourage admissible feedback loops; E.18 explicitly permits loops with budget/sentinel controls (CC-E18-13, -18).
* **Scalarization-bias risk.** Cultural defaults to single-score rankings can suppress Pareto/QD sets; E.18 keeps declared order relations and return sets visible (CC-E18-10, CC-E18-12).
* **Interop-dominance risk.** File/format ecosystems (CWL/RO-Crate/lineage) can be mistaken for semantic sources; E.18 places them in **InteropCard** and keeps governing semantics in loci/gates.
* **Over-formalization risk.** Category-theoretic formalisms can obscure operational guard-rails; E.18 grounds crossings in Bridge/UTS/CL/Phi pins and SquareLaw audits (CC-E18-11, -17).
* **Retrospective rewrite risk.** Global rewrites break replay; E.18 confines them to edition bumps and slice-local refresh (CC-E18-16).

**Mitigations.** Profile-gated publication, audit of `DecisionLog`, mandatory edition pins, Lean-to-Core upgrade conditions, and conformance tests tied to PathSlice replay.

