---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:0.2"
section_title: "What this buys"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__004_what-this-buys.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:0.2 — What this buys"
line_start: 96279
line_end: 96287
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "C.35"
  - "G.0"
  - "G.2"
  - "G.2-G.4"
  - "G.5"
  - "G.6"
  - "G.9-G.11"
  - "G.Core"
keywords:
  - "RankedShortlist"
  - "SelectorOutcomeKind"
  - "Shortlist"
  - "ShortlistId"
  - "SpecialistHandoff"
  - "abstain/escalation result"
  - "are forbidden in registry"
  - "assurance"
  - "basis pins"
  - "dispatcher"
  - "eligibility"
  - "generator-family registry"
  - "in core registry and eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set publication"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:0.2 - What this buys

- one registry that keeps rival method families disjoint but dispatchable
- one selector result form that can publish candidate sets, `Shortlist`, `RankedShortlist`, one `SpecialistHandoff`, narrowed handoff plans, or abstain outcomes honestly
- one trace addressable by DRR and SCR records with explicit basis pins instead of one hidden selector rationale
- one explicit publication closure so the declared outcome kind, any applicable public selected-set label, retained members or handoff content, ordering status, and basis pins are stated directly in the emitted result

Registry and dispatch remain the primary selector question here; selected-set publication is the explicit closure record for that selector question, not a replacement for it.

