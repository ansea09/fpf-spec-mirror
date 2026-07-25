---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:4"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__006_forces.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:4 — Forces"
line_start: 50089
line_end: 50097
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:4 - Forces

| Force                        | Tension                                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Parsimony vs sufficiency** | Fewer fields to avoid ceremony **vs** enough to drive admissible gating.                                                              |
| **Unknowns**                 | Many traits are **unknown** in the initial problem record → tri-state semantics propagate to Acceptance without silent coercions.                |
| **CHR admissibility**             | **No mean on ordinals; no unit mixing**; aggregation is admissible only after polarity and scale type are declared.                             |
| **Locality vs portability**  | The problem is **in-room**; cross-context reuse proceeds **through Bridges**, with **CL** and (if planes differ) **CL^plane** penalties → **R** only. |

