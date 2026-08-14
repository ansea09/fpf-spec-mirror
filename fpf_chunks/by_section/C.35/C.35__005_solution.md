---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Structural Synthesis and Discovery Adequacy"
section_id: "C.35:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__005_solution.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.35 — Structural Synthesis and Discovery Adequacy"
  - "C.35:4 — Solution"
line_start: 68255
line_end: 68277
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.1"
  - "A.22"
  - "A.3.4"
  - "A.6.M"
  - "A.6.RCD"
  - "C.16"
  - "C.18"
  - "C.19"
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
  - "C.32.ACS"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.36"
  - "E.18"
  - "F.6"
  - "G.5"
keywords:
  - "DSM"
  - "LLM"
  - "NAS"
  - "candidate admission"
  - "described structure"
  - "generated carrier"
  - "produced carrier"
  - "source return"
  - "structural discovery"
  - "structural synthesis"
---

### C.35:4 - Solution

Create one `StructuralSynthesisDiscoveryAdequacyNote@Project` before admitting the output into candidate synthesis, evaluation, publication, decision, or realization claims.

Read the note as an admission check between generation and architecture work. The generated output can be useful only after the record says what it carries, what it drops, which next architecture use it may support, and under what rule.

`carrierAdmissionReturnCondition` names the produced carrier or description, the described selected structure, preserved structure, lost structure, missing structure, the candidate-admission condition, and the next claim or question plus its required rule or test that must be revisited before the carrier can support the next architecture use.

Work in this order:

1. Name the grounded architecture question and selected source structure refs. If no grounded architecture question exists, require `C.30`, `C.32.P2S`, or `C.32`.
2. Name the generation or discovery Method and search or query space—for example, a DSM, MDM, MBSE query, graph grammar, model transformation, LLM proposal, NAS, DSE, QD archive, code-agent probe, simulation, benchmark, or source-mining method. When actual performed generation or discovery is part of the claim, separately name the dated `U.Work`, keep all facts required by A.15.1, A.2.1, and F.6 recoverable, and name the production, discovery-use, or work-to-change claim on which this note relies.
3. Separate produced carrier or description from described structure. The carrier may be a diagram, table, graph, query result, cluster, model file, prompt output, or benchmark trace. Naming it as produced does not by itself establish which Work produced it, entity-identity inception, production completion, or a relation to an actual transformation; cite the predicate or local claim that establishes any such assertion.
4. State preserved structure, lost structure, constraints, source-label recovery, observation and uncertainty refs, validation or comparison refs, and transformation trace when present. If an actual change is claimed, also cite the independently identified A.3.4 `U.Transformation`; the trace and the selected A.22 structures remain separate from that occurrence.
5. State candidate-admission condition. Use `C.32` only when the described structure can be used as a candidate configuration or candidate-generation input under selected structures, architecture characteristics, constraints, gains, losses, and carrier-admission return.
6. State bearer or realization boundary. Use `bearerFeasibilityQuestionRef?` only when a concrete software, physical, organizational, Method, or epistemic bearer-feasibility rule has opened that separate question. If the source says `role`, recover its actual bearer or relation through `E.10.ROLE`; a local kind or assignment bears no function merely by form. Name the function or feasibility predicate, conditions, and subject pattern, or return `missing-governor`.
7. Use `G.5` for selected-set result declaration, `C.18` and `C.19` for archive, front, and pool policy, `E.17` for a source-backed publication face and source return, and `E.24.PUB` for the publication occurrence and audience availability.
8. Handle eval programs and eval results under `C.32.ACE`; handle measurement under `C.16`; handle mathematical-lens use under `C.29`; handle descriptions and views under `C.30.AD` or `C.30.ASV`; handle decisions and ADR projections under `C.32.PAD` or `C.32.ADR`.
9. Handle reusable-generator or mechanism-suite claims with `E.20`, `G.1`, `G.10`, `G.11`, or another pattern that defines or constrains the generator claim, only after that reusable-generator object is current.
10. Stop when admissible use, non-admissible use, carrier-admission return condition, the next claim or question, and its required rule or test are named.

CGUS-aware neighbor use: when the produced carrier is useful because it describes, compresses, or demonstrates a constraint-governed unfolding structure, C.35 admits only the produced carrier for the declared architecture use. The unfolding structure itself remains governed by `A.22.CGUS`, `E.18.3`, `C.32.P2S`, `E.23`, or another direct structure pattern. If the produced object is only a route card, narrative sequence, demonstrative slice, or generated framework carrier, name it as a carrier or `DemonstrativeUnfoldingSlice@Context` before making any selected-structure claim about the `U.Structure` it presents. When it is a narrative sequence, `A.6.3.NAR` governs only the selected-source carry-through, ordering and connective account, loss, reader use, and return.

