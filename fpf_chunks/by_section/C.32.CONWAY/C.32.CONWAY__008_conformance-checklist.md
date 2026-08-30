---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Architecture-Influence and Transformed-Architecture Correspondence"
section_id: "C.32.CONWAY:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__008_conformance-checklist.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.32.CONWAY — Architecture-Influence and Transformed-Architecture Correspondence"
  - "C.32.CONWAY:7 — Conformance Checklist"
line_start: 64930
line_end: 64946
dependencies:
  - "A.10"
  - "A.12"
  - "A.13"
  - "A.15.1"
  - "A.19.CPM"
  - "A.2.1"
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
  - "F.6"
  - "G.5"
  - "U.Structure"
keywords:
---

### C.32.CONWAY:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
|---|---|---|
| `CC-C32.CONWAY-1` | `changedReferentRef` is independently identified; any claimed actual bounded change has one A.3.4 `actualTransformationRef`, while actor-side and Work-to-change relations retain their direct governors. | Recover those exact objects and relations or keep the change description provisional. |
| `CC-C32.CONWAY-2` | Every claimed actor is an admitted `U.System`; every claimed work-facing assignment names an occurrence and its declared A.2.1 species. The occurrence's holder matches the separately named acting System; the species defines the local assigned-kind domain, predicate, applicability, participant meanings, and occurrence identity. | Add the System, species, and assignment occurrence or remove the acting or assignment claim. |
| `CC-C32.CONWAY-3` | Claimed performance has every exact actual performer recovered through A.13 and exact dated Work independently admitted through A.15.1. An exact A.2.1 assignment, F.6 `performedUnderAssignment(W, RA)` occurrence, and `S = RA.HolderSystemSlot` appear only when precise assignment-bound attribution is expressly represented; missing or failed F.6 leaves Work intact. Direct actor-side or Work-to-change relations remain separate, and several performers use A.15.1 `CC-A15.1-17` forms. | Restore the independent performer and Work basis; add attribution only for a consuming claim, or remove the unsupported performance or attribution claim. |
| `CC-C32.CONWAY-4` | Every influence source retains its exact kind and direct obtaining occurrence; influence entails no actor, system-role kind or assignment, Work, changed-referent, or transformation-participation fact. | Apply the direct predicate: a missing kind or predicate returns `missing-governor`, unresolved facts stay provisional, and a false predicate removes the occurrence; delete inferred acting facts. |
| `CC-C32.CONWAY-5` | One exact pair row names two obtaining C.30 `ArchitectureRelation` occurrences, each exact holon and selected-`U.Structure` participant, the changed referent, exact obtaining influence or correspondence occurrence, admitted relation kind, direct predicate and governor, and a satisfied affirmative case. Modal architecture content remains an `ArchitectureClaim` in the frame. | Complete the satisfied actual pair; otherwise keep only the synthesis-local frame and state modal status, `missing-governor`, unresolved grounding, or false predicate exactly. |
| `CC-C32.CONWAY-6` | Equality between an architecture bearer and an actor is recorded only from independent facts. | Separate the refs and remove equality inference. |
| `CC-C32.CONWAY-7` | The two project-use fields retain their exact Work identity and direct use-relation meaning. | Add both facts when project use is claimed or keep `@Project` retrieval-only. |
| `CC-C32.CONWAY-8` | Each comparison-ready candidate states source-side change, transformed-side change, expected gain, known loss, evolution window, pattern for the next question, source-return condition, and stop; a first-pass candidate head is visibly outside comparison. | Complete the candidate before comparison or keep only its `candidateRef` as a first-pass head. |
| `CC-C32.CONWAY-8a` | Every `affectedArchitectureCharacteristicRefs[]` value resolves to a current C.32.ACS criteria row and, when composite, the exact C.25 Q-Bundle slot; a local discovery cue appears only in `provisionalArchitectureCharacteristicHeads[]` and supports no comparison, selection, or decision. | Resolve the governed ref, move the cue to the provisional-head field and use C.32.ACS/C.25, or remove the stronger claim. |
| `CC-C32.CONWAY-9` | Structural-similarity claims use C.29 or the selected structural-equivalence pattern. | Remove similarity entailment or apply the direct pattern. |
| `CC-C32.CONWAY-10` | A network record cites the pair only as a qualified reading; any `networkCrossFlowRelationRowRef` names that same exact current citing record, resolves exactly one row there, and its independently grounded occurrence and endpoint bindings agree with this pair. The singular locator qualifies no other record citation. | Remove the network link or repair the citing record, occurrence, and ordered endpoint-binding locator. |
| `CC-C32.CONWAY-11` | Source-return and evolution-window conditions are present. | Add the changed values and reopen trigger. |

