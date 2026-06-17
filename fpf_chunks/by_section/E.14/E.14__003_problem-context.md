---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human‑Centric Working‑Model"
section_id: "E.14:2"
section_title: "Problem & Context"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__003_problem-context.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "E.14 — Human‑Centric Working‑Model"
  - "E.14:2 — Problem & Context"
line_start: 62867
line_end: 62884
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

### E.14:2 - Problem & Context

Teams need **one shared Working‑Model** to make decisions at speed. Historically this shared model either:

* **drifts into jargon**—different terms for one shared working-model value, slash‑labels, partial overlaps; or
* **calcifies into machinery**—too formal for day‑to‑day design and review.

Both failure modes create friction between two audiences:
(1) **working users** (engineers, programme managers, policy owners) who need a **small, stable Working-Model text**, and
(2) **assurance authors** (ontologists, methodologists, auditors) who need **proofs that the Working-Model text is sound**.

E.14 resolves the impasse by **separating concerns**:

* A **Working‑Model layer**: curated kinds and relations expressed in plain terms, governed by simple human rules.
* An **Assurance stack** beneath it - **Mapping**, **Logical**, **Constructive** - that carries the heavy arguments (concept alignment, relational semantics, generative traces) and **never leaks back** into the Working-Model narrative.

This pattern dovetails with the framework’s unification stance (**small Working‑Model text, rigorous foundations**) and with our constructional mereology commitments (**sum/set/slice** provide extensional identity), while keeping the Kernel minimal and meta‑only.

