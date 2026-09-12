---
chunk_kind: "child"
pattern_id: "C.29.2"
pattern_title: "Computational Formulation"
section_id: "C.29.2:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.2/C.29.2__003_problem.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.29.2 — Computational Formulation"
  - "C.29.2:2 — Problem"
line_start: 60166
line_end: 60177
dependencies:
  - "A.10"
  - "A.3.1"
  - "A.3.3"
  - "A.6.1"
  - "A.6.3.RT"
  - "B.1.5"
  - "B.1.6"
  - "B.3"
  - "B.5"
  - "C.16"
  - "C.2.1"
  - "C.29.1"
  - "C.29.3"
  - "C.39"
  - "C.40"
keywords:
---

### C.29.2:2 - Problem

Knowing a condition that the answer satisfies does not always tell a practitioner how to get that answer. Writing `y = argmin f(x)` specifies a selection problem; it supplies a computation only together with a way to represent and search or otherwise solve the admitted problem. Conversely, a running procedure may return a value without establishing that it satisfies the requested condition.

Three failures make this gap expensive:

- A representation identifies cases that require different answers. No later procedure using only that representation can recover the missing distinction without another input.
- An operation such as “solve”, “update” or “sample” hides the very construction that is unavailable. Giving it a name does not make it elementary or obtainable.
- A procedure is assessed under the wrong semantics or cost model. Exact integers, fixed-width words and rounded values have different operations; a single arithmetic instruction may manipulate a growing number of bits.

The repair is to connect the requested answer to an actual construction, then follow the construction's meaning and costs. It need not start by writing software. A hand calculation, an invariant or a storage count can locate the decisive obstacle first.

