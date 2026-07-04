---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:8"
section_title: "Common anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__009_common-anti-patterns-and-repairs.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:8 — Common anti-patterns and repairs"
line_start: 67512
line_end: 67525
dependencies:
  - "A.19.ECS"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
  - "F.19"
keywords:
---

### E.9.DA:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **Heading-complete DRR.** Headings exist but authors cannot tell what to write. | Lower selected-answer, selected-locus, and drafting-action coordinates. |
| **Source packet in DRR clothing.** Sources are preserved but FPF decisions are absent. | State selected payload, rejected payload, and selected-locus obligations. |
| **Address completion without architecture.** Every locus is named but the split or merge is wrong. | Repair `FPFContentArchitectureSelectionAdequacy`. |
| **Watch item as decision.** Drafting is expected to choose the answer during pattern authoring. | Select, repair, split, or hold. |
| **Ontic candidate left to drafting.** A `DRR` uses uncertain candidate phrasing for a concept cluster or pattern set but leaves candidate sufficiency, rejected alternatives, publication boundary, and placement for the pattern author. | Close `DRROnticCandidateDisposition` now: select, reject, split, or decline the candidate by value; state the direct governing pattern when no new ontic is warranted. |
| **Review-state proxy.** Review acceptance or landing is treated as adequacy. | Use decision-content evidence only. |
| **Adequacy table without evidence loci.** Values are listed without by-value `DRR` or source loci. | Re-run the evaluation with `Coordinate | Value | ShortRationale | EvidenceLocus`; lower any coordinate whose evidence cannot be named. |
| **Apparatus-overwrapped drafting payload.** The `DRR` offers selected-pattern wording wrapped in role, publication-form, locus, flow, state, status, text, package, or process apparatus without changing a recoverable kind, relation, claim kind, admissible use, evidence value, selected locus, user-facing action, or flow role. | Classify the wording under `F.19`. If it changes a kind or claim, repair through precision restoration; if not, remove it from the future pattern payload or rewrite it as the positive subject-kind and action spine. |
| **Goodharted DRR adequacy.** A `DRR` is made easier to defend as `4` or `5` by adding source rows, selected-locus tables, boundary catalogues, or review proof, while selected answer, selected-locus obligations, source payload mutation, architecture choice, or first drafting action do not improve. | Reject apparatus-only improvement; apply `E.13` when adequacy values or review marks are replacing decision usefulness; repair the decision content, delete or relocate proof material, and record checked no-proposal only when no non-dominated decision-content improvement remains. |

