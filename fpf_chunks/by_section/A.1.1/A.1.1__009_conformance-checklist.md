---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext Semantic Frame"
section_id: "A.1.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__009_conformance-checklist.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.1.1 — U.BoundedContext Semantic Frame"
  - "A.1.1:7 — Conformance Checklist"
line_start: 1814
line_end: 1826
dependencies:
  - "A.1"
  - "A.15"
  - "A.6.5"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.24"
  - "E.24.PUB"
  - "F.0.1"
  - "F.18"
  - "F.9"
  - "U.Holon"
keywords:
---

### A.1.1:7 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A1.1-1` | A bounded-context claim names the `U.BoundedContext` by value; broad domain-family labels do not govern local meaning. |
| `CC-A1.1-2` | The context has a boundary, local vocabulary, local invariant set, local role taxonomy when role-assignment claims are current, and local episteme-use/status relation set when epistemic-use/status claims are current. |
| `CC-A1.1-3` | Role assignments name exactly one bounded context for interpretation. |
| `CC-A1.1-4` | Cross-context use is expressed through bridge relations with direction, relation kind, fit, loss, and scope. |
| `CC-A1.1-5` | No context-to-context containment or inheritance is inferred without an explicit bridge or governing relation. |
| `CC-A1.1-6` | Publication forms that describe a context are not treated as the context itself. |
| `CC-A1.1-7` | Time, edition, and currentness qualifiers refine the context boundary or publication, but they do not create a new context unless local meaning changes. |
| `CC-A1.1-8` | Objects interpreted inside a context are not automatically parts of the context holon. |

