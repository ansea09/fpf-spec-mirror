---
chunk_kind: "child"
pattern_id: "A.14"
pattern_title: "Advanced Mereology: Components, Portions, Aspects & Phases"
section_id: "A.14:10"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.14/A.14__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.14 — Advanced Mereology: Components, Portions, Aspects & Phases"
  - "A.14:10 — Common Anti-Patterns and How to Avoid Them"
line_start: 23787
line_end: 23795
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.2"
  - "B.3.5"
  - "C.13"
keywords:
  - "ComponentOf"
  - "PhaseOf"
  - "PortionOf"
  - "composition"
  - "mereology"
  - "part-of"
---

### A.14:10 - Common Anti-Patterns and How to Avoid Them

* **Member as component.** A person, team, document, or object belongs to a collection and is then counted as if it were structurally integrated into the whole.
* **Role as part.** A system plays a role, and the role label is placed inside a part tree.
* **Method as part.** A method value, recipe, or algorithm is treated as a component instead of using method, method-description, work, or transformation owners.
* **Portion without measure.** Some amount of fuel, data, time, or text is named as a portion without a measure kind, unit, and additivity condition.
* **Phase as replacement.** A version or time slice is treated as a new component when the carrier identity continues, or as the same phase when the identity criteria fail.
* **Diagram or trace as relation.** A visual breakdown, graph, table, construction trace, or `validationMode` is used as proof that parthood obtains or that the whole has one fixed identity. Recover the direct relation occurrence and the candidate's identity or reidentification rule first; use the publication and trace only as inspectable accounts.

