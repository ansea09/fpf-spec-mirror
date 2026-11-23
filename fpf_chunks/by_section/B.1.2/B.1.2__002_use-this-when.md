---
chunk_kind: "child"
pattern_id: "B.1.2"
pattern_title: "Coordinate Decisions About System Aggregation and Delimitation"
section_id: "B.1.2:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.2/B.1.2__002_use-this-when.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "B.1.2 — Coordinate Decisions About System Aggregation and Delimitation"
  - "B.1.2:0 — Use This When"
line_start: 43159
line_end: 43186
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.19"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.1"
  - "B.2"
  - "B.3"
  - "C.11"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.AD.BA"
  - "C.32.PAD"
  - "E.17"
keywords:
---

### B.1.2:0 - Use This When

Use this pattern when an engineering decision about a system whole depends on several independently grounded claims: its part-whole relations, delimitation, boundary crossings, functions and their bearers, or whole-level characteristics. The entity may already be recognized under `U.System` or still be under evaluation through A.1.

Typical moments:

- a machine, building asset, or organization is proposed as a whole assembled from identified constituents;
- a system-level characteristic is to be rolled up from constituent characteristics;
- a supply, signal, measurement, control, source, publication, evidence, or transformation relation is being mistaken for a part relation;
- a functional element must be distinguished from and allocated to physical, organizational, software, or operational bearers;
- a named decision needs one recoverable view of the system boundary, crossings, and compatibility choices without turning that view into the system.

**First useful move.** Start from the receiving decision and the system or proposed assembly it concerns. Follow its use outward when the enclosing arrangement can change that decision, and inward when two admissible internal arrangements give different answers. Identify the whole's A.1 recognition status when systemhood matters to the claim. For each claim, use the applicable subject pattern to recover its result or identify the missing defining rule or information. Then ask whether considering the results' joint organization changes the decision.

**What goes wrong if missed.** A reader may infer components and containment from placement in a diagram, treat a functional element as a physical part, or mistake an external transformation or measurement relation for parthood. A coordination record then appears to establish facts that each need grounds.

**What this buys.** The practitioner can combine the results needed for one engineering aggregation decision while retaining each claim's grounds and use conditions.

**Not this pattern when.**

- If the only open question is whether an entity qualifies as a `U.System`, use `A.1`.
- If one part-whole relation is the question, use `A.14` and its specialization.
- If constructive assembly grounding is the question, use `C.13`.
- If the question is a functional claim, use its behavior or realization predicate; use `A.6.F` when the function wording is unresolved and `C.30.ASV` when architecture-view conformance is needed.
- If bearer allocation or parthood is the question, use the allocation or part-relation pattern; use `A.6.M` only when module or interface wording needs repair.
- If a mathematical aggregation lens is the question, use `C.29`.
- For the system-of-interest role in an extended enterprise or the system-in-hand for local investigation or change, use `A.1.STM` and `A.1.SCR`. For a technical system-role assignment, Work, transformation, service or access, evidence, description, or publication, use its subject pattern.

