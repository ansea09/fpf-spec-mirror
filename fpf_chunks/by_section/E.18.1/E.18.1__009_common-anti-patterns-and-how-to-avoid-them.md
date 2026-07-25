---
chunk_kind: "child"
pattern_id: "E.18.1"
pattern_title: "P2W Problem-to-Work Carry-Through"
section_id: "E.18.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.1/E.18.1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "E.18.1 — P2W Problem-to-Work Carry-Through"
  - "E.18.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 82054
line_end: 82066
dependencies:
  - "A.15"
  - "A.15.PROD"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.2"
  - "C.29"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.18"
  - "E.18.3"
  - "F.17"
  - "F.18"
  - "F.8"
  - "F.9"
  - "G.11"
  - "G.2"
  - "G.5"
  - "G.9"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### E.18.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| **Boundary fanout.** The pattern repeats neighbouring algorithms or long lists of what P2W is not. | Keep the owner-return interface in `4.4`, relation selection in `4.6`, and the canonical owner map in Relations; local cases name only the owner-returned value, split, or stop needed by P2W. |
| **Carry-through-as-procedure.** A carry-through structure, diagram, or graph-shaped expression is read as a prescribed project sequence. | Treat it as relation-governed carry-through over FPF applications; use the `stop`, `split`, and `return` moves as method-use guidance, never as P2W relation kinds or a project-work order. |
| **ProblemCard-as-solution.** The accepted problem card is treated as method, plan, work, evidence, or result. | State the carried distinction and next FPF-use question conversationally; materialize a compact note only under named reliance, then apply the direct pattern. |
| **Math-as-authority.** A `U.Signature(profile=FormalSubstrate)` declaration, mathematical lens, or near-sameness does all downstream work. | Apply `C.29` to preserved structure, lost structure, payoff, declared use, and stop condition; continue only through the recovered relation, and add a P2W note only under named reliance. |
| **Generic result token.** "Result" becomes one local kind or P2W repeats the complete recovery method. | Apply `A.6.P.WMR`, then carry each exact direct subject claim, exact `A.6.1` application binding, or exact local `A.15.PROD`/`A.6.RCD` claim separately. Preserve an exact non-assertability result as independently `factually unsupported`, `missing-information`, or `missing-governor`; stop and name a future owner only for `missing-governor`. Introduce no generic result family. |
| **Choice-as-commitment.** A `C.11` choice result is treated as an accountable obligation, recommendation-as-duty, or prohibition. | Keep the option set, comparison basis, choice rule, and choice result under `C.11`; open a separate `A.2.8 U.Commitment` only when its accountable subject, modality, referents, scope, and window are independently recoverable. |
| **Plan, path, or proximity as actual change.** A desired state, model, method, plan, flow arrow, adjacent work, or common affected referent is treated as an actual or composite transformation. | Apply `A.3.4` and any direct work-to-change or `A.15.PROD` owner separately; carry only their returned values or blockers and open no composition or production continuation by proximity. |
| **Interface shortcut.** Interface, port, protocol, connection, resource, or integration wording selects function, method, work, evidence, gate, or architecture by itself. | Recover the module-interface, signature-slot, function, architecture, work, evidence, or gate relation before continuing. |

