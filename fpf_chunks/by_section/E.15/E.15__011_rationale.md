---
chunk_kind: "child"
pattern_id: "E.15"
pattern_title: "Pattern Change, Edition Continuity, and Impact Analysis"
section_id: "E.15:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.15/E.15__011_rationale.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "E.15 — Pattern Change, Edition Continuity, and Impact Analysis"
  - "E.15:10 — Rationale"
line_start: 81178
line_end: 81185
dependencies:
  - "C.18"
  - "C.19"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.8"
  - "E.9"
  - "F.0.1"
  - "F.1"
  - "F.15"
  - "F.9"
keywords:
---

### E.15:10 - Rationale

The architecture is deliberately asymmetric. The common case receives a short path because extra alternatives and records cannot improve an already understood bounded repair. The strong branch remains because architecture, ontology, and current-source decisions sometimes have several non-dominated answers.

Exact predecessor comparison and affected-reach analysis work together. The predecessor prevents history from being rewritten; actual dependency prevents an edition label from reopening everything. Independent preservation probes answer a different question from an author's change explanation: they test what the explanation may have omitted.

Delta-Class stays useful as a compact impact signal, but only after the real change is known. E.21/E.22 own pattern quality, E.9 owns content decisions, E.19 owns review, and lifecycle patterns own publication and landing. E.15 connects these results without duplicating them.

