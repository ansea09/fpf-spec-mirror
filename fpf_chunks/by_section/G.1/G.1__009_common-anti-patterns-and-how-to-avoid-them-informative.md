---
chunk_kind: "child"
pattern_id: "G.1"
pattern_title: "CG‑Frame‑Ready Generator"
section_id: "G.1:8"
section_title: "Common Anti‑Patterns and How to Avoid Them (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.1/G.1__009_common-anti-patterns-and-how-to-avoid-them-informative.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "G.1 — CG‑Frame‑Ready Generator"
  - "G.1:8 — Common Anti‑Patterns and How to Avoid Them (informative)"
line_start: 98593
line_end: 98609
dependencies:
  - "A.10"
  - "A.15.3"
  - "A.19"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.Core"
keywords:
  - "CGFrameLibraryId"
  - "CGKitId manifest"
  - "RSCR linkage surfaces"
  - "RefreshReadinessCardId"
  - "ShortlistId"
  - "SoTA_SetId"
  - "UTS/Name Cards"
  - "VariantPoolId"
  - "and set-result scaffold"
  - "edition pins"
  - "generator"
  - "generator chassis"
  - "selector"
  - "set-result outcome"
  - "set-return selection"
  - "shipping and refresh boundaries"
  - "six-card kit (M1-M6)"
---

### G.1:8 - Common Anti‑Patterns and How to Avoid Them (informative)

* **Anti‑pattern: “Shadow CN/CG spec inside the chassis.”**
  *Avoid:* keep CN/CG as cited governing spec refs; use pins and governing definition references only.

* **Anti‑pattern: “Chassis hard‑codes a favourite algorithm.”**
  *Avoid:* keep M3 core method‑agnostic; add algorithm families only via Extensions with explicit governing patterns and edition pins.

* **Anti‑pattern: “Shortlist = one winner.”**
  *Avoid:* preserve selected-set returns; any singleton choice must be an explicit downstream decision rule (policy‑bound).

* **Anti‑pattern: “Refresh plan described as prose triggers.”**
  *Avoid:* record canonical `RSCRTriggerKindId` and payload pins; aliases only as labels and only if docked.

* **Anti-pattern: “Packaging implies shipping governance.”**
  *Avoid:* treat M5 as a library index; treat M6 as readiness wiring; ship only via `G.10`.

