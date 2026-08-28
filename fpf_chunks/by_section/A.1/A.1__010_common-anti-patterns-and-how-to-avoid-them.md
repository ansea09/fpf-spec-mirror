---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
section_id: "A.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "A.1 — Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
  - "A.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 1770
line_end: 1781
dependencies:
  - "A.1.1"
  - "A.1.STM"
  - "A.10"
  - "A.14"
  - "A.15.1"
  - "A.22"
  - "A.3.4"
  - "A.6.1"
  - "B.2"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.20"
  - "C.30"
  - "E.10.ARCH"
  - "E.24.UK"
  - "G.11"
keywords:
---

### A.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| System as universal root | A theory, document, model, source, or dashboard receives physical system properties. | Re-type as `U.Episteme`, publication, source-use object, or another direct object before using system claims. |
| Document edited itself | A model, theory, or document is said to perform a revision. | Name the `U.System` and the revision Work; add a local system-role kind or `U.SystemRoleAssignment` only when that separate fact is material. Changed claim content identifies another `U.Episteme`; test any edition relation separately, and distinguish publication or carrier changes under their own patterns. |
| Collection as actor | A list, batch, pool, fleet, or community is said to decide or perform Work. | Recover who or what belongs to the collection under its own rule, a possible holon, a whole-level characteristic, an acting collective System, or B.2 whole reidentification. |
| Interaction as one umbrella | Signal, source use, publication use, transformation, measurement, and control are all called interaction. | Recover the exact direct relation; use F.9 for a current crossing claim and `A.3.4` when bounded change is current. |
| Omnibus participation relation | References to system-role-kind classification or assignment, capability, method, work, transformation, evidence, and time are packed into one additional relation-shaped record. | Keep the direct relation occurrences separate; select their organization as `U.Structure` only when that organization changes the receiving use. |
| Boundary by drawing | A box, folder, section, dashboard view, or diagram is treated as the holon boundary. | Recover the exact delimitation relation, criterion, or selected structure from its direct pattern; keep the drawing as a description or view. |
| Architecture without holon | A selected structure is discussed without the holon whose structure is selected. | Use A.1 to name the holon, then `A.22` and `C.30` for selected structure and architecture. |

