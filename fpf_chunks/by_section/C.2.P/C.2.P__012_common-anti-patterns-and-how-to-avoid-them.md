---
chunk_kind: "child"
pattern_id: "C.2.P"
pattern_title: "Epistemic Precision Restoration"
section_id: "C.2.P:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P/C.2.P__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "C.2.P — Epistemic Precision Restoration"
  - "C.2.P:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 42197
line_end: 42209
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

### C.2.P:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Avoidance |
| --- | --- | --- |
| Token swap | Replace `display` with `face` or `host` with `file` without recovering kind and sentence function. | Apply head-kind and relation recovery before rewriting. |
| Group-kind list | Leave a list such as `pattern, record, relation, or action` as if the list names one kind. | Decide whether the sentence needs one kind, a relation record, a tuple-like record, alternative cases, or a blocked ontology. |
| Type-correct but inert rewrite | All overread is removed, all heads are typed, and no practical guidance remains: the reader can see that local checks passed but cannot tell why the distinction matters, what to do, or which FPF pattern application or project-side FPF kind carries the claim being made. | Recover the didactic or recognition function in wording whose claim being made is recovered through the named FPF pattern, keep any Plain line mapped to the recovered Tech interpretation when both registers are current, state the remaining reader use, or demote the phrase to reduced-use cue, blocked use, or rewrite incomplete instead of pretending the repair landed. |
| Expressive overread rebound | A repair tries to restore practical guidance with a memorable Plain or didactic line, but that line carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or use-boundary claim not recoverable from the Tech fields, FPF kind named by value, recovered relation, project-side FPF reference or relation, disposition, or named FPF pattern application. | Rewrite the line as ordinary recognition aid mapped to the recovered Tech interpretation under `E.10:6.2`; recover the claim being made through the Tech fields named by value, name the governing FPF pattern ontology that carries the claim being made, or demote the phrase to reduced-use cue, blocked use, or rewrite incomplete. |
| Pillar-blind precision pass | A broad cleanup proves trigger removal and kind recovery, but never checks whether `E.2` `P-2`, `E.6`, `E.8`, or `E.12` still let the intended reader see the working situation, why it matters, and what first useful move remains. | For FPF-governed Problem frames, Problem sections, recognition texts, examples, and worked slices, state the remaining reader use or FPF pattern application. Preserve intentional didactic metaphors when they are ordinary recognition aids or when their claim being made maps back to Tech. If the didactic function was harmed, repair the Plain wording so it maps back to the recovered Tech interpretation, or mark the rewrite incomplete instead of accepting type-correct but inert wording. |
| Source-companion header leakage | Carry a source-companion header into a pattern and let `Authority: none` or `Current use` define the new pattern. | State the pattern-use claim and authority claim in the pattern header and relations. |
| Pattern as procedure | Say the pattern is called, routed, invoked, or chained as if it were executable code. | Say the FPF pattern is applied in a problem situation; name project-side `U.Work` occurrence, `U.Method`, `C.11` decision value, or `A.6.A` action invitation when project activity is current. |
| Strength metaphor | Say a claim is strong or weak without a characteristic, threshold, evidence class, scope, gate, or use-boundary relation. | Name the comparison characteristic, threshold, evidence class, scope, gate, or use-boundary relation, or replace the metaphor with the recovered use-boundary relation. |

