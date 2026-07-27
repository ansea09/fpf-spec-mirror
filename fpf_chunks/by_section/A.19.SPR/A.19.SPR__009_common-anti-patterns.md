---
chunk_kind: "child"
pattern_id: "A.19.SPR"
pattern_title: "State-Family Precision Restoration"
section_id: "A.19.SPR:7"
section_title: "Common anti-patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SPR/A.19.SPR__009_common-anti-patterns.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.19.SPR — State-Family Precision Restoration"
  - "A.19.SPR:7 — Common anti-patterns"
line_start: 28897
line_end: 28906
dependencies:
  - "A.10"
  - "A.16"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.P"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.P"
  - "C.27"
  - "C.29"
  - "C.30.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.8"
  - "E.9.DA"
  - "F.18"
keywords:
---

### A.19.SPR:7 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Posture as cover.** | A sentence uses `posture` to avoid saying source relation, evidence path, assurance result, gate decision, or release state. | Recover the bearer and governing pattern; rewrite to the FPF field or block named by value. |
| **Support-to-state laundering.** | Old `support` wording becomes `support posture`, `basis posture`, or `source posture`. | Apply `A.6.P`, `A.6.6`, `C.2.P`, `A.10`, `B.3`, `C.16.P`, `C.29`, or the pattern governing the recovered claim. |
| **Finite field without value set.** | A `...Status` or `...Posture` field appears with no values or non-overread boundary. | Complete the field or replace it with the phrase or record required by the governing pattern. |
| **External administrative state in pattern prose.** | A project-side administrative, review, dispatch, release or admission, or source-control state appears as if it were user-facing pattern guidance. | Move the state claim to the project-side record; keep only an informative boundary if useful. |
| **Semio sink.** | Every state-like word is sent to source-publication or language-state repair. | Use semio only for source, publication, or language-state cases; assign evidence, assurance, gate, work, temporal, lens-use, and administrative cases to governing patterns or project-side records. |

