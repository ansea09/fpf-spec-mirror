---
chunk_kind: "child"
pattern_id: "E.13"
pattern_title: "Pragmatic Utility and Proxy-to-Value Alignment"
section_id: "E.13:9"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.13/E.13__012_rationale.md"
commit_sha: "6e0d4301aad71e3fff553886d2598e6595d1b963"
heading_path:
  - "E.13 — Pragmatic Utility and Proxy-to-Value Alignment"
  - "E.13:9 — Rationale"
line_start: 103286
line_end: 103291
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "E.12"
  - "E.14"
  - "E.19"
  - "E.2"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
keywords:
  - "Campbell"
  - "Goodhart"
  - "minimally viable value slice"
  - "pragmatic utility"
  - "proxy-to-value alignment"
  - "surrogation"
---

### E.13:9 - Rationale

FPF needs measurement, evaluation, assurance, and release checks, but those checks remain instruments. They are not the value by themselves. `E.13` keeps the visible instrument attached to the intended value and asks whether the value survives optimization pressure.

The pattern is intentionally small. Goodhart-style failure is not repaired by another large audit apparatus. It is repaired by restoring the relation among value, proxy, use position, protected qualities, and a small slice where the value is visible.

