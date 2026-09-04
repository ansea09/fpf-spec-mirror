---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:8"
section_title: "Common anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__009_common-anti-patterns-and-repairs.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:8 — Common anti-patterns and repairs"
line_start: 74785
line_end: 74805
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
| **Specification or record as evaluator.** A filled coordinate table, published record, or E.9.DA pattern is said to have assessed the DRR, issued assurance, accepted it, or authorized drafting. | Name the actual evaluator `U.System`; do not replace it with an evaluator-role label. Leave an ordinary review outside Work admission. Add Method, application, or Work identity only when the receiving claim uses it. If dated `U.Work` is asserted, use the complete branch in 4.2. An optional local system-role classification is a separate claim. |
| **Conditional branch collapsed into Work.** A reusable result is said to require assessment Work, or a Method or A.6.1 application is described as Work merely because all three can occur in one stronger case. | Keep Method, application, and Work independently conditional. The Work branch requires the Method and application used here, every precise performer's A.13 core, and independent A.15.1 admission. Add F.6 only when precise assignment-bound attribution is also current. Method or application alone implies no Work, and an application is related to Work only through a separately defined obtaining relation. |
| **Heading-complete DRR.** Headings exist but authors cannot tell what to write. | Return the missing selected answer, selected-locus obligation, and first drafting action for repair; in a complete reusable evaluation, lower the corresponding coordinates. |
| **Question-complete around the wrong frame.** Every named question is answered, but the DRR omitted a question that changes the answer, architecture, source use, consumer obligation, first action, or stop. | Run the one bounded content-first omitted-question search before coordinate closure. Return the question as a finding and lower the coordinates whose claims it changes; do not narrow the frame to preserve the values. |
| **Source packet in DRR clothing.** Sources are preserved but FPF decisions are absent. | State selected payload, rejected payload, and selected-locus obligations. |
| **Address completion without architecture.** Every locus is named but the split or merge is wrong. | Repair `FPFContentArchitectureSelectionAdequacy`. |
| **Watch item as decision.** Drafting is expected to choose the answer during pattern authoring. | Select, repair, split, or hold. |
| **Ontic candidate left to drafting.** A `DRR` uses uncertain candidate phrasing for a concept cluster or pattern set but leaves candidate sufficiency, rejected alternatives, publication boundary, and placement for the pattern author. | Close `DRROnticCandidateDisposition` now: select, reject, split, or decline the candidate by value; when no new ontic is warranted, name the existing concrete pattern, relation, or bounded local account that carries the actual contribution. |
| **Review-state proxy.** Review acceptance or landing is treated as adequacy. | Use decision-content evidence only. |
| **Floor or scope laundering.** After seeing weak values, the evaluator chooses an easier use, lower floor, smaller selected-locus set, or shorter window and reports an admissible result. | Recover the required use and floor source before judging evidence. Return `newFrameRequired`, repair, split, or hold for the original request; a different frame is another evaluation, not a pass. |
| **Adequacy table without evidence loci.** Values are listed without by-value `DRR` or source loci. | Re-run the evaluation with `Coordinate | Value | ShortRationale | EvidenceLocus`; lower any coordinate whose evidence cannot be named. |
| **Apparatus-overwrapped drafting payload.** The DRR offers selected-pattern wording wrapped in role, publication-form, locus, flow, state, status, text, package, or process apparatus without changing a recoverable kind, relation, claim, admissible use, selected locus, user-facing action, or flow role. | Apply `F.19`. If a kind or claim changes, repair it through the concrete defining or constraining pattern; otherwise remove the apparatus and restore the positive subject and first action. |
| **Proxy replay for a broad rule.** A schema, invented fact pack, lane test, or promise inside the DRR is used as evidence for language or actionability. | Replay the complete proposed rule on an actual predecessor/proposed host pair and its true consumers; lower the affected values or return repair when use worsens. |
| **Formal assessment before semantic judgement.** Configuration, Method, application, Work, result-episteme, and evidence-use fields are completed before anyone can state the DRR's decision and first drafting action. | Judge the exact DRR, bounded omitted-question search, and actual-host effect first. Open each reliance-bearing identity only when a receiving use needs it. |
| **Goodharted DRR adequacy.** A DRR is made easier to defend as `4` or `5` by adding source rows, locus tables, boundary catalogues, or review proof while the selected answer and first action do not improve. | Reject apparatus-only improvement; repair decision content, delete or relocate proof material, and use `E.13` when the measure substitutes for decision usefulness. |
| **Solution architecture evaporates after DRR.** A DRR solves a multi-locus unfolding or first-entry problem, but hosts receive only fragments and the DRR remains the only place where the structure is understandable. | Move the surviving solution into selected pattern bodies, local unfolding blocks, E.11 entry expansions, or concrete relation loci; recheck true direct consumers. |

