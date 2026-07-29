---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:8"
section_title: "Gating Profiles (applied to E.18)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__011_gating-profiles-applied-to-e-18.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:8 — Gating Profiles (applied to E.18)"
line_start: 82458
line_end: 82470
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.18.NET"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.18:8 - Gating Profiles (applied to E.18)
This table is a selected-structure coverage table for E.18 crossings and path slices. It does not govern `GateProfile` semantics. `A.21` governs gate decision semantics, folds, `DecisionLog` minima, and the GateFit check-catalog boundary.

> Gating is expressed as **publication-gating** per E.17 profiles. The structure model aligns with the **CC items** listed for the chosen profile; broader obligation profiles include all narrower-profile items.

| Profile                          | Required CC‑items                                         | Additional notes                                                                               |
| -------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Lean**                         | 01–06, 08–09, 11–12, 15, 19–21, 25                                                                                                           | Minimal MVPK presence; LaunchGate keeps `FreshnessUpToDate` and `DesignRunTagConsistency`. |
| **Core**                         | **Lean** + 07, 10, 13–14, 16–18, 22–23, 24                                                                                                  | Adds CV⇒GF order, CSLC pins, budgeted loop, guards, valuation and sentinel refresh, error folds, SquareLaw, and the UNM declaration locus. |
| **Safety‑Critical or RegulatedX** | **Core** + profile‑specific GateChecks (safety envelope, regulator id and editions) with stricter folds per **CC-E18‑22**; SquareLaw audits tightened | — |

**Recommended defaults (non-normative, tie-in to `A.21` and `G.11`).** Profiles inherit along a `PathSlice`; local overrides only **add** GateChecks; weakening uses a new `PathSlice` and refresh wiring through the current `G.11` locus when refresh wiring is current.

