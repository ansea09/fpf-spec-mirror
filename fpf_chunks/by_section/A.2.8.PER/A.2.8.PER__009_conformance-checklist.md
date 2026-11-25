---
chunk_kind: "child"
pattern_id: "A.2.8.PER"
pattern_title: "Granted Permission, Exercise, and Non-Prohibition"
section_id: "A.2.8.PER:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8.PER/A.2.8.PER__009_conformance-checklist.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "A.2.8.PER — Granted Permission, Exercise, and Non-Prohibition"
  - "A.2.8.PER:7 — Conformance Checklist"
line_start: 9126
line_end: 9138
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.5"
  - "A.2.8"
  - "A.2.9"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "F.6"
  - "U.Work"
keywords:
  - "checked non-violation"
  - "exact policy rule or decision result"
  - "matching dated-work exercise"
  - "permission or prohibition conflict"
  - "policy-valid strong grant"
  - "weak non-prohibition finding"
---

### A.2.8.PER:7 - Conformance Checklist

| ID | Check |
|---|---|
| `CC-A2.8.PER-1` | Support a rule-based entitlement by the applicable affirmative rule and case facts. For a right granted to several parties jointly, use the instrument and the conditions on their joint action in §4.2. When reporting a `GrantedPermissionRelation@Context`, its §4.5 exercise relation, or a finding declared in §§4.3–4.6, establish the conditions of the corresponding declaration. |
| `CC-A2.8.PER-2` | For a single beneficiary within the §4.2 reference union, select exactly one of `beneficiarySystemRoleKindRef : U.KindRef`, `beneficiarySystemRoleAssignmentRef : U.RelationRef constrained to U.SystemRoleAssignment`, or `beneficiaryPartyRef : PartyRef`, with its branch-specific eligibility test. For an entitlement held jointly, apply the instrument to the participants and their required action together (§4.2). The branch record introduces no beneficiary U-kind. |
| `CC-A2.8.PER-3` | A strong grant identifies its participants, effective scope and interval, current policy and the act or combination that instituted this occurrence. Each grant-making contribution meets the authority and assignment conditions that the rule requires. Several contributors to one act and several required acts remain distinguishable. |
| `CC-A2.8.PER-4` | Weak findings require a current frame explicitly complete enough for the intended use; incompleteness returns `unresolved`. |
| `CC-A2.8.PER-5` | For exercise of a right conferred by an instrument, identify the dated Work and establish the match to the beneficiary or joint beneficiaries, authorized action, scope and time. The exercise relation in §4.5 identifies the exact §4.4 grant occurrence. Establish the eligibility of the contributions required by the instrument. A support provider may contribute without holding the right. |
| `CC-A2.8.PER-6` | Neither exercise nor non-exercise establishes `NonViolationFinding@Context`; non-exercise does not violate the grant, exercise alone does not establish obligation satisfaction, and exercise does not consume a grant without an explicit policy. |
| `CC-A2.8.PER-7` | A same-scope conflict is settled when a current applicable rule selects the outcome, or when decision Work supplies the result the precedence policy requires. In the decision branch, each required deciding contribution and its authority are established for this issue, scope and time. A named office with authority leaves its actual decision open. |
| `CC-A2.8.PER-8` | Permit episteme, carrier, evidence, admissibility, readiness, gate, capability, Work, and result remain distinct and are handled under their respective subject patterns. |

