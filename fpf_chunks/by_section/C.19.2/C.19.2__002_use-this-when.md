---
chunk_kind: "child"
pattern_id: "C.19.2"
pattern_title: "Use-Bounded Apparatus Application"
section_id: "C.19.2:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.2/C.19.2__002_use-this-when.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.19.2 — Use-Bounded Apparatus Application"
  - "C.19.2:0 — Use this when"
line_start: 49277
line_end: 49286
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.7.1"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.22.1"
  - "C.31.ASAP"
  - "E.23"
keywords:
  - "configuration or adaptation work"
  - "declared result and guarantee"
  - "one selected apparatus"
  - "reuse horizon"
  - "setup cost"
  - "use-bounded apparatus application"
---

### C.19.2:0 - Use this when

Use this pattern when one practical result matters and a relevant method, model, formalism, assurance technique, ontology, or other direct-kind apparatus is available, but the work needed to configure and apply it may cost more than the result warrants. Start here whether one apparatus is already selected or a real choice among available alternatives has become current.

The first useful move is to name the practical use, result kind, claimed guarantee, constraints, and reuse horizon, then ask whether the next adaptation and application work can reach a useful result within the available budget. This keeps a small, adequate path small while letting repeated or high-consequence use justify richer configuration.

**Not this pattern when.** If candidate material does not yet exist, use `C.18` to generate or reframe it. If the live question is a local choice over an existing option set, `C.11` owns that choice. If the real blocker is an ontology conflation, use `A.7.1`; if it is a material conflict among FPF premises, use `A.7.2`.

The primary working reader is an engineer, method or model selector, or technical lead. The pattern describes a method; an admitted `U.System` under a current role assignment performs the dated configuration and application `U.Work` and produces a separately governed problem-facing result.

