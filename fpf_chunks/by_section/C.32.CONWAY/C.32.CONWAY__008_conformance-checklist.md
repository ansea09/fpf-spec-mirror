---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Architecture-Influence and Transformed-Architecture Correspondence"
section_id: "C.32.CONWAY:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__008_conformance-checklist.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.32.CONWAY — Architecture-Influence and Transformed-Architecture Correspondence"
  - "C.32.CONWAY:7 — Conformance Checklist"
line_start: 77335
line_end: 77351
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
| `CC-C32.CONWAY-2` | Every claimed actor is an admitted `U.System`; every claimed work-facing assignment names an occurrence and its declared A.2.1 species. The occurrence's holder matches the separately named acting System; the species defines the local assigned-kind domain, predicate, applicability, participant meanings, and occurrence identity. | Restore the missing fact for the claim that needs it. Retain independently supported System and acting claims when a separate assignment assertion fails. |
| `CC-C32.CONWAY-3` | Claimed performance has every exact actual performer recovered through A.13 and exact dated Work independently admitted through A.15.1. The same obtaining assignment is already part of each A.13 core. Its separate A.2.1 occurrence/species reference, F.6 `performedUnderAssignment(W, RA)` and `S = RA.HolderSystemSlot` are represented when precise assignment-bound attribution is consumed; missing or failed F.6 attribution alone leaves Work intact while its independent A.13/A.15.1 grounds still hold. Direct actor-side or Work-to-change relations remain separate, and several performers use A.15.1 `CC-A15.1-17` forms. | Restore the independent performer and Work basis; add attribution only for a consuming claim, or remove the unsupported performance or attribution claim. |
| `CC-C32.CONWAY-4` | Every asserted influence fact retains the source kind and its directly grounded obtaining relation; provisional pressure stays visibly provisional. Influence entails no actor, system-role kind or assignment, Work, changed-referent, or transformation-participation fact. | Apply the direct predicate: a missing kind or predicate returns `missing-governor`, unresolved facts stay provisional, and a false predicate excludes the occurrence claim; delete inferred acting facts. |
| `CC-C32.CONWAY-5` | One exact pair row names two obtaining C.30 `ArchitectureRelation` occurrences, each exact holon and selected-`U.Structure` participant, the changed referent, exact obtaining influence or correspondence occurrence, admitted relation kind, direct predicate and governor, and a satisfied affirmative case. Modal architecture content remains an `ArchitectureClaim` in the frame. | Complete the satisfied actual pair; otherwise keep only the synthesis-local frame and state modal status, `missing-governor`, unresolved grounding, or false predicate exactly. |
| `CC-C32.CONWAY-6` | Equality between an architecture bearer and an actor is recorded only from independent facts. | Separate the refs and remove equality inference. |
| `CC-C32.CONWAY-7` | The two project-use fields retain their exact Work identity and direct use-relation meaning. | Add both facts when project use is claimed or keep `@Project` retrieval-only. |
| `CC-C32.CONWAY-8` | Each candidate used for comparison explains which sides change or remain fixed, expected gain and its grounds, known loss, relevant window, receiving use and action-changing return conditions. A first-pass head alone is not a comparison-ready configuration. | Complete the content needed by the comparison or retain the candidate as provisional with its missing grounds explicit. |
| `CC-C32.CONWAY-8a` | Every `affectedArchitectureCharacteristicRefs[]` value resolves to a current C.32.ACS criteria row and, when composite, the exact C.25 Q-Bundle slot; a local discovery cue appears only in `provisionalArchitectureCharacteristicHeads[]` and supports no comparison, selection, or decision. | Resolve the governed ref, move the cue to the provisional-head field and use C.32.ACS/C.25, or remove the stronger claim. |
| `CC-C32.CONWAY-9` | Mathematical structural-similarity claims use C.29 or the selected structural-equivalence pattern. | Remove similarity entailment or apply the direct pattern. |
| `CC-C32.CONWAY-10` | A network record cites the pair only as a qualified reading; any `networkCrossFlowRelationRowRef` names that same exact current citing record, resolves exactly one row there, and its independently grounded occurrence and endpoint bindings agree with this pair. The singular locator qualifies no other record citation. | Remove the network link or repair the citing record, occurrence, and ordered endpoint-binding locator. |
| `CC-C32.CONWAY-11` | The correspondence retains the applicability window required by its predicate or use and a return condition for any action-changing omitted source detail. | Add the changed values and reopen trigger. |

