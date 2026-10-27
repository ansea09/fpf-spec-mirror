---
chunk_kind: "child"
pattern_id: "A.2.6"
pattern_title: "Unified Scope Mechanism (USM): Test Scope Membership and Combine Scopes"
section_id: "A.2.6:20"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.6/A.2.6__021_rationale.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "A.2.6 — Unified Scope Mechanism (USM): Test Scope Membership and Combine Scopes"
  - "A.2.6:20 — Rationale"
line_start: 7366
line_end: 7455
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
  - "& guard style)"
  - "alone"
---

### A.2.6:20 - Rationale

USM expresses the set-valued conditions under which a claim, qualified ability claim or publication may be used. Membership makes those conditions composable while preserving the F/G/R distinction. When local senses require translation, F.9 supplies the Bridge, C.2.1 the separate claim about this use, and A.10 or B.3 the applicable reliance basis; A.2.6 governs the scope calculation and membership question.

#### A.2.6:20.1 - SoTA-Echoing - Source distinctions and scope terminology

> **Intent.** This annex compares **USM** terms with usage in the sources below and explains the **Unified Tech** and **Plain** names used in A.2.6.

##### A.2.6:20.1.1 - Comparison basis

**Compared sources:**

1. **ISO/IEC/IEEE 42010** (architecture description)
2. **OMG Essence** (Kernel: Alphas, Work Products, States)
3. **NIST AI RMF 1.0/1.1** (trustworthy AI)
4. **ASME V\&V 40–2018 / FDA 2021–2023** (model credibility)
5. **W3C SHACL (2017+) / SHACL‑AF** (data constraints)
6. **OWL 2 / ontology engineering (2012+, current practice)**
7. **IETF BCP 14 (RFC 2119/8174)** (normative keywords & guard style)
8. **DO‑178C + DO‑333** (avionics, formal methods supplement)
9. **ISO 26262:2018/2025** (automotive functional safety)
10. **IEC 61508 (2010+, current revisions)** (basic safety)
11. **ACM Artifact Review & Badging v1.1** (reproducibility signals)
12. **MLOps/Cloud SLO practice (SRE / platform)** (operational guardrails)

**Terms compared:** `U.ContextSlice`, generic **Scope** and set algebra, **Claim scope (G)**, **Work scope**, **Bridge plus a separate bounded-use claim and reliance basis**, **Γ\_time**, **widen**, **narrow**, **refit**, **translate**, **SpanUnion**, **serial intersection**, separation from **F** and **R**, and avoidance of overloaded **validity** and **operation** terms.

##### A.2.6:20.1.2 - Source term comparisons

