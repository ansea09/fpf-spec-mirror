---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "U.EvidenceRole"
section_id: "A.2.4:14"
section_title: "Migration notes (quick wins)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__015_migration-notes-quick-wins.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "A.2.4 — U.EvidenceRole"
  - "A.2.4:14 — Migration notes (quick wins)"
line_start: 3308
line_end: 3315
dependencies:
  - "A.10"
  - "A.2"
  - "B.3"
keywords:
  - "claim"
  - "episteme"
  - "evidence"
  - "justification"
  - "support"
---

### A.2.4:14 - Migration notes (quick wins)

1. **Enumerate claims**: For each evidence collection, identify claims and create explicit bindings with polarity.
2. **Separate work from reports**: Facts stay on `U.Work`; create report epistemes to link as evidence.
3. **Name the calculus**: Replace free-form confidence with context-declared weight model and required inputs.
4. **Fence by version/time**: Bindings carry `timespan` and version fences; add decay class if applicable.
5. **Bridge explicitly**: Cross-context evidence goes through `U.Alignment`, not by fiat.

