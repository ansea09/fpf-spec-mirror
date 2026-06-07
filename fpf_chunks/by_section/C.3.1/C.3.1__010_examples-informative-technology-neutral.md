---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind & SubkindOf (Core)"
section_id: "C.3.1:9"
section_title: "Examples (informative, technology‑neutral)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__010_examples-informative-technology-neutral.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "C.3.1 — U.Kind & SubkindOf (Core)"
  - "C.3.1:9 — Examples (informative, technology‑neutral)"
line_start: 37756
line_end: 37763
dependencies:
  - "A.1"
  - "A.2.6"
  - "C.3.2"
  - "C.3.3"
keywords:
  - "kind"
  - "partial order"
  - "subkind"
  - "type hierarchy"
---

### C.3.1:9 - Examples (informative, technology‑neutral)

1. **Vehicle/PassengerCar.**
   Mint `Kind Vehicle`. Later add `PassengerCar ⊑ Vehicle`. Claims about **Vehicle** may be reused by narrowing to **PassengerCar** without touching **G**. Scope remains an independent predicate over `U.ContextSlice`.

2. **Request/AuthenticatedRequest.**
   If multiple policies speak about “authenticated requests,” declare `AuthenticatedRequest ⊑ Request`. Do **not** widen G to compensate for missing authentication; either change the producer’s kind or insert an adapter (C.3.2/C.3.4) while keeping G honest.

