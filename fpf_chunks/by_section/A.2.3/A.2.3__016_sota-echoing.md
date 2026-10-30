---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent — Promised Outcomes and Acceptance Criteria"
section_id: "A.2.3:10.3"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__016_sota-echoing.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.2.3 — U.PromiseContent — Promised Outcomes and Acceptance Criteria"
  - "A.2.3:10.3 — SoTA-Echoing"
line_start: 5947
line_end: 5959
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8"
  - "A.2.9"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "F.12"
  - "F.9"
  - "U.ClaimScope"
  - "U.Episteme"
  - "U.Method"
  - "U.MethodDescription"
  - "U.SystemRoleAssignment"
  - "U.Work"
  - "U.WorkPlan"
  - "U.WorkScope"
keywords:
  - "SLA"
  - "SLO"
  - "Work evidence"
  - "acceptance specification"
  - "access specification"
  - "claim scope"
  - "promise content"
  - "promised outcome"
  - "provider and consumer system-role kinds"
---

### A.2.3:10.3 - SoTA-Echoing

The question is how to specify a reusable consumer-facing promise precisely enough to evaluate its fulfilment while keeping actual obligations and performance claims recoverable. A.2.3 selects a promise-content episteme containing the outcome and acceptance specifications. Actual commitment, delivery, measurement and verdict claims use their respective direct patterns. This is an FPF construction for that bounded question; its grounds come from distinct operational and ontological contributions.

Google’s *Site Reliability Engineering* (2016, chapter 4, “Service Level Terminology”) distinguishes a service-level indicator, its target, and an agreement with consequences for meeting or missing that target. The *Site Reliability Workbook* (2018, chapter 2, “What to Measure: Using SLIs”) further separates the user-relevant SLI specification from its measurement implementation: several implementations can assess the same specification with different coverage, accuracy and cost. A.2.3 adapts these distinctions when constructing acceptance criteria and selecting evaluation methods. The observed value, target and consequence remain separate claims. [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/); [Implementing SLOs](https://sre.google/workbook/implementing-slos/).

A fuller alternative organizes the service account around commitments throughout offering, negotiation and delivery. The historical UFO-S treatment explicitly distinguishes offering and agreement descriptions from the relations they describe and from delivery actions (Nardi et al., 2015, §§4.1–4.3). The later Service Contract Ontology account likewise distinguishes an agreement description from the agreement relation (Griffo et al., 2023, §2.2). This approach supplies a richer account when the receiving question concerns agreement formation or change. For authoring one reusable clause, A.2.3 retains the narrower content object and connects it to separately established commitments through A.2.8. [UFO-S](https://ris.utwente.nl/ws/files/6413537/1-s2.0-S0306437915000228-main.pdf); [Modeling the dynamics of contractual relations](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2023.1042319/full).

Cloud storage makes the distinction consequential. Amazon’s S3 technical documentation states an annual durability design claim, while its SLA dated 28 November 2023 defines monthly availability using five-minute error rates, with account and storage-class scope, exclusions and credit conditions. These statements supply different criteria and grounds. A month of successful requests does not by itself establish the annual durability design claim. Likewise, a fulfilment judgement and eligibility for a service credit answer different questions. [S3 data protection](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html); [S3 SLA, “Service Commitment”, “Credit Request and Payment Procedures” and “Definitions”](https://aws.amazon.com/s3/sla/).

In §5, the illustrative percentages therefore require their own declared characteristics, populations, windows and evaluation methods. C.16 supplies the measurement interpretation; A.10 carries the claim-specific grounds. If the promise concerns end-to-end retrieval but observations cover only requests reaching the backend, retain that coverage limitation when judging fulfilment. If an actual obligation is claimed, establish its bearer and instituting basis under A.2.8. The cost of this separation is establishing those connections when the receiving use needs them. Revisit the source-based criteria when governing terms, measurement coverage or the intended use changes; a task whose primary result is agreement formation, amendment or remedy requires the corresponding fuller account.


