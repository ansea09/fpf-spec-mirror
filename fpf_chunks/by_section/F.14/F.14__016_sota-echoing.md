---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for System-Role and Status Name Families"
section_id: "F.14:15"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__016_sota-echoing.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "F.14 — Anti-Explosion Control for System-Role and Status Name Families"
  - "F.14:15 — SoTA-Echoing"
line_start: 97742
line_end: 97754
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "B.3"
  - "E.10.D2"
  - "E.24.PUB"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
  - "NameCard"
  - "assignment"
  - "designation"
  - "evidence use"
  - "permission"
  - "reuse"
  - "status names"
  - "system-role names"
  - "term row"
  - "vocabulary explosion"
---

### F.14:15 - SoTA-Echoing

F.14 does not import access-control, terminology, credential, or modeling-language taxonomies as FPF ontology. It uses the sources below only where they change the anti-explosion rule.

| Anti-explosion question | Exact source and source-use status | Adoption or rejection in F.14 | Currentness and reopen condition |
|---|---|---|---|
| Why is a system-role-kind label insufficient for authorization? | Rose et al., NIST [SP 800-207, *Zero Trust Architecture*](https://doi.org/10.6028/NIST.SP.800-207) (2020), is a **current security-architecture reference** that separates a subject's access to a resource, policy decision, policy administration, and policy enforcement. | **Adapt the separation.** Keep the kind name, assigned System, request, requested resource and action, policy decision, permission, and Work distinct. Reject authorization, capability, or trust inferred from a system-role-kind label. | Reopen when NIST replaces SP 800-207 or a stronger authorization architecture changes the separation among subject, policy, decision, and enforcement used by this rule. |
| Why should role-like convenience names not replace an explicit policy relation? | Cutler et al., [*Cedar: A New Language for Expressive, Fast, Safe, and Analyzable Authorization*](https://arxiv.org/abs/2403.04651) (OOPSLA 2024 extended version), is a **current primary policy-language source** separating principal, action, resource, context, policy, and authorization decision while supporting role-, attribute-, and relation-based policies. | **Adapt only the explicit-policy lesson.** Recover the direct policy relation and its participants instead of minting a hybrid system-role kind. Reject importing Cedar entities, schema, or evaluator as FPF ontology. | Reopen if current policy-language practice shows that the explicit boundary between participants and policy no longer prevents the name explosion addressed here. |
| Why must a governed value be recovered before a durable designation or family is minted? | [ISO 704:2022](https://www.iso.org/standard/79077.html) is a **current terminology standard** connecting objects, concepts, definitions, and designations. | **Adopt.** Recover the value and use first; then choose no durable name, an existing designation, a local expression, a NameCard, or a public row only at its own trigger. Reject shared spelling as value identity or semantic equivalence. | Reopen when ISO 704 or F.17 and F.18 change the distinction between a value and its designation or the publication threshold used here. |
| Why are credential presentation, status, and relying use different from the governed value? | W3C [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) (2025) is a **current W3C Recommendation** separating issuer, subject, holder, verifier, credential, presentation, and credential status, and leaving authorization decisions outside the data model. | **Adapt.** Keep status, evidence, credential, view, verifier action, and relying decision distinct. Reject a suffix, badge, credential view, or dashboard row as a system-role kind, assignment, permission, assurance, or decision. | Reopen when the VC Recommendation or its status family changes the boundaries among presentation, status, and relying use applied in the worked cases. |

SysML is intentionally excluded from the positive SoTA basis and from lineage for this pattern. The official [OMG SysML 2.0 specification](https://www.omg.org/spec/SysML/2.0) (September 2025) is recorded only as a **rejected-popular comparison**: a modeling-language role spelling does not independently establish FPF's local system-role kind, classification, assignment, capability, permission, Method, or Work. Official status and popularity are not evidence for this anti-explosion question. Reopen that rejection only if demonstrated practice supplies a directly relevant, lower-cost kind-admission and assignment boundary that improves the F.14 cases.

