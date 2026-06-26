---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Transformation Flow"
section_id: "C.32.P2S:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__005_solution.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Transformation Flow"
  - "C.32.P2S:4 — Solution"
line_start: 59104
line_end: 59133
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
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
  - "E.23"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
keywords:
  - "ProblemToStructureArchitecturingFlowCard@Project"
  - "actual-structure feedback"
  - "architecture work flow"
  - "owner-specific return"
  - "problem-to-structure architecturing flow"
  - "selected structures"
  - "structural uncertainty"
---

### C.32.P2S:4 - Solution

Create or update one `ProblemToStructureArchitecturingFlowCard@Project` and move through the smallest useful spine below. Stop at the first owner that fully governs the current claim; continue the P2S card only while the connected architecture flow remains the current object needing review.

Use the analogy with `E.18.1` P2W narrowly. P2W carries accepted problem and principle material into method, plan, work, and telemetry. C.32.P2S carries architecture-relevant pressure and structural uncertainty into candidate structures, selected structures, project architecture decision, realization work, actual-structure feedback, and owner-specific next actions. The analogy ends when the current claim is method, work, telemetry, publication, or improvement-loop governance; then use the receiving owner pattern rather than stretching P2S into generic process management.

1. Recover the problem pressure or architecture concern. Name the pressure kind, source signals, affected holon, and the first owner. If the source is still only a problem-side signal, use `C.22.2` before P2S continues.
2. Recover the described holon, bounded context, candidate or selected structure kinds, selected structures when available, and architecture characteristics. Use `C.30` for the grounded architecture claim, `C.32.HCS` for starter characteristic heads, `C.32.ACS` for project criteria rows, and `C.25` when a composite quality family is current.
3. Represent future-structure uncertainty. State unknown structure kinds, unknown internal composition, candidate bearers, interfaces, allocations, variation points, constraints, expected structures, and source-return conditions. Record what is captured, handed off, latent, hidden, or lost.
4. Generate architecture ideas, principles, constraints, and candidate structure changes. Use source material as candidate-generation pressure only after the affected structure, characteristic, gain, loss, and receiving owner are recoverable.
5. Synthesize candidate architecture configurations and candidate sets through `C.32`. Keep function-bearing feasibility, constructive modules, placement, control, transformation-flow, work, role, information, evidence, scale, and other selected structures visible when they change the candidate.
6. Compare, retain, publish, or return alternatives through the governing set owner. Use `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.18` and `C.19` for archive, front, and pool policy, `G.5` for publication of a selected set, and `C.11` for a fixed local choice.
7. Make a project architecture decision through `C.32.PAD` when implementation commitment is current. The decision relation names the selected architecture option, affected structures, trade-off, accepted losses, method and work consequences, source-return, and owner-specific repair or supersession condition.
8. Publish descriptions, views, ADR-like records, or other records only as descriptions or publication forms of structures, decision relations, method expectations, source-return, and reader use. Use `C.30.AD`, `C.30.ASV`, `C.32.ADR`, `E.17`, and `E.24.PUB` as applicable.
9. Hand transformer roles the method descriptions, constraints, readiness expectations, work expectations, and source-return conditions needed to realize selected structures. Use `A.15`, `A.15.2`, and `A.15.5` for method, work-plan, and readiness claims.
10. Realize selected structures in the transformed holon through domain work. Use `A.15.1` for performed work and `A.3.4` when one bounded transformation claim is current. The P2S card records refs; it does not perform the work.
11. Observe, inspect, measure, and evaluate actual selected structures, architecture-characteristic results, and functional-characteristic or capability implications in operation or use. Ask whether the realized structures enable or block the functions and effects they were meant to bear, and ask what selected structure, accepted loss, counter-characteristic, or functional implication got worse when a visible metric improved. Do not turn functional demand into an architecture characteristic or an eval result into decision authority. Use `C.32.ACE` for eval programs and eval results, `C.16` for measurement, and `C.25` for Q-bundles. Use `E.23` when repeated improvement method is current, `G.11` when currentness, telemetry, edition, freshness, or decay orchestration is current, `E.18` for transformation-flow slice-local refresh, `C.18` or `C.19` for archive, front, and pool updates, `C.32.PAD` or `C.32.ADA` for decision repair or supersession, `C.32` for new synthesis, and `C.30.AD` or `C.30.ASV` for source-return tied to descriptions or views. Feed actual-structure divergence, eval results, functional implications, freshness loss, source-return, and new constraints into the owner-specific return or repair action.

When one holon changes another holon, add the transformer/transformed branch before candidate synthesis becomes narrow. Name the changing relation, the transformer holon, the transformed holon, and selected structures on both sides when they constrain the candidate set. Use `C.32.CONWAY` to frame candidate families: change transformer-side structures, change transformed-side structures, change both, or declare a bounded mismatch with source-return.

Stop conditions:

- stop at `C.22.2` when the signal is not yet a reviewable problem-side record;
- stop at `C.30` or `C.30.ASV` when the current need is only architecture claim or structural-view adequacy;
- stop at `C.32` when the next useful artifact is a candidate palette rather than a whole P2S carry-through record;
- stop at `C.32.PAD` when the project architecture decision is current;
- stop at the A.15 family when the current question is method, work planning, readiness, or performed work;
- stop at `C.16`, `C.25`, `C.29`, `C.32.ACE`, `E.23`, or `G.11` when the current claim is measurement, quality-bundle, mathematical-lens, eval, improvement, or `G.11` currentness refresh;
- return to P2S only when a later owner returns architecture pressure that changes candidate structures, expected structures, actual structures, selected structures, or source-return.

