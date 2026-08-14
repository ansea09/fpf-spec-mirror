---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual and Temporal Aggregation"
section_id: "B.1.4:4"
section_title: "Admissible Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__007_admissible-checks.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "B.1.4 — Contextual and Temporal Aggregation"
  - "B.1.4:4 — Admissible Checks"
line_start: 36260
line_end: 36291
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
  - "B.2-family"
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

### B.1.4:4 - Admissible Checks

For contextual order aggregation:

- the ordered relation refs are named by value;
- the `OrderSpec` is declared as total order, partial order, or another named relation;
- independence, branch, or join conditions are named when parallel factors are used;
- the record names its included positions, ClaimScope when needed, and admissible use; any holon-boundary crossing is named by an exact relation;
- method, method-description, work, transformation, and resource claims use the patterns that define or test them.

For temporal phase aggregation:

- the carrier identity is recoverable;
- the time window is declared;
- phase intervals are covered and non-overlapping, or the admissible use is narrowed;
- identity change is not hidden as another phase;
- work-resource and evidence-currentness claims use `B.1.6`, `A.10`, and `C.27` when current.

**B.1 invariant carry-through.** `B.1.4` keeps B.1 invariants only after the current relation is recovered. A singleton ordered relation or singleton phase is idempotent for the selected use. Contextual aggregation is deterministic only relative to the declared `OrderSpec` and join or independence conditions. Temporal aggregation is valid only relative to carrier identity, coverage, and non-overlap. Weakest-link and monotonicity claims must name the characteristic being bounded or improved; otherwise the aggregate is only an aggregation record, not a performance, safety, or assurance claim.

#### B.1.4:4.1 - Compact Obligation Rows

| Obligation | What must be named | Why it matters |
| --- | --- | --- |
| Independence and joins | Branch relation refs, join relation refs, and the condition under which branches may be combined. | Prevents an ordered aggregate from silently treating dependent branches as independent evidence or work. |
| Order specification | Total order, partial order, precedence relation, or another named relation over the selected positions. | Keeps order-sensitive claims from being read as unordered collection claims. |
| Decisive dependency relation | The relation that makes one position, delay, or missing step decisive for the aggregate use. | Allows weakest-link claims only when the decisive relation is visible. |
| Carrier identity | The carrier being followed across phases and the condition under which it remains the same EntityOfConcern. | Prevents temporal aggregation from hiding identity change or MHT. |
| Temporal coverage | Time window, phase refs, coverage rule, and non-overlap or overlap policy. | Prevents missing phases and double counting. |
| Chronological discipline | The rule that separates chronological order, logical order, publication order, and performed-work order. | Keeps a document sequence, argument sequence, and work occurrence sequence from substituting for one another. |
| Monotone characteristic | The exact characteristic that is preserved, bounded, or improved when the aggregate grows. | Blocks generic monotonicity claims over an unspecified aggregate. |

