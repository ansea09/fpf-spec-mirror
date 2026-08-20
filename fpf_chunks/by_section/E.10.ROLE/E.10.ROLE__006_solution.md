---
chunk_kind: "child"
pattern_id: "E.10.ROLE"
pattern_title: "Recovering What “Role” Means in the Current Claim"
section_id: "E.10.ROLE:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ROLE/E.10.ROLE__006_solution.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "E.10.ROLE — Recovering What “Role” Means in the Current Claim"
  - "E.10.ROLE:4 — Solution"
line_start: 76352
line_end: 76393
dependencies:
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "A.6.RSIR"
  - "E.10"
  - "E.10.ARCH"
  - "F.18"
  - "F.19"
keywords:
  - "ambiguous role wording"
  - "assignment"
  - "declaration slot"
  - "interface place"
  - "ordinary wording"
  - "relation participant"
  - "representation position"
  - "responsibility"
  - "system-role kind"
---

### E.10.ROLE:4 - Solution

Use the sentence's intended claim, not the trigger word, to select the result.

1. Quote or locate the bounded phrase only when its source identity matters.
2. Write the ordinary sentence the reader should understand, naming the recognizable object and action or relation.
3. Select one branch below from that recovered claim. The examples are non-exhaustive; they illustrate result families and do not define a new role taxonomy.
4. Apply the selected pattern only as far as the receiving claim needs. Add a Tech designation, occurrence identity, predicate, assertion, reference, evidence, or assurance only when omitting it would change truth, action, reuse, or reliance.
5. Stop when one exact object or relation and its pattern are selected, or return the exact `missing-governor`, missing-information, quote-only, or ordinary-non-use result.

| Current claim recovered from the wording | Required result and route |
|---|---|
| One assignable work-facing classification of systems | Recover one exact context-local system-role kind through C.3 and A.2. A durable local designation normally ends in `...SystemRole`, for example `ReviewerSystemRole`. |
| One obtaining assignment of an admitted system to that kind | Recover one occurrence of an exact direct species under `U.SystemRoleAssignment` through A.2.1. Assignment creates neither system admission, another classification, capability, participation, responsibility, nor Work. |
| “The system as reviewer” or similar readable designation | Name the exact system plus its separately obtaining classification or assignment. Create no `SystemInRole` individual. |
| Participant meaning or actual participant of a direct relation | Use `A.6.RSIR` and the pattern for that direct relation. State the participant meaning and actual participant without calling either a system role. |
| One place in a declaration, for example a source-named field, argument, result, endpoint, slot, or port | Use `A.6.RSIR`, followed by A.6.5, A.6.1, or the exact interface pattern. Recover `SlotKind`, `SlotSpec`, an argument or result declaration, or the interface term rather than `SystemRole`. |
| One position in a representation, for example a tuple component, formula argument, graph endpoint, diagram place, schema field, or call position | Use the pattern for the selected representation and C.29 correspondence. The position is neither participant meaning nor system-role kind. |
| Another object or relation, for example participation, functioning, capability, Method, Work, obligation, permission, access, authority, responsibility, position, result, or status | Use the direct pattern and relation for that claim. If exact participants are known but no current direct relation closes the use, return the exact `missing-governor` result through A.6.RCD. |
| A use of an episteme, for example when a report, standard, dataset, description, model, or publication “plays a role” | Recover the exact evidence-use, source-use, description-use, publication-use, reliance, status-use, or other direct relation. The episteme does not become a system-role holder. |
| Ordinary or quoted wording carrying no FPF claim | Retain it as ordinary or source wording. Create no Tech token, kind, assignment, or repair record. |

#### E.10.ROLE:4.1 - Boundary with A.6.RSIR

`E.10.ROLE` starts from the ambiguous word and recovers the sentence's work-facing or use-facing object. Use `A.6.RSIR` for the narrower question of direct-relation participation, reusable declaration, interface, operation declaration or binding, and representation position.

When the recovered branch is a direct relation, declaration, interface, or representation question, continue through `A.6.RSIR`. When it is a system-role kind, assignment, capability, Work, deontic relation, evidence use, or ordinary non-use, leave RSIR closed and use the direct route above. Neither pattern duplicates the other's subject rules.

#### E.10.ROLE:4.2 - Lightweight Result

For a local repair, the result is normally only:

```text
source sentence: the report played a role in approval
recovered sentence: reviewers used Report-R as evidence for ApprovalClaim-C
result route: A.10 evidence-use relation
blocked overread: Report-R has no system-role assignment by this claim
stop: return to the approval question
```

No separate repair record is required unless another named use must inspect or reuse the decision.

