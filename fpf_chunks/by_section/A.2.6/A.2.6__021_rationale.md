---
chunk_kind: "child"
pattern_id: "A.2.6"
pattern_title: "Unified Scope Mechanism (USM): Test Scope Membership and Combine Scopes"
section_id: "A.2.6:20"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.6/A.2.6__021_rationale.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.2.6 — Unified Scope Mechanism (USM): Test Scope Membership and Combine Scopes"
  - "A.2.6:20 — Rationale"
line_start: 7417
line_end: 7513
dependencies:
  - "A.1.1"
  - "A.15.1"
  - "A.2.2"
  - "A.22"
  - "A.6.0"
  - "A.6.1"
  - "A.7"
  - "C.2.1"
  - "C.2.2"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "E.24.UK"
  - "F.9"
keywords:
  - "alone"
---

### A.2.6:20 - Rationale

USM expresses the set-valued conditions under which a claim, qualified ability claim or publication may be used. Membership makes those conditions composable while preserving the F/G/R distinction. When local senses require translation, F.9 supplies the Bridge, C.2.1 the separate claim about this use, and A.10 or B.3 the applicable reliance basis; A.2.6 governs the scope calculation and membership question.

A stated domain condition and its calibration calculation can answer a standalone mathematical applicability question. For the adhesive, apply the calibration rule and compare the resulting interval with the supported range. When that result is used by an FPF rule requiring scope membership, identify the condition as the required scope value, identify the target slice and perform the guard. Capability gating uses `U.WorkScope` and the other conditions of §10.3; claim use follows its Claim-scope guard. Neither case requires an additional result record unless the receiving use needs one.

USM's additional result is an independently identified scope that further uses can compare, intersect across dependencies, combine across independently supported alternatives, or translate under declared rules. The API-and-dataset use in §11.4, for example, needs one common slice to satisfy both component scopes; a changed dataset edition changes that joint result. The domain argument supplies each applicability condition, the calibration or performance claim, and the justification for relying on it.

#### A.2.6:20.1 - SoTA-Echoing - Source distinctions and scope terminology

> **Intent.** This annex compares **USM** terms with usage in the sources below and explains the **Unified Tech** and **Plain** names used in A.2.6.

##### A.2.6:20.1.1 - Comparison basis

**Compared sources and the passages used here:**

