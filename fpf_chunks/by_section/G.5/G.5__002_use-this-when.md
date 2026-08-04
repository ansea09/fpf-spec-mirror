---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__002_use-this-when.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:0 — Use this when"
line_start: 99628
line_end: 99644
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

For ordinary method-family dispatch, open `G.5` when two or more already admitted Methods are live under grounded selector rows for the same declared task and the current question is the selector-facing set result: which candidates remain admissible, whether the emitted result may truthfully order them, or whether it must be a shortlist, narrowed handoff, abstain, or escalation. If the live question is still one local choice among available options, route it through `C.11` first. Reuse already grounded method-family rows when they exist; do not rebuild a registry on every run. Create a new reusable row only when the grouping itself must recur, carry family-level policy, be versioned, or be published. Crossing, evidence/reliance, assurance, stable public identity, and actual publication are conditional branches, not an entry fee.



Before opening G.5 for method dispatch, resolve every selectable `MethodRef` to an exact `U.Method` already admitted under A.3.1. A `MethodFamilyId` is a selector-facing registry designator for a declared grouping: its row must cite the exact Methods it groups and the independently governed classification claim, membership relation, or local grouping criterion used for this selector. Neither the row, its label, a family card, a `U.MethodDescription`, an eligibility or maturity record, a policy, an evidence pin, a shortlist, nor a publication makes a candidate a Method or makes family membership obtain. Where no direct pattern admits an ontic family or membership relation, keep the row as a project-local selector grouping under its declared criterion. If only labels, descriptions, cards, or unresolved references are available, return to A.3.1, C.2.1, or the direct family-relation owner and stop before selection.

Also say whether the current claim is only a reusable registry, selector, policy, template, or result-content declaration, or whether an actual selection and publication occurred. An actual selection requires its exact acting system, dated A.15.1 Work, and actual A.6.1 `Select` application with effective argument and `SelectionSlot` bindings under A.19.SelectorMechanism. Any persisted result episteme, A.10 evidence-provenance relation, B.3 assurance claim, authorization, and E.24.PUB publication occurrence remain separate. A row, declaration, record, telemetry pin, or selected-set label supplies none of them by appearance.



- several method families or generator families can admissibly act on the same declared task family or work target
- you need one selector to return a `Shortlist`, `RankedShortlist`, one `SpecialistHandoff`, one other narrowed handoff plan, or one abstain outcome without pretending that there is always one scalar winner
- the published result must carry enough basis pins for later comparison, handoff, or escalation without changing its declared outcome kind or any applicable public selected-set label

