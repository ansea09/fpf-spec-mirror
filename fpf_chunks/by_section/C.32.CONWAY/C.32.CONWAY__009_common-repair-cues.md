---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Transformer and Transformed Architecture Correspondence"
section_id: "C.32.CONWAY:8"
section_title: "Common Repair Cues"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__009_common-repair-cues.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.32.CONWAY — Transformer and Transformed Architecture Correspondence"
  - "C.32.CONWAY:8 — Common Repair Cues"
line_start: 64689
line_end: 64700
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.3.4"
  - "A.3.4.P"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.29"
  - "C.30"
  - "C.32"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.18"
  - "G.5"
keywords:
  - "Conway correspondence"
  - "changing relation"
  - "coordination cost"
  - "inverse Conway maneuver"
  - "selected-structure correspondence"
  - "transformed holon"
  - "transformer holon"
---

### C.32.CONWAY:8 - Common Repair Cues

| Repair cue | Symptom | First repair |
|---|---|---|
| `TransformerArchitectureOmitted` | The transformed-holon candidate requires independent change, testing, deployment, certification, or maintenance that the declared changing holon cannot support. | Add transformer-side candidates, transformed-side retargeting candidates, joint candidates, and bounded-mismatch candidates before the palette enters comparison, selection, local choice, or decision work. |
| `TransformedArchitectureNoTransformerFit` | The desired transformed-holon architecture cannot be produced or sustained by the declared changing holon. | Open inverse Conway retargeting or transformed architecture retargeting as candidate alternatives. |
| `InverseConwayNoTransformerChange` | The text says inverse Conway but names no transformer-side selected structure change. | Name the transformer-side selected structure changed, affected architecture characteristic, loss, migration burden, and receiving pattern. |
| `CoordinationCostHidden` | A candidate reduces visible coupling in the changed holon while shifting coordination cost into shared work, test, approval, evidence, manufacturing, or operational structures. | Name the transformer-side structure carrying the cost and prepare candidate alternatives that change it, change the transformed architecture, or keep a bounded mismatch. |
| `MirroringNoExceptionTest` | A mirroring claim is used without stating preserved structure, lost structure, exception condition, or evolution window. | Keep it as diagnostic pressure, or use `C.29` for a declared structural-similarity lens. |
| `TransformerTransformedCollapse` | The changing holon architecture and changed holon architecture are written as one architecture. | Name the two architecture refs, selected structures on each side, and the changing relation between them. |
| `BoundedMismatchHidden` | A known mismatch is kept without cost or trigger. | Record exception cost, bounded-use limit, source-return condition, and reopen trigger. |

