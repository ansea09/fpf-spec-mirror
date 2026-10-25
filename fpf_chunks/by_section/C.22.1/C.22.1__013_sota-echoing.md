---
chunk_kind: "child"
pattern_id: "C.22.1"
pattern_title: "Task-family adaptation signature"
section_id: "C.22.1:12"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.1/C.22.1__013_sota-echoing.md"
commit_sha: "ea8c54542bf017f36659167f36e816fad4de88cb"
heading_path:
  - "C.22.1 — Task-family adaptation signature"
  - "C.22.1:12 — SoTA-Echoing"
line_start: 63280
line_end: 63302
dependencies:
  - "A.15"
  - "C.19.1"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "E.10"
  - "E.16"
  - "E.19"
  - "E.22"
  - "E.23"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "adaptation signature"
  - "budget-to-threshold"
  - "corridor entry"
  - "downside field"
  - "prior exposure"
  - "retention"
  - "stepping stone"
  - "task-family specialization"
  - "time-to-threshold"
  - "transfer"
---

### C.22.1:12 - SoTA-Echoing

**Claim 1.** A comparison of specialization acquisition keeps the declared work-measure threshold and prior exposure explicit. It reports time and budget to threshold or states that the threshold was not reached.

**Practice source, local alignment, and adoption decision.** [FactorMiner v1 (2026-02-16)](https://arxiv.org/html/2602.14670v1), §§4.1–4.4, separates factor quality and redundancy, the effect of experience memory on screening yield, and factor-evaluation computation time. [SkillOpt v2 (2026-05-25)](https://arxiv.org/html/2605.23904v2), §§3.1, 3.4–3.5 and 4.3–4.4, changes an external skill text while holding the task-execution model fixed, selects text revisions through held-out validation, and evaluates transfer and training tokens per test-score gain. This pattern **adopts** these distinctions among the changed object, attained result, evaluation or training cost, and tested reuse.

**The shared field set is an original FPF construction.** For the question in §§1–6, §7 **adapts** those narrower comparisons by connecting the acquisition history to one `TaskFamilyRef` or `TaskSignature` and work-measure threshold. A terminal score and total cost per score gain can describe the attained result and average improvement cost, yet leave the resources needed to reach a particular threshold unresolved. Recording threshold timing and prior exposure adds observation effort but makes histories with the same final score distinguishable; §8 then separates claimed transfer, retention, and downside. The pattern **rejects** substituting either paper's reported metrics for this shared acquisition account. Reopen the comparison if a rival protocol supports the same specialization judgement with less observation, or exposes a consequential difference that these fields cannot express.

**Claim 2.** Current open-ended exploration work treats corridor entry and stepping stones as evidence-bearing novelty signals rather than decorative commentary.

**Practice source, local alignment, and adoption decision.** Current `QD`/`OEE` sources and current FPF `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` neighbours distinguish real corridor entry from one exotic sample by asking for explicit baseline, stable descriptor shift, reproducible solution class, or an explicit stepping-stone trace. This pattern **adopts** explicit corridor baseline/evidence discipline, **adapts** it as declared adaptation-signature fields, and **rejects** novelty talk that names no baseline, evidence source, or evidence locus.

**Claim 3.** Current selector and parity practice needs one stable shared field set for specialization claims.

**Practice source, local alignment, and adoption decision.** Current FPF selector and parity neighbours keep compared candidates reviewable only when candidates reuse the same published field set for threshold, prior exposure, transfer, retention, downside, and corridor-entry field. This pattern **adopts** that reuse discipline, **adapts** it by publishing one stable adaptation-signature field set here, and **rejects** silent downstream field redefinition in `G.5` or `G.9`.

**Evidence-source note.** Use each source result with its measured object and evaluation conditions. Factor admission and skill-edition selection concern different objects from a holder's acquisition of usable specialization. For `timeToThreshold` and `budgetToThreshold`, relate the acquisition evidence named in §11 to the declared threshold and prior exposure; faster evaluation or tokens per score-point gain alone cannot supply that history. Transfer, retention, and corridor-entry claims keep their separately stated evidence requirements.

| Source-bound anchor family | Source-use relation/currentness | What it disciplines in this pattern |
| --- | --- | --- |
| `QD` / `OEE` corridor-entry work | Current QD overview plus current FPF OEE/NQD neighbours. | Corridor baseline, descriptor shift, stepping-stone evidence, and whether novelty is reproducible rather than one exotic sample. |
| Agentic adaptation studies | FactorMiner v1 and SkillOpt v2: versioned preprints, used for the bounded comparisons above. | FactorMiner distinguishes factor quality, memory-guided yield, and evaluation cost; SkillOpt distinguishes text revision, validation, transfer, and training cost. The common acquisition field set is constructed in §§7–11. |
| Transfer / retention evaluation | Source-use relation/currentness supplied by the applying benchmark or neighbour pattern. | Transfer target, retention window, downside, and reuse evidence so specialization speed is not confused with one isolated threshold crossing. |
