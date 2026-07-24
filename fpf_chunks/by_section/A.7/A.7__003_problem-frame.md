---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__003_problem-frame.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:2 — Problem frame"
line_start: 21538
line_end: 21548
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.21"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "E.10"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
keywords:
  - "EntityOfConcern ≠ Description episteme"
  - "Role ≠ Work"
  - "category error"
  - "ontology"
---

### A.7:2 - Problem frame

* **Holons (A.1) and systems.** All holons are part-whole units; **systems or acting holons** enact behaviour through work-facing role assignments in a bounded context.
* **Transformation (A.3.4) and role assignment (A.2/A.2.1).** Every claimed change names the transformation or work occurrence, the affected entity, and any current `U.RoleAssignment` for the acting system or holon; there is no “self-magic”.
* **Method/work backbone (A.3.1, A.3.2, A.15).** We separate **MethodDescription** (description), **Method** (abstract way-of-doing), **Capability** (a system's ability or envelope to enact a Method under conditions), **WorkPlan** (intent window), and **Work** (run-time occurrence), with the acting side expressed through `U.RoleAssignment` when a work-facing role is current.
* **Evidence (A.10).** Knowledge claims cite evidence-provenance and carrier/source-currentness relations; epistemes never “act”; systems inspect, revise, publish, store, or rely on the carriers, publication forms, and project records that make an episteme available.

Practitioner check: if a sentence could be read as “the document decided” or “the process executed itself”, it violates A.7.

Boundary for use from other patterns: A.7 restores the `EntityOfConcern`, the admissible describing relation, and the publication boundary, then returns the work to the subject pattern. Do not let A.7 turn an architecture, structure, work, method, evidence, characterization, or decision question into a general discussion of descriptions. If the `EntityOfConcern` is itself a Description episteme or view, keep the pattern centered on that episteme as the item under concern; description-of-description or publication-force issues open only when they are the exact claim being made.

