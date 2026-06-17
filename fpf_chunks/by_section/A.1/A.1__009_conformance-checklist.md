---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "U.Holon, U.System, and U.Episteme"
section_id: "A.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__009_conformance-checklist.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "A.1 — U.Holon, U.System, and U.Episteme"
  - "A.1:7 — Conformance Checklist"
line_start: 1533
line_end: 1546
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.22"
  - "A.6.5"
  - "A.7"
  - "C.2.1"
  - "C.30"
  - "E.10.ARCH"
  - "E.24"
  - "E.24.PUB"
keywords:
---

### A.1:7 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A1-1` | A modeled object is first typed as `U.Entity`, `U.Holon`, `U.System`, `U.Episteme`, or another accepted subtype before part-whole, role, work, or architecture claims rely on it. |
| `CC-A1-2` | Part-whole and aggregation claims apply only to holons or accepted holon subtypes. |
| `CC-A1-3` | A current holon use names the bounded context and governing boundary for the claim. |
| `CC-A1-4` | Contested holon membership uses dependency, internal interaction, and emergence tests. |
| `CC-A1-5` | Acting roles, method enactment, and work occurrence claims attach to `U.System` or an accepted acting-system subtype, not to `U.Episteme`. |
| `CC-A1-6` | A set or collection is not treated as an acting collective unless modeled as a `U.System` with boundary and role assignments. |
| `CC-A1-7` | `U.Episteme` is non-agentive; systems may transform, publish, or use epistemes, but the episteme does not act by itself. |
| `CC-A1-8` | Slot positions such as EntityOfConcern, grounding holon, role holder, transformed entity, or described holon do not create new kinds for their fillers. |
| `CC-A1-9` | Publication forms and descriptions of holons are kept distinct from the holons they describe. |

