---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description - Description Episteme for U.Role"
section_id: "F.4:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__002_use-this-when.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "F.4 — Role Description - Description Episteme for U.Role"
  - "F.4:0 — Use This When"
line_start: 90477
line_end: 90512
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.3"
  - "F.6"
  - "F.8"
  - "F.9"
keywords:
  - "Role Characterisation Space (RCS)"
  - "RoleStateGraph (RSG)"
  - "invariants"
  - "role template"
  - "status template"
---

### F.4:0 - Use This When

**Plain name.** Role-description episteme.

Use this pattern when a project needs a short, reusable description that makes one work-facing `U.Role` recognizable, teachable, and checkable under one named role-taxonomy episteme and effective `U.ReferenceScheme`.

Typical moments:

- a project has a role name such as `ReviewerRole`, `OperatorRole`, `InspectorRole`, `TransformerRole`, `ShipyardCoordinatorRole`, or `ModelCardReviewerRole`, but the governing role-taxonomy episteme, effective reference scheme, admitted holder kind, role invariants, capability conditions, or work-facing boundary are unclear;
- a method description names required roles, but readers cannot tell what role value is required before a `U.RoleAssignment` can be checked;
- a role name is starting to carry method, capability, work, permission, evidence, publication, or status claims that belong to neighboring patterns;
- a former source phrase says that a report, standard, dataset, theorem, dashboard, publication, or requirement has a "role" and the text must decide whether that phrase is a real work-facing role description or a direct episteme-use relation.

**Primary EntityOfConcern.** The exact C.2.1 EntityOfConcern of the role-description episteme is the described `U.Role` value. The governed object is one `U.Episteme` constituted under `C.2.1` by its exact ClaimGraph, that role value, and the effective `U.ReferenceScheme`; its claims name the role-taxonomy episteme that supplies the vocabulary. The role-description episteme is not the role value itself, holder, role assignment, capability, method description, performed work, status-use relation, or publication form.

**Primary working reader.** The first reader is an engineer-manager, analyst, method author, or pattern author who must let people recognize a role while keeping role value, holder, assignment, capability, method, work, evidence use, status use, and publication use distinct.

**First useful move.** Name the role value, its role-taxonomy episteme, the effective reference scheme, the admitted holder kind, and the smallest role invariants needed by the next assignment, method, work, naming, or bridge claim.

**What goes wrong if missed.** A role-description card becomes a hidden method, access policy, permission badge, evidence relation, status assertion, staffing plan, or work log. Then FPF grows one role ontology for acting holons and a second role-like ontology for epistemes, publications, statuses, and relation positions.

**What this buys.** A project can publish a compact, human-readable role description while keeping operational claims in their direct patterns. The role remains recognizable; the assignment remains checkable; capability, method, work, evidence, status, and publication claims stay inspectable instead of being smuggled into the role name.

**Not this pattern when.**

- If the current claim is the role value itself or role taxonomy, use `A.2`.
- If the current claim is which admitted system holds which role and during which uninterrupted assignment occurrence, use `A.2.1`.
- If the current claim is role state or enactable-state admission, use `A.2.5`.
- If the current claim is role-requirement substitution, role incompatibility, role-factor qualification, or bundle expression, use `A.2.7`.
- If the current claim is capability, use `A.2.2`.
- If the current claim is method, method description, work plan, or performed work, use `A.15` and its neighbors.
- If the current claim is evidence use, status use, source use, standard use, requirement use, publication use, assurance use, gate use, or decision use of an episteme, use the direct pattern for that relation. Do not call that episteme a role holder.
- If the current issue is only a durable name, use `F.18`.
- If the current issue is correspondence between role meanings under different taxonomies or reference schemes, use `F.9`.
- If "role" means a relation position, use `A.6.5` SlotSpec discipline.

