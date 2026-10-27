---
chunk_kind: "child"
pattern_id: "B.1"
pattern_title: "Holon Aggregation and Part-Whole Construction"
section_id: "B.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1/B.1__006_solution.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "B.1 — Holon Aggregation and Part-Whole Construction"
  - "B.1:4 — Solution"
line_start: 40801
line_end: 40887
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
  candidateWholeRef: U.Holon
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
- `C.13` for constructional grounding such as sum, set, slice, or another accepted construction;
- `B.3.5` when a working model relies on the part-whole claim for assurance or evidence;
- `C.16` when the current output is a whole-level characteristic;
- `A.1` and `A.15` when the whole is claimed to be an acting collective system.

#### B.1:4.2 - Didactic Firewall

| Source claim | Ontology-side recovery | Subject pattern |
| --- | --- | --- |
| "This object is made of these parts." | Part-whole construction over admitted holons. | `A.1`, `A.14`, `C.13`, `B.3.5` when assurance is current. |
| "These items belong to this collection." | The collection's own belongs-to rule or collection-as-whole grounding; no `ComponentOf` inference. | `A.14`, `C.13`, `C.16` for a collection-level or whole-level characteristic. |
| “This role is combined from role factors.” | Unresolved source wording. It may mean an exact relation among local system-role kinds, a classification or assignment, a direct participation relation, a naming question, or ordinary prose; none is holonic parthood by default. | `E.10.ROLE` first; then `A.2.7` only for the exact relation among local system-role kinds, or the direct pattern for the recovered classification, assignment, participation, or naming claim; use `C.29` only if a mathematical lens is selected. |
| "This method has steps, parameters, guards, or variants." | Method relation structure, method family, method description, or work plan; not performed work by default. | `A.15`, Method patterns, `C.29` if mathematical lens is selected. |
| "This run contained episodes or concurrent sub-runs." | Work occurrence holarchy with timing, evidence, occurrence identity, and work-part relation. | `A.15.1`, temporal pattern, evidence-use pattern. |
| "This graph or algebraic notation represents the structure." | Mathematical or representation description of a selected structure. | `C.29`, `A.22`, architecture or description pattern. |
| "The whole shows emergence." | Existing-whole explanation first; B.2 only when the whole itself must be reidentified. | `B.2`, `B.2.P`, or the direct characteristic, measurement, architecture, capability, or Work pattern. |

#### B.1:4.3 - Work Occurrence Holarchy

A Method's composition and the parts of a performed Work require different grounds.

A dated Work may have independently admitted temporal or operational parts under `A.15.1`. C.27 governs temporal claims, and B.1.4 aggregates recovered order or temporal relations when that is the question. Resource roll-ups use B.1.6; composing effects needs the direct relation and composition rule for those effects. Neither kind of calculation establishes Work parthood or makes a Method or role expression a holonic part.

Use A.15.1 when the claim needs occurrence identity, temporal coverage, `Gamma_time`, `Gamma_work`, episode policy, overlap policy, resource aggregation, or performed-work evidence.

#### B.1:4.4 - Mathematical And Representation Apparatus

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

#### B.1:4.5 - Existing-Whole Before MHT

Before declaring B.2 whole reidentification, ask whether the whole-level gain can be explained inside the existing whole:

- better parts;
- corrected part relation;
- improved measurement;
- role or method relation repair;
- work occurrence evidence repair;
- a correction to the selected functional or architectural structure;
- source, publication, or representation correction.

Use B.2 only when the whole itself must be reidentified.

