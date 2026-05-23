---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design‑Rationale Record (DRR) Method"
section_id: "E.9:0.2"
section_title: "What this buys"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__004_what-this-buys.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "E.9 — Design‑Rationale Record (DRR) Method"
  - "E.9:0.2 — What this buys"
line_start: 51081
line_end: 51095
dependencies:
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.5.4"
  - "E.8"
keywords:
---

### E.9:0.2 - What this buys

- one external decision record that states the bounded FPF change by value before Core text is rewritten
- one minimum kernel that keeps Problem frame, Decision, Rationale, and Consequences recoverable for later review and replay
- one temporary convergence record for coordinated changes, while keeping enduring Core text in the selected patterns and selected non-pattern FPF kind-reference pairs rather than in the DRR
- one temporary convergence record that fixes the selected answer (the chosen content answer for the bounded content decision question) before later drafting fans out across several selected patterns or selected non-pattern FPF kind-reference pairs

**First useful move.** State the bounded FPF content decision question, the selected answer, the rationale for that answer, and the selected distribution across patterns or selected non-pattern FPF kind-reference pairs before drafting or landing the Core text.

**Cheap stop.** If the live change is ordinary local wording repair, application of an already accepted pattern, or editorial cleanup that does not change FPF semantics, obligations, boundaries, names, admissible uses, or normative force, do not open a full DRR. Use the lighter governing pattern for the local repair: `E.17.AUD.LHR` for one overloaded local lexical head inside one publication unit, `E.10.SEMIO` for one semio-heavy phrase requiring local semantic recovery, `E.10` for general lexical repair, `F.18` only when a durable reusable name is being minted, and `E.8` for authoring-form correction. Leave `E.9` for bounded content decisions that need rationale by value.

**Governed object in plain terms.** The governed object here is one external decision-rationale record for one bounded FPF content decision or one bounded coordinated change set. The minimal lens is simple: the record must keep the problem frame, decision, rationale, consequences, and impact/boundary account recoverable enough that accepted content can be distributed into the selected Core patterns and selected non-pattern FPF kind-reference pairs without semantic invention.

**Primary working reader.** The first working reader is an FPF author, reviewer, or steward who must evaluate, challenge, or land one bounded content decision. Downstream pattern readers benefit from the landed Core text; they are not the primary reader of the DRR itself.

