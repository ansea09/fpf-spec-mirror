---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Is This Claim Supported for This Use? — Trust and Assurance Calculus"
section_id: "B.3:10.1"
section_title: "Decision-bearing SoTA account"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__013_decision-bearing-sota-account.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "B.3 — Is This Claim Supported for This Use? — Trust and Assurance Calculus"
  - "B.3:10.1 — Decision-bearing SoTA account"
line_start: 44733
line_end: 44741
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.2.6"
  - "A.21"
  - "A.22"
  - "A.6.1"
  - "B.1.5"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.10"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
---

### B.3:10.1 - Decision-bearing SoTA account

| Practical question | Source | Contribution to B.3 | Applicability condition |
| --- | --- | --- | --- |
| What makes an assurance case inspectable? | [ISO/IEC/IEEE 15026-2:2022, edition 2](https://www.iso.org/standard/80625.html) specifies assurance-case structure and maintenance. The [GSN Community Standard v3](https://scsc.uk/gsn-standard) gives engineering-argument notation and guidance. | **Adopt** explicit claim, argument, evidence, context, defeater, and maintenance structure. **Adapt** it to the compact and replay paths. **Reject** document or diagram appearance as assurance, approval, or permission. Sections 4.1–4.2 apply this structure to the smallest result sufficient for the use. | Use the governing assurance-case edition and check that the compact result states the claim, argument, and evidence needed for the receiving use. |
| How may reliability-like inputs be combined? | NASA's [Fault Tree Handbook with Aerospace Applications, v1.1](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Fault%20Tree%20Handbook_NASA.pdf), chapter 6, derives AND-event probability from conditional probability and uses a product only under independence. | **Adopt** dependency- and assumption-specific calculation. **Reject** universal `min` and any claim that it is always conservative. Section 4.4 and case 6.1 apply the dependency model before selecting arithmetic. | Use a dependence model warranted for the current claim. A different validated domain model changes which calculation applies. |
| Can one trustworthiness tuple compare unlike AI or system properties? | [NIST AI Risk Management Framework 1.0](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=936225) treats trustworthiness characteristics as context- and use-dependent and recognizes trade-offs and domain metrics. | **Adopt** named characteristics and use-specific thresholds. **Reject** same-letter cross-domain comparability and monotone formality. Section 4.3 keeps the bearer and scale explicit. | Keep numerical assessments of unlike properties separate unless a validated common measurement model supplies the bearers, scales, units, and interpretation needed for their comparison. |
| What can provenance and attestation establish? | [C2PA Technical Specification 2.4](https://spec.c2pa.org/specifications/specifications/2.4/index.html) distinguishes provenance validity from value judgments. [in-toto Attestation Framework 1.2](https://github.com/in-toto/attestation/releases/tag/v1.2.0) defines authenticated metadata about software artifacts. | **Adopt** exact subject, source, binding, and verification claims. **Reject** a valid credential, manifest, attestation, or display as automatic truth, safety, compliance, readiness, or release. Section 4.6 and case 6.2 distinguish the verified property from the later decision. | Check the property warranted by the applicable specification and whether the direct domain rule makes it sufficient for the named use. |

