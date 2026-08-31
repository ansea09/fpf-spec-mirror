---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:8"
section_title: "Subkind Comparison and Change"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__010_subkind-comparison-and-change.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:8 — Subkind Comparison and Change"
line_start: 45436
line_end: 45455
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
  - "E.24.UK"
keywords:
---

### C.3.2:8 - Subkind Comparison and Change

Whenever `SubkindOfObtains(k1,k2)` holds under C.3.1, its practical consequence is checked only where both candidate requests are admissible under the aligned declarations:

> For the same candidate and slice, an admissible `true` judgment for `k1` must not coexist with an admissible `false` judgment for `k2` within the relation's declared applicability.

C.3.1 decides whether exact criterion entailment or exhaustive evaluation over a deliberately closed finite domain makes the relation obtain. Non-exhaustive classifications support its assertion or expose a counterexample; they do not establish an open-domain relation. A `not-applicable` request is outside the comparison. Cross-local use first compares kind identities: reuse the same kind directly when its membership distinction continues; only distinct kinds with an obtaining correspondence use C.3.3. A bridge never transfers source classification truth.

Keep these changes distinct:

| Change | Direct consequence | What does not follow automatically |
| --- | --- | --- |
| practice, source, team, or locality changes | compare the exact kind definitions and declaration meanings | another kind or `KindBridge` |
| two distinct kinds and a directional correspondence are current | test C.3.3 obtaining and evaluate the receiving candidate afresh | transferred source truth |
| criterion, candidate domain, applicability, `EntityOfConcern`, or scheme changes | another `KindSignature` edition; C.3.1 decides kind continuity | another kind merely by edition |
| candidate fails ValueKind or slice applicability | `not-applicable`; no judgment | `unknown` or `false` |
| candidate state changes | reevaluate in the relevant slice when admissible | a new signature or kind |
| support or dependency becomes unavailable | `unknown` for an admissible request | `not-applicable` or known `false` |
| publication form changes | another form or carrier may express the same episteme | another signature, kind, or classification |

