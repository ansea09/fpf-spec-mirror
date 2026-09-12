---
chunk_kind: "child"
pattern_id: "C.29.2"
pattern_title: "Computational Formulation"
section_id: "C.29.2:10"
section_title: "Architectural Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.2/C.29.2__011_architectural-rationale.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.29.2 — Computational Formulation"
  - "C.29.2:10 — Architectural Rationale"
line_start: 60880
line_end: 60891
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

### C.29.2:10 - Architectural Rationale

**Why formulate around the answer and operations together?** Starting with a data structure is convenient when it already supports the required query. Otherwise it can discard the needed distinction or force an unnecessarily expensive computation. Starting only with an answer predicate has the opposite defect: it can hide unavailable operations. Connecting the two makes each choice answerable to the same use.

**Why recover a known construction before inventing another?** Its procedure and argument may already resolve the question at low cost. A new representation or specialized algorithm becomes worthwhile when a concrete input property, repeated use, precision requirement or resource limit changes the result. A direct formula, a library routine, exhaustive enumeration and a new algorithm are genuine alternatives; none wins merely by looking more formal or sophisticated.

**Why keep a simple procedure when a faster one exists?** A small exact baseline exposes meaning and can provide expected results for selected implementation tests. Bisection's interval reduction is easy to inspect; a more elaborate solver can reduce expensive evaluations. The choice depends on the present cost of evaluation and the needed guarantee. A reference calculation is not required if an already adequate construction supplies those answers.

**Why separate computability, correctness and feasibility?** A finite procedure can be correct yet exceed available memory. A fast implementation can return the wrong interpretation. A failed search can leave computability open. Distinguishing these questions makes the return useful: obtain a construction, repair its argument, choose another representation, or change the execution arrangement.

**Why allow formulation to return from realization?** Available physical operations may suggest a better computational model, and a mismatch may reveal that an assumed primitive or output is unavailable. The connected use therefore permits revising the formulation and the proposed executing arrangement together. The formulation still needs an interpretable result and a justified computational claim; the physical comparison remains a separate contribution.

