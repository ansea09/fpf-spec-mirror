---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher & MethodFamily Registry"
section_id: "G.5:0.4"
section_title: "First output"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__006_first-output.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "G.5 — Multi‑Method Dispatcher & MethodFamily Registry"
  - "G.5:0.4 — First output"
line_start: 79537
line_end: 79548
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
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
  - "in core registry/eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set publication"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:0.4 - First output

The first useful output from this dispatcher/registry question is one published selector outcome: one set-result outcome such as `Shortlist` or `RankedShortlist`, one `SpecialistHandoff` or other narrowed handoff plan, or one abstain/escalation result, with the outcome kind, any public selected-set label, retained members or handoff content, ordering status when relevant, and basis pins stated in one place.

If that first output still cannot be written honestly, the current publication result is not finished `G.5` publication yet.

G.5 keeps the dispatcher/registry object set here and leaves universal Part-G invariants to `G.Core`; method- or generator-specific semantics stay in their named source patterns and arrive here only through explicit pins.

When `C.11` has already emitted one local choice result, `C.19` one pool-policy result, or `C.24` one enactment-facing next move, `G.5` begins where the question becomes selector-facing publication of the retained set or narrowed handoff result rather than one more explanation of why the result looked reasonable. A conformant `G.5` pass should therefore publish the retained set, narrowed handoff, or abstain result directly, with its declared outcome kind, any applicable public selected-set label, and basis pins explicit in the result itself.

A publication result remains unfinished if the declared outcome kind, any applicable public selected-set label, retained members or handoff content, ordering status, abstain or escalation condition, or basis pins are still only implicit in upstream notes.

