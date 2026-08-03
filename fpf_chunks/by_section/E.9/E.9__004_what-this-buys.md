---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design‑Rationale Record (DRR) Method"
section_id: "E.9:0.2"
section_title: "What this buys"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__004_what-this-buys.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "E.9 — Design‑Rationale Record (DRR) Method"
  - "E.9:0.2 — What this buys"
line_start: 72862
line_end: 72880
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.6.1"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.5.4"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.10"
  - "F.19"
  - "G.11"
  - "G.6"
keywords:
---

### E.9:0.2 - What this buys

- one external decision record that states the bounded FPF change by value before Core text is rewritten
- one minimum kernel that keeps Problem frame, Decision, Rationale, and Consequences recoverable for later review and replay
- one temporary convergence record for coordinated changes, while keeping enduring Core text in the selected patterns and selected non-pattern FPF kind-reference pairs rather than in the DRR
- one temporary convergence record that fixes the selected answer (the chosen content answer for the bounded content decision question) before later drafting fans out across several selected patterns or selected non-pattern FPF kind-reference pairs

**First useful move.** Name the exact bounded FPF decision question and the dated decision/authoring work applying `DRRMethod`; then make the selected-answer result, rationale, consequences, source-use relations, and selected distribution recoverable in one C.2.1 DRR episteme before downstream Core drafting begins.

**Cheap stop.** If the change is ordinary local wording repair, application of an already accepted pattern, or editorial cleanup that does not change FPF semantics, obligations, boundaries, names, admissible uses, or normative force, do not open a full DRR. Use the lighter governing pattern for the local repair: `E.17.AUD.LHR` for one overloaded local lexical head inside one publication unit, `C.2.P` for one episteme, publication, or source-use phrase requiring local epistemic precision restoration, `E.10` for general lexical repair, `F.18` only when a durable reusable name is being minted, and `E.8` for authoring-form correction. Leave `E.9` for bounded content decisions that need rationale by value.

**Kind-or-boilerplate diagnostic.** When a DRR proposes wording for selected patterns, apply `F.19` to separate boilerplate from remaining content before any wording is treated as pasteable pattern prose. If the remaining content still hides wording-use, naming, relation, claim, admissible-use, selected-locus, user-action, or flow-role precision, the DRR names the applied `E.10`, `E.10.ARCH`, `F.18`, or governing pattern. Process, architecture, review, or reference boilerplate belongs in its own carrier, not in pasteable pattern prose.

Wording proposed in a DRR is not pasteable pattern prose until the selected-answer basis includes a kind-restoration check. The record must expose the pre/post object, relation, claim, slot, use, admissibility, and scope readings—or explicitly record a semantic rather than editorial change. Nicer wording is not decision evidence when it narrows a graph into a sequence, turns method into work, widens evidence into assurance, or changes a kind/use relation. The DRR cites each direct governor; it does not redefine slot, lens, role, method, work, evidence, assurance, gate, or decision ontology.

**Primary EntityOfConcern in plain terms.** For one DRR episteme, the EntityOfConcern is the exact bounded FPF content-decision question or coordinated change set. Its ClaimGraph states the selected-answer decision result, rationale, consequences, distribution, exclusions, and reopen boundary. The DRR record, method, decision work, acceptance status, assessment, and later Core realization are not that EntityOfConcern.

**Primary working reader.** The first working reader is an FPF author, reviewer, or steward who must evaluate, challenge, or land one bounded content decision. Downstream pattern readers benefit from the landed Core text; they are not the primary reader of the DRR itself.