|  # | Context / Source      | Local label(s) (native)                                                     | Closest USM concept                                                                      | Notes on fit & deltas                                                                                                                                                                         |
| -: | ------------------ | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  1 | ISO/IEC/IEEE 42010 | *Architecture context; environment; stakeholder concerns; viewpoints and views* | **ContextSlice** (addressable slice); **Scope** as view‑specific applicability           | 42010 is about **views in context**; it has no first‑class set‑valued scope char but aligns with “evaluate **in a concrete context**” → USM uses explicit **slice tuples**.                   |
|  2 | OMG Essence        | *Alpha State; Work Product State; Level of Detail (LoD)*                    | **Work scope** (guards), **Detail (D)** (LoD), **ESG/RSG**                               | Essence separates **status** (states) and **work evidence**; LoD is **detail**, not scope. USM treats **scope** as guardable membership over slices; states/LoD map to ESG & **D**, not to G. |
|  3 | NIST AI RMF | *Context of use; validity, reliability, robustness; monitoring* | **Claim scope (G)** for declared use conditions; **R** for the relevant support | USM separates the conditions under which a claim holds from the evidence supporting reliance. The source term “validity” requires interpretation rather than a name-based assignment to either scope or assurance. |
|  4 | ASME V\&V 40 / FDA | *Context of use; credibility factors; verification/validation*              | **Claim scope (G)**; **R** (credibility)                                                 | Direct fit for G via “context of use”. Credibility/evidence freshness contribute to **R**, not to G; USM keeps them separate in guards.                                                       |
|  5 | [W3C SHACL §2.1.3](https://www.w3.org/TR/shacl/#targets) | *Shapes; targets (sh\:targetClass, sh\:target); constraints* | Target selection provides an analogy for delimiting applicability; **F** concerns expression properties | SHACL targets select nodes to validate. A USM scope instead contains declared `U.ContextSlice` values; those slices and their membership predicate must be identified before using the analogy. C.2.3 assesses the actual expression properties. |
|  6 | [OWL 2 Direct Semantics §2.2](https://www.w3.org/TR/owl2-direct-semantics/#Interpretations) | *Class extension; domain/range; imports/version IRI* | Set extension provides an analogy for scope algebra | An ontology class has its own member domain. A.2.6 uses independently identified `U.ContextSlice` values as members; class membership does not by itself supply that slice construction. |
|  7 | [IETF BCP 14: RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html) | *MUST/SHALL/SHOULD; requirements language* | Requirement strength in normative guard statements | BCP 14 defines the special meanings of its uppercase requirement keywords. The observable, deterministic membership conditions are USM requirements; they do not follow from those keywords alone. |
|  8 | DO‑178C / DO‑333   | *Operational conditions; DAL; formal method objectives; TQL*                | **Work scope** (operating conditions); **F** (expressed formal properties and derivations), **R** (assurance objectives) | Operational applicability = **Work scope**; formal method objectives select needed expression properties; Tool qualification impacts **TA/R**, not G.                                                                  |
|  9 | ISO 26262          | *Operational situation & operating modes; ASIL; OSED*                       | **Work scope** (operating modes/situations)                                              | OSED/operating modes define **where capability can be exercised** → **Work scope**. Assurance level (ASIL) relates to **R**, not G.                                                           |
| 10 | IEC 61508          | *SIL; demand mode; proof test interval*                                     | **Work scope** (demand vs continuous mode) + **R freshness**                             | Mode concepts influence **where/how** a function can be claimed → **Work scope**; proof test interval sits in **R** (freshness/decay).                                                        |
| 11 | ACM Artifacts      | *Available/Evaluated/Reusable; Reproduced/Replicated*                       | **R** signals; **ContextSlice** (reproduction environment)                               | Badges encode **evidence availability and warrant level**; the declared environment maps to a **slice**; scope of claim is often implicit → USM makes it explicit.                                     |
| 12 | SRE / Cloud SLO    | *SLOs; error budgets; regions/tiers; rollout windows*                       | **Work scope** (regions/tiers) + **measures**; `gammaTime` only for a membership-changing rollout interval | SLO measures and error-budget windows stay in their measure or reliance guards. A rollout interval enters Work scope only when crossing its exact start or end changes whether that job slice belongs. |

These comparisons suggest two useful questions: which concrete conditions are being considered, and under which of them the claim or ability holds. A.2.6 answers them with independently identified slices and set-valued scopes. A source's operating mode, shape target, class extension or view context retains its own meaning; the table supplies an analogy for scope work, not an identity between those constructs. Any relied-on translation follows §7.5.

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

| local context phrase                          | Use in USM wording                                          |
| ------------------------------------------ | ----------------------------------------------------------- |
| “Context of use” (NIST, ASME/FDA)          | **Claim scope (G)** on explicit **Context slice**           |
| “Operating modes/situations” (ISO 26262)   | **Work scope** with measures & qualification windows             |
| “Target (class/shape)” (SHACL/OWL)         | **Claim scope predicates** (membership)                     |
| “Architecture view context” (42010)        | **Context slice** + **Scope** checks inside the view        |
| “Capability envelope” (safety documents) | **Work scope**                                              |
| “Domain” (informal)                        | **Context slice** elements; not acceptable as a guard input |


