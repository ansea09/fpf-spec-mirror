---
chunk_kind: "child"
pattern_id: "E.10.ROLE"
pattern_title: "Recovering What “Role” Means in the Current Claim"
section_id: "E.10.ROLE:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ROLE/E.10.ROLE__006_solution.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "E.10.ROLE — Recovering What “Role” Means in the Current Claim"
  - "E.10.ROLE:4 — Solution"
line_start: 73635
line_end: 73678
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
5. For one recovered claim, stop when one exact object or relation and its pattern are selected, or return the exact `missing-governor`, missing-information, quote-only, or ordinary-non-use result.

If recovery shows that the same bounded phrase carries several distinct claims at once, rewrite them as separate ordinary sentences and apply steps 3–5 to each sentence. Ambiguity by itself is not evidence of several claims. Use A.6.C **Contract Unpacking for Boundaries** only when its contract-like boundary-language trigger holds; otherwise apply the direct rule for each recovered claim. Do not create a multi-claim record or an umbrella role object.

| Current claim recovered from the wording | Required result and next action |
|---|---|
| One exact local work-facing system-role kind, or a technical claim that one admitted system counts under it | For kind recovery, use C.3 and A.2 to identify one exact context-local system-role kind; a durable local designation normally ends in `...SystemRole`, for example `ReviewerSystemRole`. For a current classification judgment, use A.2 and C.3.2 and keep the admitted candidate system, exact kind, current `KindSignature` edition, context slice, and `true | false | unknown` result recoverable. Kind admission is not the classification judgment. |
| One obtaining assignment of an admitted system to that kind | Recover one occurrence of an exact direct species under `U.SystemRoleAssignment` through A.2.1. Assignment creates neither system admission, another classification, capability, participation, responsibility, nor Work. |
| “The system as reviewer” or similar readable designation | Keep the readable actor designation when it carries the needed ordinary claim. Recover exact system identity, a separately obtaining classification, or an assignment only when the receiving claim uses that distinction. Create no `SystemInRole` individual. |
| Participant meaning or actual participant of a direct relation | Use `A.6.RSIR` and the pattern for that direct relation. State the participant meaning and actual participant without calling either a system role. |
| One place in a declaration, for example a source-named field, argument, result, endpoint, slot, or port | Use `A.6.RSIR`, followed by A.6.5, A.6.1, or the exact interface pattern. Recover `SlotKind`, `SlotSpec`, an argument or result declaration, or the interface term rather than `SystemRole`. |
| One position in a representation, for example a tuple component, formula argument, graph endpoint, diagram place, schema field, or call position | Use the pattern for the selected representation and C.29 correspondence. The position is neither participant meaning nor system-role kind. |
| Another object or relation, for example participation, functioning, capability, Method, Work, obligation, permission, access, authority, responsibility, position, result, or status | Use the direct pattern and relation for that claim. If exact participants are known but no current direct relation closes the use, return the exact `missing-governor` result through A.6.RCD. |
| A use of an episteme, for example when a report, standard, dataset, description, model, or publication “plays a role” | Recover the exact evidence-use, source-use, description-use, publication-use, reliance, status-use, or other direct relation. The episteme does not become a system-role holder. |
| Ordinary or quoted wording carrying no FPF claim | Retain it as ordinary or source wording. Create no Tech token, kind, assignment, or repair record. |

#### E.10.ROLE:4.1 - Boundary with A.6.RSIR

`E.10.ROLE` starts from the ambiguous word and recovers the sentence's work-facing or use-facing object. Use `A.6.RSIR` for the narrower question of direct-relation participation, reusable declaration, interface, operation declaration or binding, and representation position.

If the recovered claim leaves a direct-participation, reusable-declaration, interface, operation-declaration-or-binding, or representation-position question unanswered, apply `A.6.RSIR` to that question. If it recovers a system-role kind, assignment, capability, Work, deontic relation, evidence use, another direct object, or ordinary non-use, apply that object's direct rule and do not apply RSIR. Neither pattern duplicates the other's subject rules.

#### E.10.ROLE:4.2 - Lightweight Result

For a local repair, the result is normally only:

```text
source sentence: the report played a role in approval
recovered sentence: reviewers used Report-R as evidence for ApprovalClaim-C
applicable rule: A.10 evidence-use relation
blocked overread: Report-R has no system-role assignment by this claim
stop: ApprovalClaim-C remains the current question
```

No separate repair record is required unless another named use must inspect or reuse the decision.

