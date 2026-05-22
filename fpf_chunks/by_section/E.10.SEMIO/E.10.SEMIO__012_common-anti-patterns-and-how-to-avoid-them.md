---
chunk_kind: "child"
pattern_id: "E.10.SEMIO"
pattern_title: "Episteme-Publication Semantic Rewrite Discipline"
section_id: "E.10.SEMIO:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.SEMIO/E.10.SEMIO__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "E.10.SEMIO — Episteme-Publication Semantic Rewrite Discipline"
  - "E.10.SEMIO:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 53140
line_end: 53152
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
  - "A.6.P"
  - "A.6.Q"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "E.10"
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

### E.10.SEMIO:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Avoidance |
| --- | --- | --- |
| Token swap | Replace `surface` with `face` or `host` with `file` without recovering kind and sentence function. | Apply head-kind and relation recovery before rewriting. |
| Group-kind list | Leave a list such as `pattern, record, relation, or action` as if the list names one kind. | Decide whether the sentence needs one kind, a relation record, a tuple-like record, alternative cases, or a blocked ontology. |
| Type-correct but inert rewrite | All overread is removed, all heads are typed, and no practical force remains: the reader can see that local checks passed but cannot tell why the distinction matters, what to do, or where the live claim moved. | Recover the didactic or recognition function in admissible wording, keep any Plain line mapped to the recovered Tech reading when both registers are live, state the remaining admissible reader move, or demote the phrase to reduced-use cue, quote-only wording, blocked transfer, or rewrite incomplete instead of pretending the repair landed. |
| Expressive overread rebound | A repair tries to restore practical force with a memorable Plain or didactic line, but that line carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load not recoverable from the Tech fields, exact FPF kind, recovered relation, project-side source reference, disposition, or named handoff. | Rewrite the line as ordinary recognition aid mapped to the recovered Tech reading under `E.10:6.2`, recover the load through the exact Tech fields, name the neighboring-pattern handoff that carries the live claim, or demote the phrase to reduced-use cue, quote-only wording, blocked transfer, or rewrite incomplete. |
| Pillar-blind precision pass | A broad cleanup proves trigger removal and kind recovery, but never checks whether `E.2` `P-2`, `E.6`, `E.8`, or `E.12` still let the intended reader see the working situation, why it matters, and what first useful move remains. | For load-bearing Problem frames, Problem sections, recognition texts, examples, and worked slices, state the remaining admissible reader move or named neighboring-pattern handoff. Preserve intentional didactic metaphors when they are ordinary recognition aids or when their load maps back to Tech. If the didactic function was harmed, repair the wording in admissible Plain mapped to Tech, or mark the rewrite incomplete instead of accepting type-correct but inert wording. |
| Source-status leakage | Carry a source-companion header into a pattern and let `Authority: none` or `Current use` define the new pattern. | State current pattern status in the pattern header and relations. |
| Pattern as procedure | Say the pattern is called, routed, invoked, or chained as if it were executable code. | Say the FPF pattern is applied in a problem situation; name exact project-side `U.Work` occurrence, `U.Method`, `C.11` decision value, or `A.6.A` action invitation when project activity is live. |
| Strength metaphor | Say a claim is strong or weak without a characteristic, threshold, evidence class, scope, gate, or admissibility relation. | Name the exact comparison basis or replace the metaphor with the recovered admissibility relation. |

