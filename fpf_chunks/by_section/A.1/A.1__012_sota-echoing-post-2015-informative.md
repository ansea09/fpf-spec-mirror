---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "Holonic Foundation: Entity → Holon"
section_id: "A.1:11"
section_title: "SoTA-Echoing (post‑2015, informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__012_sota-echoing-post-2015-informative.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "A.1 — Holonic Foundation: Entity → Holon"
  - "A.1:11 — SoTA-Echoing (post‑2015, informative)"
line_start: 1284
line_end: 1295
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.14"
  - "A.2"
  - "B.1"
  - "U.Boundary"
  - "U.Episteme"
  - "U.Holon"
  - "U.System"
keywords:
  - "U.Episteme"
  - "U.System"
  - "entity"
  - "holon"
  - "part-whole composition"
  - "system boundary"
---

### A.1:11 - SoTA-Echoing (post‑2015, informative)

This solution echoes several modern (post‑2015) research and engineering streams. We **adopt** their boundary‑and‑composition insights, but **reject** any requirement to commit to a single formalism (per Notational Independence).

| Stream | Representative sources | Adopt / Adapt / Reject | What we take (and what we diverge from) |
|---|---|---|---|
| Compositional open systems | Baez & Courser (2017); Fong & Spivak (2019) | **Adapt** | Take the idea that composition should be explicit and typed; diverge by keeping the Core notation‑independent (no category‑theory prerequisite). |
| Software boundaries and bounded contexts | Newman (2021); Vernon (2022) | **Adopt** | Take boundary‑scoped meaning and ownership as the default; diverge by lifting “bounded context” to a kernel boundary concept rather than a software‑only practice. |
| FAIR and provenance for epistemes and carriers | Wilkinson et al. (2016); Boeckhout et al. (2018) | **Adopt** | Take provenance and episteme/carrier separation; diverge by modelling claim-bearing knowledge as non-agentive `U.Episteme` rather than agents. |
| Digital twin / digital thread | Grieves & Vickers (2017); NIST DT/Thread (2019–2021) | **Adapt** | Take the run↔design seam; diverge by requiring a boundary kind at the holon level. |
| Systems/control criteria for emergence | Matni et al. (2024) | **Adopt** | Take emergence as a criterion for systemhood; diverge by requiring explicit boundary declarations even when “obvious”. |

