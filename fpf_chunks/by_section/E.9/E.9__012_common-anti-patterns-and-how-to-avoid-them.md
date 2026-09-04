---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design‑Rationale Record (DRR) Method"
section_id: "E.9:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "E.9 — Design‑Rationale Record (DRR) Method"
  - "E.9:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 74344
line_end: 74358
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.6.1"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.5.4"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.10"
  - "F.19"
  - "G.11"
  - "G.6"
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
| **Free paraphrase import** | The DRR restates a source-borne method, architecture claim, accepted decision-ground item, or reusable source passage in smoother prose but does not say whether it quoted, narrowed, instantiated, used as decision grounds, turned into draft guidance, kept example-only, or retired the source use. | The paraphrase can widen, weaken, or redirect the source while appearing to preserve it. | State the source-use result and loss and addition account, or keep the passage as a quotation or an example-only source named by value. |
| **Decorative SoTA appendix** | Sources are listed after the fact or treated as SoTA because they are official, recent, popular, or famous, but they do not change the selected answer, boundary, or validation obligation. | The record looks researched while the decision remains unchallenged by current best-known practice. | State what each load-bearing source makes the decision adopt, adapt, or reject, why it is current under E.8, and which uncertainty would materially change the answer. |
| **Negative catalogue as the decision** | Discussion history, every rejected option, every Pillar, and every taxonomy lens occupy more space than the positive answer and first drafting action. | Authors must reconstruct the selected move from exclusions and ritual coverage. | Keep only alternatives and lens effects that explain the selected answer, boundary, or reopen condition. Leave the rest outside the current DRR; retain it elsewhere only when a named later use needs that history. |
| **Proxy replay for a broad rule** | A schema, invented fact pack, lane comparison, or checklist is used to justify a rule that will rewrite practitioner-facing hosts. | The tested proxy can stay usable while the actual host entry, action, result, or burden degrades. | Replay the complete proposed rule on an actual predecessor/proposed host pair and its true direct consumers before fanout. |
| **Record as work or authority** | A filled, approved-looking, published, or adequate-looking DRR is said to have made the decision, passed review, authorized Core change, or performed realization. | Method, work, result, episteme, assessment, status/authority, and downstream change collapse. | Recover only the distinctions the current claim needs; let the DRR record rather than perform them. |

