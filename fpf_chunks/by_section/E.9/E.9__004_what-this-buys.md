---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design‑Rationale Record (DRR) Method"
section_id: "E.9:0.2"
section_title: "What this buys"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__004_what-this-buys.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "E.9 — Design‑Rationale Record (DRR) Method"
  - "E.9:0.2 — What this buys"
line_start: 70148
line_end: 70166
dependencies:
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.22"
  - "E.23"
  - "E.5.4"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.19"
keywords:
---

### E.9:0.2 - What this buys

- one external decision record that states the bounded FPF change by value before Core text is rewritten
- one minimum kernel that keeps Problem frame, Decision, Rationale, and Consequences recoverable for later review and replay
- one temporary convergence record for coordinated changes, while keeping enduring Core text in the selected patterns and selected non-pattern FPF kind-reference pairs rather than in the DRR
- one temporary convergence record that fixes the selected answer (the chosen content answer for the bounded content decision question) before later drafting fans out across several selected patterns or selected non-pattern FPF kind-reference pairs

**First useful move.** State the bounded FPF content decision question, the selected answer, the rationale for that answer, and the selected distribution across patterns or selected non-pattern FPF kind-reference pairs before drafting or landing the Core text.

**Cheap stop.** If the change is ordinary local wording repair, application of an already accepted pattern, or editorial cleanup that does not change FPF semantics, obligations, boundaries, names, admissible uses, or normative force, do not open a full DRR. Use the lighter governing pattern for the local repair: `E.17.AUD.LHR` for one overloaded local lexical head inside one publication unit, `C.2.P` for one episteme, publication, or source-use phrase requiring local epistemic precision restoration, `E.10` for general lexical repair, `F.18` only when a durable reusable name is being minted, and `E.8` for authoring-form correction. Leave `E.9` for bounded content decisions that need rationale by value.

**Kind-or-boilerplate diagnostic.** When a DRR proposes wording for selected patterns, apply `F.19` to separate boilerplate from remaining content before any wording is treated as pasteable pattern prose. If the remaining content still hides wording-use, naming, relation, claim, admissible-use, selected-locus, user-action, or flow-role precision, the DRR names the applied `E.10`, `E.10.ARCH`, `F.18`, or governing pattern. Process, architecture, review, or reference boilerplate belongs in its own carrier, not in pasteable pattern prose.

A DRR-proposed wording repair is not pasteable pattern prose until it carries a kind-restoration check. The DRR must show the pre-repair and post-repair object kind, relation or claim kind, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope, or explicitly decide that the change is a semantic change rather than an editorial repair. A nicer head word, shorter phrase, or removed trigger word is not decision evidence when it narrows a graph into a sequence, turns a method into work, widens an evidence record into assurance, treats a use relation as a new kind, or otherwise changes the kind or use relation without an accepted decision. When the decision depends on slot, lens, role, method, work, evidence, assurance, gate, or decision ontology, the DRR cites the governing pattern rather than redefining that ontology locally.

**Primary EntityOfConcern in plain terms.** The primary EntityOfConcern here is one external decision-rationale record for one bounded FPF content decision or one bounded coordinated change set. The minimal lens is simple: the record must keep the problem frame, decision, rationale, consequences, and impact and boundary account recoverable enough that accepted content can be distributed into the selected Core patterns and selected non-pattern FPF kind-reference pairs without semantic invention.

**Primary working reader.** The first working reader is an FPF author, reviewer, or steward who must evaluate, challenge, or land one bounded content decision. Downstream pattern readers benefit from the landed Core text; they are not the primary reader of the DRR itself.

