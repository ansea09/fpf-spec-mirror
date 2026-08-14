---
chunk_kind: "child"
pattern_id: "E.10.ROLE"
pattern_title: "Recovering What “Role” Means in the Current Claim"
section_id: "E.10.ROLE:5"
section_title: "Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ROLE/E.10.ROLE__007_worked-slices.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "E.10.ROLE — Recovering What “Role” Means in the Current Claim"
  - "E.10.ROLE:5 — Worked Slices"
line_start: 76786
line_end: 76803
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

### E.10.ROLE:5 - Worked Slices

#### E.10.ROLE:5.1 - Alice Is Reviewer

“Alice is reviewer” may stay as readable prose when the local task needs only recognition. If classification matters, state separately that Alice is an admitted System classified under `ReviewerSystemRole` in the named context. If assignment identity matters, first name the declared assignment species `JournalReviewAssignmentRelation`, then identify `ReviewAssignment-82` as its obtaining occurrence with actual participants, holder, applicability, and extent. If performed Work matters, point to the complete A.15.1/F.6 basis for `ReviewWork-82`, including the relation saying that Alice performed it under `ReviewAssignment-82`. Classification, assignment, Work, and attribution remain separate. None follows merely from the ordinary sentence. A short projection may omit only an assignment identifier unused by its receiving claim; the Work basis and every performer remain recoverable.

#### E.10.ROLE:5.2 - A Report Plays a Role in Approval

The report is an episteme. Rewrite the claim as “reviewers used Report-R as evidence for ApprovalClaim-C”, then use A.10 for the evidence-use relation and B.3 only when an assurance claim or material-reliance threshold is current. The report becomes neither a system nor a holder of a system-role assignment.

#### E.10.ROLE:5.3 - API Provider Role

“The API role is provider” is not one claim. First ask whether a provider System is current and whether its classification under a local provider system-role kind matters. If the assignment itself matters, name its declared assignment species and the obtaining occurrence separately; do not infer either from root-family typing or the word *role*. Provision, service, declaration, interface, schema position, publication, promise, and access claims each use their own pattern. Only when provider Work is current should A.15.1 and F.6 identify its dated Work, performer, and assignment. The API description is neither assigned nor a performer.

#### E.10.ROLE:5.4 - Passive Test Article

A passive test article may independently pass A.1 and be classified under `TestArticleSystemRole`. If an assignment claim matters, name its declared assignment species before identifying an occurrence. Neither classification nor assignment makes the article an agent or performer. The role-bearing source claim to recover is: `TestArticle-7 participates passively in TestWork-9 during TestInterval-9`; its intended participant order is article, Work, then applicability interval. No current pattern supplies a direct passive-participation predicate with those participants, applicability, and occurrence identity, so the current result is the A.6.RCD `missing-governor` for that exact attempted claim. Any tester or test-rig Work uses A.15.1 and F.6 separately. A short projection may omit an unused assignment identifier, but it keeps the article, Work, interval, and missing relation recoverable.

