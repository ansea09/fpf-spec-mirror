---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus"
section_id: "B.3:10.1"
section_title: "Decision-bearing SoTA account"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__013_decision-bearing-sota-account.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "B.3 — Trust and Assurance Calculus"
  - "B.3:10.1 — Decision-bearing SoTA account"
line_start: 38363
line_end: 38373
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.2.6"
  - "A.21"
  - "A.22"
  - "A.6.1"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.10"
  - "G.11"
  - "G.6"
keywords:
---

### B.3:10.1 - Decision-bearing SoTA account

| Practical question | Exact current source | Adopt, adapt, or reject in B.3 | Reopen condition |
| --- | --- | --- | --- |
| What makes an assurance case inspectable? | [ISO/IEC/IEEE 15026-2:2022, edition 2](https://www.iso.org/standard/80625.html) specifies assurance-case structure and maintenance. The [GSN Community Standard v3](https://scsc.uk/gsn-standard) gives current engineering-argument notation and guidance. | **Adopt** explicit claim, argument, evidence, context, defeater, and maintenance structure. **Adapt** it to the compact and replay paths. **Reject** document or diagram appearance as assurance, approval, or permission. This decision shapes 4.1, 4.2, 5, and the dashboard case. | A successor changes the required claim-argument-evidence relation or validated use shows that a compact field is missing or redundant. |
| How may reliability-like inputs be combined? | NASA's [Fault Tree Handbook with Aerospace Applications, v1.1](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Fault%20Tree%20Handbook_NASA.pdf), chapter 6, derives AND-event probability from conditional probability and uses a product only under independence. | **Adopt** dependency- and assumption-specific calculation. **Reject** universal `min` and any claim that it is always conservative. This decision shapes 4.4 and worked case 6.1. | A direct domain model with different validated dependence semantics applies to the current claim. |
| Can one trustworthiness tuple compare unlike AI or system properties? | [NIST AI Risk Management Framework 1.0](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=936225) treats trustworthiness characteristics as context- and use-dependent and recognizes trade-offs and domain metrics. | **Adopt** named characteristics and use-specific thresholds. **Reject** same-letter cross-domain comparability and monotone formality. This decision shapes 4.3. | A validated common measurement model supplies shared bearers, scales, units, and interpretation for the exact properties being compared. |
| What can provenance and attestation establish? | [C2PA Technical Specification 2.4](https://spec.c2pa.org/specifications/specifications/2.4/index.html) distinguishes provenance validity from value judgments. [in-toto Attestation Framework 1.2](https://github.com/in-toto/attestation/releases/tag/v1.2.0) defines authenticated metadata about software artifacts. | **Adopt** exact subject, source, binding, and verification claims. **Reject** a valid credential, manifest, attestation, or display as automatic truth, safety, compliance, readiness, or release. This decision shapes 4.6 and case 6.2. | A successor specification changes the property warranted by the artifact or a direct domain rule makes that property sufficient for the named use. |

Older assurance-case editions and generic weakest-link slogans are lineage, not decision authority. Popularity, formal appearance, and publication recency do not establish the selected architecture.

