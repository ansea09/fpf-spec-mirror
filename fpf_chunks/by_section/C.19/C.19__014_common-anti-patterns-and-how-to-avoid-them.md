---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore–Exploit Governor (E/E‑LOG)"
section_id: "C.19:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__014_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "C.19 — Explore–Exploit Governor (E/E‑LOG)"
  - "C.19:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 43489
line_end: 43495
dependencies:
  - "B.3"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.24"
  - "C.28"
  - "G.5"
  - "G.9"
keywords:
  - "DecisionSubject clarification"
  - "EmitterPolicy"
  - "InsertionPolicy"
  - "dominance default routing"
  - "explore-exploit"
  - "keep frontier"
  - "lens id"
  - "live candidate pool"
  - "narrow to subset"
  - "pool-policy result"
  - "reroute"
  - "sunset line"
  - "widen"
---

### C.19:8 - Common Anti-Patterns and How to Avoid Them

- **Treating one scalarized top-1 as the frontier.** Avoid by naming the governing lens and keeping the live frontier distinct from any lens-ranked pick.
- **Running exploration without one explicit next treatment.** Avoid by ending each pass with one explicit pool-side action: `widen`, `keep frontier`, `narrow to subset`, `sunset line`, or `reroute`.
- **Letting `Surprise` or `Illumination` quietly become dominance criteria.** Avoid by promoting them only through one declared lens or policy id and recording that promotion in provenance.
- **Absorbing neighboring questions.** Avoid by rerouting fixed-option choice to `C.11`, enactment-facing call planning to `C.24`, and selector-facing publication to `G.5`.

