---
chunk_kind: "child"
pattern_id: "C.3.5"
pattern_title: "KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
section_id: "C.3.5:9"
section_title: "Worked mini-examples (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.5/C.3.5__010_worked-mini-examples-informative.md"
commit_sha: "dba39812b83cac74dd2a3251c134cdc23dfaec86"
heading_path:
  - "C.3.5 — KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
  - "C.3.5:9 — Worked mini-examples (informative)"
line_start: 58692
line_end: 58698
dependencies:
  - "A.2.6"
  - "C.2.2"
  - "C.2.3"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.4"
  - "C.3.A"
keywords:
  - "K0-K3"
  - "KindAT"
  - "assurance planning"
  - "declaration planning"
  - "editorial facet"
---

### C.3.5:9 - Worked mini-examples (informative)

- **K0.** `Account_US_GAAP_2025_Q1_Cohort`: suppose the approved quarter roster defines this cohort. Check the account identifier against that edition of the roster. Counting the confirmed entries answers a separate question.
- **K1.** `RetrySafeRequest`: the declared criterion permits repeating a request after a lost reply without duplicating its intended effect. Check that property for the admitted failures, including a reply lost after the first execution completed.
- **K2.** `Account`: use explicit posting and balance invariants, test relevant subkinds, and evaluate each candidate with the signature edition and slice.
- **K3.** `UndirectedGraph` up to node relabeling: state the equivalence notion and require equivalence witnesses that preserve it. Any KindBridge use additionally needs the distinct-kind correspondence and preservation basis required by C.3.3.

