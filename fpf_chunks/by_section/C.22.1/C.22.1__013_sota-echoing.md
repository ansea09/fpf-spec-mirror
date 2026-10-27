---
chunk_kind: "child"
pattern_id: "C.22.1"
pattern_title: "Task-family adaptation signature"
section_id: "C.22.1:12"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.1/C.22.1__013_sota-echoing.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.22.1 — Task-family adaptation signature"
  - "C.22.1:12 — SoTA-Echoing"
line_start: 62335
line_end: 62357
dependencies:
  - "A.15"
  - "C.19.1"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "E.10"
  - "E.16"
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

**Claim 2.** A corridor-entry claim needs a baseline and evidence for the claimed difference.

C.17 separates novelty and diversity relative to a declared comparison basis; C.18 distinguishes generated candidates, retained archives and fronts. Here that distinction supplies a conditional question: when acquisition includes a claimed new corridor, which prior repertoire and observations establish it? The fields in §8 make that evidence recoverable without treating one unfamiliar sample as reproducible entry.

**Claim 3.** Selector and parity comparisons depend on compatible interpretations of the fields they consume.

G.5 and G.9 consume this shared field set. Their users must retain its threshold, prior-exposure and conditional reuse meanings when comparing candidates; a silent downstream redefinition would change the comparison basis.

**Evidence-source note.** Use each source result with its measured object and evaluation conditions. Factor admission and skill-edition selection concern different objects from a holder's acquisition of usable specialization. For `timeToThreshold` and `budgetToThreshold`, relate the acquisition evidence named in §11 to the declared threshold and prior exposure; faster evaluation or tokens per score-point gain alone cannot supply that history. Transfer, retention, and corridor-entry claims keep their separately stated evidence requirements.

| Source-bound anchor family | Source-use relation/currentness | What it disciplines in this pattern |
| --- | --- | --- |
| Novelty and search accounts | C.17 and C.18 provide the internal distinctions used above. | Corridor baseline, descriptor shift, stepping-stone evidence, and whether novelty is reproducible rather than one unfamiliar sample. |
| Agentic adaptation studies | FactorMiner v1 and SkillOpt v2: versioned preprints, used for the bounded comparisons above. | FactorMiner distinguishes factor quality, memory-guided yield, and evaluation cost; SkillOpt distinguishes text revision, validation, transfer, and training cost. The common acquisition field set is constructed in §§7–11. |
| Transfer / retention evaluation | The applying comparison must name its observations, task family and evaluation conditions. | Transfer target, retention window, downside and reuse evidence remain separate from first threshold attainment. |
