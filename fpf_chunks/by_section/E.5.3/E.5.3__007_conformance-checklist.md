---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency between FPF Families"
section_id: "E.5.3:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__007_conformance-checklist.md"
commit_sha: "5e9f4d868afa1f9db90d4c7ff6840bd55f3b8d18"
heading_path:
  - "E.5.3 — Unidirectional Dependency between FPF Families"
  - "E.5.3:6 — Conformance Checklist"
line_start: 102498
line_end: 102505
dependencies:
  - "E.4"
  - "E.5"
keywords:
---

### E.5.3:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC-UD.1** | The graph of actual imports among FPF ecosystem family members **MUST** be acyclic, including imports within a family. |
| **CC-UD.2** | The permitted directions for distinct families **SHALL** form a strict partial order, including after an extension. Each cross-family import must follow that order. A same-family import must satisfy CC-UD.1. |
| **CC‑UD.3** | Reject an import forbidden by the governing order. A DRR can resolve the design without that import or propose an amendment under E.3 and E.9. The amendment must take effect before the import can be admitted. |

