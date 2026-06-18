---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "U.Holon, U.System, and U.Episteme"
section_id: "A.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.1 — U.Holon, U.System, and U.Episteme"
  - "A.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 1546
line_end: 1555
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

### A.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| System as universal root | A theory, document, or model receives physical system properties. | Re-type as `U.Episteme` or another holon subtype, then use the governing pattern for the claim. |
| Document edited itself | A model, theory, or document is said to perform a revision. | Name the `U.System` in role that performed the work and the `U.Episteme` that was changed. |
| Collection as actor | A list or set is said to decide or perform work. | Model a collective `U.System` or name the actual acting system-in-role. |
| Boundary by section heading | A document section, org chart box, or folder is treated as a holon boundary by appearance. | Name the bounded context and boundary relation; apply membership tests. |
| Architecture without holon | A selected structure is discussed without the holon whose structure is selected. | Use A.1 to name the holon, then `A.22` and `C.30` for selected structure and architecture. |

