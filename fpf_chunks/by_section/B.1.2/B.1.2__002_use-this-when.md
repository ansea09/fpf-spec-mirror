---
chunk_kind: "child"
pattern_id: "B.1.2"
pattern_title: "System Aggregation and Holon Delimitation"
section_id: "B.1.2:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.2/B.1.2__002_use-this-when.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "B.1.2 — System Aggregation and Holon Delimitation"
  - "B.1.2:0 — Use This When"
line_start: 36740
line_end: 36767
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

Use this pattern when one exact entity recognized under the already admitted `U.System` kind, or one exact entity still being evaluated under A.1 for that kind, is being considered as a whole and an engineering decision depends on coordinating its independently governed part-whole, delimitation, crossing, function/bearer, and whole-characteristic claims.

Typical moments:

- a machine, plant, robot, vehicle, building asset, service organization, or operating unit is proposed as a whole assembled from exact constituents;
- a system-level characteristic is to be rolled up from constituent characteristics;
- a supply, signal, measurement, control, source, publication, evidence, or transformation relation is being mistaken for a part relation;
- a functional element must be distinguished from and allocated to physical, organizational, software, or operational bearers;
- a named decision needs one recoverable view of the system boundary, exact crossings, and compatibility choices without turning that view into the system.

**First useful move.** Name the exact whole and its A.1 recognition status, the decision being made, and each load-bearing claim. For every claim, select its subject pattern and either recover the exact result or state the exact missing governor or information. Only then ask whether their joint organization itself changes the named decision.

**What goes wrong if missed.** System aggregation becomes a drawing exercise. Ports, suppliers, documents, digital twins, dashboards, source records, and measuring instruments become components by placement. Functional elements become physical parts by label. External change or measurement is read as containment. One convenient record then appears to establish all those unrelated facts.

**What this buys.** B.1.2 coordinates one engineering aggregation decision while leaving system recognition, exact parthood, assembly, delimitation, crossing, function, bearer, characteristic, evidence, description, representation, and decision claims with their subject patterns.

**Not this pattern when.**

- If the exact entity has not yet been evaluated under the already admitted `U.System` kind, use `A.1`; do not promote the proposal into a durable kind-like label.
- If one exact part-whole relation is the question, use `A.14` and its direct specialization.
- If constructive assembly grounding is the question, use `C.13`.
- If functional behavior or a functional element is the question, use `A.6.F` and the exact architecture structural-view pattern.
- If module or bearer allocation is the question, use `A.6.M` and the exact architecture or part-relation pattern.
- If a mathematical aggregation lens is the question, use `C.29`.
- If the question is project system-of-interest designation, system-role assignment, Work, transformation, service or access, evidence, description, or publication, use that subject pattern; B.1.2 neither identifies nor defines those relations.

