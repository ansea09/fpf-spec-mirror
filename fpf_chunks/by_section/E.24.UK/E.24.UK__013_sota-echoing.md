---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__013_sota-echoing.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:11 — SoTA-Echoing"
line_start: 89571
line_end: 89604
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.2.6"
  - "A.22"
  - "A.3.2"
  - "A.6.0"
  - "A.6.3"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10"
  - "E.17.0"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "F.18"
  - "U.MethodDescription"
  - "U.Structure"
  - "U.View"
  - "U.Viewpoint"
keywords:
---

### E.24.UK:11 - SoTA-Echoing

Use these sources as pressure on the admission decision, not as a borrowed taxonomy. The sources disagree at important seams: for example, OntoUML treats a Role as an anti-rigid type of the same bearer, whereas BFO treats a role as a specifically dependent continuant. The FPF dispositions `root`, `same-individual-dependent`, and `identity-dependent`, the C.3 split, and the durable-public threshold are therefore explicit FPF decisions. No source below is cited as if it supplied that three-way taxonomy.

**Type, membership, and dependent form.** Almeida, Guizzardi, Sales, and Fonseca's [gUFO paper, 2026](https://arxiv.org/abs/2603.20948) selects a typology of types and explicit patterns for intrinsic and relational aspects. The current [OntoUML Vocabulary](https://dev.ontouml.org/ontouml-vocabulary/) distinguishes identity-providing kinds and subkinds from relational Roles, intrinsic-condition Phases, dependent Quality individuals, and relation-grounding Relators.

FPF mutation: adopt the separation questions, not those categories. First decide whether the same already identified individual gains membership or a distinct individual needs a governed dependence relation.

**Dependence is not parthood.** [ISO/IEC 21838-2:2021 BFO](https://www.iso.org/standard/74572.html) remains the published standard lineage. The current BFO 2020 Common Logic artifacts keep [specific dependency](https://github.com/BFO-ontology/BFO-2020/blob/master/21838-2/common-logic/specific-dependency.cl) and [continuant mereology](https://github.com/BFO-ontology/BFO-2020/blob/master/21838-2/common-logic/continuant-mereology.cl) as distinct relation families. The specific-dependency axioms also prohibit a specifically dependent continuant and its bearer from sharing a continuant part.

FPF mutation: require an exact dependence governor for an identity-dependent admission and never infer part-of from dependence.

**Class inclusion, individuals, properties, and labels.** The W3C [OWL 2 Direct Semantics](https://www.w3.org/TR/owl2-direct-semantics/) and [Structural Specification](https://www.w3.org/TR/owl2-syntax/) are labelled lineage baselines, not current-best admission guidance. They distinguish class extensions, individuals, and object properties; `SubClassOf` makes the first extension a subset of the second; annotation labels have no logical effect; and imports make another ontology's axioms available.

FPF mutation: use the inclusion lesson for the same-individual root implication, but require the direct owner to supply identity and membership. A label, import, or class axiom alone admits no durable U-kind.

**Modularity, scope, and reuse.** Shimizu and Hitzler's [2024 modular-ontology direction](https://arxiv.org/abs/2411.09601), the [MODL library](https://arxiv.org/abs/1904.05405), and the operationalized [OBO Foundry principles](https://pmc.ncbi.nlm.nih.gov/articles/PMC8546234/) support reusable bounded patterns, explicit scope, and reuse of existing relations.

FPF mutation: apply the existing-governor-first rule. Repeated cross-pattern need is necessary but not sufficient for durable admission; one stable membership or identity law, one direct owner, named reliance, and a non-use boundary must also be present.

**Designation versus governed object.** [ISO 704:2022](https://www.iso.org/standard/79077.html) addresses the links among objects, concepts, definitions, and designations as separately named positions in terminology work.

FPF mutation: choose a public spelling through F.18 and the naming patterns only after the classified individuals, criterion, disposition, and direct governor are settled. A preferred term, filename, heading, or table row is naming pressure, not kind identity or admission.

#### Source-pressure tests for the FPF categories

1. **Same-individual membership and ontology-level inclusion.** `MaintenancePlan_Q3` remains the one episteme identified by C.2.1. A.15.2 may add `U.WorkPlan` membership and the implication to `U.Episteme`; it does not create a second plan individual. OntoUML Role/Phase and OWL subclassing are useful comparators, but only the FPF direct membership predicate and root-inclusion law close this admission.
2. **Identity dependence and non-parthood.** `Pump37MaintenanceCapability_2026` would be distinct from holder system `Pump37`. gUFO/BFO show that dependent aspects can be distinct individuals, but they do not provide the missing FPF capability-to-holder relation or its identity effect. The candidate therefore remains at `E24UK-BLK-U-CAPABILITY-01`; even a future dependence result would establish no part-of claim.
3. **Role and phase near-misses.** A technician role or a damaged-pump phase does not by itself reidentify its bearer. When the distinction is only participation in a current relation or an intrinsic condition for one bounded use, keep the same individual and use the direct relation or a C.3 local kind. Do not mint either another individual or a durable U-kind merely because an external taxonomy offers Role or Phase.
4. **Quality and relator near-misses.** A source model may treat a pressure quality or a contract relator as a distinct dependent individual. FPF opens a distinct-individual admission only when a direct owner identifies that individual and governs its dependence. A measurement value, quality assertion, participant pair, contract document, or relation record is not that individual and cannot move the case into `identity-dependent`.
5. **C.3 separation and the durable threshold.** `HighRiskPump@Turnaround2026`, defined by one turnaround's risk rule, can support local quantification through one C.3.2 declaration without becoming a public durable U-kind. No selected source mandates this exact FPF split. E.24.UK owns it as a governance decision: only repeated cross-pattern reliance that cannot be preserved by existing kinds, direct relations, and one bounded local declaration may proceed to positive durable admission.

Reopen this source basis when a cited edition changes, a stronger current source defeats one of these mutations, or a worked counterexample shows that the FPF branch returns the wrong individual, membership, dependence, inclusion, local-kind boundary, or non-parthood result.

