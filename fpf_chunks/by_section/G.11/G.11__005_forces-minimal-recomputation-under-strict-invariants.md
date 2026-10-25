---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)"
section_id: "G.11:3"
section_title: "Forces — Minimal recomputation under strict invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__005_forces-minimal-recomputation-under-strict-invariants.md"
commit_sha: "64ebce216e1be91beb67120d83f4308a42795eaf"
heading_path:
  - "G.11 — Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)"
  - "G.11:3 — Forces — Minimal recomputation under strict invariants"
line_start: 131397
line_end: 131404
dependencies:
  - "A.10.1"
  - "A.6.RCD"
  - "B.3.4"
  - "C.11.DUA"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.28"
  - "C.32.P2S"
  - "E.18"
  - "F.15"
  - "G.10"
  - "G.12"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G11"
keywords:
  - "Bridge Sentinels"
  - "PathSlice"
  - "RSCR"
  - "deprecation"
  - "edition-aware"
  - "epistemic debt"
  - "re-shipping"
  - "refresh"
  - "telemetry"
  - "use-qualified currentness"
---

### G.11:3 - Forces — Minimal recomputation under strict invariants

* **Minimal scope vs. completeness.** Include every actual dependent use that can change, while excluding unrelated work. The resulting closure can contain several slices.
* **Operational urgency vs. auditability.** Actual refresh Work must remain inspectable through the needed pins, references and paths. A currentness decision or an unchanged use must not become a fictitious Work occurrence.
* **Alias stability vs. semantic unification.** Existing trigger labels must remain usable, but their meaning must be one governing definition and id-based.
* **Modularity vs. orchestration power.** `G.11` must coordinate harvesting, parity, and shipping without re-implementing them or importing discipline-specific method semantics into core.
* **Policy-bound behavior vs. “smart defaults.”** Ordering, priority and budget handling must follow their declared policies rather than hidden universal rules.

