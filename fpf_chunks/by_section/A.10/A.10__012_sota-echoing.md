---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
section_id: "A.10:8.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__012_sota-echoing.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.10 — Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
  - "A.10:8.1 — SoTA-Echoing"
line_start: 22913
line_end: 22926
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.PROD"
  - "A.19"
  - "A.2.4"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "G.11"
  - "G.4"
keywords:
  - "RelianceDisposition"
  - "actual-use relation"
  - "bounded use"
  - "carrier"
  - "claim/result episteme"
  - "currentness"
  - "dated work"
  - "direct relation"
  - "evidence-provenance path"
  - "relied-on claim"
  - "rival explanation"
  - "source publication"
  - "unsupported overread"
---

### A.10:8.1 - SoTA-Echoing

Source qualification was checked against the publishers' current surfaces on 2026-07-30. It remains qualified through 2027-07-30 unless a latest specification, Recommendation, tagged framework release, status mechanism, or adopted documentation baseline changes earlier. Each source changes only the bounded A.10 locus named below; lineage and popular comparators not listed here are non-governing.

| Exact source and source-use decision | Visible A.10 mutation | Rejected overread | Smallest source-change replay |
| --- | --- | --- | --- |
| [W3C PROV-O, Recommendation 30 April 2013](https://www.w3.org/TR/prov-o/) — **adapt** qualified provenance descriptions and stable source/activity/agent references to A.10's exact FPF objects and direct relations. | §4.4 requires each path edge to cite an independently governed relation; checklist items 3 and 7 require source/copy/transform identity and reject graph membership as fact creation. | A PROV-shaped graph, `wasGeneratedBy` label, or qualified relation does not establish FPF work, participation, result, truth, currentness, or later use. | Reopen only §4.4's edge rule, the affected path in one worked case, and checklist items 3 and 7 if PROV-O's qualified-relation contract changes. |
| [W3C Verifiable Credentials Data Model v2.0, Recommendation 15 May 2025](https://www.w3.org/TR/vc-data-model-2.0/) — **adapt** issuer, subject/holder, verifier, validity/status, proof, and relying-context separation. | §4.6b's credential/status row, the credential-display case, and checklist items 8–9 require the exact verifier rule, status source, window/currentness, bounded use, and local disposition. | A conforming or cryptographically verifiable credential does not by itself create transitive trust, permission, role assignment, gate passage, assurance, or truth of every represented claim. | Reopen only the credential/status classifier row, the credential-display case, and checklist items 8–9 when the VC data model or its adopted status contract changes. |
| [SLSA specification v1.2](https://slsa.dev/spec/v1.2/) together with [in-toto Attestation Framework v1.2, `Statement/v1`](https://github.com/in-toto/attestation/blob/main/spec/README.md) — **adapt** artifact subject, predicate type, producing context, inputs, authenticated envelope, verifier expectation, and versioned attestation separation. | The §4.6b supply-chain row and software-attestation slice require a bounded build/source claim, producing work or system, verifier rule, source inputs, holder, window, and unsupported attempted use; checklist items 3 and 9 retain provenance and reliance separately. | A signed attestation, SLSA level, or verification summary is not runtime safety, release approval, gate passage, assurance, or proof that an uncited work/result relation obtains. | Reopen only that classifier row, the software-attestation slice, and checklist items 3 and 9 when SLSA's adopted provenance/verification contract or in-toto `Statement/v1` semantics change. |
| [C2PA Content Credentials Technical Specification 2.4, April 2026](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html) — **adapt** asset/manifest identity, claim generator, assertions, ingredients/actions, signature validation, trust policy, and specification version for claim-bound content attribution. | §4.6b's provenance/authenticity row, generated-content boundary, credential-display case, and checklist items 3 and 8 require the exact carrier, manifest/assertion, transformation, verifier/trust regime, edition, and currentness window. | A valid manifest, repository receipt, authenticity mark, or visible Content Credential does not establish truth of the represented world state, authorship beyond its exact assertion, permission, safety, or adequacy. | Reopen only the content-provenance classifier row, the credential-display case, and checklist items 3 and 8 when C2PA changes manifest/assertion identity, validation, trust, or versioning rules. |
| Mitchell et al., [*Model Cards for Model Reporting*, FAT* 2019](https://doi.org/10.1145/3287560.3287596), and Gebru et al., [*Datasheets for Datasets*, CACM 64(12), 2021](https://doi.org/10.1145/3458723) — **adapt** intended use, evaluation conditions, performance/limitation, motivation, composition, collection, and maintenance disclosures as source-finding inputs. | §4.6b's generated-explanation/documentation row and checklist items 1, 3, and 6 require every relied-on operative claim to return to its exact source, work, local result, carrier, and bounded use rather than relying on the document's presence. | A model card, datasheet, polished summary, or disclosed limitation is not evidence for an unstated claim, performed evaluation, assurance, approval, or deployment permission. | Reopen only the documentation classifier row, the one model/data-document path that uses it, and checklist items 1, 3, and 6 when the adopted disclosure fields or their claim boundary change. |

The current source decisions deliberately do not import a credential, attestation, documentation, or provenance ontology as A.10 authority. Source refresh replays the named rule, case, and checklist rows first and widens only if that local replay exposes a direct contradiction.

