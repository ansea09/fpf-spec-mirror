---
chunk_kind: "child"
pattern_id: "B.1.2"
pattern_title: "System Aggregation and Holon Delimitation"
section_id: "B.1.2:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.2/B.1.2__002_use-this-when.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "B.1.2 — System Aggregation and Holon Delimitation"
  - "B.1.2:0 — Use This When"
line_start: 35478
line_end: 35504
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15.1"
  - "A.19"
  - "A.22"
  - "A.3.4"
  - "A.6.5"
  - "A.6.F"
  - "A.6.M"
  - "B.1"
  - "C.13"
  - "C.16"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.AD.BA"
keywords:
---

### B.1.2:0 - Use This When

Use this pattern when a physical, operational, organizational, cyber-physical, or socio-technical system is treated as a whole made from parts, and the aggregation claim depends on how the system is delimited from its environment.

Typical moments:

- a machine, plant, robot, vehicle, building asset, service organization, or operating unit is aggregated from components or subholons;
- a system-level characteristic is rolled up from component characteristics;
- an external signal, supply, measurement, control, source, or publication relation is being mistaken for a part;
- a functional element must be allocated to candidate physical or organizational bearers;
- a boundary-interface-compatibility check is needed for a system aggregate.

**First useful move.** Name the candidate system whole, the candidate part relations, and the holon delimitation relation. Then decide which crossing relations remain external, which become internal after aggregation, and which are represented in a view or publication.

**What goes wrong if missed.** System aggregation becomes a drawing exercise. Ports, suppliers, documents, digital twins, dashboards, source records, and measuring instruments become components by placement. Functional parts become physical parts by label. External change or measurement is read as containment.

**What this buys.** B.1.2 makes system aggregation usable for engineering while keeping part-whole, holon delimitation, boundary crossing, functional structure, module allocation, and mathematical expression distinct.

**Not this pattern when.**

- If the object is not an admitted `U.System` or candidate system, use `A.1` first.
- If the question is generic part-whole vocabulary, use `A.14`.
- If the question is constructive grounding, use `C.13`.
- If the question is functional behavior or functional element, use `A.6.F` and architecture structural-view owners.
- If the question is module or bearer allocation, use `A.6.M` and architecture owners.
- If the question is a mathematical aggregation lens, use `C.29`.

