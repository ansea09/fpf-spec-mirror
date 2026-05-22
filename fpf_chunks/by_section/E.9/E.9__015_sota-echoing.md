---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design‑Rationale Record (DRR) Method"
section_id: "E.9:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__015_sota-echoing.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "E.9 — Design‑Rationale Record (DRR) Method"
  - "E.9:11 — SoTA-Echoing"
line_start: 51271
line_end: 51283
dependencies:
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.5.4"
  - "E.8"
keywords:
---

### E.9:11 - SoTA-Echoing

`E.9` aligns with contemporary architecture-decision and rationale-capture practice, but its contribution is not the existence of a decision record. ADR practice already carries compact context, decision, and consequence records. FPF uses the DRR as a decision-rationale record for one bounded FPF content decision, with enough by-value rationale to distribute durable content into selected patterns and selected non-pattern FPF kind-reference pairs.

| Practice source family | Local FPF invariant and practical implication | Popular shortcut rejected |
|---|---|---|
| **Architecture-description standards such as joint ISO, IEC, and IEEE 42010:2022** | Architecture work must make concerns, viewpoints, decisions, and rationale inspectable. A DRR adapts this to FPF content deltas by exposing the concerns and alternatives that shape the FPF change, not only the edited text. | Reject treating a patch or edited wording as self-explanatory architecture rationale. |
| **Markdown ADR practice, including post-2015 lightweight ADR and MADR-style templates** | Context, decision, and consequence records are useful when the live change is local. A semantic FPF amendment needs enough by-value support for later pattern drafting without reinvention. | Reject treating a generic ADR template as sufficient when a multi-pattern FPF change needs Pillar, lens, naming, SoTA, distribution, or loss and recoverability support. |
| **Continuous and evolutionary architecture decision-record practice** | Decision records are revisitable support for evolving systems. FPF keeps mutable process state out of the DRR and handles reopened content with a successor decision record. | Reject turning the DRR into a live status log, gate diary, or permanent shadow law. |
| **Research and design-rationale traditions around alternatives and trade-off capture** | Rejected alternatives and trade-offs must remain recoverable enough that future authors do not re-litigate or silently reverse the selected answer. FPF adapts this through the Eleven Pillars and Principle-Taxonomy lenses. | Reject recording only the selected answer while leaving why-this-not-that implicit. |

The practical gain is content-selection quality under semantic load: the DRR decides the selected answer, alternatives, losses, boundary, and distribution target before pattern drafting begins. Any durable rule, example, or support obligation that remains useful after acceptance belongs in the selected FPF pattern or selected non-pattern FPF kind-reference pair, not in the DRR as a permanent shadow canon.

