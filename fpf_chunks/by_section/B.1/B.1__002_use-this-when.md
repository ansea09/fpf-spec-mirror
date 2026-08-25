---
chunk_kind: "child"
pattern_id: "B.1"
pattern_title: "Holon Aggregation and Part-Whole Construction"
section_id: "B.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1/B.1__002_use-this-when.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "B.1 — Holon Aggregation and Part-Whole Construction"
  - "B.1:0 — Use This When"
line_start: 34505
line_end: 34531
dependencies:
  - "A.1"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.7"
  - "A.22"
  - "B.2"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.29"
  - "C.30"
  - "E.10.ROLE"
keywords:
---

### B.1:0 - Use This When

Use this pattern when a project needs to say how several admitted objects are considered as a whole, or when a whole-level claim depends on parts, collection belonging under the collection's own rule, component structure, constructional grounding, or a selected aggregation rule.

Typical moments:

- a product, plant, dataset, paper, model family, organization, fleet, batch, or research program is discussed as a whole;
- a dashboard rolls part measurements into a whole-level characteristic;
- a team says that a method, role, graph, or algebra "decomposes" something and may be smuggling part-whole claims;
- a collection needs whole-level characteristics without becoming an acting collective system;
- an aggregation claim is being used for architecture, assurance, evidence, or MHT reasoning.

**First useful move.** Recover the claim kind before choosing notation: part-whole construction, collection belonging under the collection's own rule, collection-as-whole grounding, a relation among local system-role kinds, a direct participation or assignment relation, method relation structure, work occurrence holarchy, selected architecture structure, or mathematical description. If claim-bearing source wording still says only “role,” use `E.10.ROLE` before choosing one of these branches.

**What goes wrong if missed.** Γ, graph, algebra, decomposition, factor, component, step, phase, and collection wording become one universal composition language. Roles and methods become parts; work occurrence evidence is inferred from method structure; a graph is mistaken for the structure; a collection becomes an acting whole by label.

**What this buys.** B.1 gives one doorway into part-whole construction while keeping its neighbors clean: A.14 is the pattern for relation vocabulary, C.13 is the pattern for constructional grounding, B.3.5 is the pattern for Working-Model assurance grounding, A.15.1 is the pattern for work-occurrence holarchy, and C.29 is the pattern for mathematical-lens use.

**Not this pattern when.**

- If the question is the local relation word, use `A.14`.
- If the question is constructive part-whole grounding, use `C.13`.
- If the question is assurance grounding for a working model, use `B.3.5`.
- If the question is an exact relation among local system-role kinds, use `A.2.7`; if it is classification, assignment, or a direct participation relation, state that fact through its own pattern and predicate. Send unresolved claim-bearing “role” wording through `E.10.ROLE`. Use the Method patterns for method relation structure and `C.29` when a mathematical lens is relied on for the current claim.
- If the question is performed-work occurrence parts, use `A.15.1`.
- If the question is whole reidentification or emergence-family wording, use `B.2` or `B.2.P`.

