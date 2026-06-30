---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human‑Centric Working‑Model"
section_id: "E.14:9"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "E.14 — Human‑Centric Working‑Model"
  - "E.14:9 — Common Anti-Patterns and How to Avoid Them"
line_start: 71434
line_end: 71443
dependencies:
  - "B.3.5"
  - "C.13"
  - "C.2.3"
  - "E.10"
  - "E.7"
  - "E.8"
keywords:
  - "assurance layers"
  - "grounding"
  - "human-centric"
  - "publication surface"
  - "working model"
---

### E.14:9 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Machinery-first working text | The reader meets constructor traces, proof apparatus, or evidence ids before the working model. | Put the recognition text and chosen Working-Model labels first; keep assurance below. |
| Assurance leakage upward | Mapping, proof, or empirical records rename the public working vocabulary. | Preserve downward grounding: Working-Model terms are not back-defined by assurance publications. |
| Slash-label compromise | Several source labels are displayed because no chosen governed value was selected. | Use Mapping to record source labels and show one chosen Working-Model label. |
| Structure-time collapse | Order, phase, or execution is encoded as part-whole structure. | Keep time and order in their governing relation families. |
| Forever-light prose | Human-facing prose becomes so small that the reader cannot recover the problem, payoff, or assurance boundary. | Keep recognition text concise but still include problem framing, rationale, and worked slices. |

