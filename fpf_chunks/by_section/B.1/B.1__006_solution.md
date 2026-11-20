---
chunk_kind: "child"
pattern_id: "B.1"
pattern_title: "Holon Aggregation and Part-Whole Construction"
section_id: "B.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1/B.1__006_solution.md"
commit_sha: "d325a051ac7b2bb37cd870f90b4ed8b2d0426e58"
heading_path:
  - "B.1 — Holon Aggregation and Part-Whole Construction"
  - "B.1:4 — Solution"
line_start: 42682
line_end: 42771
dependencies:
  - "A.1"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.7"
  - "A.22"
  - "B.2"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.29"
  - "C.30"
  - "E.10.ROLE"
keywords:
---

### B.1:4 - Solution

Use B.1 as a discriminator and construction frame.

#### B.1:4.1 - Holon Aggregation Claim Frame

When part-whole construction is current, recover:

```text
HolonAggregationClaim@Context:
  candidateWholeRef: U.Entity
  candidatePartRefs:
  aggregationPolicyRef?
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  identityOrRecognitionRule:
  partRelationRefs:
  constructionBasisRef?
  selectedStructureRef?
  wholeLevelCharacteristicRefs?
  assuranceGroundingRef?
  neighboringNonPartRelationRefs?
  mathLensOrRepresentationRef?
```

This claim frame identifies the objects, relations, and qualifications needed to rely on the aggregation claim. Include optional fields when they change that claim or its use.

Use:

- `A.14` for `ComponentOf`, `ConstituentOf`, `PortionOf`, `PhaseOf`, collection belonging under the collection's own rule, aspect, and related vocabulary;
- `C.13` for constructional grounding through its sum, set or slice accounts;
- `B.3.5` when a publication choice or named current requirement elects its assurance profile for the relation claim;
- `C.16` when the current output is a whole-level characteristic;
- `A.1` and `A.15` when the whole is claimed to be an acting collective system.

#### B.1:4.2 - Distinguish part-whole claims from other claims

| Source claim | Ontology-side recovery | Subject pattern |
| --- | --- | --- |
| "This object is made of these parts." | Identify the candidate whole and constituents and establish the part relations and construction rule. When holonhood is claimed, apply all six A.1 components and the kind-specific conditions. | `A.1` for holon recognition, `A.14`, `C.13`; `B.3.5` when a publication choice or named current requirement elects its assurance profile. |
| "These items belong to this collection." | The collection's own belongs-to rule or collection-as-whole grounding; no `ComponentOf` inference. | `A.14`, `C.13`, `C.16` for a collection-level or whole-level characteristic. |
| “This role is combined from role factors.” | Unresolved source wording. It may mean a relation among local system-role kinds, a classification or assignment, a participation relation, a naming question, or ordinary prose; none is holonic parthood by default. | `E.10.ROLE` first; then `A.2.7` only for the relation among local system-role kinds, or the pattern for the recovered classification, assignment, participation, or naming claim; use `C.29` when a separate mathematical representation-choice, transfer or reliance question remains unresolved. |
| "This method has steps, parameters, guards, or variants." | Method relation structure, method family, method description, or work plan; not performed work by default. | `A.15`, Method patterns, `C.29` when a separate mathematical representation-choice, transfer or reliance question remains unresolved. |
| "This run contained episodes or concurrent sub-runs." | Work occurrence holarchy with timing, evidence, occurrence identity, and work-part relation. | `A.15.1`, temporal pattern, evidence-use pattern. |
| "This graph or algebraic notation represents the structure." | Mathematical or representation description of a selected structure. | `A.22` and the applicable architecture or description pattern; `C.29` when a separate mathematical representation-choice, transfer or reliance question remains unresolved. |
| "The whole shows emergence." | Check applicable explanations within the existing whole first. Use B.2 when changed facts leave a consequential question about whether that whole remains sufficient or a new whole is required. | `B.2`, `B.2.P`, or the characteristic, measurement, architecture, capability, or Work pattern. |

#### B.1:4.3 - Work Occurrence Holarchy

A Method's composition and the parts of a performed Work require different grounds.

A dated Work may have independently admitted temporal or operational parts under `A.15.1`. C.27 governs temporal claims, and B.1.4 aggregates recovered order or temporal relations when that is the question. Resource roll-ups use B.1.6; composing effects needs the relation and composition rule for those effects. Neither kind of calculation establishes Work parthood or makes a Method or role expression a holonic part.


#### B.1:4.4 - Use mathematical and other representations

Before using Γ notation or another aggregation representation, name the object and selected relation.

Acceptable uses:

- a mathematical lens for a selected structure;
- a constructional expression for a part-whole claim already admitted by A.14 and C.13;
- a representation of dependency relations;
- a checking apparatus for invariants or conservative bounds.

Blocked uses:

- graph wording as parthood admission;
- algebraic factorization as role, method, or work parthood admission;
- source notation as a new U-kind;
- one fold rule as a universal replacement for the subject pattern.

**Model the same holon at two scales.** Name the whole, the characteristic under investigation and the constituent conditions on which the answer depends. For an existing whole, use its established constitution. For a proposed assembly, identify the parts, their intended arrangement and the conditions stipulated in the design. Report the consequence as conditional until evidence of realization warrants an actual-system claim. For a system this can be an interaction between components. For an episteme, B.1.3 traces a joint conclusion to the claims, meanings and sources being combined. For a method, B.1.5 recovers which constituent supplies what the next one needs. For an occurrence of work, A.15.1 and B.1.5.EW distinguish its actual constituent work from work elsewhere that supplies a result. C.20 identifies what joins reusable practice and knowledge in one discipline.

State the relation that carries the inference across the two scales. For a straightforward forward calculation, apply the established rule to the known values. For a sensitivity question, vary a consequential condition and check whether the whole can behave as before and whether it retains its identity. For an inverse question, the observed whole constrains which constituent configurations could account for it. For a design allocation question, the prescribed whole constrains the permitted designs. A mass budget leaves several allocations open until the designer chooses one. Across several scales, establish each direct composition and each step of the inference under the rule for its kind. Swapping the masses of two parts can preserve their total mass while changing their load distribution. A capability that arises from organized interaction needs grounds in that interaction. When you assert an actual encompassing whole, identify its obtaining part relation. A.1:4.2 gives the separate constructive test for possible participation in a larger assembly. Use B.5.MR when two models are also being compared for refinement.

#### B.1:4.5 - Consider explanations within the existing whole

To assess whether changed facts require a different whole for the receiving use, first consider applicable explanations within the existing whole, such as:

- better parts;
- corrected part relation;
- improved measurement;
- role or method relation repair;
- work occurrence evidence repair;
- a correction to the selected functional or architectural structure;
- source, publication, or representation correction.

If a supported explanation is sufficient for the receiving use, keep the existing whole and stop. Use B.2 when changed facts leave a consequential question about whether that whole remains sufficient or a new whole is required; retain an unresolved comparison when its deciding grounds are missing.

