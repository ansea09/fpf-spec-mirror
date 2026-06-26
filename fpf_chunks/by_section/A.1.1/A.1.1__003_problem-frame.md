---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext Semantic Frame"
section_id: "A.1.1:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__003_problem-frame.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.1.1 — U.BoundedContext Semantic Frame"
  - "A.1.1:1 — Problem Frame"
line_start: 1704
line_end: 1711
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

### A.1.1:1 - Problem Frame

Meaning is local. The same expression can be coherent in one bounded context and misleading in another. "Service" in software, service operations, military organization, and contract law is not one global object by spelling. "Evidence" in a courtroom, a scientific review, a machine-learning benchmark, and a gate review is not one global role by spelling.

`U.BoundedContext` is the FPF ontic for this locality of meaning. It is a `U.Holon` that holds one semantic frame: local vocabulary, local invariants, local role taxonomy when role-assignment claims are current, local episteme-use/status relations when epistemic-use or status claims are current, and bridge relations to other contexts.

A bounded context is not an enclosing object for all work in a domain. It is the semantic frame in which a term, rule, role assignment, or inference is interpreted.

