---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and RoleDescription Labels"
section_id: "F.5:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__002_use-this-when.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and RoleDescription Labels"
  - "F.5:0 — Use This When"
line_start: 78732
line_end: 78769
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
  - "E.24.UK"
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
keywords:
  - "U-kind naming"
  - "lexical rules"
  - "morphology"
  - "naming conventions"
  - "role-description labels"
  - "twin registers"
---

### F.5:0 - Use This When

**Plain name.** Meaning-first naming discipline.

Use this pattern when a project needs a durable name for either:

- a U-kind or other cross-context concept admitted through `E.24.UK`, a Concept-Set row, or a direct governing pattern; or
- a label used by a role-description episteme for one work-facing `U.Role` in one `U.BoundedContext`.

Typical moments:

- a Concept-Set row has enough witnesses to admit a reusable FPF name, but the candidate names import one source tradition too strongly;
- a role-description episteme names a role such as `ReviewerRole`, `OperatorRole`, `InspectorRole`, or `TransformerRole`, and the label must stay faithful to the bounded context without smuggling capability, permission, method, work, evidence, or status;
- a role-like external phrase must be named for local use, but the project has not yet decided whether it is a work-facing `U.Role`, a status-use relation, an access or policy term, a relation slot, or only a local phrase;
- two similar names threaten to make a U-kind, a `U.Role`, a status value, a method, and a work occurrence look like one object.

**Primary EntityOfConcern.** The EntityOfConcern is the naming discipline for these two name families. It governs the relation between a recovered meaning and its Tech and Plain labels. It does not define the named U-kind, does not define the described `U.Role`, does not assign a holder to a role, does not assert status, does not provide evidence, and does not make a publication form authoritative.

**Primary working reader.** The first reader is an engineer-manager, analyst, pattern author, or terminology steward who already has a candidate meaning and must choose a name that remains usable by readers without creating a second ontology.

**First useful move.** Before choosing the label, recover the named value kind and its source of meaning: `E.24.UK`, Concept-Set row, or direct governing pattern for a U-kind; role-description episteme, described `U.Role`, bounded context, and local sense for a role label. Then choose Tech and Plain labels whose morphology matches that kind and whose scope does not exceed the recovered meaning.

**What goes wrong if missed.** Names become arguments. A role label starts implying permission or capability. A status phrase becomes a role. A U-kind name imports one context's private ontology. A pretty global word hides that the Concept-Set witnesses do not agree. Downstream patterns then repair "semantics" that were actually broken at naming time.

**What this buys.** Readers can use short names without guessing the ontology. U-kind names stay neutral across their witnesses. RoleDescription labels stay local to their bounded context and point to work-facing roles. Status, evidence, access, requirement, source, publication, assurance, and gate names remain governed by their direct patterns instead of becoming "roles" by naming accident.

**Not this pattern when.**

- If the current problem is ordinary phrase repair rather than a durable name, use `E.10`, `E.10.ARCH`, `A.6.P`, or the direct governing pattern.
- If the current issue is whether a `U.*` spelling or structural name should survive as a durable U-kind, use `E.24.UK` before F.5.
- If the current issue is the broader local-first naming protocol, Name Cards, candidate fronts, lineage, or public naming governance, use `F.18`.
- If the current issue is a role-description episteme itself, use `F.4`.
- If the current issue is role assignment, holder, context, window, or performed-work attribution, use `A.2.1`.
- If the current issue is status classification, use `F.10` or the direct status-use pattern.
- If the current issue is evidence, source, standard, requirement, publication, assurance, gate, or decision use of an episteme, use the direct pattern for that relation.
- If "role" means a relation position, use `A.6.5` SlotSpec discipline.
- If cross-context sameness or translation is current, use `F.9`.

