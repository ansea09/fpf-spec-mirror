---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:0.2"
section_title: "What this buys"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__004_what-this-buys.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:0.2 — What this buys"
line_start: 99766
line_end: 99774
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "C.35"
  - "E.17"
  - "E.24.PUB"
  - "E.4.PFR"
  - "G.0"
  - "G.11"
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
- one selector result form that uses the closed `SelectorOutcomeKind` rules in §4.4b and the closed `SetResultFamily` set when the result is set-shaped
- one trace addressable by DRR and SCR records with explicit basis pins instead of one hidden selector rationale
- one explicit selected-set result that states the outcome kind, applicable public label, retained members or keyed joint-use entries, ordering, named use where required, handoff content, and basis pins instead of leaving them implicit upstream

Registry and dispatch remain the primary selector question here; the explicit selected-set result closes that question without replacing registry or dispatch.

