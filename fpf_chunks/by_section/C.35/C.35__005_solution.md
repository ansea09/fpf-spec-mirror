---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Structural Synthesis and Discovery Adequacy"
section_id: "C.35:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__005_solution.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "C.35 — Structural Synthesis and Discovery Adequacy"
  - "C.35:4 — Solution"
line_start: 67637
line_end: 67659
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

Read the note as an admission check between generation and architecture work. The generated output can be useful only after the record says what it carries, what it drops, and which governing pattern can use it next.

`carrierAdmissionReturnCondition` names the produced carrier or description, the described selected structure, preserved structure, lost structure, missing structure, the candidate-admission condition, and the receiving governing pattern or receiving claim that must reopen before the carrier can support the next architecture use.

Work in this order:

1. Name the grounded architecture question and selected source structure refs. If no grounded architecture question exists, return to `C.30`, `C.32.P2S`, or `C.32`.
2. Name the generation or discovery Method and search or query space: DSM, MDM, MBSE query, graph grammar, model transformation, LLM proposal, NAS, DSE, QD archive, code-agent probe, simulation, benchmark, or source-mining method. When actual performed generation or discovery is part of the claim, separately name the dated `U.Work`, its exact A.15.1/F.6 basis, and the direct production, discovery-use, or work-to-change claim on which this note relies.
3. Separate produced carrier or description from described structure. The carrier may be a diagram, table, graph, query result, cluster, model file, prompt output, or benchmark trace. Naming it as produced does not by itself establish which Work produced it, entity-identity inception, production completion, or a relation to an actual transformation; cite the exact direct or local claim when any of those assertions is current.
4. State preserved structure, lost structure, constraints, source-label recovery, observation and uncertainty refs, validation or comparison refs, and transformation trace when present. If an actual change is claimed, also cite the independently identified A.3.4 `U.Transformation`; the trace and the selected A.22 structures remain separate from that occurrence.
5. State candidate-admission condition. Route to `C.32` only when the described structure can be used as a candidate configuration or candidate-generation input under selected structures, architecture characteristics, constraints, gains, losses, and carrier-admission return.
6. State bearer or realization boundary. Use `bearerFeasibilityQuestionRef?` only when the direct governing pattern has opened a separate software, physical, organizational, method, role, or epistemic bearer-feasibility question.
7. Route selected-set publication, archive, front, and pool policy to `G.5`, `C.18`, or `C.19`.
8. Route eval programs and eval results to `C.32.ACE`; route measurement to `C.16`; route mathematical-lens use to `C.29`; route descriptions and views to `C.30.AD` or `C.30.ASV`; route decisions and ADR projections to `C.32.PAD` or `C.32.ADR`.
9. Route reusable generator or mechanism-suite governance to `E.20`, `G.1`, `G.10`, `G.11`, or another selected governing pattern only after that reusable-generator object has been selected as the current governed object.
10. Stop when admissible use, non-admissible use, carrier-admission return condition, receiving governing pattern, and receiving claim kind are named.

CGUS-aware neighbor use: when the produced carrier is useful because it describes, compresses, or demonstrates a constraint-governed unfolding structure, C.35 admits only the produced carrier for the declared architecture use. The unfolding structure itself remains governed by `A.22.CGUS`, `E.18.3`, `C.32.P2S`, `A.6.3.NAR`, `E.23`, or another local governing pattern. If the produced object is only a route card, narrative sequence, demonstrative slice, or generated framework carrier, name it as a carrier or `DemonstrativeUnfoldingSlice@Context` before making any selected-structure claim about the `U.Structure` it presents.

