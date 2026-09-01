---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:10.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__012_sota-echoing.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:10.1 — SoTA-Echoing"
line_start: 4856
line_end: 4868
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

Source qualification was checked against the publishers' current surfaces on 2026-07-30. It remains qualified through 2027-07-30 unless a Recommendation, specification/tag, assurance standard, online causal edition, or adopted foundational-ontology account changes earlier. Only sources that change A.2.4's first-use classifier are decision-governing; other lineage examples remain non-governing.

| Exact source and source-use decision | Visible A.2.4 mutation | Rejected overread | Smallest source-change replay |
| --- | --- | --- | --- |
| [C2PA Content Credentials 2.4, April 2026](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html), [W3C Verifiable Credentials Data Model 2.0, Recommendation 15 May 2025](https://www.w3.org/TR/vc-data-model-2.0/), [SLSA 1.2](https://slsa.dev/spec/v1.2/), and [in-toto Attestation Framework 1.2 with `Statement/v1`](https://github.com/in-toto/attestation/blob/main/spec/README.md) — **adapt** their subject, issuer/producer, verifier, proof/status, time, input, and relying-context separations. | `EvidenceProvenanceConstraintSlot`, `StatusProvenanceConstraintSlot`, the dashboard-status case, and `CC-A2.4-7/10` require the exact source/status/proof relation while keeping first-use classification separate from provenance and currentness. | A valid credential, manifest, signature, attestation, SLSA level, or displayed status does not become truth, permission, gate passage, work, result, or assurance. | Reopen only those two provenance-constraint SlotKinds, the dashboard-status case, and `CC-A2.4-7/10` when one adopted source changes subject, status, proof, verifier, or version semantics. |
| [ISO/IEC/IEEE 15026-2:2022, *Systems and software assurance — Part 2: Assurance case*](https://www.iso.org/standard/80625.html) — **adapt** the separation between cited evidence and the structure/maintenance of an assurance case. | `EvidenceAssuranceUseSlot`, §4.6 object 8, and `CC-A2.4-9` handle assurance outward under B.3 after A.10 provenance/reliance recovery. | Evidence presence, a confidence label, or an A.2.4 classification is not an assurance claim, safety result, readiness result, compliance result, or release confidence. | Reopen only `EvidenceAssuranceUseSlot`, §4.6 item 8, the measurement-use case's assurance exit, and `CC-A2.4-9` if the adopted assurance-case structure or maintenance boundary changes. |
| Hernán and Robins, [*Causal Inference: What If*, 2020 book, online 26 April 2024 edition](https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/04/hernanrobins_WhatIf_26apr24.pdf) — **adapt** the explicit separation of observational data, interventions, target-trial questions, counterfactual outcomes/estimands, identification assumptions, and realized results; C.28 retains the actual value set and verdict. | §4.5's causal line, the simulation-only case, and `CC-A2.4-11` prevent first-use wording from promoting observational association or simulation output into interventional or realized-counterfactual evidence. | A causal label, model, target-trial analogy, or simulated counterfactual does not establish intervention, identification, realized outcome, or a causal-use verdict. | Reopen only §4.5's causal line, the simulation-only case, and `CC-A2.4-11` if the adopted evidence-class or target-trial boundary changes. |
| Guizzardi et al., [*UFO: Unified Foundational Ontology*, Applied Ontology 17(1), 2022](https://doi.org/10.3233/AO-210256) — **adapt** only its distinctions among kinds and types, roles, relators and relations, events, and situations as an anti-collapse comparator. The [gUFO usage specification](https://nemo-ufes.github.io/gufo/overview.html) and Almeida et al., [*gUFO: A Gentle Foundational Ontology for Semantic Web Knowledge Graphs*, 2026 preprint](https://arxiv.org/abs/2603.20948), are watch-only implementation evidence, not additional A.2.4 authority. | §4.0, §4.1/4.2 SlotKind boundaries, and `CC-A2.4-2` keep an episteme in a relation position without making it a new U-kind or a work-facing system-role-assignment holder. | External `Role`, `Relator`, `Situation`, or OWL class vocabulary does not import a new FPF kind, replace an obtaining direct relation, or authorize an episteme system-role assignment. | Reopen only the §4.0 anti-collapse sentence, the affected SlotKind boundary, the proof-result first-use case, and `CC-A2.4-2` if the adopted role and relation-position distinction changes. |

Source refresh is local: replay the row's named SlotKind or rule, one case, and checklist locus before widening. A changed source cannot by itself alter the domain-local result, Work, provenance, currentness, assurance, causal verdict, local system-role kind, or system-role assignment handled under a neighboring subject pattern.

