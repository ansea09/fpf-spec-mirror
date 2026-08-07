---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:5"
section_title: "Worked Architecture Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__006_worked-architecture-cases.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:5 — Worked Architecture Cases"
line_start: 64458
line_end: 64467
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
  - "U.Structure"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "synthesis structure map"
  - "trade-off front"
---

### C.32:5 - Worked Architecture Cases

| Grounded working case | Synthesis question | C.32 candidate work | Stop condition |
|---|---|---|---|
| Regulated product family with growing field exceptions | How should functions, module interfaces, placement, and evidence scope be configured so substitutability and certification burden stay acceptable? | Prepare candidates that narrow interface grammar, split the family by evidence scope, change placement responsibility, or keep a bounded exception with source return. | Stop at palette unless G.5 publication of a selected set, assurance, or architecture decision is current. |
| Built-asset digital-twin handover where a method-defined digital-twin view hides source loss | Which selected structures do the digital-twin dimensions actually describe, and which source-return obligations must survive maintenance use? | Prepare candidates that split information view, add source-return scope, retarget maintenance responsibility, or change module and placement structure. | Stop before built-asset architecture-description, MVPK publication-face, or A.10 evidence-relation claims unless `C.30.AD.BA`, `E.17`, `E.24.PUB`, or evidence patterns are current. |
| Emergency-department triage work arrangement whose local desk is fast but hospital-wide escalation is brittle | How should role-enactor, procedural-work, control, and evidence structures be configured so speed does not erase escalation adequacy? | Prepare candidates that retarget responsibility among role-holding systems, add a mediator role assignment, split triage scope by patient class, or adjust evidence capture. | Stop before ethical mediation, evidence, or staffing decision unless those claims are current. |
| AI-agent review setup where local autonomy conflicts with policy scope | How should control, module-interface, evidence-refresh, and work-method structures be configured so autonomy and policy conformance stay jointly acceptable? | Prepare candidates that add supervisor relation, narrow model interface behavior, change evidence refresh cadence, or alter work-method responsibility. | Stop before safety, release, gate, or causal claims unless their governing patterns are current. |
| Method family whose reusable template speeds authoring and slows review | How should method structure, authored-section structure, review evidence, and responsibility of role-holding systems under role assignments be configured so repeatability does not create hidden review residue? | Prepare candidates that split method variants, add review evidence scope, retarget role assignments, or accept bounded local method residue. | Stop before method governance, curriculum decision, description use, or publication-face use unless the receiving pattern is current. |

