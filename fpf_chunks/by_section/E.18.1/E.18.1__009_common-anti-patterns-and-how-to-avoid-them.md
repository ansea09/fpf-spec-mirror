---
chunk_kind: "child"
pattern_id: "E.18.1"
pattern_title: "P2W Problem-to-Work Carry-Through"
section_id: "E.18.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.1/E.18.1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "E.18.1 — P2W Problem-to-Work Carry-Through"
  - "E.18.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 81052
line_end: 81062
dependencies:
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.0"
  - "A.6.1"
  - "C.16"
  - "C.22.2"
  - "C.29"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.18"
  - "E.18.3"
  - "F.9"
  - "G.11"
  - "G.2"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### E.18.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| **Boundary fanout.** The pattern repeats long lists of what P2W is not. | Keep relation discipline in `E.18.1:4.4`; make local sections state the next P2W application. |
| **Carry-through-as-procedure.** A carry-through structure, diagram, or graph-shaped expression is read as a prescribed project sequence. | Treat it as relation-governed carry-through over FPF applications; use `stop`, `split`, and `return` relations. |
| **ProblemCard-as-solution.** The accepted problem card is treated as method, plan, work, evidence, or result. | Write the carried distinction and next FPF-use question before selecting an application. |
| **Math-as-authority.** A `U.Signature(profile=FormalSubstrate)` declaration, mathematical lens, or near-sameness does all downstream work. | Record preserved structure, lost structure, payoff, and stop condition; continue through the recovered relation. |
| **Generic result token.** "Result" becomes one local kind. | Split the phrase into artifact, telemetry, acceptance, quality, measurement, refresh, source-use relation, evidence, or role-enactability relation. |
| **Interface shortcut.** Interface, port, protocol, connection, resource, or integration wording selects function, method, work, evidence, gate, or architecture by itself. | Recover the module-interface, signature-slot, function, architecture, work, evidence, or gate relation before continuing. |

