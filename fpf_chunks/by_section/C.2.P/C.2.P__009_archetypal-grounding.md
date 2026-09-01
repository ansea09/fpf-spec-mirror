---
chunk_kind: "child"
pattern_id: "C.2.P"
pattern_title: "Epistemic Precision Restoration"
section_id: "C.2.P:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P/C.2.P__009_archetypal-grounding.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "C.2.P — Epistemic Precision Restoration"
  - "C.2.P:5 — Archetypal Grounding"
line_start: 42552
line_end: 42591
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.A"
  - "A.6.F"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.1"
  - "C.30.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.12"
  - "E.17"
  - "E.17.0"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.2"
  - "E.6"
  - "E.7"
  - "E.8"
  - "E.9"
  - "F.18"
keywords:
---

### C.2.P:5 - Archetypal Grounding

#### C.2.P:5.0.1 - Cheap case: ordinary reader help

**Starting sentence:** “The note supports the reader.”

**Questions:** What does the note let the reader do? Does the sentence claim evidence, authority, gate passage, work permission, or assurance?

**Result:** It only helps navigation. Rewrite: “The note helps the reader find section 4.2.” The recovered function is ordinary reader help. No FPF kind, relation, compact row, or full check is needed. Stop after the sentence.

#### C.2.P:5.0.2 - Mixed case: display and decision

**Starting sentence:** “The dashboard approves launch.”

**Questions:** Is the dashboard the decision, or does it display one? Which exact project object carries the approval claim?

**Result when a decision exists:** “The dashboard shows `GateDecision GD-17` for release candidate R; the decision, not the display, records that the gate passed.” E.17 and E.24.PUB keep the dashboard on the publication side; A.21 supplies the gate-decision meaning. The reader may find and cite GD-17, but must use the direct release or permission rule for launch. Stop.

**Result when no decision resolves:** “The dashboard is only a cue; launch approval is unresolved.” Block approval-bearing use until the exact decision exists.

#### C.2.P:5.1 - Boundary and Anti-Cases
| Boundary case | C.2.P result | Why this protects use |
| --- | --- | --- |
| Ordinary reader help | The sentence says a note helps a reader find another section, with no evidence, authority, use-boundary, work, gate, decision, or project reliance claim. Leave ordinary wording ordinary or make one local wording repair. | Keeps ordinary prose affordable; `support` as ordinary help is not forced into a record. |
| Relation-only support wording | The sentence says one claim, source description, grounding relation, evidence record, `B.3` `AssuranceResult`, engineering-justification result, causal-use relation, mathematical-lens relation, characteristic relation, declared-use boundary, work relation, or publication-companion use bears on another claim, and source-relation use or publication construction is already clear. Apply `A.6.P`; no C.2.P recovery is needed. | Prevents this pattern from absorbing relation precision restoration. |
| Known FPF kind named by value | The sentence already names the project-side FPF kind and reference, such as an evidence path, gate decision, decision record, Work occurrence, `B.3` `AssuranceResult`, or architecture pattern application. Apply the named pattern without an intermediate C.2.P step. | Avoids a needless logical hop and keeps the relevant neighboring-pattern application intact. |
| Source phrase without recovered FPF-governed use | Source wording is interesting but its FPF kind, relation, or use disposition cannot be recovered. Keep it as reduced-use cue or block its FPF use. | Preserves source meaning without guessing FPF meaning. |
| Replacement head is another umbrella | A proposed repair changes `support` to `basis`, `display` to `face`, or `route` to `path` while the kind and relation are still hidden. Mark repair incomplete. | Blocks lexical churn and forces the kind named by value, relation, and declared use boundary to be recovered. |
| Apparatus too heavy | A one-sentence local repair is replaced by a full record, checklist, and source note with no additional declared use boundary. Use the local sentence or compact row instead. | Keeps first-use cost and maintenance cost inside the quality claim. |

#### C.2.P:5.2 - Transfer Coverage

`C.2.P` is intentionally narrow but must transfer across three recurrent publication situations:

- FPF-side drafting: pattern text, DRR text, source-relation notes, review-use notes, and pattern draft prose;
- project-side publication: dashboards, explanations, cards, documents, front-ends, rendered files, and generated summaries used around evidence, work, gates, decisions, assurance, or methods;
- external source-expression clarification: seminar fragments, papers, reviews, standards, and tool outputs being clarified before possible FPF use.

In all three situations the same invariant holds: before accepting the wording as current FPF text, recover the distinction between source wording and current FPF wording, claim-bearing episteme, publication construction, carrier-relation construction, relation-like slice, the applicable neighboring pattern for any non-C.2.P field, and remaining reader use.

