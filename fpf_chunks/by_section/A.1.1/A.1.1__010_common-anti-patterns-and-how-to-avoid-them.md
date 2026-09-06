---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "Bounded Model-Use Structure and DDD Bounded-Context Recovery"
section_id: "A.1.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.1.1 — Bounded Model-Use Structure and DDD Bounded-Context Recovery"
  - "A.1.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 2264
line_end: 2274
dependencies:
  - "A.1"
  - "A.14"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.17.0"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
---

### A.1.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
|---|---|---|
| Context holon | Nearby systems, Work, and epistemes become parts of one extra whole. | Keep their direct identities; select only the decision-relevant relation organization as `U.Structure`. |
| Subsystem shortcut | Location or team ownership identifies the bounded context. | Recover all four A.22 discriminators. One subsystem can support several model-use structures. |
| One-relation or missing-frame shortcut | Applicability or actual use alone is expected to carry coherence, constraints, or the selection decision. | Stop at the direct relation until all three relation families, applied constraints, and one exact frame are current. |
| Description or publication substitution | A map, code repository, schema file, view, or publication is treated as the model-use organization or an occurrence. | Classify the exact content, carrier, system, structure, and publication claims under their subject patterns. |
| Locality inflation | A term, rule, unit, evidence use, or status use gets a context or structure proxy. | Apply the A.1.1:4.4 triage and keep the direct governed value or relation. |
| Crossing by label | *Mapped*, *Conformist*, or shared wording is treated as an obtaining structure crossing. | Preserve the proposal and apply `WF-A1.1-CROSS`; stop until the direct crossing governor exists. |

