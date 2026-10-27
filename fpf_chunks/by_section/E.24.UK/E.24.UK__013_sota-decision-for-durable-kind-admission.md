---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:11"
section_title: "SoTA Decision for Durable Kind Admission"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__013_sota-decision-for-durable-kind-admission.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:11 — SoTA Decision for Durable Kind Admission"
line_start: 115699
line_end: 115716
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
| [gUFO, March 2026](https://arxiv.org/html/2603.20948v1), an OWL implementation of UFO; [ISO/IEC PRF 21838-5](https://www.iso.org/standard/89915.html) concerns UFO and remains under development | Role and phase classifications can change while their bearers retain identity. The source also distinguishes qualities represented by properties from dependent individuals and permits minimal use with optional richer patterns. | The minimal route is a relevant alternative for a bounded modeling task. Its types still need mapping to the receiving FPF use; gUFO `Kind` is a specific metatype, not the whole FPF `U.Kind` category. | **Adapt** the same-individual/distinct-individual question and choose only the distinctions the use needs. Classify under C.3.2 when sufficient; test public admission separately. |
| Current [BFO 2020 artifacts](https://github.com/BFO-ontology/BFO-2020), maintained for the ISO 21838 top-level-ontology line | Formal separation of specific dependence, continuant parthood, process, role, and disposition. A BFO role is a dependent realizable individual; gUFO Role concerns a classification of bearers. | The existing relations can clarify a dependence claim. Selecting a durable FPF kind still requires its receiving use and admission grounds; the source establishes no comparative cost for that choice. | **Adopt** the separation of dependence and parthood and require an exact dependence rule when a distinct dependent individual is needed. Map each source meaning separately; BFO classification or official status supplies no FPF admission result. |
| Modular ontology-design-pattern work, including [MODL (2019)](https://arxiv.org/abs/1904.05405), and [LLM-assisted ontology engineering (2024)](https://arxiv.org/html/2411.09601v1) | Reusable, adaptable modules organize modeling. The LLM study explores task-relevant conceptual modules through bounded prompting experience and open research questions. | Pattern discovery and adaptation still cost work. The LLM paper establishes neither generally cheap, frequent ontology changes nor the superiority of these eight admission conditions. | **Adopt** existing-governor reuse and bounded modules in steps 2–4. Treat any future reduction in assisted-change cost as a reason to reconsider admission effort; this is an FPF forecast. |
| Current operational [OBO Foundry principles](https://obofoundry.org/principles/fp-000-summary.html) | Scope, versioning, membership-informing textual definitions, semantic relation reuse, identifiers, and term stability make shared ontologies maintainable. Term stability preserves meaning under an identifier while allowing newly recognized instances. | These principles contribute semantic as well as publication discipline. The choice between a local classifier and a durable FPF kind still needs the receiving use and the eight admission conditions. | **Adapt** scope, semantic reuse, version, and reopen boundaries in the decision and registry. Preserve the distinction between stable meaning and the members recognized under it. |
| [OWL 2 semantics](https://www.w3.org/TR/owl2-direct-semantics/) and [ISO 704:2022](https://www.iso.org/standard/79077.html) | OWL distinguishes class, individual, and property interpretations and permits classes defined by relation participation. Annotations, including labels, do not affect its Direct Semantics. ISO 704 distinguishes objects, concepts, definitions, and designations in terminology work. | These mature lineage baselines supply distinctions, not FPF's durable/local admission procedure. OWL labels retain human or application meaning; ISO 704 does not govern world-side admission. | **Adopt** the interpretation distinctions and same-individual inclusion. **Adapt** concept analysis before a final designation to FPF object recovery; ISO also permits starting the inquiry from existing designations. Apply the FPF admission tests before public naming. |

**Contribution to the FPF admission decision.** E.24.UK first tests reuse of an accepted kind and bounded C.3 classification, and recovers a direct relation or other non-kind object when no classification result is needed for the receiving use. A new durable kind requires repeated cross-pattern reliance and an exact membership or dependence rule. Where the simpler result already preserves the needed distinction, it avoids another ontology commitment while retaining identity, non-member, reliance, and reopen tests.

The shared E.24 decision is part of that gain. It prevents the ontic and public-kind questions from being answered by two incompatible cards. The U.Kind case retains the independent root admission and returns direct rule use without an additional durable ontic; the separate U.SubkindOf settlement remains under its own direct relation and receiving-use grounds. In the capability case, recovery returns qualified holder-ability claims and rejects an unnecessary additional kind. In the WorkPlan case, the same episteme gains dependent membership without a second plan. A role or phase near-miss stays with a direct relation or local kind; `HighRiskPump@Turnaround2026` stays a local C.3 distinction; and public spelling waits for F.18 after the object is settled. A source may model a pressure quality or an obligation-bearing relation as a separate dependent individual. FPF does so only when a direct rule identifies that individual and its exact dependence. A measurement value, assertion, participant pair, agreement document, or relation record cannot admit it by representation alone.

The main remaining failure risks are also explicit. The progressive route can under-admit a distinction if a bounded use hides later cross-pattern reliance, or over-admit it if repeated wording is mistaken for stable membership. Reopen when a stronger current alternative offers the same identity assurance at lower effort, when an admitted kind loses its member/non-member or continuity test, or when a worked counterexample changes the same-individual, identity-dependent, local-kind, or non-kind decision.

