---
chunk_kind: "child"
pattern_id: "B.1"
pattern_title: "Holon Aggregation and Part-Whole Construction"
section_id: "B.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1/B.1__006_solution.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "B.1 — Holon Aggregation and Part-Whole Construction"
  - "B.1:4 — Solution"
line_start: 30672
line_end: 30756
dependencies:
  - "A.1"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.22"
  - "B.2"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
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
  boundedContextRef:
  identityOrRecognitionRule:
  partRelationRefs:
  constructionBasisRef?
  selectedStructureRef?
  wholeLevelCharacteristicRefs?
  assuranceGroundingRef?
  neighboringNonPartRelationRefs?
  mathLensOrRepresentationRef?
```

This is a claim frame, not a U-kind and not an acting record. It says what must be named before the aggregation claim is relied on.

Use:

- `A.14` for `ComponentOf`, `ConstituentOf`, `PortionOf`, `PhaseOf`, `MemberOf`, aspect, and related vocabulary;
- `C.13` for constructional grounding such as sum, set, slice, or another accepted construction;
- `B.3.5` when a working model relies on the part-whole claim for assurance or evidence;
- `C.16` when the current output is a whole-level characteristic;
- `A.1` and `A.15` when the whole is claimed to be an acting collective system.

#### B.1:4.2 - Didactic Firewall

| Source claim | Ontology-side recovery | Direct owner |
| --- | --- | --- |
| "This object is made of these parts." | Part-whole construction over admitted holons. | `A.1`, `A.14`, `C.13`, `B.3.5` when assurance is current. |
| "These members form a collection." | Membership or collection-as-whole grounding; no `ComponentOf` inference. | `A.14`, `C.13`, `C.16` for whole-level characteristic. |
| "This role is combined from role factors." | Role relation structure or role naming; not holonic parthood by default. | `A.2.7`, role patterns, `C.29` if mathematical lens is selected. |
| "This method has steps, parameters, guards, or variants." | Method relation structure, method family, method description, or work plan; not performed work by default. | `A.15`, method owners, `C.29` if mathematical lens is selected. |
| "This run contained episodes or concurrent sub-runs." | Work occurrence holarchy with timing, evidence, occurrence identity, and work-part relation. | `A.15.1`, temporal owner, evidence owner. |
| "This graph or algebraic notation represents the structure." | Mathematical or representation description of a selected structure. | `C.29`, `A.22`, architecture or description owner. |
| "The whole shows emergence." | Existing-whole explanation first; B.2 only when the whole itself must be reidentified. | `B.2`, `B.2.P`, or the direct characteristic, measurement, architecture, capability, or work owner. |

#### B.1:4.3 - Work Occurrence Holarchy

Performed work is different from structural composition.

A work occurrence can have temporal parts, episode parts, operational parts, concurrent sub-runs, retries, resource roll-ups, and effect composition. That is a work-occurrence holarchy governed by `A.15.1`, not evidence that the method or role expression is a holonic part-whole structure.

Use A.15.1 when the claim needs occurrence identity, temporal coverage, `Gamma_time`, `Gamma_work`, episode policy, overlap policy, resource aggregation, or performed-work evidence.

#### B.1:4.4 - Mathematical And Representation Apparatus

Use Γ, graph, algebra, tuple, matrix, embedding, or neural representation only after the object under concern and selected relation are named.

Acceptable uses:

- a mathematical lens for a selected structure;
- a constructional expression for a part-whole claim already admitted by A.14 and C.13;
- a representation of dependency relations;
- a checking apparatus for invariants or conservative bounds.

Blocked uses:

- graph wording as parthood admission;
- algebraic factorization as role, method, or work parthood admission;
- source notation as a new U-kind;
- one fold rule as a universal replacement for the direct owner.

#### B.1:4.5 - Existing-Whole Before MHT

Before declaring B.2 whole reidentification, ask whether the whole-level gain can be explained inside the existing whole:

- better parts;
- corrected part relation;
- improved measurement;
- role or method relation repair;
- work occurrence evidence repair;
- functional or architecture selected-structure repair;
- source, publication, or representation correction.

Use B.2 only when the whole itself must be reidentified.

