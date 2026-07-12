---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
section_id: "G.12:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__004_forces.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "G.12 — DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
  - "G.12:3 — Forces"
line_start: 96321
line_end: 96328
dependencies:
  - "A.19"
  - "C.18"
  - "C.19"
  - "C.21"
  - "E.10"
  - "E.5.2"
  - "F.17"
  - "F.18"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.Core"
keywords:
  - "DHC"
  - "PathId/PathSliceId"
  - "RSCR/refresh wiring"
  - "UTS twins"
  - "admissible telemetry"
  - "dashboard"
  - "discipline health"
  - "edition pins"
  - "time-series"
  - "view-only slices"
---

### G.12:3 — Forces

* **Legality and comparability are governed by CN-Spec and CG-Spec.** Dashboards must not invent local legality/acceptance/normalization “mini‑specs”; they pin and cite **CN‑Spec** and **CG‑Spec** surfaces as required by **G.Core** conformance.
* **Ordinal discipline is non‑negotiable.** The most common dashboard failure mode is illicit arithmetic on ranks/categories; the kit must make “compare‑only” enforceable.
* **Set‑returning discipline survives into views.** Dashboards must not silently scalarize partial orders or selector selected-set results; any scalarization/promotion is an explicit governing-pattern policy cited through **G.Core** conformance; semantics are governed by the relevant pattern or policy.
* **Edition‑awareness is the difference between “trend” and “drift”.** If the method definition changes, the dashboard must either (i) fork series edition, or (ii) emit telemetry and refresh slices under pinned conditions.
* **RSCR must be actionable.** Causes are emitted as **canonical ids** (typed trigger kinds + id‑valued pins), not prose.

