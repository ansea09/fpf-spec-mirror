---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:5"
section_title: "Archetypal grounding (worked, didactic)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__006_archetypal-grounding-worked-didactic.md"
commit_sha: "d514a6fcb7908af8e773ed054b9582394f755caf"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:5 — Archetypal grounding (worked, didactic)"
line_start: 37128
line_end: 37163
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.PROD"
  - "A.6.1"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.11"
  - "C.19.2"
  - "C.2"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
  - "F.9"
  - "U.Work"
keywords:
  - "KD-CAL"
  - "epistemic"
  - "knowledge aggregation"
  - "provenance"
  - "trust"
---

### B.1.3:5 - Archetypal grounding (worked, didactic)

#### B.1.3:5.1 - Episteme — **Heterogeneous evidence into a guidance statement**

This is a didactic evidence-composition case, not a clinical recommendation. The receiving question concerns a treatment's pain outcome for an identified acute low-back-pain population within six weeks. The exact population and outcome, not a label or taxonomy operation, identify the subject.

* **Inputs:** `E₁` is a randomized trial, `E₂` an observational study, and `E₃` a mechanistic model. Retain their designs, findings, uncertainty, assumptions, and scope. A bare “R=0.84/0.55/0.60” list has no declared common quantity here and cannot support a numerical aggregate. Likewise, “medium/wide/narrow” is not a substitute for actual ClaimScope.
* **Synthesis:** retain protocols, datasets, analysis scripts, and other participating carriers in the SCR. Establish any dosage or outcome mapping from its actual measurement basis; units named mg and IU do not themselves establish a conversion. Keep chronic cohorts and different outcomes separate unless a warranted transport relation supports the receiving claim.
* **Necessary-premise case:** if the proposed inference requires an outcome mapping that is unsupported, withhold that mapped inference. Retain the trial's narrower source-scale conclusion rather than discard every source.
* **Complementary case:** a limited `E₂` may help assess a confounding explanation left open by `E₁`; `E₃` may constrain a mechanism without establishing the clinical effect size. Explain those contributions and their limits. The minimum of three unexplained scores neither captures them nor defeats the existing trial conclusion.
* **Dependence case:** if two reports reuse a cohort or share an outcome-measurement bias, do not count them as two independent confirmations. Different designs alone are insufficient to establish different biases.
* **Contrary-result case:** a credible `E₂` result conflicts with `E₁` in an overlapping subgroup. Keep the disagreement. Different baseline severity is a possible explanation only to the extent supported by the sources. Narrow or qualify the guidance claim; do not silently average the conflict away or call it an uninformative study.
* **Completion:** return the bounded guidance statement with its distinct supporting contributions, contrary result, scope, and unresolved interpretation. No common quantitative model has been supplied, so no aggregate R is returned. Whether another study is feasible and worth its total burden is a separate C.11/C.19.2 decision, not a condition for completing this synthesis.

For **Γ_epist^compile**, map the retained claims into the journal's scheme, carry the same limitations and any justified recalculation, and produce the compilation SCR and required hashes. C.2.1 identifies the target-scheme episteme “Guidance Statement v1.0”; later journal publication remains a separate occurrence.

#### B.1.3:5.2 - Episteme — **Controller proof and a real protective function**

* **Inputs:** a requirement specification, hazard analysis, test logs, and a proof of controller property P under assumptions A. Preserve each source's actual formal basis and support. No common R scale follows from four labels or formality levels.
* **Formal receiving question:** “Does A entail P in the stated model?” Retain the valid proof and its assumptions as the useful result. An empirical study is not needed to turn that result into an invented empirical R; F describes checkability, not the probability that the actual controller is safe.
* **World-facing receiving question:** “Does the installed controller deliver the protective function in these operating conditions?” Expose the reliance on A, the implementation/model correspondence, and the actual operating scope. If A is unsupported for this use, the proof alone does not establish the world-facing claim. If logs show an edge case violating A, retain that counterevidence and withhold the stronger assurance while preserving the theorem A ⇒ P.
* **Threshold case:** a receiving acceptance clause requires a justified probability of at least 0.95 for the real protective function. Substituting a high F or its rescaled value cannot meet it. A declared ordinal checkability comparison remains usable as an ordinal comparison. A numerical acceptance result requires the model and evidence that warrant that particular probability; otherwise return the narrower formal conclusion and the unresolved actual-system assurance.
* **Positive quantitative case:** if a receiving model actually establishes two necessary independent conditions, each with probability 0.9, their conjunction is 0.81. A 0.85 threshold is not met by replacing 0.81 with min(0.9, 0.9). If independence is unavailable, the joint probability needs the actual conditional model or remains unresolved; the formal proof is unchanged.

For **Γ_epist^compile**, map the retained claims to the certification scheme. Where local meanings differ, identify exact source and receiving `SchemeSenseCell` values, test the F.9 Bridge, state the bounded certification use and permitted loss, and establish relied-on use separately. C.2.1 identifies the resulting episteme. Certification, authorization, a publication occurrence, and actual system protection remain separate claims.

#### B.1.3:5.3 - Contrast (didactic)

| Aspect          | **Γ\_epist (Knowledge)**                                         | **Γ\_sys (Physical)**                       |
| --------------- | ---------------------------------------------------------------- | -------------------------------------------- |
| What is folded? | Claims, models, datasets, arguments                              | Components, materials, assemblies            |
| Conservatism | Support roles, dependence, and mapping limits under the named B.3 model; no invented aggregate | WLNK for a quantity whose physical model justifies a weakest-part bound |
| Fit             | **Mappings** with declared **CL**                                | **Interfaces/BIC** compatibility             |
| Order/time | Optional **Γ\_ctx** for argument order; C.2.1 for distinct episteme identities and edition relations; A.14 for a proper restriction of one unchanged episteme; B.1.4/**Γ\_time** for bounded aggregation of recovered temporal relations | Γ\_ctx for workflows; Γ\_time for phases of directly governed enduring carriers |
| Work/cost       | External in **Γ\_work** (compute, curation)                      | External in **Γ\_work** (energy, labour)     |

