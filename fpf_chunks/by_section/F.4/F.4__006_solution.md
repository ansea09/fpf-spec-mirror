---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "SystemRoleKindDescription — Describing an Exact System-Role Kind"
section_id: "F.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__006_solution.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "F.4 — SystemRoleKindDescription — Describing an Exact System-Role Kind"
  - "F.4:4 — Solution"
line_start: 92320
line_end: 92393
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RSIR"
  - "A.7"
  - "C.2.1"
  - "C.3"
  - "C.3.2"
  - "E.10.D2"
  - "E.10.ROLE"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.5"
  - "F.9"
keywords:
  - "classification criterion"
  - "description episteme"
  - "effective scheme"
  - "local kind"
  - "non-inference boundary"
  - "system-role-kind description"
---

### F.4:4 - Solution

Constitute one `SystemRoleKindDescription` through C.2.1. Its ClaimGraph describes one exact local system-role kind, and that kind is its EntityOfConcern. It makes the kind's candidate domain, operative membership condition, intended member/non-member boundary, continuity rule, current `KindSignature`, and effective `U.ReferenceScheme` recoverable. It may record source or practice provenance so readers can find and compare definitions, but provenance is not a kind-identity key. The description gives readers enough to recognize and check the kind while routing neighboring claims to their direct rules.

The following is a content checklist, not a relation signature or mandatory record.

**Always make recoverable:**

- the described local system-role kind;
- the candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule;
- the current `KindSignature` edition and effective reference scheme;
- a short recognition explanation;
- the full A.1 range of possible candidate systems, using examples only when helpful;
- the smallest direct-feature criteria or invariants needed by the current use; and
- the explicit boundary: the description asserts no classification, assignment, capability, Method, Work, evidence, status, permission, responsibility, publication, or relation-position occurrence.

**Add only when the current use depends on them:**

- a `SystemRoleAssignmentStatePredicate` or state-relation reference under A.2.5;
- capability-condition references under A.2.2;
- Method or MethodDescription references under A.3 and A.15;
- durable-name or lineage references under F.18;
- C.3.3 or F.9 Bridge references; and
- a selected `BoundedModelUseStructure` only when that structure changes the described interpretation or receiving use.

These are claims or references in an episteme. They are not `SlotSpec` declarations and add no participant to `U.SystemRoleAssignment` or another relation. A card, table row, Method appendix, or pattern section may express the description. When availability matters, a separate E.24.PUB occurrence makes the exact description edition available through its publication form and carrier.

#### F.4:4.1 - Content Meanings

| Content element | Meaning |
| --- | --- |
| Described system-role kind | The exact local `U.Kind` that is the episteme's EntityOfConcern. |
| Kind recovery basis | The candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule that distinguish this kind. Source or practice provenance may locate the definition but does not decide identity. |
| Kind criterion | The exact current `KindSignature` edition used to judge candidates directly. |
| Effective scheme | The by-value interpretation scheme used for the description's vocabulary; it is not a kind-identity authority. |
| Recognition explanation | A first-minute explanation that distinguishes this kind from neighboring kinds and objects. |
| Candidate-system range | Candidates must first be admitted as `U.System`; people, teams, organizations, and non-human technical objects are possible examples, not four subkinds declared here. |
| Conditional neighboring references | Add neighboring references for assignment state, capability, Method, naming, and Bridges only when the receiving use depends on them. |
| Non-inference boundary | Explicit separation from classification, assignment, Work, evidence, status, permission, responsibility, publication, and relation-position claims. |

A quick local description may stop after the always-recoverable content. A consequence-bearing Work-admission use requires only the neighboring relations it actually needs.

#### F.4:4.2 - Description versus Neighboring Values

| Current question | Direct locus |
| --- | --- |
| What local system-role kind is this, and does a candidate satisfy it? | A.2 with C.3 and C.3.2 |
| Which admitted system is assigned to it, and for which uninterrupted occurrence? | A.2.1 |
| Does this assignment satisfy this state condition during the required window? | A.2.5 |
| Can the system do the relevant Work? | A.2.2 |
| Which Method, MethodDescription, WorkPlan, or Work occurrence is current? | A.3, A.15, A.15.1, and A.15.2 |
| Which substitution, incompatibility, qualification, bundle, or other relation among kinds obtains? | A.2.7 |
| What durable name should the kind or description have? | F.18 and F.5 |
| How are two exact local kinds related? | C.3.3, only when its predicate obtains |
| How are two exact source-local senses related? | F.9 between exact F.17 `SchemeSenseCell` values, only when its predicate obtains |
| How is an episteme used in evidence, source, requirement, status, publication, or assurance claims? | The exact direct relation |
| Which relation position admits which filler kind? | A.6.5 and A.6.RSIR |

F.4 points to these loci; it does not copy their ontology.

Keep the description episteme, the exact local system-role kind it describes, the `KindSignature` that states the membership criterion, the effective scheme used to read the description, and any classification judgment about a candidate separate. Add an F.17 `SchemeSenseCell` only when a later use needs a stable local-sense address; cite a `LocalSenseBasisRelation` only when that relation actually obtains. An ordinary F.4 description requires neither.

#### F.4:4.3 - Positive Construction Rule

Write a description in this order:

1. Name the described local system-role kind and state its candidate domain, operative membership distinction, one useful member/non-member boundary, and continuity rule. Record source or practice provenance only when it helps the reader locate or compare the definition.
2. Name the current `KindSignature` edition and effective reference scheme.
3. Give one short recognition paragraph, including the broad A.1 system range when a cold reader could narrow it incorrectly.
4. State the smallest direct criteria or invariants that distinguish the kind.
5. State what the description does not assert about classification, assignment, capability, Method, Work, evidence, status, permission, responsibility, publication, or relation positions.
6. Add neighboring references only when the receiving use depends on them.
7. Use F.18 for a durable public name. Use C.3.3 only when an actual relation between exact local kinds is current; use F.9 only when the receiving claim relates distinct F.17 local-sense cells.

