---
chunk_kind: "child"
pattern_id: "F.3"
pattern_title: "Intra‑Context Sense Clustering"
section_id: "F.3:10"
section_title: "Anti‑patterns & remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/F.3/F.3__011_anti-patterns-remedies.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "F.3 — Intra‑Context Sense Clustering"
  - "F.3:10 — Anti‑patterns & remedies"
line_start: 84509
line_end: 84523
dependencies:
  - "A.11"
  - "A.7"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "Local-Sense"
  - "SenseCell"
  - "counter-examples"
  - "disambiguation"
  - "sense clustering"
---

### F.3:10 - Anti‑patterns & remedies

| #       | Anti‑pattern               | Symptom in thought                                                            | Why it harms                                            | Remedy (conceptual move)                                                                                          |
| ------- | -------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **A1**  | **String = Sense**         | Treating surface identity (*service*, *SLO*) as sameness of meaning.          | Collapses distinct uses; hides selectional differences. | Compare **selectional frames** and entailments inside the Context; merge only if conclusions never diverge.          |
| **A2**  | **Cross‑context creep**       | Folding BPMN *process* with PROV *activity* while clustering **inside** BPMN. | Imports foreign usage; violates locality.               | Constrain attention to **one context**; postpone Cross‑context talk to F.9.                                             |
| **A3**  | **Over‑granulation**       | Splitting minor orthographic variants (*service‑level‑objective* vs *SLO*).   | Adds friction; no conceptual gain.                      | Consolidate **canon‑blessed aliases** into one Local‑Sense.                                                       |
| **A4**  | **Under‑granulation**      | One sense for incompatible roles (*event* as node‑type vs occurrence).        | Causes contradictory inferences later.                  | Split on **role/entailment** conflict; add a **counter‑example** to sharpen the cut.                              |
| **A5**  | **Imported definitions**   | Borrowing dictionary glosses not used in the canon.                           | Drifts from the Context’s idiom; confuses labels.          | Ground every sense line in **statements the canon actually makes**.                                               |
| **A6**  | **Label drift**            | Tech label in canon idiom; Plain label broadens scope.                        | Teaches the wrong thing; leaks meaning.                 | Keep **Tech** idiomatic; make **Plain** helpful yet strictly **within** the same usage.                           |
| **A7**  | **Behaviour/math leakage** | Sense lines include runtime metrics, deontic rules, type axioms.              | Mixes EntityOfConcern, Description episteme, and specification-use positions; duplicates Part C work.                   | Sense lines are **usage‑only**; no equations, no policies.                                                        |
| **A8**  | **Edition blend**          | Mixing 2011 and 2020 usage under one Local‑Sense.                             | Hidden shifts; brittle bridges later.                   | If usage changed with edition, treat as **different Contexts** (F.1) or distinct Local‑Senses with **edition note**. |
| **A9**  | **Collocate worship**      | Declaring sameness solely from similar nearby words.                          | Correlates ≠ causes; misses entailments.                | Use collocates as **cues**, then decide by **entailment/role** checks.                                            |
| **A10** | **Temporal fudge**         | Treating a design‑time sense as if it were run‑time (or vice versa).          | Category errors at enactment.                           | Respect the Context’s **time stance**; keep senses aligned to *design* or *run* as declared in F.1.                  |

