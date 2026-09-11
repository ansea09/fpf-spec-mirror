---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:10.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__012_sota-echoing.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:10.1 — SoTA-Echoing"
line_start: 4937
line_end: 4946
dependencies:
  - "A.10"
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10.D2"
  - "E.10.ROLE"
  - "E.17"
  - "F.10"
  - "G.11"
  - "G.6"
  - "U.SystemRoleAssignment"
keywords:
  - "claim"
  - "episteme"
  - "evidence-use relation"
  - "provenance"
  - "role-shaped source phrase"
  - "source-use wording"
  - "status-use relation"
---

### A.2.4:10.1 - SoTA-Echoing

| Source | Practical distinction | Limit |
| --- | --- | --- |
| [C2PA Content Credentials 2.4, April 2026](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html), [W3C Verifiable Credentials Data Model 2.0, Recommendation 15 May 2025](https://www.w3.org/TR/vc-data-model-2.0/), [SLSA 1.2](https://slsa.dev/spec/v1.2/), and [in-toto Attestation Framework 1.2 with `Statement/v1`](https://github.com/in-toto/attestation/blob/main/spec/README.md) | Distinguish subject, issuer or producer, verifier, proof or status, time, inputs, and relying context. Use A.10/G.6 for source and provenance and G.11 for currentness; first-use classification remains separate from those questions. | A valid credential, manifest, signature, attestation, SLSA level, or displayed status does not become truth, permission, gate passage, work, result, or assurance. |
| [ISO/IEC/IEEE 15026-2:2022, *Systems and software assurance — Part 2: Assurance case*](https://www.iso.org/standard/80625.html) | Cited evidence is distinct from the structure and maintenance of an assurance case. For an actual named assurance claim, use B.3 after A.10 source/provenance and bounded-reliance recovery. | Evidence presence, a confidence label, or an A.2.4 classification is not an assurance claim, safety result, readiness result, compliance result, or release confidence. |
| Hernán and Robins, [*Causal Inference: What If*, 2020 book, online 26 April 2024 edition](https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/04/hernanrobins_WhatIf_26apr24.pdf) | Distinguish observational data, interventions, target-trial questions, counterfactual outcomes and estimands, identification assumptions, and realized results. C.28 governs the evidence class and causal-use result. | A causal label, model, target-trial analogy, or simulated counterfactual does not establish intervention, identification, realized outcome, or a causal-use verdict. |
| Guizzardi et al., [*UFO: Unified Foundational Ontology*, Applied Ontology 17(1), 2022](https://doi.org/10.3233/AO-210256); related implementation accounts: [gUFO usage specification](https://nemo-ufes.github.io/gufo/overview.html) and Almeida et al., [*gUFO: A Gentle Foundational Ontology for Semantic Web Knowledge Graphs*, 2026 preprint](https://arxiv.org/abs/2603.20948) | Distinguish kinds and types, roles, relators and relations, events, and situations. In FPF, evidence-use and status-use SlotKinds name relation positions; they do not classify an episteme under a work-facing system-role kind or make it an assignment holder. | External `Role`, `Relator`, `Situation`, or OWL class vocabulary does not import a new FPF kind, replace an obtaining direct relation, or authorize an episteme system-role assignment. |


