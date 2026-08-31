---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design‑Rationale Record (DRR) Method"
section_id: "E.9:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__015_sota-echoing.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "E.9 — Design‑Rationale Record (DRR) Method"
  - "E.9:11 — SoTA-Echoing"
line_start: 74044
line_end: 74058
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

### E.9:11 - SoTA-Echoing

`E.9` draws on mature decision-record and design-rationale lineages, but no listed standard or template is automatically current SoTA for every FPF decision. The DRR selects current problem-owning evidence under E.8 when that evidence is load-bearing. Its distinctive contribution is a decision-rationale record for one bounded FPF content decision, with enough by-value rationale to distribute durable content without making the record a shadow specification.

| Practice source family | Local FPF invariant and practical implication | Popular shortcut rejected |
|---|---|---|
| **Mature architecture-description standards lineage, including joint ISO, IEC, and IEEE 42010:2022** | Concerns, viewpoints, decisions, and rationale should remain inspectable. E.9 adapts that lineage to FPF content deltas; it does not treat an architecture-description standard as the sole or automatically current SoTA for the decision question. | Reject treating a patch as self-explanatory rationale or selecting a familiar standard by prestige. |
| **Markdown ADR practice, including post-2015 lightweight ADR and MADR-style templates** | Context, decision, and consequence records are useful when the change is local. A semantic FPF amendment needs enough by-value decision-ground and source-use content for later pattern drafting without reinvention. | Reject treating a generic ADR template as sufficient when a multi-pattern FPF change needs Pillar, lens, naming, SoTA, distribution, or loss and recoverability content. |
| **Continuous and evolutionary architecture decision-record practice** | Decision records are revisitable decision records for evolving systems. FPF keeps mutable process state out of the DRR and handles reopened content with a successor decision record. | Reject turning the DRR into a status log, gate diary, or permanent shadow law. |
| **Research and design-rationale traditions around alternatives and trade-off capture** | Rejected alternatives and trade-offs must remain recoverable enough that future authors do not re-litigate or silently reverse the selected answer. FPF adapts this through the Eleven Pillars and Principle-Taxonomy lenses. | Reject recording only the selected answer while leaving why-this-not-that implicit. |

The practical gain is content-selection quality under semantic load: decision work selects the answer, alternatives, losses, boundary, and loci; the DRR episteme makes that result replayable before pattern drafting. Any durable rule, example, or obligation useful after realization belongs in the selected FPF pattern or non-pattern kind-reference pair, not in the DRR as permanent shadow canon.

When a source document, workstream plan, queue, review packet, standard, article, ADR-like note, or prior decision shapes the answer, the DRR records how it is used and which payload is selected or left behind, including any material loss, locus, non-use boundary, and reopen condition. Name the exact source episteme, publication, and source-use relation when the decision or a named later reliance depends on those identities. Citation alone creates no doctrine, child DRR, review result, gate, evidence sufficiency, or landing source.

