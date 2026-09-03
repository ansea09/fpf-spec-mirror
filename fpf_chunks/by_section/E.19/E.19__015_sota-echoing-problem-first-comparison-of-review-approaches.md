---
chunk_kind: "child"
pattern_id: "E.19"
pattern_title: "Pattern Quality Gates: Review and Refresh Profiles"
section_id: "E.19:11"
section_title: "SoTA-Echoing — problem-first comparison of review approaches"
source_path: "FPF-Spec.md"
output_path: "by_section/E.19/E.19__015_sota-echoing-problem-first-comparison-of-review-approaches.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "E.19 — Pattern Quality Gates: Review and Refresh Profiles"
  - "E.19:11 — SoTA-Echoing — problem-first comparison of review approaches"
line_start: 88572
line_end: 88589
dependencies:
  - "A.15.1"
  - "A.6.P"
  - "E.10"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
  - "(see H-8)"
  - "inside the predicate)"
  - "under E.8 H-8 and CC-SG.4"
  - "where a non-deontic Invariant: predicate is required)"
---

### E.19:11 - SoTA-Echoing — problem-first comparison of review approaches

**Working trade-off.** For one exact FPF pattern edition, detect semantic, ontological, practitioner-use, and source-currentness defects without making an ordinary review cost more than its likely harm warrants. **Design inference from the compared scopes:** combine narrowly targeted tools, human review of contextual defects, practitioner evidence for claimed transfer, and living-guidance methods for volatile claims. The source contributions and their limits are stated separately below.

**Evidence binding.** If a current SoTA Synthesis Pack answers this exact review or refresh trade-off, cite it and keep this section consistent with it. Otherwise, use the source contributions below for the named review question and decision; source identity alone does not establish the quality of that decision.

