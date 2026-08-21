---
chunk_kind: "child"
pattern_id: "A.19.SPR"
pattern_title: "State-Family Precision Restoration"
section_id: "A.19.SPR:7"
section_title: "Common mistakes"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SPR/A.19.SPR__009_common-mistakes.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "A.19.SPR — State-Family Precision Restoration"
  - "A.19.SPR:7 — Common mistakes"
line_start: 28730
line_end: 28739
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

### A.19.SPR:7 - Common mistakes

| Mistake | Symptom | Repair |
| --- | --- | --- |
| **Status word as cover** | `posture` or `status` hides a source relation, evidence result, assurance result, gate decision, or release claim. | Say what item has which value or relation under the direct rule. |
| **One broad word replaces another** | `support` becomes `support posture`, `basis posture`, or `source posture`. | Recover the actual source, evidence, assurance, relation, characteristic, or reader-help claim before choosing words. |
| **Technical field without meaning** | A `...Status` or `...Posture` field has no object, possible values, or rule. | Complete those three facts or replace the field with an ordinary sentence. |
| **Project status in pattern prose** | Review, dispatch, landing, release, or source-control state appears as user guidance. | Move it to the project record and keep only the practical boundary the pattern user needs. |
| **Everything becomes a source-language case** | Evidence, assurance, gate, Work, temporal, or lens-use claims are all sent to source or publication repair. | Use the direct pattern for the actual claim. |

