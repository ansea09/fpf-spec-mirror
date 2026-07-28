---
chunk_kind: "child"
pattern_id: "C.32.FAIL"
pattern_title: "Architecture Failure Recognition and Repair"
section_id: "C.32.FAIL:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.FAIL/C.32.FAIL__008_conformance-checklist.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "C.32.FAIL — Architecture Failure Recognition and Repair"
  - "C.32.FAIL:7 — Conformance Checklist"
line_start: 65483
line_end: 65494
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.27"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.P"
  - "C.31"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.24.PUB"
  - "G.5"
keywords:
  - "architecture failure cue"
  - "architecture repair cue"
  - "candidate repair"
  - "repair-entry family"
  - "selected-structure relation"
  - "source overread"
  - "stressed architecture object"
---

### C.32.FAIL:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-C32.FAIL-1` | The cue states a recognizable symptom in practitioner language. | Keeps the pattern usable at first contact. |
| `CC-C32.FAIL-2` | The described holon, bounded context, and architecture object under stress are named. | Prevents source wording from replacing object recovery. |
| `CC-C32.FAIL-3` | The blocked overread is stated in one sentence. | Makes the failure precise enough to repair. |
| `CC-C32.FAIL-4` | The first governing pattern is named. | Keeps architecture, lens, work, evidence, assurance, and decision claims distinct. |
| `CC-C32.FAIL-5` | The repair action changes architecture handling. | Prevents warning-only rows. |
| `CC-C32.FAIL-6` | The stop condition or receiving pattern is named. | Keeps the cue lightweight and composable. |
| `CC-C32.FAIL-7` | New cue rows name the architecture object, first repair action, and stop or receiving pattern. | Prevents warning-bank inflation. |

