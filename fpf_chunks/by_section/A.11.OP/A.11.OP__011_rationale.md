---
chunk_kind: "child"
pattern_id: "A.11.OP"
pattern_title: "Decision-Relevant Least Action and Operational Parsimony"
section_id: "A.11.OP:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.11.OP/A.11.OP__011_rationale.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "A.11.OP — Decision-Relevant Least Action and Operational Parsimony"
  - "A.11.OP:10 — Rationale"
line_start: 23746
line_end: 23755
dependencies:
  - "A.10"
  - "A.11"
  - "A.11.OP"
  - "A.15.1"
  - "A.15.7"
  - "A.19"
  - "A.3.1"
  - "A.3.2"
  - "B.3"
  - "C.11"
  - "C.19.2"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.13"
  - "E.23"
  - "E.5"
keywords:
---

### A.11.OP:10 - Rationale

Operational parsimony is about relevance, not abstract minimization. The fewest-step method can be wrong when one additional action realizes the chosen result, changes a later policy, or preserves a relied-on condition. The longest method can also be wrong when its extra actions have no substantive receiver. Comparing keeping and removing one proposed requirement makes that difference visible without inventing a global cost function.

The three branches cover distinct reasons for mandatory status. Decision-changing result preserves exploration and discrimination. Selected realization preserves deterministic work. Assurance or recoverability preservation protects a named relied-on condition. Each reason justifies only mandatory status for the declared use and horizon; its direct owner establishes every downstream claim.

The horizon must be substantive and bounded. A next-event horizon hides delayed information value; an indefinite horizon lets hypothetical future usefulness justify everything. The nearest named receiver is the smallest horizon that can carry the reason and the smallest reopen boundary when the use changes.

The rule coordinates existing decisions, transformations, results, evidence, assurance, and recovery uses. Keeping these objects under their direct patterns preserves FPF layering while giving practitioners one discoverable admission question.

