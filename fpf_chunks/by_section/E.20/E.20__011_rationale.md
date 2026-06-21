---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol"
section_id: "E.20:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__011_rationale.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "E.20 — Mechanism Introduction Protocol"
  - "E.20:10 — Rationale"
line_start: 71745
line_end: 71750
dependencies:
  - "A.15.3"
  - "A.6.1"
  - "A.6.7"
  - "E.10"
  - "E.15"
  - "E.18"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.18"
  - "G.2"
  - "G.Core"
  - "G.x"
keywords:
  - "MIP-run manifest"
  - "P2W seam"
  - "PQG profiles"
  - "SlotKind lexicon discipline"
  - "alias docking"
  - "authoring protocol"
  - "canonical card-first"
  - "governing-definition assignment"
  - "mechanism introduction"
  - "no dangling …IntensionRef"
  - "regression envelope"
  - "suite boundary hygiene"
  - "typed RSCR triggers"
---

### E.20:10 - Rationale

Mechanisms are high-leverage semantic units: a small change can touch suites, planned baselines, wiring modules, and audits. Without a protocol, the corpus tends toward **semantic duplication across governing loci** and **non-local correctness** (you can’t know what changed without reading everything).

Governing-definition-directed authoring is a pragmatic compromise: it does not depend on tooling, yet it gives a stable governing-definition map that enables subsequent review and refresh.

