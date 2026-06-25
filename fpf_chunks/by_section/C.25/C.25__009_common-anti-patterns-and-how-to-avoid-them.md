---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 47916
line_end: 47924
dependencies:
  - "A.15"
  - "A.16.0"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.26.3"
  - "C.33"
  - "C.34"
  - "C.35"
  - "F.9"
  - "F.9.1"
keywords:
  - "admissible quality-family use"
  - "characteristic plus scope"
  - "endpoint classification"
  - "failure mode"
  - "ility"
  - "mechanism/status slots"
  - "proxy metric"
  - "quality bundle"
  - "quality family"
  - "viability envelope"
---

### C.25:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **One-number `-ility`** | `Resilience = 82` with no declaration of what is being measured and what scope/scenario is intended. | `CC-C.25-2` requires a Q-Bundle when the family is composite. |
| **Scope as metric** | The claim treats wider applicability as a higher quality value rather than as a larger USM set. | `CC-C.25-3` keeps scope set-valued and non-CHR. |
| **Mechanism equals quality** | Presence of a mechanism or certificate is reported as if it were the measurement itself. | `CC-C.25-4` keeps mechanism/status slots distinct from measures. |
| **Collapsed guard prose** | One sentence mixes coverage, thresholds, windows, and mechanisms without typed separation. | `C.25` rewrites the claim into explicit slots and typed guard factors. |

