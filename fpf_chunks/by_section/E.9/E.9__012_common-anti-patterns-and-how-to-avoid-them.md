---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design‑Rationale Record (DRR) Method"
section_id: "E.9:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "E.9 — Design‑Rationale Record (DRR) Method"
  - "E.9:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 58159
line_end: 58170
dependencies:
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.22"
  - "E.23"
  - "E.5.4"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.19"
keywords:
---

### E.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | Why it fails | Repair |
|---|---|---|---|
| **Process brief disguised as DRR** | The record explains baton movement, packet state, review timing, or current campaign state. | It describes development process rather than the FPF content decision. | Remove mutable process state and keep only the decision grounds, selected answer, alternatives, and consequences. |
| **Shadow specification** | The DRR becomes the only place where stable semantics, examples, source-use rules, or validation rules remain after the Core has moved. | Later FPF readers cannot use the decision because it never became pattern content. | Distribute enduring content into the selected patterns and selected non-pattern FPF kind-reference pairs; leave the DRR as provenance. |
| **Four-label shell** | The record has Problem frame, Decision, Rationale, and Consequences headings, but no decision grounds, use-value, alternatives, content distribution, or impact account by value. | The minimum kernel is labeled but not substantively recoverable. | Fill the decision-inspection content blocks needed for the decision, or use the lightweight variant only for true `Delta-0` / `Delta-1` edits. |
| **Tentative carrier list** | The DRR says a pattern may need work later, is most likely affected, or should be watched if touched. | A named distribution question is postponed while pretending to be decided. | Classify each named pattern or selected non-pattern FPF kind-reference pair now: selected, rejected, inherited unchanged, or outside the current decision with a named record. |
| **Loss without use/reopen rule** | The decision summarizes, redacts, simplifies, or otherwise declares a source-loss mode but does not state admissible use, non-admissible downstream use, recoverability, and reopen conditions. | A representation with undeclared source loss can be used as if it were the full source. | Add the source-loss and recoverability template: preserved distinctions, dropped distinctions, admissible uses, non-admissible uses, recoverability class, and reopen or stop rule. |
| **Free paraphrase import** | The DRR restates a source-borne method, architecture claim, accepted decision-ground item, or reusable source passage in smoother prose but does not say whether it quoted, narrowed, instantiated, used as decision grounds, turned into draft guidance, kept example-only, or retired the source use. | The paraphrase can widen, weaken, or redirect the source while appearing to preserve it. | State the source-use result and loss and addition account, or keep the passage as an quote or example-only source named by value example. |
| **Decorative SoTA appendix** | Sources are listed after the fact or treated as SoTA because they are official, recent, popular, or famous, but they do not change the selected answer, boundary, or validation evidence obligation. | The record looks researched while the decision remains unchallenged by current best-known practice. | State what each load-bearing source makes the DRR adopt, adapt, or reject, why that source family is current for the DRR decision question under E.8, and which uncertainty would materially change the answer. |

