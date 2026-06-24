---
chunk_kind: "child"
pattern_id: "A.6.0"
pattern_title: "U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
section_id: "A.6.0:9"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.0/A.6.0__012_rationale.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "A.6.0 — U.Signature - Universal, law-governed declaration for a SubjectKind over a RangedValueKind"
  - "A.6.0:9 — Rationale"
line_start: 10240
line_end: 10244
dependencies:
  - "A.2.6"
  - "A.6.1"
  - "A.6.5"
  - "D.CTX"
  - "E.10"
  - "E.10.D1"
  - "E.5.3"
  - "E.8"
  - "U.Mechanism"
  - "U.RelationSlotDiscipline"
keywords:
  - "RFC 2119"
  - "applicability"
  - "bounded context"
  - "laws"
  - "signature"
  - "vocabulary"
---

### A.6.0:9 - Rationale

**Why “SubjectBlock”?** A.6.1 showed that making the **ranged-over value kind explicit** (here: *RangedValueKind*) avoids category mistakes when moving between domains (e.g., *set-algebra on context slices* vs *equivalence-classes of normalisations*). A.6.0 lifts this to the kernel so every signature can declare **what it is about** before saying **what it provides**.
**Why one universal Block?** Experience with extension and mechanism signatures shows the value of a single canonical shape for Vocabulary, Laws, Applicability, and Alignment; A.6.0 factors that universal core so other families can add headers and views without fragmenting the Kernel.

