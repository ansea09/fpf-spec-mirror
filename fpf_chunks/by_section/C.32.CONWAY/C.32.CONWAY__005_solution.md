---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Transformer and Transformed Architecture Correspondence"
section_id: "C.32.CONWAY:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__005_solution.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.32.CONWAY — Transformer and Transformed Architecture Correspondence"
  - "C.32.CONWAY:4 — Solution"
line_start: 64214
line_end: 64257
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.3.4"
  - "A.3.4.P"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.29"
  - "C.30"
  - "C.32"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.18"
  - "G.5"
keywords:
  - "Conway correspondence"
  - "changing relation"
  - "coordination cost"
  - "inverse Conway maneuver"
  - "selected-structure correspondence"
  - "transformed holon"
  - "transformer holon"
---

### C.32.CONWAY:4 - Solution

Build a correspondence frame before treating Conway or inverse Conway as guidance.

Work in eight steps:

1. Name the changing relation. Use `A.3.4` when one bounded transformation is being claimed, `E.18` when a transformation-flow structure is being claimed, or the direct work and method patterns when the claim is work or method use.
2. Name the transformer holon and the transformed holon. Keep their architectures distinct even when they belong to one larger holon.
3. Map only the selected structures that carry the constraint or option shaping the candidate frame. On the transformer side, name the actual structure that makes one transformed-holon architecture feasible or infeasible. On the transformed side, name the actual structure that must carry the desired function or architecture characteristic. Stop at the smallest pair that can change the candidate frame or the later comparison input.
4. State only the architecture characteristics that can change the comparison. Use the local q-bundle when possible; otherwise name the few characteristics under pressure, such as independent change, substitutability, evidence reuse, latency, coupling, cohesion, coordination load, or source-return cost.
5. State the correspondence claim. Say which transformer-side selected structure constrains or enables which transformed-side selected structure, what is preserved, what is hidden or lost, and which receiving pattern governs the next claim.
6. Generate candidate architecture configurations:
   - change the transformer-side structure so the desired transformed architecture becomes feasible;
   - change the transformed-side architecture to fit a transformer constraint that is not worth changing now;
   - change both sides as one co-synthesis candidate;
   - keep a bounded mismatch with exception cost, source-return condition, and reopen trigger.
7. Use `C.29` only when the correspondence is claimed as structural similarity, homomorphism-like mapping, equivalence, or formal preservation. Otherwise keep it as architecture synthesis material.
8. Stop when the C.32 candidate palette contains the fields required by `A.19.CPM` explicit comparison, `C.32.MLAO` residual reduction, `C.32.FAIL` repair, publication of a selected set under `G.5`, `C.11` choice, or `C.32.PAD`.

Correspondence repair rows are local C.32.CONWAY entries. They do not create new FPF kinds.

| Correspondence repair row | Use | Minimum repair against overread |
|---|---|---|
| `changingRelationRecovery` | The case names a designer, team, line, tool, method, or organization before the changed object and change relation are clear. | Recover the bounded transformation, work, method-use, or transformation-flow relation before making an architecture claim. |
| `transformerStructureMapping` | A selected structure of the changing holon makes one transformed architecture feasible or infeasible. | Keep the selected transformer structure distinct from the transformed-holon architecture. |
| `transformedStructureMapping` | A selected structure of the changed holon must carry the desired function or architecture characteristic. | Name the selected transformed structure and the architecture characteristic it must support. |
| `inverseConwayRetargeting` | The desired transformed architecture is sound, but the changing holon cannot produce or sustain it. | Change transformer-side selected structures and record migration cost, new burden, and stop condition. |
| `transformedArchitectureRetargeting` | The transformer-side structure is fixed or expensive to change in the declared evolution window. | Change the transformed architecture candidate and record the lost desired property or exception. |
| `jointCorrespondenceSynthesis` | Neither side alone can carry the architecture characteristic. | Create a candidate that changes both sides and records preserved structure, lost structure, and coordination burden. |
| `boundedCorrespondenceMismatch` | A mismatch is tolerable for now. | State exception cost, bounded-use limit, source-return condition, and reopen trigger. |

**Didactic mini-slices.**

| Situation | C.32.CONWAY repair row | Candidate repair |
|---|---|---|
| A field-device family wants replaceable modules, but the manufacturing line and certification evidence are organized by full-product batches. | Name manufacturing and certification as transformer-side selected structures; name module-interface and evidence-scope structures on the transformed side. | Either change cells and evidence roles, change module split, or keep a bounded batch exception with certification cost. |
| A software group wants independently deployable services, but every release still crosses a shared test environment and shared approval role. | Treat team, work, test, and approval structures as transformer-side constraints; treat service and deployment structures as transformed-side structures. | Use inverse Conway retargeting for team and test responsibility, or choose a less independent service architecture for this evolution window. |
| A reusable review method changes authored specifications, but no role carries exception evidence after automated checks. | Treat the review method and exception role as transformer-side selected structures; treat authored-section and evidence-scope structures as transformed-side structures. | Add an exception role and evidence scope, change the method step, or reject the automation candidate. |
| An AI-agent toolchain changes project tasks, but policy control and evidence refresh remain outside the tool boundary. | Treat toolchain module, control, and evidence-refresh structures as transformer-side structures; treat task architecture and policy-conformance evidence as transformed-side structures. | Add supervisor relation and evidence refresh, change task decomposition, or keep bounded autonomy with source-return trigger. |

**Stop condition.** Stop when the frame names both holons, the changing relation, selected structures on both sides, architecture characteristics under pressure, candidate changes, known losses, receiving patterns, and source-return conditions.

**Lowering condition.** Keep a correspondence claim as C.32.CONWAY synthesis material only while the changing relation, both holons, both selected structures, affected architecture characteristics, preserved structure, lost or hidden structure, evolution window, and receiving pattern remain current. Lower the claim to diagnostic pressure when one of those values is unknown, stale, or outside the current synthesis question. Retire a candidate configuration when its transformer-side change, transformed-side change, bounded mismatch, or known loss no longer belongs to the declared evolution window. Return to `A.3.4` or `E.18` when the changing relation is not recovered, to work or organization-governance patterns when no transformed-holon architecture characteristic is under pressure, and to `C.29` when the current claim is structural similarity, preservation, mapping, or equivalence.

