---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U.Type Names and RoleDescription Labels"
section_id: "F.5:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__002_use-this-when.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "F.5 — Naming Discipline for U.Type Names and RoleDescription Labels"
  - "F.5:0 — Use This When"
line_start: 73164
line_end: 73200
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.Type"
keywords:
  - "U.Type naming"
  - "lexical rules"
  - "morphology"
  - "naming conventions"
  - "twin registers"
---

### F.5:0 - Use This When

**Plain name.** Meaning-first naming discipline.

Use this pattern when a project needs a durable name for either:

- a `U.Type` or other cross-context concept admitted through a Concept-Set row; or
- a label used by a role-description episteme for one work-facing `U.Role` in one `U.BoundedContext`.

Typical moments:

- a Concept-Set row has enough witnesses to admit a reusable FPF name, but the candidate names import one source tradition too strongly;
- a role-description episteme names a role such as `ReviewerRole`, `OperatorRole`, `InspectorRole`, or `TransformerRole`, and the label must stay faithful to the bounded context without smuggling capability, permission, method, work, evidence, or status;
- a role-like external phrase must be named for local use, but the project has not yet decided whether it is a work-facing `U.Role`, a status-use relation, an access or policy term, a relation slot, or only a local phrase;
- two similar names threaten to make a `U.Type`, a `U.Role`, a status value, a method, and a work occurrence look like one object.

**Primary EntityOfConcern.** The EntityOfConcern is the naming discipline for these two name families. It governs the relation between a recovered meaning and its Tech and Plain labels. It does not define the named `U.Type`, does not define the described `U.Role`, does not assign a holder to a role, does not assert status, does not provide evidence, and does not make a publication form authoritative.

**Primary working reader.** The first reader is an engineer-manager, analyst, pattern author, or terminology steward who already has a candidate meaning and must choose a name that remains usable by readers without creating a second ontology.

**First useful move.** Before choosing the label, recover the named value kind and its source of meaning: Concept-Set row for a `U.Type`; role-description episteme, described `U.Role`, bounded context, and local sense for a role label. Then choose Tech and Plain labels whose morphology matches that kind and whose scope does not exceed the recovered meaning.

**What goes wrong if missed.** Names become arguments. A role label starts implying permission or capability. A status phrase becomes a role. A `U.Type` name imports one context's private ontology. A pretty global word hides that the Concept-Set witnesses do not agree. Downstream patterns then repair "semantics" that were actually broken at naming time.

**What this buys.** Readers can use short names without guessing the ontology. `U.Type` names stay neutral across their witnesses. RoleDescription labels stay local to their bounded context and point to work-facing roles. Status, evidence, access, requirement, source, publication, assurance, and gate names remain governed by their direct patterns instead of becoming "roles" by naming accident.

**Not this pattern when.**

- If the current problem is ordinary phrase repair rather than a durable name, use `E.10`, `E.10.ARCH`, `A.6.P`, or the direct governing pattern.
- If the current issue is the broader local-first naming protocol, Name Cards, candidate fronts, lineage, or public naming governance, use `F.18`.
- If the current issue is a role-description episteme itself, use `F.4`.
- If the current issue is role assignment, holder, context, window, or performed-work attribution, use `A.2.1`.
- If the current issue is status classification, use `F.10` or the direct status-use pattern.
- If the current issue is evidence, source, standard, requirement, publication, assurance, gate, or decision use of an episteme, use the direct pattern for that relation.
- If "role" means a relation position, use `A.6.5` SlotSpec discipline.
- If cross-context sameness or translation is current, use `F.9`.

