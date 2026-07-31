---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Architecture-Influence and Transformed-Architecture Correspondence"
section_id: "C.32.CONWAY:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__008_conformance-checklist.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "C.32.CONWAY — Architecture-Influence and Transformed-Architecture Correspondence"
  - "C.32.CONWAY:7 — Conformance Checklist"
line_start: 65156
line_end: 65172
dependencies:
  - "A.10"
  - "A.12"
  - "A.15.1"
  - "A.19.CPM"
  - "A.22"
  - "A.3.4"
  - "A.3.4.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.3"
  - "C.11"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ACS"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.18"
  - "E.18.NET"
  - "G.5"
keywords:
---

### C.32.CONWAY:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
|---|---|---|
| `CC-C32.CONWAY-1` | `changedReferentRef` is independently identified; any changing relation has its direct governor. | Recover the referent and relation or keep the change description provisional. |
| `CC-C32.CONWAY-2` | Every claimed actor is one exact `U.System`; every claimed role has an obtaining role assignment. | Add the System and assignment or remove actor or role wording. |
| `CC-C32.CONWAY-3` | Claimed performance has exact dated Work, `performedUnderAssignment(W, RA)`, `S = RA.HolderSystemSlot`, and direct actor-side or work-to-change relations; several performers use A.15.1 forms. | Restore the Work basis and relations or remove the performance claim. |
| `CC-C32.CONWAY-4` | Every influence source retains its exact kind and direct obtaining occurrence; influence entails no actor, role, Work, changed-referent, or transformation-participation fact. | Apply the direct predicate: missing kind/predicate returns `missing-governor`, unresolved facts stay provisional, and a false predicate removes the occurrence; delete inferred acting facts. |
| `CC-C32.CONWAY-5` | One exact pair row names one influence-source architecture, one transformed architecture, selected structures, changed referent, exact obtaining occurrence, admitted relation kind, direct predicate/governor, and a satisfied affirmative case. | Complete the satisfied case; otherwise keep only the synthesis-local frame and state `missing-governor`, unresolved grounding, or false predicate exactly. |
| `CC-C32.CONWAY-6` | Equality between an architecture bearer and an actor is recorded only from independent facts. | Separate the refs and remove equality inference. |
| `CC-C32.CONWAY-7` | The two project-use fields retain their exact Work identity and direct use-relation meaning. | Add both facts when project use is claimed or keep `@Project` retrieval-only. |
| `CC-C32.CONWAY-8` | Each comparison-ready candidate states source-side change, transformed-side change, expected gain, known loss, evolution window, receiving pattern, source-return condition, and stop; a first-pass candidate head is visibly outside comparison. | Complete the candidate before comparison or keep only its `candidateRef` as a first-pass head. |
| `CC-C32.CONWAY-8a` | Every `affectedArchitectureCharacteristicRefs[]` value resolves to a current C.32.ACS criteria row and, when composite, the exact C.25 Q-Bundle slot; a local discovery cue appears only in `provisionalArchitectureCharacteristicHeads[]` and supports no comparison, selection, or decision. | Resolve the governed ref, move the cue to the provisional-head field and return to C.32.ACS/C.25, or remove the stronger claim. |
| `CC-C32.CONWAY-9` | Structural-similarity claims use C.29 or the selected structural-equivalence pattern. | Remove similarity entailment or apply the direct pattern. |
| `CC-C32.CONWAY-10` | A network record cites the pair only as a qualified reading; any `networkCrossFlowRelationRowRef` names that same exact current citing record, resolves exactly one row there, and its independently grounded occurrence and endpoint bindings agree with this pair. The singular locator qualifies no other record citation. | Remove the network link or repair the citing record, occurrence, and ordered endpoint-binding locator. |
| `CC-C32.CONWAY-11` | Source-return and evolution-window conditions are present. | Add the changed values and reopen trigger. |

