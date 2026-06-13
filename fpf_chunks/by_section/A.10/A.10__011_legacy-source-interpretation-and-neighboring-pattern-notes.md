---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
section_id: "A.10:10"
section_title: "Legacy source interpretation and neighboring-pattern notes"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__011_legacy-source-interpretation-and-neighboring-pattern-notes.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "A.10 — Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
  - "A.10:10 — Legacy source interpretation and neighboring-pattern notes"
line_start: 19433
line_end: 19446
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.8"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "B.1"
  - "B.1.1"
  - "B.3"
  - "B.4"
  - "C.16"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "E.17.EFP"
  - "F.9"
keywords:
  - "SCR/RSCR"
  - "authority-reliance evidence path"
  - "claim support"
  - "evidence"
  - "evidence carrier"
  - "exact authority reference"
  - "generated-explanation source support"
  - "probe/distributed/export/causal evidence"
  - "provenance"
  - "register excerpt"
  - "status register"
  - "traceability"
---

### A.10:10 - Legacy source interpretation and neighboring-pattern notes

Legacy sources may use names such as `manifest`, `release manifest`, `creator`, `observer`, `symbol register`, `SCR`, `RSCR`, `MIC`, or evidence `path` without the current FPF distinctions. Treat those names as recovery prompts, not as live vocabulary to copy unchanged.

Use these recoveries:

- a source register used for evidence carriers becomes a `Symbol Carrier Register (SCR)`;
- a release-context source register becomes a release-scoped SCR or RSCR when the bounded context, identifiers, and hashes matter for publication or release use;
- an internal `creator` or `observer` used as evidencer becomes an external `TransformerRole` or source-maintenance role assignment when the claim needs externality;
- a method instantiation note is a method relation or work relation only when it states the `U.Method`, the method-description source, ordering relation when relevant, and work-trace relation;
- resource rosters in `Γ_work` remain separate from evidence-carrier registers; cite meter, log, or observation carriers through the evidence-provenance graph.

When a legacy source also claims approval, permission, gate passage, assurance, causal authority, measured comparability, representation shift, or publication-face effect, keep A.10 to the evidence-provenance graph relation and apply the neighboring governing pattern for that extra claim.

