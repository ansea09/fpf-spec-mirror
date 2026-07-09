---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Unfolding"
section_id: "C.32.P2S:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Unfolding"
  - "C.32.P2S:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 60320
line_end: 60330
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22.CGUS"
  - "A.3.4"
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
  - "expected structures"
  - "governing-pattern-specific return"
  - "problem-to-structure architecturing unfolding"
  - "selected structures"
  - "structural uncertainty"
---

### C.32.P2S:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Description stop | The project stops after producing a view set, diagram, ADR-like record, or architecture description even though no candidate structure, decision, realization, or feedback path is recoverable. | Return to step 2 or 5. Name selected or unknown structures, architecture characteristics, and the next governing pattern: `C.30`, `C.30.ASV`, `C.32`, or `C.32.PAD`. |
| Relation index P2S | The P2S artifact lists neighboring patterns but does not tell the architect what to do from pressure to realized selected structures. | Write the positive action spine in the card: pressure, structures, uncertainty, candidates, retention or selection, decision, descriptions, method and work handoff, realized structures, feedback, and governing-pattern-specific return. |
| Eval-as-decision | An eval result, score, metric, telemetry event, or dashboard value selects the architecture. | Route the eval to `C.32.ACE`, measurement to `C.16`, and composite quality to `C.25`; ask what selected structure, accepted loss, counter-characteristic, or functional implication worsened; then use comparison, selected-set, local-choice, or `C.32.PAD` if selection or decision is current. |
| Hidden transformer | The transformed holon is designed as if the changing holon has no architecture. | Open the transformer/transformed branch and `C.32.CONWAY`; add candidate families that change transformer-side structures, transformed-side structures, both, or a bounded mismatch. |
| Lost structure left silent | The description, decision, method handoff, or eval report compresses away distinctions needed for later work. | Fill the P2S structural-information slots: what is captured, handed off, latent or hidden, lost, and what stronger-structure inspection return condition restores the selected or expected structure needed by the next claim. |
| Work governing-pattern takeover | P2S prose starts authorizing work or replacing method, readiness, work-plan, or performed-work records. | Keep P2S as architecture carry-through. Send method and work claims to A.15-family patterns and record only refs plus expected selected-structure effects. |

