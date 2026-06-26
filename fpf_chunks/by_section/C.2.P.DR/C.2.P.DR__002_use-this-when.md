---
chunk_kind: "child"
pattern_id: "C.2.P.DR"
pattern_title: "Declarative Representation Precision Restoration"
section_id: "C.2.P.DR:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P.DR/C.2.P.DR__002_use-this-when.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "C.2.P.DR — Declarative Representation Precision Restoration"
  - "C.2.P.DR:0 — Use this when"
line_start: 39759
line_end: 39788
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.19.SPR"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.1"
  - "A.7"
  - "B.3"
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

Use this pattern when a declarative representation is about to guide action, reliance, gate, release, evidence, method, mechanism, work, or pattern-application claims by its shape alone.

**First useful move.** Fill one compact `DeclarativeRepresentationRepair` note: encountered representation; representation kind; represented EntityOfConcern or claim; current source or publication relation; tempting imperative overread; recovered governing pattern; retained use; blocked overread; and stop or reopen condition.

**Quick example.** A heat-flow graph in a reactor-cooling review can show preserved and lost flow relations. It does not authorize a valve change by graph shape. The repair keeps the graph path as graph structure, returns release or gate reliance to the gate, source, and evidence patterns, and blocks the hidden work-permission claim.

Use this pattern especially when:

- a graph path, `PathSlice`, flow valuation, transformation-flow structure line, or graph expression over such a structure is overread as a prescribed work route or workflow;
- an `A.10` evidence path is overread as approval, permission, release, gate passage, or assurance;
- a query, access path, query plan, table, dashboard, schema, checklist predicate, or API description is overread as method, work plan, performed work, gate, permission, or proof;
- a publication face, source-chain relation, carrier file path, mathematical representation, method-description representation, or FPF pattern relation is overread as call, dispatch, invocation, send, receive, route, or pattern application;
- method-like wording hides whether the current claim concerns `U.Method`, `U.MethodDescription`, formal substrate, mathematical-lens use, `U.Mechanism`, `U.WorkPlan`, dated `U.Work`, evidence relation, source relation, or quote-only source wording.

**What goes wrong if missed.** The representation appears to do work it cannot do. A path "routes" a decision, a query "calls" a pattern, a dashboard "authorizes" release, a checklist predicate "runs" a process, an evidence path "permits" action, or a program-looking text becomes "the method" without recovering method semantics, method description, formal substrate, mechanism, work plan, work, evidence, or source-use relation.

**What this buys.** The working reader keeps the representation useful without making it magical. Graph paths remain graph paths, evidence paths remain evidence paths or provenance paths, queries remain representations, pattern relations remain declarative relations, and method-like wording is assigned to the current ontic slot, relation position, use relation, claim kind, or governing pattern named by value before it guides work, evidence, gate, release, assurance, or method claims.

**Not this pattern when.**

- If the graph path, `PathSlice`, or flow valuation is already current as graph structure, use `E.18` directly.
- If the evidence relation or provenance relation for a claim is already current, use `A.10` directly.
- If the publication face or source-use relation is already current, use `E.17`, `E.17.EFP`, `C.2.P`, or the direct publication pattern.
- If the current claim concerns a semantic way of doing, use `A.3.1`; if it concerns the description of that way, use `A.3.2`.
- If the current claim concerns operation algebra, laws, admissibility predicates, transport, audit, or governing-definition assignment, use `A.6.1` or `E.20`.
- If the current claim concerns planned work or dated work, use `A.15.2` or `A.15.1`.
- If the word is only quoted source wording or ordinary navigation prose with no FPF-governed claim, keep it quote-only or ordinary.

