---
chunk_kind: "child"
pattern_id: "A.3.3.TR"
pattern_title: "Construct a Rule for State Change"
section_id: "A.3.3.TR:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.TR/A.3.3.TR__002_problem-frame.md"
commit_sha: "8581bcf6502498b53aaa9fd42ed925a1371c08d1"
heading_path:
  - "A.3.3.TR — Construct a Rule for State Change"
  - "A.3.3.TR:1 — Problem frame"
line_start: 9828
line_end: 9839
dependencies:
  - "A.22.CGUS"
  - "A.3.3"
  - "A.3.3.CC"
  - "B.5.FM"
  - "B.5.MPC"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### A.3.3.TR:1 - Problem frame

Use this pattern when you can describe a situation's state but still need to work out how it can change. A connection limits two bodies' positions but leaves their acceleration to be determined. Each participant in a computation has a valid procedure, yet their interleaving can produce an unexpected result. A transformation preserves a mathematical property but can repeat forever.

**First useful move.** Choose one possible change and write which values it reads, which values it changes, what must hold for it to occur and which other values stay fixed during that step. For a participant that has saved a counter value r, its later write sets x' = r + 1. It need not produce x' = x + 1: another participant may have changed x since the read. This small rule exposes the lost-increment case in :5.1.

The Method constructs a rule relating states or describing their continuous evolution under stated inputs. “Allowed” means permitted by that model. The resulting rule can support a conditional calculation, reveal competing continuations or identify a missing interaction, operation or input. A.3.3 supplies the criteria for a U.Dynamics episteme and connects its state space, transition law and observation account.

The finite cases require ordinary arithmetic and conditions. The continuous case additionally uses derivatives and Newton's equation for a stated ideal mechanical model. Subject laws and operation semantics supply the content that the common construction combines.

If a suitable state-change rule already answers the question, apply it directly. When only compatible arrangements are needed, A.3.3.CC can supply that result before a rule of change is available. Use the present Method to construct or revise the rule, not as an extra reporting stage for every calculation.

