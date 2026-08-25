---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Relation"
section_id: "B.2.5:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__009_conformance-checklist.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Relation"
  - "B.2.5:6 — Conformance Checklist"
line_start: 37689
line_end: 37700
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15.1"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.3.4"
  - "A.6.M"
  - "B.1"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.13"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30.LCA"
  - "G.6"
keywords:
---

### B.2.5:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-B2.5-1` | A conforming use names supervised holons and the supervising acting system; it adds the local supervisor system-role kind and exact assignment only when each independently obtains. |
| `CC-B2.5-2` | A conforming use names the observation, report, or source side and the influence, constraint, or objective side. It also names any feedback policy, ClaimScope, qualification window, and evidence that changes the relation claim or its later use. |
| `CC-B2.5-3` | `SupervisorSubholonFeedbackRelation@Context` is used instead of loop wording unless a separate C.29 mathematical-lens use selects a loop object. |
| `CC-B2.5-4` | No `U.TransformerRef` or `U.InteractionRef` is created. |
| `CC-B2.5-5` | Parthood, control-structure view, publication and source-use relation, and feedback relation are kept separate. |
| `CC-B2.5-6` | Stability, safety, timing, causal, evidence, assurance, gate, and mathematical-lens claims use the patterns that define or test them. |
| `CC-B2.5-7` | Episteme examples name the acting systems that perform review, revision, publication, or use. |

