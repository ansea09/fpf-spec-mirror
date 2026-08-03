---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:8"
section_title: "Subkind Monotonicity and Change"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__010_subkind-monotonicity-and-change.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:8 — Subkind Monotonicity and Change"
line_start: 45009
line_end: 45027
dependencies:
  - "A.14"
  - "A.2.6"
  - "A.6.0"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
keywords:
---

### C.3.2:8 - Subkind Monotonicity and Change

For exact reference-scheme edition `RS`, monotonicity is a law over judgments whenever `SubkindOfObtains(k1, k2; RS)` holds. Use an identified `R_sub : U.SubkindOf` occurrence only when a receiving use needs occurrence identity; an assertion that the predicate holds is a separate C.2.1 episteme:

> When both judgments are defined for the same candidate and context slice under the paired signature editions used by the comparison, `J(candidate, k1, edition1, slice) = true` implies `J(candidate, k2, edition2, slice) = true`.

A counterexample diagnoses an inconsistent subkind link, incompatible signature editions, or an undeclared context bridge. Repair that governing defect; do not silently edit the extension table. Cross-context classification goes through C.3.3. When a kind bridge is used, C.3.3 governs its `CL^k` and reliance/assurance consequence; the bridge does not by itself change signature formality, claim scope, or either local classification judgment.

Keep these changes distinct:

| Change | Direct consequence | What does not follow automatically |
| --- | --- | --- |
| typed use crosses from one bounded context to another | assess the exact source and target local kinds through C.3.3 and evaluate under the target `KindSignature` edition | kind continuity or an adequate bridge merely because schemes or slices match |
| criterion, evaluation domain, signature `EntityOfConcern`, or effective reference scheme changes within one bounded context | another `KindSignature` episteme edition | a new local kind; C.3.1 decides continuity |
| candidate state changes | reevaluate that candidate in the relevant slice | a new signature or kind |
| context slice changes | another judgment input and potentially another extension | scope on the kind |
| formality or evidence changes | declaration rigor or assertion support changes | a different judgment truth in an otherwise fixed and already settled world |
| publication form changes | another form or carrier for the same episteme may exist | another signature, kind, or classification |

