---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__013_relations.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:12 — Relations"
line_start: 67323
line_end: 67348
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.19.1"
  - "C.22.1"
  - "C.24"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.23:12 - Relations

| Pattern | Relation |
|---|---|
| `A.19.ECS` | Constructs or repairs an object-under-improvement evaluation `CharacteristicSpace` when no adequate object-under-improvement evaluation exists for the object being improved. `E.23` starts only after that evaluation is declared. |
| `E.22` | Frames each quality review inside the loop and can return one candidate improvement proposal or a bounded proposal portfolio. `E.23` governs repetition, absorption, object-version-under-improvement change, re-read, method-family selection, and decisions to stop, narrow, continue, switch method, or hold for more exact information. |
| `E.21` | Receives FPF pattern-quality reads. `E.23` can improve one pattern version under `E.21`, but `E.21` supplies coordinates, values, statuses, and stop meanings. |
| `E.9.DA` | Receives `DRR` decision-adequacy reads. `E.23` can improve one `DRR` under a declared authoring use, but the result remains a decision record, not a prewritten pattern. |
| `E.2.DA` | Receives whole-FPF or FPF-corpus Pillar-adequacy reads. `E.23` can improve that FPF object under improvement under `E.2.DA`, but `E.2.DA` supplies Pillar coordinates, values, and stop meanings. |
| `F.18` | Receives durable-name and term-improvement reads through its local lexical quality vector. `E.23` can improve naming candidates under `F.18`, but `F.18` supplies naming coordinates, candidate-front discipline, and name-card meanings. |
| `C.25` | May supply the Q-Bundle endpoint for engineering quality-family objects under improvement. `E.23` does not create one universal quality score. |
| `A.6.Q` | Repairs load-bearing ambiguous `quality` wording before a loop can rely on it. `A.6.Q` is not the loop method. |
| `C.19.1` | Governs BLP method preference and waiver discipline for general adaptive versus specialized method families. |
| `C.22.1` | Carries durable task-family adaptation-signature claims produced through an `E.23` loop when threshold, time-to-threshold, budget-to-threshold, prior exposure, transfer, retention, downside, or corridor-entry claims are live. |
| `C.24` | Governs call plans, checkpoint returns, tool-call budgets, stop or replan conditions, and separation between call plan and executed work when an `E.23` loop is enacted through tool-using agents. |
| `E.18` | Supplies transduction graph, path, crossing, flow-valuation, and declared transduction-result context when the object under improvement is produced by a transduction. |
| `C.17` | Governs candidate novelty, use-value, surprise, constraint fit, diversity, originality, and resource-efficiency characterization when those are live for OEE/NQD improvement. |
| `C.18` | Governs NQD generation, descriptor and distance pins, archive and front semantics, and illumination telemetry. `E.23` may improve `Q` movement for one object under improvement but does not govern `C.18` semantics. |
| `C.19` | Governs live candidate-pool policy. `E.23` does not decide whether to widen, keep frontier, narrow, sunset, or reroute the pool. |
| `G.5` | Governs selected-set publication, including `Shortlist`, `RankedShortlist`, narrowed handoff, abstain, and escalation results. |
| `G.9` | Governs parity and benchmark comparison over selected sets, archives, fronts, or method families when those claims are live. |
| `G.11` | Governs refresh of shipped set results, archive telemetry, parity reports, or OEE/NQD pins. |
| `C.11` | Governs local decision value when proposal rows become an explicit choice among alternatives rather than a loop-internal object-version change. |
| `A.10`, `B.3`, `A.20`, `A.21`, `A.15` | Govern evidence, assurance, local CV status, gates, and work when a loop result is reused for project-side claims. `E.23` blocks that overread unless the exact neighbouring pattern is opened. |
| `E.10`, `A.6.P`, `C.2.P`, `F.18` | Repair load-bearing wording and names introduced by a loop record. `E.23` does not accept source, authority, basis, support, record, view, object under improvement, or quality as umbrella substitutes for exact kinds and relations. |

