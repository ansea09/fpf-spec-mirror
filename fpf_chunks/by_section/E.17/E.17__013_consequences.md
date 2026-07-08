---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:11"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__013_consequences.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:11 — Consequences"
line_start: 73926
line_end: 73934
dependencies:
  - "A.15.4"
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicViewing"
  - "U.MultiViewDescribing"
keywords:
---

### E.17:11 - Consequences

| Benefit | Why it matters | Trade-off and mitigation |
| --- | --- | --- |
| **Arrow traceability.** | Composition preserved across views enables chain‑of‑evidence on pipelines. | Slight authoring overhead → MVPK templates. |
| **Review-ready faces.** | Pins plus CHR references make numeric claims verifiable. | Declared publication checks perform MVPK checks; project gates stay with the relevant `OperationalGate(profile)` or `GateDecision` source when the gate claim is present. |
| **Terminology hygiene.** | Clear View vs Viewpoint, Publication vs Presentation. | Enforce publication-face-kind discipline tokens in CI. |
| **Notation independence.** | Viewpoints talk concerns, not tools. | Provide adapters to local publication toolchains. |

