---
chunk_kind: "child"
pattern_id: "C.2.P"
pattern_title: "Epistemic Precision Restoration"
section_id: "C.2.P:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P/C.2.P__009_archetypal-grounding.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "C.2.P — Epistemic Precision Restoration"
  - "C.2.P:5 — Archetypal Grounding"
line_start: 42105
line_end: 42135
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

| Scenario | Show - failure without C.2.P | Show - repair with C.2.P |
| --- | --- | --- |
| FPF pattern prose | A pattern section, row, or source line appears to support an action. The reader cannot tell whether the sentence is about applying a pattern, a section as `PublicationUnit`, a document, a file, or a relation. | Name the object and sentence function that matter. Keep an ordinary pattern-use claim when that is all the sentence says; narrow it to source-finding when the publication only helps navigation; use the named FPF pattern when its definition, constraint, or test carries the action claim. |
| Engineering project publication | A green dashboard tile, certificate badge, or generated explanation is treated as evidence, gate passage, engineering justification, assurance, or permission for work. | The engineer names the generic publication face, MVPK face under E.17 constraints, or carrier, then names the one project-side FPF kind and reference that carries the downstream claim: evidence record, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `B.3` assurance or engineering-justification record, `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, `U.Method`, or `U.MethodDescription`. The next action is orientation or source-finding only, or finding or creating the named evidence, gate, decision, assurance, plan, work, method, or invitation before work or reliance proceeds. Choose one current value, not the list. |
| Source-wording or source-relation text | A source note says that material supplies a claim without naming the recovered field: pattern application, selected source `U.Episteme`, publication occurrence when availability matters, publication form or carrier, relation record, or project-side FPF kind and reference. | State the recovered field and sentence function. Apply the relevant FPF pattern or cite the selected source episteme, publication occurrence, or relation. If the meaning remains unclear, reduce the phrase to source-finding or block its claim-bearing use. |
| Pattern-control wording | A text says that one pattern routes into another, calls another pattern, exits to a pattern, or chains patterns. The reader may treat pattern application as executable process control. | If the sentence is about applicability, say that a practitioner uses or applies the pattern in the problem situation. If it is about project activity, name the action, work, method, decision, or invitation needed for that claim. Add the acting `U.System`, `U.MethodDescription`, `U.Method`, dated `U.Work`, or separate decision and invitation identities only when their distinction changes the claim or its later use. |
| Architecture or structure wording | A source says an architecture description, structure representation, design rationale, or structural view carries a claim, but the sentence does not show whether the use under repair is a described holon, architecture description, structure, structural view, relation, publication face, or carrier. | `C.2.P` first recovers the source expression, source-relation function, and publication and carrier relation set. If the architecture claim, structure kind, structure relation, view, publication relation, or source relation is still hidden, use `C.30.P`; if it is already recoverable, use `C.30`, `C.30.ASV`, `A.22`, `C.31`, or the applicable architecture or structure pattern. Use `A.6.P` for relation-like wording. |

#### C.2.P:5.1 - Boundary and Anti-Cases

| Boundary case | C.2.P result | Why this protects use |
| --- | --- | --- |
| Ordinary reader help | The sentence says a note helps a reader find another section, with no evidence, authority, use-boundary, work, gate, decision, or project reliance claim. Leave ordinary wording ordinary or make one local wording repair. | Keeps ordinary prose affordable; `support` as ordinary help is not forced into a record. |
| Relation-only support wording | The sentence says one claim, source description, grounding relation, evidence record, assurance record, causal-use relation, mathematical-lens relation, characteristic relation, declared-use boundary, work relation, or publication-companion use warrants another claim, and source-relation use or publication construction is already clear. Apply `A.6.P`; no C.2.P recovery is needed. | Prevents this pattern from absorbing relation precision restoration. |
| Known FPF kind named by value | The sentence already names the project-side FPF kind and reference, such as an evidence path, gate decision, decision record, work occurrence, assurance record, or architecture pattern application. Apply the named pattern without an intermediate C.2.P step. | Avoids a needless logical hop and keeps the relevant neighboring-pattern application intact. |
| Source phrase without recovered FPF-governed use | Source wording is interesting but its FPF kind, relation, or use disposition cannot be recovered. Keep it as reduced-use cue or block its FPF use. | Preserves source meaning without guessing FPF meaning. |
| Replacement head is another umbrella | A proposed repair changes `support` to `basis`, `display` to `face`, or `route` to `path` while the kind and relation are still hidden. Mark repair incomplete. | Blocks lexical churn and forces the kind named by value, relation, and declared use boundary to be recovered. |
| Apparatus too heavy | A one-sentence local repair is replaced by a full record, checklist, and source note with no additional declared use boundary. Use the local sentence or compact row instead. | Keeps first-use cost and maintenance cost inside the quality claim. |

#### C.2.P:5.2 - Transfer Coverage

`C.2.P` is intentionally narrow but must transfer across three recurrent publication situations:

- FPF-side drafting: pattern text, DRR text, source-relation notes, review-use notes, and pattern draft prose;
- project-side publication: dashboards, explanations, cards, documents, front-ends, rendered files, and generated summaries used around evidence, work, gates, decisions, assurance, or methods;
- external source-expression clarification: seminar fragments, papers, reviews, standards, and tool outputs being clarified before possible FPF use.

In all three situations the same invariant holds: before accepting the wording as current FPF text, recover the distinction between source wording and current FPF wording, claim-bearing episteme, publication construction, carrier-relation construction, relation-like slice, the applicable neighboring pattern for any non-C.2.P field, and remaining reader use.

