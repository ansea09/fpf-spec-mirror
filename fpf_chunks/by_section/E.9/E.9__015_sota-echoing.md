---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design‑Rationale Record (DRR) Method"
section_id: "E.9:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__015_sota-echoing.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "E.9 — Design‑Rationale Record (DRR) Method"
  - "E.9:11 — SoTA-Echoing"
line_start: 71660
line_end: 71674
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

### E.9:11 - SoTA-Echoing

`E.9` aligns with contemporary architecture-decision and rationale-capture practice, but its contribution is not the existence of a decision record. ADR practice already carries compact context, decision, and consequence records. FPF uses the DRR as a decision-rationale record for one bounded FPF content decision, with enough by-value rationale to distribute durable content into selected patterns and selected non-pattern FPF kind-reference pairs.

| Practice source family | Local FPF invariant and practical implication | Popular shortcut rejected |
|---|---|---|
| **Architecture-description standards such as joint ISO, IEC, and IEEE 42010:2022** | Architecture work must make concerns, viewpoints, decisions, and rationale inspectable. A DRR adapts this to FPF content deltas by exposing the concerns and alternatives that shape the FPF change, not only the edited text. | Reject treating a patch or edited wording as self-explanatory architecture rationale. |
| **Markdown ADR practice, including post-2015 lightweight ADR and MADR-style templates** | Context, decision, and consequence records are useful when the change is local. A semantic FPF amendment needs enough by-value decision-ground and source-use content for later pattern drafting without reinvention. | Reject treating a generic ADR template as sufficient when a multi-pattern FPF change needs Pillar, lens, naming, SoTA, distribution, or loss and recoverability content. |
| **Continuous and evolutionary architecture decision-record practice** | Decision records are revisitable decision records for evolving systems. FPF keeps mutable process state out of the DRR and handles reopened content with a successor decision record. | Reject turning the DRR into a status log, gate diary, or permanent shadow law. |
| **Research and design-rationale traditions around alternatives and trade-off capture** | Rejected alternatives and trade-offs must remain recoverable enough that future authors do not re-litigate or silently reverse the selected answer. FPF adapts this through the Eleven Pillars and Principle-Taxonomy lenses. | Reject recording only the selected answer while leaving why-this-not-that implicit. |

The practical gain is content-selection quality under semantic load: the DRR decides the selected answer, alternatives, losses, boundary, and selected loci before pattern drafting begins. Any durable rule, example, or content obligation that remains useful after acceptance belongs in the selected FPF pattern or selected non-pattern FPF kind-reference pair, not in the DRR as a permanent shadow canon.

When a DRR relies on a source document, workstream plan, campaign queue, external review packet, standard, article, ADR-like note, or prior accepted decision, it states how the source is used and the source adoption/adaptation/rejection decision, then carries the selected payload by value: adopt, adapt, reject, lineage-only, rationale-only, selected payload, rejected or non-carried payload, source loss, selected locus, non-use boundary, and reopen condition. A cited source is not FPF doctrine, child DRR, review result, gate, evidence sufficiency, or monolith landing source by citation alone.