1. [ISO's published scope for ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html), *Software, systems and enterprise — Architecture description*.
2. [OMG Essence 1.2](https://www.omg.org/spec/Essence/1.2/PDF), October 2018, §9.3.3.5–9.3.3.7 and §9.3.4.9–9.3.4.11.
3. [NIST AI 100-1, *AI RMF 1.0*](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), January 2023, §3.1 and §5.2/MAP.
4. [FDA, *Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions*](https://www.fda.gov/media/154985/download), final guidance, 17 November 2023, §IV and §VI.A, including definitions attributed there to ASME V&V 40–2018.
5. [W3C SHACL](https://www.w3.org/TR/2017/REC-shacl-20170720/), Recommendation, 20 July 2017, §2.1.2–2.1.3; [SHACL Advanced Features](https://www.w3.org/TR/2017/NOTE-shacl-af-20170608/), Working Group Note, 8 June 2017, §3.
6. W3C OWL 2 Second Editions, Recommendations, 11 December 2012: [*Direct Semantics*](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/), §2.2–2.2.3 and §2.3.2–2.3.3; [*Structural Specification and Functional-Style Syntax*](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/), §3.1–3.4.
7. IETF BCP 14: [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html), March 1997, as clarified by [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html), May 2017, §2.
8. [FAA AC 20-115D](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115D.pdf), 21 July 2017, §1, §4, §6, §8 and §10, describing use of RTCA DO-178C, DO-333 and DO-330 (13 December 2011).
9. ISO's published scope summaries for ISO 26262 [Part 1: Vocabulary](https://www.iso.org/standard/68383.html), [Part 3: Concept phase](https://www.iso.org/standard/68385.html) and [Part 9: ASIL-oriented and safety-oriented analyses](https://www.iso.org/standard/68391.html), second editions, December 2018.
10. IEC's [*Overview of IEC 61508 & Functional Safety*](https://assets.iec.ch/public/acos/IEC%2061508%20%26%20Functional%20Safety-2022.pdf), 2022, slides 9–18, alongside its [IEC 61508-1:2010 edition 2 description](https://webstore.iec.ch/en/publication/5515); HSE's older [*Control systems*](https://www.hse.gov.uk/comah/sragtech/techmeascontsyst.htm), “Proof testing”, for the effect of test intervals on a failure claim.
11. ACM Artifact Review and Badging v1.1 as applied in [SIGSIM PADS 2022](https://sigsim.acm.org/conf/pads/2022/blog/artifact-evaluation/) and [CCS 2025](https://sigsac.hosting.acm.org/ccs/CCS2025/call-for-artifacts/), “Evaluation Criteria and Badges” and “Packaging Artifacts”.
12. Google, [*Site Reliability Engineering*, Chapter 4: “Service Level Objectives”](https://sre.google/sre-book/service-level-objectives/), especially “Standardize Indicators” and “Defining Objectives”.

**Terms compared:** `U.ContextSlice`, generic **Scope** and set algebra, **Claim scope (G)**, **Work scope**, **Bridge plus a separate bounded-use claim and reliance basis**, **Γ\_time**, **widen**, **narrow**, **refit**, **translate**, **SpanUnion**, **serial intersection**, separation from **F** and **R**, and avoidance of overloaded **validity** and **operation** terms.

##### A.2.6:20.1.2 - Source term comparisons

|  # | Context / Source      | Local label(s) (native)                                                     | Closest USM concept                                                                      | Notes on fit & deltas                                                                                                                                                                         |
| -: | ------------------ | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | ISO/IEC/IEEE 42010:2022, published scope | *Architecture description; entity of interest; architecture viewpoints; model kinds* | **Context slice** and **Scope** for a selected applicability question | 42010 specifies the structure and expression of architecture descriptions. A claim recorded in such a description may have a USM scope; construct its slices and predicate from that claim's conditions. A viewpoint does not by itself identify those values. |
| 2 | OMG Essence 1.2 | *Alpha State; Work Product; LevelOfDetail; EntryCriterion; CompletionCriterion* | **D** for information detail; **ESG** for claim-use conditions in state transitions; **A.2.5** for assignment-state conditions used in **RSG**; **Scope** for applicability | Entry and completion criteria test an alpha state or work-product level of detail. Keep the information-detail aspect of LoD with D. Reuse a checklist condition in ESG or RSG only after identifying its claim-use or assignment-state meaning. Scope requires a separate condition delimiting applicable slices. |
| 3 | NIST AI RMF 1.0, §3.1 and §5.2/MAP | *Context of use; targeted application scope; validity, reliability, robustness; monitoring* | **Claim scope (G)** for specified applicability conditions; performance measures and reliance grounds remain distinct | MAP places application scope within purposes, settings, affected people and risks. Extract conditions for the claim's scope predicate; preserve performance/risk assessment and monitoring. Interpret validity-related claims by content, and keep the source's performance reliability distinct from FPF **R**. |
| 4 | FDA final guidance (2023), §IV and §VI.A; ASME V&V 40–2018 definitions reproduced there | *Context of use; model risk; credibility; verification and validation* | **Claim scope (G)** for extracted applicability conditions; **R** for justified reliance | The COU also states the model's role in answering a question and its use with other evidence. Preserve that decision relation when expressing applicability as a scope. Credibility is assessed for that use and its model risk; scope membership alone does not establish it. |
| 5 | W3C SHACL §2.1.2–2.1.3; SHACL-AF §3 | *Shapes; focus nodes; targets (`sh:targetClass`; AF `sh:target`); constraints* | Target selection provides an analogy for delimiting applicability; **F** concerns expression properties | SHACL targets produce RDF terms to validate; constraints determine their conformance. A USM scope contains declared `U.ContextSlice` values. Identify those slices and their membership predicate before using the analogy; target selection alone does not establish that a claim holds. C.2.3 assesses the actual expression properties. |
| 6 | OWL 2 Direct Semantics and Structural Specification, Second Editions | *Class extension; intersection/union; property domain/range; imports; version IRI* | Set extension as an analogy for scope algebra; ontology editions as selectors or interpretation inputs when applicable | Class extensions supply sets; property domain/range axioms imply membership of property-pair ends in specified classes or data ranges. Construct the corresponding USM slice domain independently. Imports supply ontology dependencies; version IRIs identify editions. An edition enters the slice when claim applicability depends on it; otherwise retain a required edition in the interpretation basis. |
|  7 | [IETF BCP 14: RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html) | *MUST/SHALL/SHOULD; requirements language* | Requirement strength in normative guard statements | BCP 14 defines the special meanings of its uppercase requirement keywords. The observable, deterministic membership conditions are USM requirements; they do not follow from those keywords alone. |
| 8 | FAA AC 20-115D on DO-178C, DO-333 and DO-330 | *Software level; formal-methods supplement; tool qualification level (TQL); life-cycle objectives and evidence* | **F** for actual expression and proof properties; **R** for justified reliance; scope kind follows the bounded claim or capability | The software level selects applicable objectives; the formal-methods supplement and tool qualification address distinct assurance work. A condition on a software or tool claim can delimit Claim scope, while a capability's operating conditions can delimit Work scope. Neither a level label nor a method name supplies the resulting FPF scope or assurance judgement. |
| 9 | ISO 26262:2018, published scope summaries | *Item definition; hazard analysis and risk assessment; functional safety concept; ASIL-oriented analyses* | **Claim scope** or **Work scope** for stated applicability conditions | An operating situation or mode can supply a selector when it changes applicability of the receiving claim or capability. Item definition and safety analysis also determine domain requirements. Preserve those requirements and their evidence; an ASIL label alone supplies neither a scope nor a measured value of FPF **R**. |
| 10 | IEC functional-safety overview; HSE control-systems explanation | *Safety function; SIL; demand/continuous mode; proof-test interval* | **Claim scope** or **Work scope** for stated operating conditions; performance requirements and reliance grounds remain distinct | SIL specifies safety-integrity requirements. A proof-test interval affects the basis of a failure-probability claim, so it cannot be reduced to evidence age. State which operating or maintenance condition bounds applicability and which support condition must hold before reliance. |
| 11 | ACM artifact badging, PADS 2022 and CCS 2025 | *Available; Evaluated—Functional/Reusable; Results Reproduced/Replicated* | Evidence relevant to **R**; **Context slice** when the evaluated environment is explicitly identified | The badges distinguish availability, artifact assessment and independent result checks. Use the actual badge criteria, checked claim and environment when assessing support; the badges do not form a single FPF warrant scale. An environment description supplies slice selectors only when their schema and values are made explicit. |
| 12 | Google SRE, “Service Level Objectives” | *SLIs; SLOs; measurement windows; workload classes; error budgets* | Performance **measures**; **Claim scope** or **Work scope** for stated service conditions | Keep metric definitions and aggregation windows with their measures. A workload class or region enters a scope when it changes applicability. In a USM rollout example, `gammaTime` enters scope only when crossing the declared start or end changes membership; an error-budget window alone does not establish that boundary. |

These comparisons suggest two useful questions: which conditions matter to the receiving use, and under which of them the claim or ability applies. A.2.6 answers them with independently identified slices and set-valued scopes. Choose Claim scope or Work scope from what is being bounded; the source term alone does not choose the scope kind. Preserve the source's decision relation, performance measures, safety requirements and evidence where the receiving use depends on them. Any relied-on translation follows §7.5.

##### A.2.6:20.1.3 - Scope names and their use

###### A.2.6:20.1.3.1 - Selected names (normative)

| Concept in A.2.6                | **Unified Tech** (lexicon)                      | **Unified Plain** (manager‑friendly) | Allowed short form   | Avoid / unpack                                                    |
| ------------------------------- | ----------------------------------------------- | ------------------------------------ | -------------------- | --------------------------------------------------------------------- |
| Addressable evaluation context  | **`U.ContextSlice`**                            | **Context slice**                    | *Slice* (when local) | “domain” (as guard input), “latest” time                              |
| Extensional scope value | **`U.Scope`**                                   | **Scope**                            | —                    | “applicability”, “envelope”, “validity” (as characteristic names)     |
| Episteme applicability          | **`U.ClaimScope`** (*nick **G**)               | **Claim scope**                      | **G**                | “generality”, “applicability/envelope (of claim)”                     |
| Capability applicability        | **`U.WorkScope`**                               | **Work scope**                       | —                    | “capability envelope”, “operational applicability”, “operation scope” |
| Time selector                   | **`Γ_time`**                                    | **Time selector**                    | —                    | implicit “latest”                                                     |
| Exact local-sense translation | **Obtaining F.9 Bridge + separate affirmative C.2.1 use claim + current A.10 or B.3 reliance** | **Bridge, translation rule and tolerance, checked reliance** | — | automatic Bridge use or treating a loss score as permission |
| Parallel coverage               | **SpanUnion**                                   | **Union of supported areas**         | —                    | unqualified “union” without independence                              |
| Serial dependency               | **Intersection**                                | **Intersection of scopes**           | —                    | ordinal “more/less general” language                                  |
| Scope edits                     | **ΔG+ (widen), ΔG− (narrow), Refit, Translate** | **Widen, narrow, refit, translate**  | —                    | stealth widening (“it’s obvious”)                                     |
| Optional didactics              | **`Detail (D)`, `AbstractionTier (AT)`**        | **Detail and abstraction tier**      | **D / AT**           | avoid as G substitutes                                                |

**Naming rationale:**

* **“Scope”.** This name designates the extension over independently identified slices; domain words such as “envelope” or “validity” require interpretation before that designation is warranted.
* **“Claim scope” vs “Work scope”.** These names distinguish claim uses and capability uses of the common set-valued scope notion.
* **G** names **Claim scope** in the F–G–R triple.
* **“Context slice”** keeps the evaluation target addressable through its exact declared selector schema and values; one membership predicate may inspect only a projection without reidentifying the slice.

###### A.2.6:20.1.3.2 - Wording membership and scope changes

* Use **“Claim scope (G) covers TargetSlice”** and **“Work scope covers JobSlice”** in guards.
* When time changes membership, name exact **`gammaTime`** and its membership boundary; never say “latest.” A time-independent predicate need not inspect `gammaTime`, but keep every selector already declared in the slice.
* To compose, say: **“intersection along dependency paths; SpanUnion across independent support lines.”**
* When exact local-sense translation is current, say: **“through an obtaining F.9 Bridge and a separate affirmative C.2.1 claim for this direction, rule, and tolerance; rely on it only through the current A.10 or B.3 branch, then evaluate membership on the returned scope.”**
* When widening/narrowing, write **“ΔG+ / ΔG−”** and log the support change; use **“Refit”** for unit/param normalization.

###### A.2.6:20.1.3.3 - Source-phrase comparison summary

Use these conditional paraphrases with the source distinctions in §20.1.2.

| Local source phrase | Use in USM wording |
| --- | --- |
| “Context of use” (NIST, FDA/ASME) | Extract a particular claim's applicability conditions into **G** on stated slices; preserve the wider decision context. |
| “Operating modes/situations” | May supply selectors for **Claim scope** or **Work scope**, according to what is bounded; retain performance and qualification conditions. |
| “Target” (SHACL) | Selects RDF terms for validation. Construct any corresponding slice domain and scope predicate separately. |
| “Class extension; property domain/range; imports/version” (OWL) | Class sets supply an analogy; property axioms, ontology dependencies and edition identity keep their own meanings. Construct the corresponding **Context slices** separately. |
| “Architecture view context” (42010) | Locate the claim and its conditions, then construct the relevant slice and scope; the view's organization does not determine them. |
| “Capability envelope” (safety documents) | **Work scope** when it delimits a capability's job slices, with performance and assurance requirements retained separately. |
| “Domain” (informal) | Unpack the intended conditions into declared selectors and a predicate before using them in a scope guard. |


