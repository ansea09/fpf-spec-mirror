---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "Acting-Side Externalization and Reflexive Split"
section_id: "A.12:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__009_conformance-checklist.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "A.12 — Acting-Side Externalization and Reflexive Split"
  - "A.12:6 — Conformance Checklist"
line_start: 23719
line_end: 23731
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.6"
  - "A.2.7"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "B.2.5"
  - "C.13"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
keywords:
---

### A.12:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A12-1` | A self-action or passive change claim names one exact continuing changed subject by the identity rule that defines that referent and one exact proposed acting entity separately. `ActingSideExternalization@Context` requires `actingEntityRef`; before A.1 recognition it keeps the exact disposition or blocker and leaves `actingSystemRef` unfilled, and after recognition that optional position identifies the same entity under `U.System`. A filled `transformationRef` identifies an A.3.4 bounded change of that same `changedSubjectRef`. `ReflexiveSplit@Context` carries only acting and changed part positions; a companion acting-side frame carries this recognition boundary when needed. |
| `CC-A12-2` | A reflexive case identifies distinct exact entity parts or subsystems inside one containing holon, and each position has its independently obtaining direct part relation. Temporal phases keep their phase identity rules; assignments use A.2.1; parthood uses A.14 or the exact part-relation rule; descriptions use C.2.1; selected structures use A.22. None fills an A.12 part position merely by being nearby. |
| `CC-A12-3` | A.12 does not create `U.Transformer`, `U.Boundary`, or `U.Interaction`. |
| `CC-A12-4` | Bounded transformation claims require `A.3.4`; method and work claims require `A.15` and `A.15.1`. |
| `CC-A12-5` | A system-role-assignment field is filled only by one exact obtaining work-facing `U.SystemRoleAssignment`; any claim that exact Work was performed under it uses `F.6`. System-role-kind relation claims require `A.2.7`. |
| `CC-A12-6` | Evidence and source-use claims use A.10's direct relations; a separately current assurance conclusion uses B.3. |
| `CC-A12-7` | Episteme and publication cases do not assign agency to the episteme or publication form. |
| `CC-A12-8` | Changing another holon does not make it a part of the acting system. A filled singular crossing reference resolves one exact obtaining relation and its direct governor. If that governor is absent, the field stays unfilled and the account returns an exact `A.6.RCD missing-governor` naming the participants, needed sentence, and receiving use. Any containing-whole claim requires a separately admitted exact part-whole relation. |

