---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__004_problem-frame.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:2 — Problem frame"
line_start: 21706
line_end: 21716
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
  - "MethodDescription ≠ Method ≠ Capability ≠ Work"
  - "category error"
  - "system-role kind and assignment ≠ Work"
---

### A.7:2 - Problem frame

* **Holons (A.1) and systems.** All holons are part-whole units; **systems or acting holons** enact behaviour. When assignment matters, name the assignment occurrence and its declared species in the bounded context.
* **Transformation (A.3.4) and system-role assignment (A.2 and A.2.1).** Every claimed change names the transformation or Work occurrence, the affected entity, and any assignment of the acting System or holon, including the occurrence and its declared `U.SystemRoleAssignment` species; there is no “self-magic”.
* **Method and Work backbone (A.3.1, A.3.2, A.15).** We separate **MethodDescription** (the same already identified episteme only after A.3.2 membership obtains), **Method** (abstract way-of-doing), **Capability** (a System's ability or envelope to enact a Method under conditions), **WorkPlan** (intent window), and **Work** (run-time occurrence). An assignment names both its occurrence and declared species without making either the actor.
* **Evidence (A.10).** Knowledge claims cite evidence-provenance and carrier/source-currentness relations; epistemes never “act”; systems inspect, revise, publish, store, or rely on the carriers, publication forms, and project records that make an episteme available.

Practitioner check: if a sentence could be read as “the document decided” or “the process executed itself”, it violates A.7.

Boundary for use from other patterns: A.7 restores the `EntityOfConcern`, the admissible describing relation, and the publication boundary, then requires the subject pattern for the work. Do not let A.7 turn an architecture, structure, work, method, evidence, characterization, or decision question into a general discussion of descriptions. If the `EntityOfConcern` is itself a Description episteme or view, keep the pattern centered on that episteme as the item under concern; description-of-description or publication-force issues open only when they are the exact claim being made.

