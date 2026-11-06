---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
section_id: "B.1.4:8.2"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__014_sota-echoing.md"
commit_sha: "d8dd955fddb923b5b946d2c5865d0665cff5a67e"
heading_path:
  - "B.1.4 — Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
  - "B.1.4:8.2 — SoTA-Echoing"
line_start: 42139
line_end: 42146
dependencies:
  - "A.1.1"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "B.1"
  - "B.1.6"
  - "B.2"
  - "B.2.P"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.18"
  - "E.18.2"
keywords:
---

### B.1.4:8.2 - SoTA-Echoing

For the question "which aggregate answers this receiving use?", B.1.4 adopts A.15.1:9.1's Work-interval distinction: union answers covered time, while convex hull answers elapsed span. C.27.TA:0 and :4.2 explain how to state the bearer, temporal reference and interval on which either calculation relies. The operation and its conditions, rather than a generic total or operator label, decide the result.

In the Work-interval case above, the same inputs give a justified 4-hour covered duration and a justified 5-hour elapsed span. Either can be sufficient for its question; using an unqualified total would hide which question was answered. The order-dependent calculation similarly distinguishes a usable partial-order specification from a unique numerical result that its permitted orders do not yet determine. Sections :2-:4 therefore require the actual rule, result kind and applicable conditions while allowing the ordinary sufficient answer.

The additional burden is recovering those inputs, rules and conditions; an inspectable record is needed only for a receiving use that consumes it. These constructed comparisons support the stated mathematical and subject distinctions. They do not establish empirical effectiveness or a ranking of external engineering notations. Reopen the operation or result choice when the receiving question, input identities, temporal reference, relation facts or applicable operation law changes.

