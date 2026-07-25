---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__002_use-this-when.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:0 — Use this when"
line_start: 96265
line_end: 96271
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

### G.5:0 - Use this when
When loop-engineering work retains several loop candidates, harness variants, method families, workflow-store entries, or DPF framework candidates for downstream use, use `G.5` only when the live claim is selector-facing publication of that retained set. The published result states the outcome kind, retained members, ordering status if any, and basis pins. It does not prove that any member improved, that work occurred, or that a local choice has been made.

- several method families or generator families can admissibly act on the same declared task family or work target
- you need one selector to return a `Shortlist`, `RankedShortlist`, one `SpecialistHandoff`, one other narrowed handoff plan, or one abstain outcome without pretending that there is always one scalar winner
- the published result must carry enough basis pins for later comparison, handoff, or escalation without changing its declared outcome kind or any applicable public selected-set label

