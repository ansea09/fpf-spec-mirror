---
chunk_kind: "child"
pattern_id: "A.19.CHR"
pattern_title: "CHRMechanismSuite: Shared Rules for Characterization and Selection"
section_id: "A.19.CHR:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CHR/A.19.CHR__011_rationale.md"
commit_sha: "d5df418106507cff0972788834c0bf8825597de0"
heading_path:
  - "A.19.CHR — CHRMechanismSuite: Shared Rules for Characterization and Selection"
  - "A.19.CHR:10 — Rationale"
line_start: 37364
line_end: 37375
dependencies:
  - "A.15.2"
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.21"
  - "A.6.1"
  - "A.6.7"
  - "A.6.RCD"
  - "C.23"
  - "E.10"
  - "E.18"
  - "E.19"
  - "G.0"
  - "G.10"
  - "G.5"
keywords:
  - "CG-Spec"
  - "CHR suite"
  - "CN-Spec"
  - "P2W seam"
  - "SlotFillingsPlanItem"
  - "admissibility conditions"
  - "applicable correspondence and crossing conditions"
  - "characterization core"
  - "crossing visibility"
  - "model-bound assurance penalties"
  - "no hidden scalarization"
  - "no hidden thresholds"
  - "planned baseline"
  - "set-return selection"
  - "suite obligations"
  - "tri-state guard decision"
---

### A.19.CHR:10 - Rationale

The suite description records membership and shared conditions, while each member declaration supplies its own operation contract. This arrangement has four consequences:

1. **Member contracts remain distinct.** The suite is a D-episteme that enumerates mechanisms and obligations. Each A.6.1 member declaration retains its arguments, results, laws and admission conditions.

2. **Spec refs remain centralized.** CN-Spec and CG-Spec state the applicable comparison, normalization, indicator-choice and numeric-admission conditions. The suite cites those specifications without copying their content.

3. **P2W integration becomes explicit without turning planning into execution.** Ordinary A.15.2 content records the edition/reference baseline. Typed A.15.3 filling is needed only for an independently declared position; only enactment supplies actual bindings and launch witnesses.

4. **Uncertainty has an explicit disposition.** Tri-state guard decisions distinguish passing, qualified degradation and abstention. Safety of a receiving use still depends on its evidence and policy; a decision token supplies no missing ground. Gate decisions and decision logs remain with OperationalGate(profile).

