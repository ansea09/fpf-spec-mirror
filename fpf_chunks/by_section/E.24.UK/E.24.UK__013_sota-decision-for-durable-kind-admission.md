---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:11"
section_title: "SoTA Decision for Durable Kind Admission"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__013_sota-decision-for-durable-kind-admission.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:11 — SoTA Decision for Durable Kind Admission"
line_start: 92641
line_end: 92658
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.2.6"
  - "A.22"
  - "A.6.0"
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
  - "F.17"
  - "F.18"
  - "F.8"
  - "U.Kind"
  - "U.SubkindOf"
keywords:
---

### E.24.UK:11 - SoTA Decision for Durable Kind Admission

The bounded question is practical: **when should a reusable distinction become a durable public kind, when is a local classifier or direct relation enough, and what identity commitment does each choice add?** Compare alternatives at the effort of repairing or authoring one FPF pattern—not at the effort of adopting a whole enterprise ontology.

| Current line | Strong contribution | Failure mode or extra effort for this question | FPF decision and receiving locus |
| --- | --- | --- | --- |
| [gUFO, 2026](https://arxiv.org/abs/2603.20948), with its current type typology, intrinsic and relational aspects, situations, and higher-order types; standardization is still at ISO/IEC CD 21838-5 | Rich distinctions expose whether one bearer gains a classification or a distinct dependent individual needs grounding. | Using the whole typology first adds a foundational-ontology mapping and can choose an imported category before the FPF receiving use and local alternative are known. | **Adapt** the same-individual/distinct-individual question in the admission tree and the WorkPlan, capability, role, phase, and quality cases. **Reject** automatic import of the taxonomy or its labels as FPF admission. |
| Current [BFO 2020 artifacts](https://github.com/BFO-ontology/BFO-2020), maintained for the ISO 21838 top-level-ontology line | Strong formal separation of dependence, continuant mereology, process, role, and disposition. | Adopting the whole upper ontology is expensive for a bounded FPF authoring decision, and its categories do not decide whether one FPF name deserves durable public reliance. | **Adopt** the warning that dependence is not parthood and require an exact dependence rule for the capability case. **Reject** BFO classification or official status as the admission gate. |
| Modular ontology-design-pattern work, including [MODL](https://arxiv.org/abs/1904.05405), and the emerging [LLM-assisted ontology-engineering direction](https://arxiv.org/abs/2411.09601) | Reusable small modules reduce duplicated modeling; the newer direction makes modularity important when assisted changes become cheap and frequent. | Pattern discovery and adaptation still cost work. The LLM paper states a research direction, not evidence that this pattern's eight conditions or result architecture is best. | **Adopt** existing-governor reuse and bounded modules in steps 2–4. Treat LLM assistance as a reopen pressure only, never as the load-bearing admission basis. |
| Current operational [OBO Foundry principles](https://obofoundry.org/principles/fp-000-summary.html) | Scope, versioning, textual definition, reuse, identifiers, and operational conformance make shared ontologies maintainable. | These governance and publication checks do not by themselves settle world-side kind identity, membership, dependence, or the difference between a local classifier and durable FPF kind. | **Adapt** explicit scope, reuse, version, and reopen boundaries in the decision and registry. **Reject** conformance to a publication regime as proof of admission. |
| [OWL 2 semantics](https://www.w3.org/TR/owl2-direct-semantics/) and [ISO 704:2022](https://www.iso.org/standard/79077.html) | OWL cleanly separates classes, individuals, properties, and semantics-free labels; ISO 704 separates objects, concepts, definitions, and designations. | These are mature lineage baselines, not a current low-effort method for deciding FPF's durable/local/non-kind boundary or its identity dependence. | **Adopt** class/individual/property separation, same-individual inclusion, and naming-after-object recovery. **Reject** a class axiom, label, definition, or designation as sufficient admission. |

**Selected non-dominated contribution.** None of these lines supplies the same progressive cost boundary. E.24.UK first reuses an accepted kind, then tries one bounded C.3 classification, then recovers a direct relation or other non-kind object, and only then admits a new durable kind for repeated cross-pattern reliance with an exact membership or dependence rule. At comparable authoring effort, this reduces ontology commitment while preserving exact identity, non-member, reliance, and reopen tests. The gain is not universal superiority over a foundational ontology; it is a better effort/traceability trade for FPF pattern repair.

The shared E.24 decision is part of that gain. It prevents the ontic and public-kind questions from being answered by two incompatible cards. In the `U.Kind` and `U.SubkindOf` cases, one atomic decision returns two sibling results. In the capability case, the missing dependence rule stops only that admission. In the WorkPlan case, the same episteme gains dependent membership without a second plan. A role or phase near-miss stays with a direct relation or local kind; `HighRiskPump@Turnaround2026` stays a local C.3 distinction; and public spelling waits for F.18 after the object is settled. A source may model a pressure quality or an obligation-bearing relation as a separate dependent individual. FPF does so only when a direct rule identifies that individual and its exact dependence. A measurement value, assertion, participant pair, agreement document, or relation record cannot admit it by representation alone.

The main remaining failure risks are also explicit. The progressive route can under-admit a distinction if a bounded use hides later cross-pattern reliance, or over-admit it if repeated wording is mistaken for stable membership. Reopen when a stronger current alternative offers the same identity assurance at lower effort, when an admitted kind loses its member/non-member or continuity test, or when a worked counterexample changes the same-individual, identity-dependent, local-kind, or non-kind decision.

