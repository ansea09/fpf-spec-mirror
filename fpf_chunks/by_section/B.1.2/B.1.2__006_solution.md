---
chunk_kind: "child"
pattern_id: "B.1.2"
pattern_title: "System Aggregation and Holon Delimitation"
section_id: "B.1.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.2/B.1.2__006_solution.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "B.1.2 — System Aggregation and Holon Delimitation"
  - "B.1.2:4 — Solution"
line_start: 35782
line_end: 35837
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.19"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.1"
  - "B.2"
  - "B.3"
  - "C.11"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.AD.BA"
  - "C.32.PAD"
  - "E.17"
keywords:
---

### B.1.2:4 - Solution

Use B.1.2 to coordinate one named system-aggregation or delimitation decision across independently governed results. Do not introduce `SystemAggregationRelation@Context`, `HolonDelimitationRelation@Context`, `HolonBoundaryCrossingRelation@Context`, or another record-shaped relation merely to hold the answers together.

#### B.1.2:4.1 - Recover Each Direct Result Or Blocker

| Working question | Direct owner | Exact result or stop |
| --- | --- | --- |
| Which exact whole is being considered? | `A.1` and the kind-specific owner | One exact entity recognized under the already admitted `U.System` kind; or the exact entity, six constructive components, kind-specific condition, and `true | false | unknown` evaluation needed for recognition; otherwise the missing recognition basis. |
| Which constituents are parts, portions, phases, or members, and how do they assemble? | `A.14`, the exact part-relation specialization, and `C.13` for constructive assembly grounding | Exact obtaining part-relation occurrences and the assembly they support; otherwise the missing direct governor, participant identity, obtaining fact, or assembly basis. |
| Which facts and selected boundary-use claim delimit the system for this decision? | `A.1` for system identity; `A.14`, the exact part-relation specialization, and `C.13` for parthood and assembly; every exact crossing-relation owner for external participants; `C.11` for a local choice among already available boundary readings; `C.32.PAD` for a post-synthesis architecture decision concerning exact project Work; `C.2.1` only for a separately persistent claim | First return exact identity, obtaining parthood and assembly, and crossing facts. If those facts answer the question, stop. If the named use additionally selects a boundary reading, return the C.11 `ChoiceResult` or C.32.PAD `ArchitectureDecisionRelation@Project` that makes its inclusion, exclusion, identity-preservation, and use claim current. Another choice branch passes only after its admitted direct decision owner and result are named; otherwise return the exact missing owner, participant, obtaining fact, decision governor, or information blocker. When durable reliance is needed, one separate C.2.1 episteme states that claim and cites its basis; it creates none of the world facts. A selected `U.Structure` remains a separate B.1.2:4.2 branch. |
| Which relation crosses the selected boundary? | The direct source, supply, flow, coupling, control, measurement, evidence, publication, transformation, commitment, or other relation owner; `F.9` only for the current crossing or bridge wording claim | One exact obtaining relation occurrence with its participant bindings and direct predicate; otherwise the missing governor, endpoint, binding, or obtaining fact. |
| Which function is realized by which bearer? | `A.6.F`, `A.6.M`, and the exact architecture, allocation, or parthood owner | Separate exact function, bearer, allocation or correspondence, and any obtaining parthood claims; otherwise the missing bearer, allocation, or relation owner. |
| Which whole-level characteristic is claimed? | `C.16`, `A.19`, and `C.29` when a mathematical lens is used | Exact bearer, characteristic, assignment or value, scale, threshold or aggregation relation, and lens-use boundary; otherwise the missing bearer, scale, relation, or evidence. |
| Which evidence, description, representation, or publication supports inspection? | `A.10`, `B.3`, `C.2.1`, `C.29`, `E.17`, and the exact source or architecture-description owner | The exact episteme and exact evidence, assurance, description, representation, source-use, or publication relation; otherwise the missing identity, relation, applicability, or reliance basis. |

Naming those results together does not create a further world-side relation. Stop at the first direct blocker that prevents the named decision; do not weaken it into an aggregate-shaped placeholder.

#### B.1.2:4.2 - Select A Structure Only When The Joint Organization Matters

If the joint organization of several exact results itself changes the named decision, select one ordinary `U.Structure` under `A.22`. Recover all four identity discriminators: exact independently identified constituents, exact selected obtaining relation occurrences, exact constraints as applied, and one named selection-use frame with its admissible action or stop.

The selected structure is non-agentive. It creates no system, part, crossing, allocation, characteristic, evidence, or decision fact and does not become the system, its environment, or its containing whole. A box, list, graph, table, description, view, or publication can represent or describe the selected organization but supplies none of the four discriminators by form.

#### B.1.2:4.3 - Make Interface Choices About Exact Crossing Relations

When the aggregate exposes, namespaces, internalizes, excludes, or leaves a crossing with its direct owner, make that choice about one exact crossing-relation occurrence and one named use. These words are ordinary decision options, not a closed FPF enumeration and not another relation kind.

Name the direct world facts, affected endpoints, crossing-relation owner, preserved obligation or information, evidence if relied on, and the C.11 `ChoiceResult` or C.32.PAD `ArchitectureDecisionRelation@Project` that chooses among the ordinary interface options when either owner applies. A different choice passes only after its admitted direct owner and result are named; otherwise stop with the missing-governor blocker. If a later use must inspect the choice, identify a separate C.2.1 episteme whose claim content describes it and cites that direct result; the episteme does not make the crossing, parthood, compatibility, or decision fact obtain. This preserves interface accountability without an omnibus compatibility-check object. Without that account, an apparent simplification can silently drop an external obligation or proliferate unmanaged endpoints.

#### B.1.2:4.4 - Whole-Level Characteristics

Roll up system-level characteristics only after the exact bearer, characteristic relation or assignment, scale, and aggregation or inference rule are selected under their direct owners.

Useful families include:

- additive quantities such as mass, cost, energy stock, or material amount;
- limiting quantities such as pressure rating, weakest connector, safety class, or availability bottleneck;
- logical or capability claims such as emergency-stop availability or vulnerability exposure;
- architecture characteristics that depend on selected structure.

Use `C.16`, `A.19`, and `C.29` when characteristic space, scale, threshold, or mathematical lens is relied on for the current claim. Use B.2 when redundancy, closure, or coordination creates or reveals a whole that must be reidentified.

#### B.1.2:4.5 - Functional Elements And Bearers

A functional element in a functional view is not automatically a system part.

Recover separately:

- functional behavior or functional element under `A.6.F`;
- physical, organizational, software, or operational bearer under `A.6.M`, A.14, C.13, and architecture owners;
- allocation or correspondence between function and bearer;
- system aggregation only when bearer parthood is independently admitted.

One bearer may realize several functions. One function may require several bearers. This is allocation and correspondence before it is part-whole.

