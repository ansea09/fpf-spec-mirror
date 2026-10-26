---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
section_id: "B.5.2.1:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__002_problem-frame.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "B.5.2.1 — Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
  - "B.5.2.1:1 — Problem Frame"
line_start: 49575
line_end: 49581
dependencies:
  - "A.17"
  - "A.18"
  - "B.4"
  - "B.5"
  - "B.5.2"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.19"
  - "G.5"
keywords:
---

### B.5.2.1:1 - **Problem Frame**
* **Conceptual binding:** **B.5.2 Abductive Loop** (this pattern specifies the *how* for Steps 2–3).
* **Characteristics and records:** use **Creativity‑CHR** under **C.17** for the Characteristics in §3, **C.18** for generation/archive/front records and **C.19 E/E-LOG** for EmitterPolicy.
* **Manager’s mental model (informative):** “We add measurable characteristics for *newness*, *spread*, and *fit*, then use a generator that explores widely and returns a **front over the declared Q components** together with retained exploration/archive evidence when the policy asks for it, not a single winner and not one bundled `{Q,N,D}` default.”
* **Further work:** generated hypotheses may contribute to **B.4 Canonical Evolution Loop** when adaptation is needed. **B.5 Canonical Reasoning Cycle** selects the reasoning contribution needed by the current question.
* **Decision-subject note.** Later choices are attributed to one declared `DecisionSubject` at explicit `DecisionSubjectGranularity`. The **Context** supplies the measurement spaces and admissible policies that frame the decision.

