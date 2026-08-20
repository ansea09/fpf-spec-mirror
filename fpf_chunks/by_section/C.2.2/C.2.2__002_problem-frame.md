---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__002_problem-frame.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:1 — Problem frame"
line_start: 42284
line_end: 42302
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.2.6"
  - "A.21"
  - "A.6.3.RT"
  - "B.1.3"
  - "B.3"
  - "B.3.3"
  - "B.3.4"
  - "C.16"
  - "C.2"
  - "C.2.3"
  - "C.21"
  - "C.29"
  - "C.3"
  - "C.3.3"
  - "C.3.A"
  - "E.14"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.2"
  - "G.6"
  - "G.7"
keywords:
  - "ClaimScope (G)"
  - "Congruence Level (CL / CL^k / CL^plane)"
  - "F–G–R"
  - "Reliability (R)"
  - "TA/VA/LA lanes"
  - "direct relation"
  - "evidence-bound"
  - "no implicit averaging"
  - "pathwise justification (PathId)"
  - "warrant"
  - "weakest-link"
---

### C.2.2:1 - Problem frame

KD‑CAL asks a simple operational question: *“Where can I safely use this claim?”*
FPF answers with a minimal “epistemic location” built from three coordinates. Any relations traversed by a justification path are named separately:

* **F** (Formality) describes *how the claim is expressed* and how strongly it supports verification workflows (C.2.3).
* **G** (Claim scope) describes *where the claim is asserted to apply* as a set-like object (A.2.6).
* **R** (Reliability) describes *how strongly the claim is warranted* by linked evidence under that scope.
* **CL / CL^k / CL^plane** (Congruence Levels) describe fit or loss for the relation families that define them—for example, a semantic relation, kind relation, or reference-plane relation (B.3, C.3, F.9).
  A CL value belongs to the declared relation or traversal used by the path, not to the claim as a fourth coordinate. Shared wording about a "context" creates no relation and no loss value.
In practice, the triad is frequently used before it is made explicit:

* Authors implicitly “average” disparate evidence and report a single confidence.
* Teams treat higher formality (F) as if it automatically implies higher warrant (R).
* Scope growth is smuggled in through phrasing instead of explicit scope operators (A.2.6).
* A claim or its evidence is reused after a change of scope, kind, plane, notation, source-local meaning, model-use basis, or evidence basis without naming the actual relation and routing its declared loss into R.

This pattern makes **R** explicit in KD‑CAL and fixes the **triad discipline** required by Kind‑CAL (C.3) and the Trust & Assurance calculus (B.3).

