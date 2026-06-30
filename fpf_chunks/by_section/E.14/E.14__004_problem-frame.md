---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human‑Centric Working‑Model"
section_id: "E.14:2"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__004_problem-frame.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "E.14 — Human‑Centric Working‑Model"
  - "E.14:2 — Problem Frame"
line_start: 71184
line_end: 71201
dependencies:
  - "B.3.5"
  - "C.13"
  - "C.2.3"
  - "E.10"
  - "E.7"
  - "E.8"
keywords:
  - "assurance layers"
  - "grounding"
  - "human-centric"
  - "publication surface"
  - "working model"
---

### E.14:2 - Problem Frame

Teams need **one shared Working-Model** to make decisions at speed. Historically this shared model either:

* **drifts into jargon** - different terms for one shared working-model value, slash-labels, partial overlaps; or
* **calcifies into machinery** - too formal for day-to-day design and review.

Both failure modes create friction between two audiences:
(1) **working users** (engineers, programme managers, policy owners) who need a **small, stable Working-Model text**, and
(2) **assurance authors** (ontologists, methodologists, auditors) who need **proofs that the Working-Model text is sound**.

E.14 resolves the impasse by **separating concerns**:

* A **Working-Model layer**: curated kinds and relations expressed in plain terms, governed by simple human rules.
* An **Assurance stack** beneath it - **Mapping**, **Logical**, **Constructive** - that carries the heavy arguments (concept alignment, relational semantics, generative traces) and **never leaks back** into the Working-Model narrative.

This pattern dovetails with the framework's unification stance (**small Working-Model text, rigorous foundations**) and with our constructional mereology commitments (**sum/set/slice** provide extensional identity), while keeping the Kernel minimal and meta-only.

