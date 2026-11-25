---
chunk_kind: "child"
pattern_id: "B.1.2"
pattern_title: "Coordinate Decisions About System Aggregation and Delimitation"
section_id: "B.1.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.2/B.1.2__006_solution.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "B.1.2 — Coordinate Decisions About System Aggregation and Delimitation"
  - "B.1.2:4 — Solution"
line_start: 43251
line_end: 43303
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

Coordinate one named system-aggregation or delimitation decision using the independently grounded results below. A record can bring those results together; establishing any further relation requires grounds.

Use an established fact about the whole directly when it settles the decision. To compare proposed designs, hold their common requirements fixed and follow each proposed allocation or crossing to its consequence for the intended use. A model may group designs with the same relevant consequence and grounds. An inventory of existing components supports a different decision from choosing or realizing a new assembly. Read the questions below for the claims the result actually needs. For a proposal, identify its stipulated relations and conditions of use. Evidence that they obtain is needed for an as-built claim.

#### B.1.2:4.1 - Recover Each Result Or Blocker

| Working question | Subject pattern | Result or stop |
| --- | --- | --- |
| Which whole is being considered? | `A.1` and the kind-specific recognition pattern | For a design comparison, the proposed whole, its intended use and the arrangement under consideration. For a claim about an existing `U.System`, a recognized entity or the A.1 evaluation of its six constructive components and kind-specific condition, including any unresolved basis. |
| Which constituents are parts, portions, phases, or members, and how do they assemble? | `A.14`, the part-relation specialization, and `C.13` for constructive assembly grounding | For an actual system, the obtaining part relations and assembly. For a design comparison, the proposed relations and their consequences under the stated assumptions; otherwise the missing governor, participant identity, obtaining fact, or assembly basis. |
| Which facts and selected boundary-use claim delimit the system for this decision? | `A.1` for system identity; `A.14`, the part-relation specialization, and `C.13` for parthood and assembly; every crossing-relation pattern for external participants; `C.11` for a local choice among already available boundary readings; `C.32.PAD` for a post-synthesis architecture decision concerning project Work; `C.2.1` only for a separately persistent claim | First identify the system and the parts, assembly or boundary crossings that affect this question. For a proposed option identify the corresponding design stipulations. For a claim about the actual system establish the relevant facts. If those facts answer the question, stop. If the named use additionally selects a boundary reading, return the C.11 `ChoiceResult` or C.32.PAD `ArchitectureDecisionRelation@Project` that makes its inclusion, exclusion, identity-preservation, and use claim current. Another choice branch passes only after its admitted decision predicate, source, and result are named; otherwise return the missing predicate or defining pattern, participant, obtaining fact, decision governor, or information blocker. When durable reliance is needed, one separate C.2.1 episteme states that claim and cites its basis; it creates none of the world facts. A selected `U.Structure` remains a separate B.1.2:4.2 branch. |
| Which relation crosses the selected boundary? | The source, supply, flow, coupling, control, measurement, evidence, publication, transformation, commitment, or other relation pattern; `F.9` only for a needed semantic correspondence or difference between two F.17 local senses from different semantic contexts | For an actual crossing, the obtaining relation with its participants and predicate. For a proposed crossing, the specified endpoints, relation and conditions; otherwise the missing governor, endpoint, binding, or obtaining fact. |
| Which function is realized by which bearer? | The behavior, realization, allocation or parthood pattern; `A.6.F` or `A.6.M` only for unresolved wording; `C.30.ASV` only for architecture-view qualification | For a current arrangement, recover the functional claim, bearer and obtaining realization or allocation relation. For a proposed allocation, establish what its bearer would have to do and whether the design supports that use. Establish parthood separately when it is claimed. If a relation required by the claim cannot be established, identify the missing predicate, participant or defining source. |
| Which whole-level characteristic is claimed? | `C.16` and `A.19`; `C.29` when a mathematical representation-choice, transfer or reliance question remains unresolved | Recover the bearer, characteristic, assignment or value, and scale, together with any threshold, aggregation or inference rule, and lens-use boundary required by the claim; identify any missing basis needed for that claim. |
| Which evidence, description, representation, or publication supports inspection? | `C.2.1` for the account; `A.2.4` for evidence-use or status-use classification. Use `A.10` for an unresolved source-to-use account, `B.3` for a requested assurance claim, `C.29` for an unresolved mathematical-lens question, or `E.17` for a needed publication face; use the applicable source or architecture-description pattern when that relation is the question | The episteme and evidence, assurance, description, representation, source-use, or publication relation; otherwise the missing identity, relation, applicability, or reliance basis. |

