---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:8"
section_title: "Common Anti-Patterns and How to Avoid Them (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__010_common-anti-patterns-and-how-to-avoid-them-informative.md"
commit_sha: "14f263bd90d449803a2ec6cb57ee7f620cc41bed"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:8 — Common Anti-Patterns and How to Avoid Them (informative)"
line_start: 107216
line_end: 107226
dependencies:
  - "A.6.RCD"
  - "B.3.4"
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
| **Full-rerun mania**               | Any edit triggers a global rebuild                                | Costs explode; drift hides (no scope rationale)          | Enforce slice-scoped plans (CC‑G11.1); require closure rationale for global scope |
| **Editionless telemetry**          | Telemetry lacks `…Ref.edition`                                    | Reruns are non-comparable; parity breaks                 | Block publication on missing pins (CC‑G11.2)                                      |
| **Alias-as-semantics**             | `T*` labels are treated as meaning                                | Trigger meaning fragments; regressions become untestable | Dock aliases through `G.Core.TriggerAliasMap.G11`; record canonical ids               |
| **Silent crossing during refresh** | Refresh changes context or plane assumptions without crossings       | Violates crossing visibility; penalties become hidden    | Require crossing pins and E.18 visibility; block publication (CC‑G11.6)             |
| **Default smuggling**              | Refresh introduces “helpful” default dominance or `PortfolioMode` behavior | Competing defaults appear; downstream arguments drift    | Cite governing definitions through `G.Core.DefaultGoverningDefinitionIndex` (CC‑G11.8)                              |
| **Lost currentness warning** | A later recipient relies beyond the supported condition or window because the changed limitation was omitted. | The old result can no longer support that receiving use. | Keep the minimum useful warning or decision with the existing result; use a deprecation notice only for actual deprecation. An unchanged immediate use needs no skip-refresh record (CC‑G11.7). |

