---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "Effect-free episteme morphing"
section_id: "A.6.2:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__004_forces.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "A.6.2 — Effect-free episteme morphing"
  - "A.6.2:3 — Forces"
line_start: 13527
line_end: 13543
dependencies:
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### A.6.2:3 - Forces

* **Epistemic purity vs operational power.**
  Effect-free episteme arrows are useful because their laws can be reasoned about algebraically and composed. If a use needs I/O, solver calls, measurements, or another effect, identify the operation application and Work separately instead of giving that activity to the arrow.

* **Preserve vs retarget.**
  A viewing arrow has endpoint epistemes with the same EntityOfConcern; a retargeting arrow has independently different ones. A separate A.6.4 use assertion states the invariant, visible loss, receiving use, conditions, support, and polarity.

* **Conservativity vs usefulness.**
  EFEM should be **conservative**: no new commitments about the EntityOfConcern beyond what input epistemes already entail. The receiving ClaimGraph may factor, aggregate, normalize, or re-express source content and may use a different representation when the loss and interpretation rule are explicit. Any operation or Work that produces that receiving episteme remains separate.

* **Locality vs reference planes and Bridges.**
  Epistemes are interpreted on **reference planes** (C.2.1). When a use relates two exact source-local senses, test the direct F.9 predicate and cite a Bridge only when it obtains; state the bounded-use claim and any reliance separately. When a use crosses a ReferencePlane, cite its applicable plane relation. EFEM cannot hide either relation inside a “pure” content rewrite, and a local-sense or plane difference alone creates neither one.

* **EntityOfConcern and Description-episteme boundary and specification-use refinement.**
  The EntityOfConcern is not identical to the Description episteme produced by this use; it may itself be `U.Episteme` when an episteme is under concern. `...Description` names a Description episteme, and `...Spec` names one admitted for specification use only when its claims are checkable and the named harness or validation relation can test them. EFEM compares what the two epistemes say, what they concern, and their effective schemes; it states what remains the same and what differs. When grounding or a describing-use viewpoint matters, name the exact relation occurrence or use qualification on each side and compare its facts. The arrow neither changes that occurrence nor establishes viewpoint selection or conformance (A.7, E.10.D2).

