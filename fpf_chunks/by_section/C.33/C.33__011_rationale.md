---
chunk_kind: "child"
pattern_id: "C.33"
pattern_title: "Structural Information Adequacy for Architecture Capture and Source Return"
section_id: "C.33:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.33/C.33__011_rationale.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "C.33 — Structural Information Adequacy for Architecture Capture and Source Return"
  - "C.33:10 — Rationale"
line_start: 62113
line_end: 62120
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "A.6.M"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.18"
  - "F.15"
  - "F.9"
  - "G.5"
keywords:
  - "captured structure"
  - "carrier"
  - "lost structure"
  - "observer boundary"
  - "selected structure"
  - "source return"
  - "structural information adequacy"
---

### C.33:10 - Rationale

Architecture work often starts from carriers that are neither useless nor complete. A mature pattern must preserve both facts. If C.33 only says "do not confuse the carrier with architecture," it becomes a negative catalogue. If it treats every carrier as an architecture description or measurement, it duplicates C.30, C.16, and C.32.ACE. The chosen solution is a small adequacy note whose center is captured selected structure, lost structure, admissible use, and source return.

This split keeps P2S as the whole architecturing spine and C.32 as candidate synthesis owner. C.33 does not synthesize architecture and does not decide the project architecture. It gives the next owner a typed account of what a carrier contributes and what must still be recovered.

The source choices explain the fields. Epiplexity motivates observer-bounded structural information but not a universal architecture metric. Multi-relational structural entropy motivates relation-kind awareness but not adequacy by number. Sapunov and ToCS motivate partial observability, active-passive gap, invariant fields, confidence, and unexplored regions. GonzoML motivates richer neural architecture operation language without making those labels FPF ontology.

