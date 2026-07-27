---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Unfolding"
section_id: "C.32.P2S:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Unfolding"
  - "C.32.P2S:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 63765
line_end: 63777
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.15.PROD"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.RCD"
  - "B.2"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.2"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.18"
  - "E.18.3"
  - "E.23"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
keywords:
  - "ArchitectureUnfoldingStructureUse@Project"
  - "ProblemToStructureArchitecturingFlowCard@Project"
  - "actual-structure feedback"
  - "candidate structures"
  - "exact domain work"
  - "expected structures"
  - "governing-pattern-specific return"
  - "independently grounded actual changes"
  - "no-automatic-composition"
  - "problem-to-structure architecturing unfolding"
  - "selected structures"
  - "structural uncertainty"
  - "subject-side actual structures"
---

### C.32.P2S:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Description stop | The project stops after producing a view set, diagram, ADR-like record, or architecture description even though no candidate structure, decision, realization, or feedback path is recoverable. | Return to step 2 or 5. Name selected or unknown structures, architecture characteristics, and the next governing pattern: `C.30`, `C.30.ASV`, `C.32`, or `C.32.PAD`. |
| Relation index P2S | The P2S artifact lists neighboring patterns but does not tell the architect what to do from pressure to subject-side actual structures recovered from directly governed obtaining facts. | Write the positive action spine in the card: pressure, structural uncertainty, candidates, retention or selection, decision, descriptions, method and work handoff, exact work, actual changes, subject-side actual structures, feedback, and governing-pattern-specific return. |
| Eval-as-decision | An eval result, score, metric, telemetry event, or dashboard value selects the architecture. | Route the eval to `C.32.ACE`, measurement to `C.16`, and composite quality to `C.25`; ask what selected structure, accepted loss, counter-characteristic, or functional implication worsened; then use comparison, selected-set, local-choice, or `C.32.PAD` if selection or decision is current. |
| Hidden transformer | The transformed holon is designed as if the changing holon has no architecture. | Open the transformer/transformed branch and `C.32.CONWAY`; add candidate families that change transformer-side structures, transformed-side structures, both, or a bounded mismatch. |
| Lost structure left silent | The description, decision, method handoff, or eval report compresses away distinctions needed for later work. | Fill the P2S structural-information slots: what is captured, handed off, latent or hidden, lost, and what stronger-structure inspection return condition restores the selected or expected structure needed by the next claim. |
| Work governing-pattern takeover | P2S prose starts authorizing Work occurrences or replacing method, readiness, WorkPlan, or separate assertion/record epistemes about performed work. | Keep P2S as architecture carry-through. Send method and work claims to A.15-family patterns and keep in the P2S card only references plus expected selected-structure effects. |
| Selected structure treated as actual | A decision, model, description, view, evaluation result, or matching label is used as proof that the selected structure obtains. | Recover the exact subject-side `U.Structure` under `A.22` from its declared substrate and directly governed obtaining relation, constraint, invariant, or other selected-organization facts; use `C.30` only for the corresponding `ArchitectureOf@Context` claim. Keep description and evaluation separately governed and test conformance only through its direct owner. |
| Common work treated as one composite transformation | Mounting, wiring, connection, or commissioning changes are merged because one assembly work occurrence, selected configuration, or time interval contains them. | Identify every actual transformation independently under `A.3.4`; cite direct work-to-change facts; return the exact missing-governor blocker if the receiving claim needs transformation composition. |

