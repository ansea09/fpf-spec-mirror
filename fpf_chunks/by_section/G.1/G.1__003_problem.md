---
chunk_kind: "child"
pattern_id: "G.1"
pattern_title: "CG‑Frame‑Ready Generator"
section_id: "G.1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.1/G.1__003_problem.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "G.1 — CG‑Frame‑Ready Generator"
  - "G.1:2 — Problem"
line_start: 79275
line_end: 79285
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

### G.1:2 - Problem

Without a chassis, CG‑Frame authoring tends to fail in repeatable ways:

* **SoTA is not locally scoped**: inputs are “in the air”, not a reconstructible set.
* **Generation is ad‑hoc**: variant candidates are emitted without a stable trace of why/when/how.
* **Selection is opaque**: eligibility/acceptance and assurance are not pinned to explicit surfaces.
* **Outputs don’t land in reusable surfaces**: no clean hand‑off into UTS / RoleDescription / Concept‑Sets / RSCR.
* **No kit‑level snapshot**: the scaffold lacks a versioned manifest, so downstream can’t reliably cite “which chassis edition” was used.
* **Refresh is unplanned**: there is no canonical wiring from edits/telemetry/decay to RSCR causes along the P2W path.

