---
chunk_kind: "child"
pattern_id: "C.17"
pattern_title: "Characterising Generative Novelty & Value (Creativity‑CHR)"
section_id: "C.17:4"
section_title: "Vocabulary (CHR terms & D‑stubs)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.17/C.17__005_vocabulary-chr-terms-d-stubs.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "C.17 — Characterising Generative Novelty & Value (Creativity‑CHR)"
  - "C.17:4 — Vocabulary (CHR terms & D‑stubs)"
line_start: 45916
line_end: 45936
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.6"
  - "B.1"
  - "B.3"
  - "B.4"
  - "B.5.2.1"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.9"
  - "D.1-D.5"
  - "E.5"
  - "F.18"
  - "F.5"
  - "F.6"
keywords:
  - "ConstraintFit"
  - "Creativity-CHR"
  - "Diversity_P"
  - "MM-CHR measurement templates"
  - "Novelty@context"
  - "Originality"
  - "ReferenceBase"
  - "ResourceEfficiency"
  - "Surprise"
  - "Use-Value and ValueGain"
  - "evidence"
  - "portfolio composition"
---

### C.17:4 - Vocabulary (CHR terms & D‑stubs)

> Names are **context‑local**; below are kernel terms. Roles like “Designer/Reviewer” are contextual (A.2). **Documents don’t act** (A.7/A.12); they are **evaluated**.

1. **`U.ReferenceBase`** *(D).* A curated, versioned **set of artifacts** (epistemes) and/or behaviours that define “what exists already” **in this Context and time window**.
   **Conformance (RB‑1):** must declare **inclusion criteria**, **time span (`TimeWindow`)**, and **coverage notes**.

2. **`U.SimilarityKernel`** *(D).* A declared **metric family** with invariances (e.g., text: cosine over embeddings, image: LPIPS, code: AST graph edit).
   **Conformance (SK‑1):** must cite **MethodDescription** and **test corpus**; state **limits**.

3. **`U.GenerativePrior`** *(D).* A model that yields **likelihood** of artifacts given the Context’s history (n‑gram/LM, design grammar, trend model).
   **Conformance (GP‑1):** must publish **training slice**, **fit method**, **perplexity/fit metrics**, and **refresh policy**.

4. **`U.CreativeOutcome`** *(D).* Any **`U.Episteme`** put forward for creative evaluation (e.g., new design, algorithm, spec, policy draft).
   **Note.** If the outcome is a **system change** without a single carrier, attach the evaluation to a **bundle** (set) of carriers referenced from Work.

5. **`U.CreativeEvaluation`** *(D).* A **`U.Evaluation`** that outputs a **`U.CreativityProfile`** and anchors to **ReferenceBase**, **Kernel/Prior**, **objective(s)**, **acceptance tests**, and **Work evidence**.

6. **`U.CreativityProfile`** *(D).* The **coordinate tuple** in `U.CreativitySpace` with provenance to the above inputs and **USM scopes**.
   **Conformance (CP‑1):** profile **must** include **scales/units**, **scopes**, **confidence bands** (B.3), and the **edition** of space definitions.

