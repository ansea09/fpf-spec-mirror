---
chunk_kind: "child"
pattern_id: "B.5.MR"
pattern_title: "Compare Models by Refinement and Abstraction"
section_id: "B.5.MR:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MR/B.5.MR__012_sota-echoing.md"
commit_sha: "5e9f4d868afa1f9db90d4c7ff6840bd55f3b8d18"
heading_path:
  - "B.5.MR — Compare Models by Refinement and Abstraction"
  - "B.5.MR:11 — SoTA-Echoing"
line_start: 50915
line_end: 50920
dependencies:
  - "B.1"
  - "B.5.FM"
  - "B.5.TC"
  - "C.2.1"
  - "C.37.MM"
keywords:
---

### B.5.MR:11 - SoTA-Echoing

Specification theory compares models that satisfy stated sentences. It supports comparison across signatures when an interpretation specifies how a later model yields an earlier one. Under ordinary set inclusion, an empty class is included in every class. If the task is to show that a specification is infeasible, emptiness can settle it. A practitioner relying on a refined model to select a feasible design or action also needs a surviving completion. Section 4.2 therefore tests existence and preservation and asks which earlier possibility is lost when strictness matters. If the receiving inquiry changes what counts as the same answer, reconsider the interpretation and the comparison under it. This is a historical formal basis for the comparison. [Sannella and Tarlecki, *Specifications in an Arbitrary Institution*, §§2 and 8](https://homepages.inf.ed.ac.uk/dts/pub/inst-asl.pdf)

Probabilistic program development also uses refinement and abstraction as converse directions while retaining probability-sensitive guarantees. A comparison of outcome sets alone loses that information; section 4.1 therefore keeps the probability claims relevant to the inquiry. The formal construction is a historical anchor, not a claim that every Method is a probabilistic program. [Morgan, *The Generalised Substitution Language extended to probabilistic programs*, §2](https://cgi.cse.unsw.edu.au/~carrollm/probs/Papers/Morgan-98.pdf)