If grounds are missing, check whether the remaining possibilities support the same decision. Give that decision and its grounds when they do. Otherwise return the established contribution and identify the missing result that could change the answer.

#### B.1.2:4.2 - Select A Structure Only When The Joint Organization Matters

When a decision depends on several results together, explain how they combine for that decision. In a design comparison, the relations and constraints stipulated for each option can warrant a conditional conclusion. When the claim selects a `U.Structure` under `A.22`, identify the subject whose organization is selected. Establish its independently identified constituents, the relation occurrences that obtain for that subject, the applied constraints and the named selection-use frame with its admissible action or stop. Relations between elements of a design can be present before the designed assembly exists.

The selected structure is non-agentive. Selecting it does not establish systemhood or the relations being selected. A diagram or other representation can express the selected organization; its form alone supplies none of the four discriminators.

#### B.1.2:4.3 - Make Interface Choices About Crossing Relations

When choosing an interface arrangement, identify the existing or proposed crossing and the use affected by the choice. Options include exposing the crossing, assigning it a namespace, internalizing it, excluding it, or leaving its treatment with its subject pattern. These are ordinary decision options.

Name the relevant world facts or design stipulations, affected endpoints, crossing predicate and any occurrence claimed, preserved obligation or information, evidence if relied on, and the C.11 `ChoiceResult` or C.32.PAD `ArchitectureDecisionRelation@Project` that chooses among the ordinary interface options when its predicate applies. A different choice passes only after its subject assertion, predicate, and result are named; otherwise stop with the established `missing-governor` blocker, whose content identifies the absent predicate source.

If a later use must inspect the choice, identify a separate C.2.1 episteme whose claim content describes it and cites that result; the episteme does not make the crossing, parthood, compatibility, or decision fact obtain. This account lets the practitioner check whether an interface change loses an external obligation or leaves an endpoint unmanaged.

#### B.1.2:4.4 - Whole-Level Characteristics

Roll up system-level characteristics only after the bearer, characteristic relation or assignment, scale, and aggregation or inference rule are selected under their subject patterns.

Useful families include:

- additive quantities such as mass, cost, energy stock, or material amount;
- limiting quantities such as pressure rating, weakest connector, safety class, or availability bottleneck;
- logical or capability claims such as emergency-stop availability or vulnerability exposure;
- architecture characteristics that depend on selected structure.

Use `C.16` and `A.19` for the characteristic, scale and aggregation rule. Retain the correspondence, assumptions and limits needed to rely on a mathematical lens; use `C.29` when its choice, transfer or reliance remains unresolved. Use B.2 when changed facts leave a consequential question about whether the existing whole still supports the claim or a new whole is required. A sufficient existing-whole explanation ends that inquiry; missing deciding grounds leave the comparison unresolved.

#### B.1.2:4.5 - Functional Elements And Bearers

A functional element in a functional view is not automatically a system part. Recover the functional claim and its intended behavior, the bearer under its kind and identity rule, the independently established realization or allocation relation, and any obtaining parthood relation. C.2.1 identifies a claim episteme when one must be cited; C.30.ASV qualifies an architecture structural view when that is the use.

Use A.6.F only to resolve an unclear function expression and A.6.M only to resolve module or interface wording. Neither pattern admits the bearer or establishes allocation or parthood. One bearer can realize several functions and one function can require several bearers when the domain relations support those claims.

