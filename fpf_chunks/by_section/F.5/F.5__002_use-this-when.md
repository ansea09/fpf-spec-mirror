---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and RoleDescription Labels"
section_id: "F.5:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__002_use-this-when.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and RoleDescription Labels"
  - "F.5:0 — Use This When"
line_start: 91330
line_end: 91369
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
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
  - "G.6"
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

- a U-kind or other cross-context concept already admitted through `E.24.UK` or its direct governing pattern; a Concept-Set row may cite comparison evidence but does not admit the value; or
- a label used by a role-description episteme for one work-facing `U.Role` interpreted under one named role-taxonomy episteme and effective `U.ReferenceScheme`.

Typical moments:

- a Concept-Set comparison has enough witnesses for a naming question and an `E.24.UK` or direct-pattern decision has already admitted the reusable value, but the candidate names import one source tradition too strongly;
- a role-description episteme names a role such as `ReviewerRole`, `OperatorRole`, `InspectorRole`, or `TransformerRole`, and the label must stay faithful to the exact role-taxonomy episteme and effective reference scheme without smuggling capability, permission, method, work, evidence, or status;
- a role-like external phrase must be named for local use, but the project has not yet decided whether it is a work-facing `U.Role`, a status-use relation, an access or policy term, a relation slot, or only a local phrase;
- two similar names threaten to make a U-kind, a `U.Role`, a status value, a method, and a work occurrence look like one object.

**Primary EntityOfConcern.** The EntityOfConcern is the naming discipline for these two name families. It governs the relation between a recovered meaning and its Tech and Plain labels. It does not define the named U-kind, does not define the described `U.Role`, does not assign a holder to a role, does not assert status, does not provide evidence, and does not make a publication form authoritative.

**Primary working reader.** The first reader is an engineer-manager, analyst, pattern author, or terminology steward who already has a candidate meaning and must choose a name that remains usable by readers without creating a second ontology.

**First useful move.** Before choosing the label, recover the exact named value and its direct source of meaning: `E.24.UK` or the direct governing pattern for a U-kind, with any Concept-Set row retained only as comparison evidence; or the role-description episteme, described `U.Role`, exact role-taxonomy episteme, effective reference scheme, and local sense for a role label. Then choose Tech and Plain labels whose morphology matches that kind and whose scope does not exceed the recovered meaning. Keep the selected label as a designator distinct from both the role value and its role-description episteme.

**Smallest useful result and stop.** Stop with one already-governed value, one Tech label, and a short Plain gloss as soon as the label resolves unambiguously for the named local use. Do not create a NameCard, public row, Bridge, or new kind merely to complete a naming form. Return to the direct subject owner when the value or kind is unresolved; open `F.18` or `F.17` only for a durable or public naming need, and open the F.9 bounded-use path only when an actual cross-scheme correspondence is consumed. If the proposed label starts carrying assignment, work, result, provenance, assurance, or publication claims, stop naming and recover those objects under their direct governors.

**What goes wrong if missed.** Names become arguments. A role label starts implying permission or capability. A status phrase becomes a role. A U-kind name imports one context's private ontology. A pretty global word hides that the Concept-Set witnesses do not agree. Downstream patterns then repair "semantics" that were actually broken at naming time.

**What this buys.** Readers can use short names without guessing the ontology. U-kind names stay neutral across their witnesses. RoleDescription labels remain interpretable through their named role-taxonomy episteme and effective reference scheme and point to work-facing roles. Status, evidence, access, requirement, source, publication, assurance, and gate names remain governed by their direct patterns instead of becoming "roles" by naming accident.

**Not this pattern when.**

- If the current problem is ordinary phrase repair rather than a durable name, use `E.10`, `E.10.ARCH`, `A.6.P`, or the direct governing pattern.
- If the current issue is whether a `U.*` spelling or structural name should survive as a durable U-kind, use `E.24.UK` before F.5.
- If the current issue is the broader local-first naming protocol, Name Cards, candidate fronts, lineage, or public naming governance, use `F.18`.
- If the current issue is a role-description episteme itself, use `F.4`.
- If the current issue is role assignment, holder, role-taxonomy episteme, effective reference scheme, assignment extent, or performed-work attribution, use `A.2.1`.
- If the current issue is status classification, use `F.10` or the direct status-use pattern.
- If the current issue is evidence, source, standard, requirement, publication, assurance, gate, or decision use of an episteme, use the direct pattern for that relation.
- If "role" means a relation position, use `A.6.5` SlotSpec discipline.
- If cross-taxonomy or cross-scheme correspondence is current, use `F.9`.

