---
chunk_kind: "child"
pattern_id: "C.2.P.DR"
pattern_title: "Repair Claims Based on Declarative Form Alone (Declarative Representation Precision Restoration)"
section_id: "C.2.P.DR:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P.DR/C.2.P.DR__002_use-this-when.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.2.P.DR — Repair Claims Based on Declarative Form Alone (Declarative Representation Precision Restoration)"
  - "C.2.P.DR:0 — Use this when"
line_start: 53982
line_end: 54011
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.19"
  - "A.19.SPR"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "E.8"
  - "F.19"
keywords:
---

### C.2.P.DR:0 - Use this when

Use this pattern when the appearance of a representation is being used to establish an operational or classification claim without its required grounds—for example, treating a green dashboard tile as release permission or a graph path as prescribed work.

**First useful move.** Identify the expression and the claim being inferred from it. Recover what the expression actually states or represents, then apply the rule for the disputed claim. Return wording that preserves the supported use and identifies what remains unestablished. A sentence can suffice. Use a `DeclarativeRepresentationRepair` note only when the receiving use needs a separately inspectable repair.

**Quick example.** A heat-flow graph in a reactor-cooling review can show preserved and lost flow relations. It does not authorize a valve change by graph shape. The repair keeps the graph path as graph structure, returns release or gate reliance to the gate, source, and evidence patterns, and blocks the hidden work-permission claim.

Use this pattern especially when:

- a graph path or selected flow structure is treated as a prescribed work sequence;
- an `A.10` evidence path is treated as permission, release or assurance;
- a query plan or program-like expression is treated as a method or as performed work;
- a publication or pattern reference is treated as an actual call, send or application;
- method-like wording leaves the way of doing, its description and an actual episode indistinguishable.

**What goes wrong if missed.** A reader relies on an effect that the expression does not establish. The green tile may report a status while the required release decision is absent; program-like text may be mistaken for a method without identifying a way of doing.

**What this buys.** The reader can retain a useful graph, query or publication while resolving the disputed operational claim under its own rule. An object under direct inspection stays distinct from a representation of that object.

**Not this pattern when.**

- If the graph path, `PathSlice`, or flow valuation is already current as graph structure, use `E.18` directly.
- If the evidence relation or provenance relation for a claim is already current, use `A.10` directly.
- If the publication face or source-use relation is already current, use `E.17`, `E.17.EFP`, `C.2.P`, or the direct publication pattern.
- If the current claim concerns a semantic way of doing, use `A.3.1`; if it concerns the description of that way, use `A.3.2`.
- If the current claim concerns operation algebra, laws, admissibility predicates, transport, audit, or governing-definition assignment, use `A.6.1` or `E.20`.
- If the current claim concerns planned work or dated work, use `A.15.2` or `A.15.1`.
- If the word is only quoted source wording or ordinary navigation prose with no FPF-governed claim, keep it quote-only or ordinary.

