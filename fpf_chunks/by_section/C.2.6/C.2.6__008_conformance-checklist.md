---
chunk_kind: "child"
pattern_id: "C.2.6"
pattern_title: "U.LanguageStateAnchoringMode"
section_id: "C.2.6:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.6/C.2.6__008_conformance-checklist.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.2.6 — U.LanguageStateAnchoringMode"
  - "C.2.6:7 — Conformance Checklist"
line_start: 42865
line_end: 42870
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.18"
  - "A.7"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.7"
  - "C.2.LS"
  - "F.9"
  - "F.9.1"
keywords:
  - "anchoring mode"
  - "document"
  - "embodiment"
  - "model state"
  - "operator loop"
  - "trace"
---

### C.2.6:7 - Conformance Checklist
- `CC-C.2.6-1` Anchoring mode **SHALL NOT** be inferred from publication phrasing alone when it matters for source use, reliance, or bridge interpretation.
- `CC-C.2.6-2` Embodiment-sensitive or operator-loop cases **SHOULD** declare the embodiment or operator anchor explicitly.
- `CC-C.2.6-3` `U.LanguageStateAnchoringMode` **MUST NOT** be collapsed into `U.LanguageStateRepresentationFactorBundle`.
- `CC-C.2.6-4` Mixed-mode declarations **SHALL** list their component modes explicitly.

