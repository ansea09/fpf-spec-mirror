---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__012_sota-echoing.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:11 — SoTA-Echoing"
line_start: 100888
line_end: 100902
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.1"
  - "A.2.4"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "F.10"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.9"
keywords:
  - "EvidenceGraph"
  - "NotCarried"
  - "PathCitationRecord"
  - "PathId"
  - "PathSliceId"
  - "actual-use relation"
  - "direct governors"
  - "downstream work"
  - "exact direct relations"
  - "exact represented objects"
  - "local refresh"
  - "obtaining claims"
  - "provenance ledger"
  - "representation correspondence"
  - "source/currentness"
  - "unresolved gaps"
---

### G.6:11 - SoTA-Echoing

Source qualification was checked against the publishers' current surfaces on 2026-07-30. These decisions remain qualified through 2027-07-30 unless a new Recommendation, specification edition, maintenance status, or replacement changes the adopted contract earlier. Internal FPF neighbour authority stays in Relations; it is not presented as an external source decision.

| Exact source and source-use decision | Visible G.6 mutation | Rejected overread | Smallest source-change replay |
| --- | --- | --- | --- |
| [W3C PROV-O, Recommendation 30 April 2013](https://www.w3.org/TR/prov-o/) — **adapt** qualified provenance descriptions and stable entity/activity/agent references only as a representation discipline for exact FPF objects and direct relations. | `RepresentedNodeRecord`, `RepresentedRelationEdgeRecord`, the measurement-to-decision case, and `CC-G6-02/03` require every node and edge to cite an independently governed object or obtaining relation with its governor and qualification. | A PROV-shaped class, activity, agent, qualified association, or derivation does not establish FPF work, participation, production, result, truth, currentness, or later use. | Reopen only §4.2's node/edge rules, the measurement-to-decision path, and `CC-G6-02/03` if PROV-O's qualified-relation contract changes. |
| [C2PA Content Credentials Technical Specification 2.4, April 2026](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html) — **adapt** asset/manifest identity, claim generator, assertions, ingredients/actions, signature validation, trust policy, and specification version for claim-bound content provenance. | `PathCitationRecord` carries source publication/carrier, C.29 representation, edition/policy, currentness, and `NotCarried`; the produced-model case and `CC-G6-07/08` retain the exact content carrier, transform chain, trust regime, and version. | A valid manifest, visible Content Credential, ingredient chain, or authenticity mark does not establish truth of the represented world state, authorship beyond its exact assertion, work, safety, permission, or adequacy. | Reopen only those `PathCitationRecord` source/version fields, the produced-model carrier slice, and `CC-G6-07/08` when C2PA changes manifest/assertion identity, validation, trust, or version semantics. |
| [SLSA specification v1.2](https://slsa.dev/spec/v1.2/) with [in-toto Attestation Framework v1.2 and `Statement/v1`](https://github.com/in-toto/attestation/blob/main/spec/README.md) — **adapt** artifact subject, predicate type, producing context, inputs, authenticated envelope, verifier expectation, and versioned attestation separation. | The produced-model/benchmark path names training work, produced model edition, dataset/method edition, benchmark work/result, source inputs, publication/carrier, verifier context, and currentness; `CC-G6-07/08` keep those refs replayable without one generic attestation edge. | A signed statement, provenance predicate, SLSA level, or verification summary does not prove an uncited build/work/result relation, benchmark superiority, runtime safety, release approval, gate passage, or assurance. | Reopen only the attestation-bearing fields of that path slice, the produced-model/benchmark case, and `CC-G6-07/08` when the adopted SLSA provenance/verification contract or in-toto `Statement/v1` semantics change. |
| [W3C Verifiable Credentials Data Model 2.0, Recommendation 15 May 2025](https://www.w3.org/TR/vc-data-model-2.0/) — **adapt** credential subject, issuer, holder, verifier, status, context, and validity separation for a path that cites an independently governed credential/status use. | `PathCitationRecord` separates source/carrier/currentness refs, downstream work, exact use relation, A.10 reliance disposition, and `NotCarried`; the dashboard-status case and `CC-G6-09` require the status cue, query/use work, verifier or relying context, and actual reliance to remain distinct. | A valid credential, successful proof check, holder presentation, status value, or graph membership does not become claim truth, authorization, permission, gate passage, release, actual reliance, or assurance. | Reopen only those credential/status/use fields, the dashboard-status path, and `CC-G6-09` if VC 2.0 or its adopted status/validity contract changes. |
| Pineau et al., [*Improving Reproducibility in Machine Learning Research*, JMLR 22(164), 2021](https://jmlr.org/papers/v22/20-303.html), and Mitchell et al., [*Model Cards for Model Reporting*, FAT* 2019](https://doi.org/10.1145/3287560.3287596) — **adapt** exact method, dataset, metric, evaluation condition, version, limitation, and run-evidence disclosure as inputs to a replayable benchmark path. | The produced-model/benchmark case, dependency-closed `PathSliceId`, and `CC-G6-02/07/08` keep model edition, training/evaluation work, dataset and method editions, local result, result episteme, source carrier, limitations, and currentness separately addressable. | A reproducibility checklist, model card, disclosed score, or limitation does not establish that training or evaluation occurred, that the reported result is current, that one model is superior, or that deployment is permitted. | Reopen only the model/benchmark slice fields, that worked case, and `CC-G6-02/07/08` if the adopted reproducibility or reporting contract changes. |
| [ISO/IEC/IEEE 15026-2:2022, *Systems and software assurance — Part 2: Assurance case*](https://www.iso.org/standard/80625.html) — **adapt** the separation between cited evidence and the structure, maintenance, and evaluation of an assurance case. | `NotCarried` names assurance explicitly, the subject-pattern map and §4.7 handle assurance under B.3, and `CC-G6-10` permits the ledger to index evidence paths without becoming an assurance result. | A complete-looking evidence path, ledger entry, confidence label, or signed carrier is not an assurance claim, safety result, readiness result, compliance result, or release confidence. | Reopen only `NotCarried`, the B.3 extension boundary, one assurance-input path, and `CC-G6-10` if the adopted assurance-case evidence or maintenance boundary changes. |

Source refresh is local: replay the changed row's named record fields, rule or case, and checklist rows first. Widen only when that replay contradicts another current G.6 locus; a changed source cannot by itself create a represented object, obtaining relation, work occurrence, result, currentness, reliance, assurance, permission, or decision.

