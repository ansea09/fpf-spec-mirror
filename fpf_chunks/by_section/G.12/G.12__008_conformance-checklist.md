---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline-Health Time Series and Views)"
section_id: "G.12:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__008_conformance-checklist.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "G.12 — DHC Dashboards (Discipline-Health Time Series and Views)"
  - "G.12:6 — Conformance Checklist"
line_start: 106561
line_end: 106576
dependencies:
  - "A.19"
  - "A.2.6"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.21"
  - "C.29"
  - "E.10"
  - "E.24.PUB"
  - "E.5.2"
  - "F.17"
  - "F.18"
  - "F.9"
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

### G.12:6 — Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-G12-1` | Every displayed coordinate resolves one exact C.21/C.16 result episteme and the active C.21 replay basis. |
| `CC-G12-2` | ClaimScope is authoritative; TargetSlice is optional, consumed explicitly, and related to that scope. |
| `CC-G12-3` | Direct same-semantics comparison uses C.16 conditions without a Bridge; actual distinct-local-sense use cites exact F.9 direction, admitted use, and loss. |
| `CC-G12-4` | Characteristic, Scale, Unit, Method, MethodDescription, model, calibration, Work, result, result episteme, series episteme, row, slice, publication, form, and carrier are not collapsed. |
| `CC-G12-5` | Numeric, ordinal, target-band, normalization, distance, comparison, and aggregation operations cite their exact lawful definitions. |
| `CC-G12-6` | A series ClaimGraph identifies exact result refs, windows, intended use, ClaimScope, and comparison basis; content change uses the applicable edition rule. |
| `CC-G12-7` | Rows and slices are view-only representations. They introduce no new objective, scalar winner, evidence, acceptance, or authority. |
| `CC-G12-8` | Public names and E.24.PUB publication are conditional and separate; local dashboards need neither. |
| `CC-G12-9` | Refresh telemetry appears only for a named maintenance receiver and identifies the exact affected slice and changed pins. |
| `CC-G12-10` | Optional panel fields appear only with their extension and preserve the source pattern's set, archive, maturity, transfer, shipping, or palette semantics. |
| `CC-G12-11` | The effective G.Core obligations are expanded by value; nil-elided or unused branches are not made mandatory. |

