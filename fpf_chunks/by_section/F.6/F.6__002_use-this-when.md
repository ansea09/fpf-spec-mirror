---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__002_use-this-when.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:0 — Use This When"
line_start: 81354
line_end: 81390
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "asserting status"
  - "conceptual moves"
  - "enactment"
  - "role assignment"
---

### F.6:0 - Use This When

**Plain name.** Role-assignment and work-attribution check.

Use this pattern when a project has a role description, role label, assignment notation, or work record and needs to decide whether it can make a work-facing `U.RoleAssignment` claim or attribute performed work through that assignment.

Typical moments:

- a method description names `ReviewerRole`, `OperatorRole`, `InspectorRole`, `TransformerRole`, or another required role, and the project must decide which holder bears that role in the bounded context;
- a work record says "Alice reviewed", "Robot-7 inspected", "the operations team approved", or "the CI service deployed", but the holder, role, bounded context, assignment window, or performed-by relation is not explicit;
- a source text uses `Holder#Role:Context@Window`, `RoleEnactment`, "assigned role", "played role", or "acted as" and the project must recover the typed assignment relation rather than preserve source notation as ontology;
- a status, evidence, requirement, source, standard, dashboard, model card, publication, or report is being described with role language, and the project must decide that this is not a work-facing role assignment;
- a cross-context role-like word appears, and the project must keep the local role assignment separate from any `F.9` bridge or `F.5` naming question.

**Primary EntityOfConcern.** The EntityOfConcern is the role-assignment and performed-work attribution check: a bounded check over a candidate `U.RoleAssignment` and, when current, a `U.Work` occurrence that may cite that assignment through `Work.performedBy` or `RoleEnactmentFact`. The check is not the role value, not the role description, not the work occurrence, not a status assertion, not evidence, and not a publication form.

**Primary working reader.** The first reader is an engineer-manager, analyst, method author, or FPF author who must keep a role label, role description, assignment relation, method requirement, work occurrence, status-use relation, and evidence-use relation from becoming one under-typed "enactment" claim.

**First useful move.** Recover the candidate holder, role value, bounded context, and assignment window or window disposition. Then decide whether the current claim is only assignment admission, performed-work attribution under an assignment, or a status, evidence, source, or publication claim governed outside F.6.

**What goes wrong if missed.** A role description becomes proof that a holder has a role. A work record names a person or label but not the role assignment that made the work attributable. A report, standard, requirement, or dashboard is made into a role holder because it constrained, evidenced, justified, displayed, or described work. Source `U.RoleEnactment` wording grows back into a second run-time ontology beside `U.Work` and `U.RoleAssignment`.

**What this buys.** The reader gets one small local check: who or what can bear the role, in which context and window, and whether a specific work occurrence may be attributed through that assignment. Status, evidence, source, publication, method, capability, and bridge claims remain with their direct patterns.

**Not this pattern when.**

- If the current claim is the role value itself, use `A.2`.
- If the current claim is the role-description episteme, use `F.4`.
- If the current claim is durable naming of a role or type label, use `F.5` or `F.18`.
- If the current claim is the `U.RoleAssignment` relation value itself and its SlotSpecs, use `A.2.1`.
- If the current claim is role state or enactable-state admission, use `A.2.5`.
- If the current claim is capability, use `A.2.2`.
- If the current claim is method, method description, work plan, performed work, or role-method-work alignment beyond the assignment check, use `A.15` and its subpatterns.
- If the current claim is status, evidence, source, standard, requirement, publication, assurance, gate, or decision use of an episteme, use the direct pattern for that relation, such as `F.10`, `A.10`, `B.3`, `C.28`, `E.17`, or `E.10.D2`.
- If the current claim is cross-context sameness, translation, or substitution, use `F.9`.
- If "role" means a relation position, use `A.6.5` SlotSpec discipline.

