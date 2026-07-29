---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__014_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 50046
line_end: 50052
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "G.11"
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
- **Running exploration without one explicit next treatment.** Avoid by ending each pass with one explicit pool-side treatment: `widen`, `keep frontier`, `narrow to subset`, or `sunset line`. If the current question is no longer pool policy, name the next governing pattern instead of inventing another pool treatment.
- **Letting `Surprise` or `Illumination` quietly become dominance criteria.** Avoid by promoting them only through one declared lens or policy id and recording that promotion in provenance.
- **Absorbing other governing questions.** Avoid by applying `C.11` for fixed-option choice, `C.24` for enactment-facing planning, and `G.5` for selector-facing publication.

