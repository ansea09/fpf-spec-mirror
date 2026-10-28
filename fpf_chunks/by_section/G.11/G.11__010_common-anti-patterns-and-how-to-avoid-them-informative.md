---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)"
section_id: "G.11:8"
section_title: "Common Anti-Patterns and How to Avoid Them (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__010_common-anti-patterns-and-how-to-avoid-them-informative.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "G.11 — Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)"
  - "G.11:8 — Common Anti-Patterns and How to Avoid Them (informative)"
line_start: 131406
line_end: 131416
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

### G.11:8 - Common Anti-Patterns and How to Avoid Them (informative)

| Anti-pattern                       | Symptom                                                           | Why it fails                                             | Repair                                                                            |
| ---------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Full-rerun mania or first-slice stop** | An edit reopens every result or only the first located slice. | The scope follows storage or discovery order instead of actual dependence. | Follow §4.3.2 through every affected branch and combining use; retain independent results and coverage limits (CC‑G11.1). |
| **Editionless telemetry**          | Telemetry lacks `…Ref.edition`                                    | Reruns are non-comparable; parity breaks                 | Block publication on missing pins (CC‑G11.2)                                      |
| **Alias-as-semantics**             | `T*` labels are treated as meaning                                | Trigger meaning fragments; regressions become untestable | Dock aliases through `G.Core.TriggerAliasMap.G11`; record canonical ids               |
| **Silent crossing during refresh** | Cross-context or plane reuse lacks required relation/use/reliance grounds, or an actual flow crossing or gate lacks required visibility pins. | The reuse or crossing cannot be checked against its governing rule. | Restore the missing grounds; apply E.18/A.21 harnesses to independently governed flow crossings or gates. Block the affected publication when required grounds or pins are missing (CC‑G11.6). |
| **Default smuggling**              | Refresh introduces “helpful” default dominance or `PortfolioMode` behavior | Competing defaults appear; downstream arguments drift    | Cite governing definitions through `G.Core.DefaultGoverningDefinitionIndex` (CC‑G11.8)                              |
| **Lost currentness warning** | A later recipient relies beyond the supported condition or window because the changed limitation was omitted. | The old result can no longer support that receiving use. | Keep the minimum useful warning or decision with the existing result; use a deprecation notice only for actual deprecation. An unchanged immediate use needs no skip-refresh record (CC‑G11.7). |

