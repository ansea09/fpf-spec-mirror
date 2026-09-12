---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
section_id: "A.10:8.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__012_sota-echoing.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.10 — Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
  - "A.10:8.1 — SoTA-Echoing"
line_start: 23160
line_end: 23173
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.PROD"
  - "A.19"
  - "A.2-family"
  - "A.2.4"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.10.ROLE"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
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

These sources contribute concrete distinctions to source-to-use recovery. Apply their relevant contracts to the selected claim and verification/use regime; identify FPF objects and direct relations independently.

| Source | Practical lesson for A.10 | Limit on reliance |
| --- | --- | --- |
| [W3C PROV-O, Recommendation 30 April 2013](https://www.w3.org/TR/prov-o/) | Qualified provenance descriptions and stable source/activity/agent references help recover source, copy, and transform identity. In an A.10 path, every edge cites an independently established direct relation between the appropriate FPF objects. | A PROV-shaped graph, `wasGeneratedBy` label, or qualified relation does not establish FPF Work, participation, result, truth, currentness, or later use. |
| [W3C Verifiable Credentials Data Model v2.0, Recommendation 15 May 2025](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/) | Distinguish issuer, represented subject, holder, verifier, validity, status, proof, and relying context. Recover the verifier rule and the currentness facts needed for the bounded use and its local disposition. Check validity limits when present or required, status when the mechanism is present or the selected policy requires it, and holder binding when the claim or verification regime requires it. Retain any stronger requirement of the actual selected policy. | The holder need not be the subject; bearer credentials need not identify the holder. A conforming or cryptographically verifiable credential does not by itself create transitive trust, permission, a `U.SystemRoleAssignment` occurrence, gate passage, assurance, or truth of every represented claim. |
| [SLSA specification v1.2](https://slsa.dev/spec/v1.2/) and [in-toto Attestation Framework v1.2](https://github.com/in-toto/attestation/blob/df02077bf97218a8860a5c534eff1f1381f56984/spec/v1/README.md), with its [`Statement/v1` contract](https://github.com/in-toto/attestation/blob/df02077bf97218a8860a5c534eff1f1381f56984/spec/v1/statement.md) | Distinguish artifact subject, predicate type, producing context, source inputs, authenticated envelope, verifier expectation, and versioned attestation. Recover the bounded build/source claim and the producing Work or System, verifier rule, holder, and window required by that claim or regime. Keep provenance separate from the reliance decision and exclude a locally plausible unsupported wider use. | A signed attestation, SLSA level, or verification summary is not runtime safety, release approval, gate passage, assurance, or proof that an uncited Work/result relation obtains. SLSA and in-toto versions are separate; `Statement/v1` alone does not identify an in-toto minor specification version. |
| [C2PA Content Credentials Technical Specification 2.4, April 2026](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html) | For claim-bound content attribution, distinguish asset/manifest identity, claim generator, assertions, ingredients/actions, signature validation, trust policy, and specification version. Recover the carrier, manifest/assertion, transformation, verifier/trust regime, edition, and currentness window relevant to that claim. | A valid manifest, repository receipt, authenticity mark, or visible Content Credential does not establish truth of the represented world state, authorship beyond its exact assertion, permission, safety, or adequacy. |
| Mitchell et al., [*Model Cards for Model Reporting*, FAT* 2019](https://doi.org/10.1145/3287560.3287596), and Gebru et al., [*Datasheets for Datasets*, CACM 64(12), 2021](https://doi.org/10.1145/3458723) | Use intended-use, evaluation-condition, performance/limitation, motivation, composition, collection, and maintenance disclosures to find sources. For every operative claim relied on, recover its source, carrier, and bounded use, plus Work and the local result when asserted. | A model card, datasheet, polished summary, or disclosed limitation is not evidence for an unstated claim, performed evaluation, assurance, approval, or deployment permission. |

A credential, attestation, documentation, or provenance model does not supply FPF authority for the claims it represents. The direct subject rule still determines what each claim establishes.

