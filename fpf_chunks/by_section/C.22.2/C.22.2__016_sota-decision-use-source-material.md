---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard"
section_id: "C.22.2:15"
section_title: "SoTA Decision-Use Source Material"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__016_sota-decision-use-source-material.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "C.22.2 — ProblemCard"
  - "C.22.2:15 — SoTA Decision-Use Source Material"
line_start: 52022
line_end: 52049
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.22.PFR"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.MOVE"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.18.1"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
---

### C.22.2:15 - SoTA Decision-Use Source Material

The following external anchors are adopted or adapted only where they change this pattern's local answer by value.

| Current source or relation line | Reference | Pattern use | Disposition |
|---|---|---|---|
| Problem framing turns an ill-structured situation into a solvable design problem and requires care because "framing" is ambiguous. | 2025 CEEA paper "Towards a Theoretical Framework of Framing in Engineering Design", `https://doi.org/10.24908/pceea.2025.19713` | Contributes deconfliction of symptom, situation, framed problem representation, and task. | Adopted as field and kind-recovery cue; wording is expressed in current FPF terms. |
| Strategic problem framing distinguishes symptoms and attention allocation from causal problem formulation. | 2025 Organization Science article "Looking at the Trees to See the Forest: Construal Level Shift in Strategic Problem Framing and Formulation", DOI suffix `2024.19134`, `https://doi.org/10.1287/orsc.2024.19134` | Motivates the fields for problem signal, problem hypothesis/cause-theory cue, and improvement check. | Adapted; causal claims still apply `C.28` plus evidence, provenance, or assurance patterns when current. |
| QD and OEE work motivates collections, fronts, archive retention, set-return, and non-single-winner treatment. | 2026 survey "A survey on Quality-Diversity optimization: Approaches, applications, and challenges", `https://www.sciencedirect.com/science/article/pii/S2210650225003979`; QD-as-MOO reference `https://arxiv.org/abs/2602.00478` checked 2026-05-20 | Motivates set-source-reference and Goldilocks docking into current `C.18`, `C.19`, `G.5`, `G.9`, `G.11`, `A.6.P:7a`, and `C.16.Q`. | Adopted as field and relation cue; no local QD or OEE vocabulary or scalar readiness score is introduced. |
| Open-ended coding agents use archives, self-improvement, problem variants, evaluator feedback, and stepping-stone retention. | Darwin Godel Machine `https://arxiv.org/abs/2505.22954`, FrontierSmith `https://arxiv.org/abs/2605.14445`, and AlphaEvolve `https://arxiv.org/abs/2506.13131`, all checked 2026-05-20 | Contributes record-form, set-source reference, Goldilocks, safe-probe, and freshness fields and relation references for archive, problem generation, safe probes, evaluator feedback, no-change and abstain dispositions, and autonomy and evidence boundaries. | Adapted as recent trend cue; `C.22.2` is not turned into AI-agent doctrine or an AI-agent management pattern. |
| External AI-agent and autonomy practice more often makes evidence, log, gate, autonomy-budget, and update-discipline claims current. | Presented material plus current FPF autonomy, evidence, and gate patterns | Motivates governing-pattern assignment for validation, AI-agent cues, and safe probing. | Non-FPF-governed for the center of `C.22.2`; FPF-governed content remains with `E.16`, `A.21`, `A.10`, `G.6`, `B.3`, `A.15`, and `G.11`. |

If a `C.22.2` use carries a wider external claim than these dispositions, the claim is outside this pattern and requires a separate content decision or demotion to a non-FPF-governed example.

Each FPF-governed SoTA use is recovered as a local test: source idea, FPF invariant, practitioner check, and popular shortcut rejected. A source citation without that local test is not enough to carry pattern use.

Local SoTA-to-action tests:

| Source or relation cue | Popular shortcut rejected | Required local result | Reopen condition |
|---|---|---|---|
| Problem framing is ambiguous and abstraction shifts matter. | Symptom, root-cause story, request, or ticket is treated as the problem. | Recover signal, framed problem representation, EntityOfConcern, effective ReferenceScheme, ClaimScope, viewpoint qualification, improvement check, and rival formulation when current. | Reopen when scheme, scope, viewpoint, rival formulation, evidence need, or improvement or acceptance probe changes. |
| P2W uses only a reviewable problem-side record. | `P2W-ready` is treated as Work authorization, gate passage, method selection, evidence proof, assurance, or selected solution. | State problem-formulation follow-up reason, validation boundary, readiness disposition, retained P2W use, blocked attempted use, and governing-pattern cue when an outside claim is current. | Reopen when the signal, EntityOfConcern, ReferenceScheme, ClaimScope, acceptance probe, follow-up reason, validation boundary, freshness, or named outside claim changes. |
| QD, OEE, and set-return work produce archives, fronts, pools, and selected sets. | Priority score, single winner, local problem portfolio, or local selected-set claim. | Preserve `sourceSetRef`, source set kind, selection or retention criterion, and a non-scalar next use; apply the governing set, parity, archive, pool, or refresh pattern when current. | Reopen when the source set, retention criterion, parity relation, archive, pool, front, selected set, budget, window, or freshness disposition changes. |
| Open-ended agents, problem variants, evaluator feedback, and stepping stones change signal interpretation. | Agent output, evaluator trace, or generated variant is treated as enough to act. | Record generator, evaluator, variant, or stepping-stone reason source only as a problem-side cue; name validation, freshness, and pattern reference named by value before probe or action. | Reopen when generator, evaluator, variant, stepping-stone reason source, safety condition, probe condition, or pattern reference named by value changes. |
| First-principles or mathematical structure can improve formulation. | A named formalism or mathematical or ontological prestige is treated as adequacy or rigor. | Record the candidate structure, either its relation to the problem-side EntityOfConcern or the `C.29` mathematical-lens-use relation, preserved and lost structure when current, practical formulation payoff, problem-formulation follow-up reason, and stop condition. | Reopen when candidate structure, preserved or lost structure, problem-formulation follow-up reason, stop condition, or `C.29` result changes. |
| Early class or kind taxonomy looks available. | A class list or ontology-first taxonomy is treated as the problem formulation. | Keep the formulation question current; record candidate structure, preserved and lost structure when current, and representation or retargeting relations before freezing kind structure. | Reopen when formulation question, kind structure, relation, representation-transition relation, or retargeting relation changes. |
| Object model looks clarifying. | Object-model clarity freezes the wrong EntityOfConcern or relation. | Keep EntityOfConcern and relation reviewable; name representation-transition, retargeting, or bridge relation references before reusing a local cue or readiness disposition. | Reopen when EntityOfConcern, relation, view, bridge relation, or representation-transition relation changes. |

