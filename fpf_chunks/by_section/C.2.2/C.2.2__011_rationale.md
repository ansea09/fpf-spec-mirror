---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__011_rationale.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:10 — Rationale"
line_start: 52158
line_end: 52169
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
  - "non-aggregate synthesis"
  - "pathwise justification (PathId)"
  - "support dependencies"
  - "warrant"
  - "weakest-link limits"
---

### C.2.2:10 - Rationale

The triad separates expression, applicability and warrant so that improving one is not mistaken for improving the others.

* **G states applicability.** It states where the claim is asserted to apply. If G is implicit, teams argue about “what was meant” instead of updating scope.
* **F describes expression properties.** It identifies what the claim's terms, semantics and inferential relations make available for interpretation, scrutiny and reuse. If these properties are conflated with R, formalisation becomes a rhetorical substitute for support.
* **R carries warrant.** It describes support for this exact claim and use under a named meaning and scale. Its inputs must not erase the distinction between a necessary premise, complementary evidence, and a credible contrary result.

Each changed value has its own rule. Route a traversed relation's declared congruence loss into **R**; change the claim's expression or scope only through the applicable expression or scope operation. Re-establish warrant for the receiving use instead of carrying it forward without a basis.

No universal fold is conservative for every support model. Minimum can overstate a conjunctive probability and can also suppress useful complementary evidence. The small common rule is to establish input meanings and dependencies, calculate only what they warrant, and otherwise preserve a useful bounded synthesis.

