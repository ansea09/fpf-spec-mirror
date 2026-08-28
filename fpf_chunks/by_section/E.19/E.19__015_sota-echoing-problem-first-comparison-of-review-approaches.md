---
chunk_kind: "child"
pattern_id: "E.19"
pattern_title: "Pattern Quality Gates: Review and Refresh Profiles"
section_id: "E.19:11"
section_title: "SoTA-Echoing — problem-first comparison of review approaches"
source_path: "FPF-Spec.md"
output_path: "by_section/E.19/E.19__015_sota-echoing-problem-first-comparison-of-review-approaches.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "E.19 — Pattern Quality Gates: Review and Refresh Profiles"
  - "E.19:11 — SoTA-Echoing — problem-first comparison of review approaches"
line_start: 87218
line_end: 87235
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
  - "MUST NOT modify modeled-world entities such as Earth"
  - "a system-role kind"
  - "an assignment"
  - "inside the predicate)"
  - "or a holon"
  - "where a non-deontic Invariant: predicate is required)"
---

### E.19:11 - SoTA-Echoing — problem-first comparison of review approaches

**Working trade-off.** For one exact FPF pattern edition, detect semantic, ontological, practitioner-use, and source-currentness defects without making an ordinary review cost more than its likely harm warrants. No single current practice dominates that trade-off. Cheap tools and fixed checklists cover narrow repeatable properties; independent human review exposes contextual defects; practitioner studies test claimed transfer; living-guidance practice keeps volatile claims current. `E.19` therefore combines the non-dominated moves below—those for which no compared alternative improves one side without worsening the other—instead of importing one external workflow.

**Evidence binding.** If a current SoTA Synthesis Pack answers this exact review or refresh trade-off, cite it and keep this section consistent with it. Otherwise, the table below is the current source-use basis for this revision. Do not copy it into another seed list or treat a reference-only source as SoTA.

| Current approach and source | Coverage and effort | E.19 decision | Where this changes E.19 |
| --- | --- | --- | --- |
| **Proportionate independent assurance.** UK Government Analysis Function, *The AQuA Book* (2025). | Scales assurance by consequence, complexity, novelty, reuse, longevity, and uncertainty; separates the analyst, independent assurer, and approver. It catches fit-for-use and reasoning defects that template checks miss, but deeper independence costs more. | **Adopt and adapt.** Use those factors to select depth and retain an independent-findings form. Do not import government roles, approval stages, or mandatory assurance records into an ordinary FPF review. | The depth rule in §4; the two-form choice in §4.1; risk-selected profiles in §4.3; result and decision separation in §4.4. |
| **Lightweight change review with bounded automation.** Sadowski, Söderberg, Church, Sipko, and Bacchelli (2018), “Modern Code Review: A Case Study at Google”. | Empirical study of nine million code reviews supports small changes, quick iterations, human review, and tool assistance as an affordable engineering line. Its evidence is code-specific and does not establish pattern semantics or transdisciplinary transfer. | **Adapt, domain-bounded.** Keep one stable candidate, cheap mechanical checks, focused recheck, and a local-repair stop. Reject the code-review workflow and approval convention as FPF review semantics. | The local stop in §0.2; quick-pass automation in §4.2.1; stable-candidate and focused-recheck rules in §4.3.3. |
| **Practitioner-facing pattern validation.** Riehle, Harutyunyan, and Barcomb (2025), “Pattern Discovery and Validation Using Scientific Research Methods”; Iba (2021) remains bounded writing and critique guidance. | Qualitative surveys, action research, and case studies test recurring applicability and transfer more directly than template conformance or three examples alone, but they cost more than desk replay. | **Adopt selectively.** Escalate when universal or transfer claims remain uncertain or a missed failure has high consequence. Keep Iba for recognition, examples, consequences, and critique; do not treat critique culture alone as validation proof. | The three-situation recognition strip; §5 transfer slice; evidence escalation in §4.3.3; the breadth test in `CC-E19-7`. |
| **Living-guidance refresh.** Cheyne et al. (2023), “Methods for living guidelines: early guidance based on practical experience. Paper 1: Introduction”; PRISMA 2020 remains reporting lineage. | Prioritises questions for living mode, varies surveillance frequency, updates the smallest recommendation affected by new evidence, and permits transition out of living mode. PRISMA adds transparent reporting of what changed, but not a living-review architecture. The approach improves currency but carries sustained cost and comes from clinical guidance. | **Adapt, domain-bounded.** Reopen the smallest affected FPF pattern or subset on a material trigger and stop continuous surveillance when its expected gain no longer justifies the effort. Reject clinical governance, GRADE machinery, and PRISMA forms as universal FPF process. | `PCP-REFRESH`; the bounded review object in §4.1; the reopen and stop rules. |
| **Narrow structural, ontology-tool, and retrieval checks.** ISO/IEC/IEEE 42010:2022; Garijo, Corcho, and Poveda-Villalón (2021), “FOOPS!: An Ontology Pitfall Scanner for the FAIR Principles”; RAGAS and ARES (2023–2024). | Each supplies a repeatable check for a different narrow property: structured-description consistency, selected FAIR-ontology pitfalls, or retrieval context relevance, answer relevance, faithfulness, and context adequacy. None tests the whole E.19 problem, and their outputs are not comparable pattern-quality scores. | **Retain only for the named property.** Use ISO 42010 as a structure reference, FOOPS! only when a machine-readable ontology is actually under review, and RAGAS or ARES only for a selected retrieval fixture. Reject a clean tool result as admission, usability, ontology, or source-currentness proof. | `PCP-BASE` structure checks; quick-pass automation in §4.2.1; `PCP-ENTRY-E4`; the no-project-certificate boundary. |

**Selected current front.** Ordinary E.19 use combines a lightweight stable-candidate review with cheap bounded automation, then scales review depth by likely harm, novelty, reuse breadth, and source volatility. It preserves independent findings as a real review form, tests breadth with practitioner evidence only when the claim warrants it, and refreshes the smallest triggered unit. A universal exhaustive checklist costs more without reliably finding contextual defects; tool-only review costs less but misses semantics, practical use, and current-source decisions. Reopen this choice when another approach demonstrates equal or better detection of those four defect families at lower comparable effort.

Action result from the pattern-review and validation practice grounding: a favorable, cautionary, or return-for-repair E.19 result episteme, clean checklist, or clean retrieval-entry check does not become project certification, project evidence, safety/compliance assurance, gate input, release justification, work authority, publication truth, or project refusal/approval. Its EntityOfConcern is the exact reviewed FPF pattern edition or subset; its ClaimGraph states the review scope, applicable profiles, findings or aggregate cleared boundary, conclusion, non-use, and reopen condition. Review/repair/verification work, witnesses and evidence use, F.10 status use, B.3 assurance, publication/currentness, and any authority-bearing admission or refresh decision remain separate. Reopen the result when the reviewed text, accepted-source-material decision, SoTA grounding, a related pattern or concrete constraint it supplies, selected companion/projection function, profile trigger, review boundary, or attempted project-side reuse changes.

