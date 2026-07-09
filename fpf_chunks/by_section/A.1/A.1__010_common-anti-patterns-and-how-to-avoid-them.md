---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
section_id: "A.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.1 — Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
  - "A.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 1656
line_end: 1666
dependencies:
  - "A.1.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.22"
  - "A.3.4"
  - "A.6.5"
  - "A.7"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.20"
  - "C.30"
  - "E.10.ARCH"
  - "E.24"
  - "E.24.UK"
keywords:
---

### A.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| System as universal root | A theory, document, model, source, or dashboard receives physical system properties. | Re-type as `U.Episteme`, publication, source-use object, or another direct object before using system claims. |
| Document edited itself | A model, theory, or document is said to perform a revision. | Name the `U.System` in role that performed the work and the `U.Episteme` or publication that changed. |
| Collection as actor | A list, batch, pool, fleet, or community is said to decide or perform work. | Recover membership, collection-as-whole, whole-level characteristic, acting collective system, or B.2 whole reidentification. |
| Interaction as one umbrella | Signal, source use, publication use, transformation, measurement, and control are all called interaction. | Recover the direct relation. Use `HolonBoundaryCrossingRelation@Context` only for the boundary-crossing relation and `A.3.4` when bounded change is current. |
| Boundary by drawing | A box, folder, section, dashboard view, or diagram is treated as the holon boundary. | Name the bounded context, identity or recognition rule, and `HolonDelimitationRelation@Context`. |
| Architecture without holon | A selected structure is discussed without the holon whose structure is selected. | Use A.1 to name the holon, then `A.22` and `C.30` for selected structure and architecture. |

