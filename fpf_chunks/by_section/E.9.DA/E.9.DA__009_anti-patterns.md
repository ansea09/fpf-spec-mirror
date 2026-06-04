---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:8"
section_title: "Anti-Patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__009_anti-patterns.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:8 — Anti-Patterns"
line_start: 57643
line_end: 57661
dependencies:
  - "A.19.ECS"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
keywords:
---

### E.9.DA:8 - Anti-Patterns

| Anti-pattern | Failure | Repair |
|---|---|---|
| **Heading-complete DRR.** | The `DRR` has `Problem`, `Decision`, `Rationale`, and `Consequences`, but pattern authors still cannot tell what to write. | Apply eligibility rows and repair `SelectedAnswerDecisiveness` plus `DraftingActionability`. |
| **Source packet in DRR clothing.** | The `DRR` preserves source content but does not select FPF content. | Repair `BoundedDecisionQuestionRecoverability`, `SelectedAnswerDecisiveness`, `DRRSourceUseDischargeMap?`, and `SourceUseAndDecisionInheritanceCarryThrough`. |
| **Neighbour mention without obligation.** | A related pattern is named but not classified as amended, receives content obligation, governs only, outside current decision, sibling decision, or intentionally unamended. | Repair `DRRReceivingLocusDispositionMap` and `ReceivingLocusObligationClosure`. |
| **Explicit but wrong FPF content architecture.** | The `DRR` assigns every locus, but the split or merge, new-pattern choice, selected companion publication, selected non-pattern FPF kind-reference pair, or neighbour and local boundary is substantively wrong. | Repair `FPFContentArchitectureSelectionAdequacy`; if the selected content object or receiving locus cannot be selected, set `holdForArchitectureDecision`. |
| **Watch item disguised as decision.** | The `DRR` says a question may be handled by drafting without selecting the answer now. | Select the answer, narrow the `DRR`, or set `splitDecisionRequired`. |
| **Lexical scorekeeping.** | The read counts trigger words but does not repair their load-bearing meaning. | Apply `E.10` closure and exact receiving-pattern recovery. |
| **Pattern-quality substitution.** | The `DRR` is judged by whether the resulting pattern text would be usable. | Judge the `DRR` decision-adequacy claim; evaluate the resulting pattern version by `E.21`. |
| **Review-state proxy.** | A `DRR` is marked adequate because a reviewer accepted it, or inadequate because it has not been reviewed. | Use content loci for coordinates; keep review state in `DRRReadQualificationWindow` or review records. |
| **Reputation medal adequacy.** | A `DRR` is marked more adequate because many sources are cited, a steward praised it, a reviewer-clean packet exists, or many downstream users rely on it; or marked less adequate because it is new and not yet used. | Rewrite the signal into exact `DRR` decision-content evidence or keep it outside the coordinate value. Adequacy changes only when selected answers, receiving-locus requirements, source-use role or status, architecture choice, validation obligations, non-use boundaries, stop conditions, or reopen conditions change or are shown weak. |
| **Workstream plan as doctrine.** | A source plan, queue, campaign source, or review packet is treated as landed FPF authority. | Add `DRRSourceUseDischargeMap?`; state source-use role, source-currentness status, and selected payload by value in the `DRR`. |
| **ADR-as-decision.** | An ADR-like publication, review packet, or note is treated as the project-side decision or as an FPF `DRR`. | Split decision, decision description, publication form, and FPF `DRR`; move project-side decision claims to exact neighbouring patterns. |
| **Graph-as-architecture.** | A TGA graph, generated relation graph, clustering result, LCA view, diagram, or dashboard is treated as architecture itself. | Name the architecture claim or structure claim, view and description relation, preserved and lost structure, source-return condition, and non-use boundary. |
| **Review packet as evidence.** | A review packet or returned finding is treated as project evidence, assurance, gate, release, or compliance proof. | Keep review material as source-use or accepted-decision material for the `DRR`; move project evidence, assurance, or gate claims to exact evaluation patterns. |
| **Companion note as Core.** | A companion architecture note, source packet, or companion document is treated as if it already changed FPF Core pattern text. | State the selected receiving loci and first drafting implications; keep companion-publication authority bounded until landed pattern text or selected non-pattern FPF kind-reference content carries the decision. |