| Current approach and source | Coverage and effort | E.19 decision | Where this changes E.19 |
| --- | --- | --- | --- |
| **Proportionate independent assurance.** UK Government Analysis Function, [*The AQuA Book*](https://www.gov.uk/guidance/the-aqua-book) (2025). | Scales assurance by consequence, complexity, novelty, reuse, longevity, and uncertainty; separates the analyst, independent assurer, and approver. Its validation questions address fitness for use as well as specification compliance; the required effort varies with the selected assurance depth. | **Adopt and adapt.** Use those factors to select depth and retain an independent-findings form. Do not import government roles, approval stages, or mandatory assurance records into an ordinary FPF review. | The depth rule in §4; the two-form choice in §4.1; risk-selected profiles in §4.3; result and decision separation in §4.4. |
| **Lightweight change review with bounded automation.** Google's Engineering Practices, [Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html) and [Speed of Code Reviews](https://google.github.io/eng-practices/review/reviewer/speed.html); Sadowski et al. (2018), [Modern Code Review: A Case Study at Google](https://research.google/pubs/modern-code-review-a-case-study-at-google/), supplies bounded empirical evidence. | Current practitioner guidance favors self-contained reviewable changes and prompt feedback while preserving review quality. The study examines nine million reviewed code changes plus interviews and a survey. The evidence is code-specific; FPF's semantic replay remains a domain adaptation. | **Adapt, domain-bounded.** Keep one stable candidate, cheap mechanical checks, focused recheck, and a local-repair stop. Reject the code-review workflow and approval convention as FPF review semantics. | The local stop in §0.2; quick-pass automation in §4.2.1; stable-candidate and focused-recheck rules in §4.3.3. |
| **Practitioner-facing pattern validation.** Riehle, Harutyunyan, and Barcomb (2025), [Pattern Discovery and Validation Using Scientific Research Methods](https://doi.org/10.1007/978-3-662-70810-1_6), with the [authors' 2021 preprint](https://arxiv.org/abs/2107.06065) for the method; Iba (2021), [How to Write Patterns](https://hillside.net/plop/2021/plopourri/PLoP21_PLOPOURRI_Iba_Methodology4.pdf), supplies bounded writing and critique guidance. | Qualitative surveys, action research, and case studies provide methods for testing recurring applicability and transfer beyond the rule-of-three heuristic. Practitioner participation and observation add work beyond desk replay. | **Adopt selectively.** Escalate when universal or transfer claims remain uncertain or a missed failure has high consequence. Keep Iba for recognition, examples, consequences, and critique; do not treat critique culture alone as validation proof. | The recognition cases in §0.2 and their subject-specific transfer in §5; evidence escalation in §4.3.3; the breadth test in `CC-E19-7`. |
| **Living-guidance refresh.** Cheyne et al. (2023), [Methods for living guidelines: early guidance based on practical experience. Paper 1: Introduction](https://research-management.mq.edu.au/ws/portalfiles/portal/256300896/Publisher_version_open_access_.pdf). | Prioritises questions for living mode, varies surveillance frequency, updates the smallest recommendation affected by new evidence, and permits transition out of living mode. The approach improves currency but carries sustained cost and comes from clinical guidance. | **Adapt, domain-bounded.** Reopen the smallest affected FPF pattern or subset on a material trigger and stop continuous surveillance when its expected gain no longer justifies the effort. Keep the clinical governance and GRADE procedures outside the portable FPF method. | `PCP-REFRESH`; the bounded review object in §4.1; the reopen and stop rules. |
| **Narrow structural, ontology-tool, and retrieval checks.** [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html); Garijo, Corcho, and Poveda-Villalón (2021), [FOOPS!](https://ceur-ws.org/Vol-2980/paper321.pdf), with its [test catalogue](https://oeg-upm.github.io/fair_ontologies/doc/catalog.html); [RAGAS](https://aclweb.org/anthology/2024.eacl-demo.16.pdf) and [ARES](https://arxiv.org/abs/2311.09476) (2023–2024). | ISO 42010 supplies requirements for architecture-description structure and expression. FOOPS! tests selected FAIR-ontology properties. The retrieval evaluators distinguish context and answer relevance, faithfulness, and context adequacy. These are different properties and evidence relations; their outputs are not interchangeable pattern-quality scores. | **Retain only for the named property.** Use ISO 42010 as an architecture-description reference and FOOPS! only for an applicable machine-readable ontology. Select a retrieval evaluator against the required fixture properties; RAGAS/ARES illustrate that property split. A clean narrow check does not settle the remaining admission, usability, ontology, or source-currentness questions. | `PCP-BASE` structure checks; quick-pass automation in §4.2.1; `PCP-ENTRY-E4`; the no-project-certificate boundary. |

**Selected current front.** Ordinary E.19 use combines a lightweight stable-candidate review with cheap bounded automation, then scales review depth by likely harm, novelty, reuse breadth, and source volatility. It preserves independent findings as a real review form, tests breadth with practitioner evidence only when the claim warrants it, and refreshes the smallest triggered unit. The selected trade-off avoids running questions for absent risks while retaining human judgement of semantics, practical use, and current-source decisions. Practitioner studies and continued surveillance add effort only when the claimed breadth or currentness warrants it. Reopen this choice when another approach demonstrates equal or better detection of those four defect families at lower comparable effort.

When a receiving use requires a reusable E.19 result, it states the review claim for one exact FPF pattern edition or subset. Its EntityOfConcern, ClaimGraph, scope, applicable profiles, findings or aggregate cleared boundary, conclusion, and reopen condition state that pattern-quality claim. Any project-side reuse supplies its own governing relation, evidence or assurance, and decision under the relevant project rule. Review, repair, verification, result publication, admission or refresh decision, and project-side reuse remain separately recoverable. Reopen the affected result claim when a change to the reviewed text, accepted source, SoTA grounding, related pattern contribution, selected companion or projection function, profile trigger, review boundary, or claimed downstream use can change its conclusion or applicability.

