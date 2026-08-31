---
chunk_kind: "child"
pattern_id: "A.2.8"
pattern_title: "U.Commitment (Deontic Commitment Relation)"
section_id: "A.2.8:9"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8/A.2.8__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.2.8 — U.Commitment (Deontic Commitment Relation)"
  - "A.2.8:9 — Common Anti-Patterns and How to Avoid Them"
line_start: 6949
line_end: 6961
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6.B"
  - "A.6.C"
  - "A.6.RCD"
  - "A.7"
  - "C.3"
  - "F.6"
keywords:
  - "actual bearer"
  - "constitutive rule"
  - "do not identify an individual bearer or institute a duty. Adapt"
  - "individual duty"
  - "instituting basis"
  - "obligation"
  - "prohibition"
  - "recommendation-as-duty"
  - "validity interval"
---

### A.2.8:9 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| “The API shall…” as duty-bearer structure | An interface description is an episteme, not the actual bearer. | Identify the policy claim and actual system or party; test institution. |
| `CommitmentSubject ::= RoleRef | RoleAssignmentRef | PartyRef` | It merges a kind, relation occurrence, and actual bearer. | Use one actual bearer branch; keep kind and assignment in the rule's grounds. |
| Optional institution source | A published sentence appears sufficient to create the relation. | Require the applicable rule and its actual instituting basis. |
| Assignment-as-duty | Staffing becomes obligation. | Treat the assignment only as a rule fact and identify a separate commitment. |
| Duty-as-responsibility | One deontic relation silently creates ownership. | State the independent responsibility predicate or return `missing-governor`. |
| Gate-as-duty | Entry conditions become obligations. | Keep the A-claim and let an independently instituted commitment cite it when required. |
| Auditable rhetoric without support | “Guaranteed” cannot be adjudicated. | Cite exact evidence claims and carriers only when reliance or adjudication is current. |
| Silent mutation | Changed bearer or rule is hidden under one ID. | Apply occurrence identity and create another relation when identity-bearing facts change. |

