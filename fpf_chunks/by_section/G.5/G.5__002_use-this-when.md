---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__002_use-this-when.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:0 — Use this when"
line_start: 102619
line_end: 102639
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

### G.5:0 - Use this when
When loop-engineering work retains several already identified candidates for downstream use—for example, loop candidates, harness variants, method families, workflow-store entries, or DPF framework candidates—or when several already identified values are all included for one named use, use `G.5` only when the live claim is the selector-facing declaration of that set result. The declared result states the outcome kind, members or keyed member entries, ordering status, named use when applicable, and basis pins. It does not prove that any member improved, that work occurred, that a local choice has been made, or that the result is available to an audience.

Use `Shortlist` or `RankedShortlist` for alternatives retained for later choice. Use `JointUseSet` only when every named member is included for one bounded use. This joint-use branch consumes exact member identities under their own rules; it does not require `MethodRef`, a method-family registry row, or Method classification for framework editions or other non-Method values.

When an earlier choice or other current inclusion basis has already fixed the exact members, use `G.5-6 DeclareSetResult` with those member refs, the named use, inclusion conditions, ordering, and sufficient basis pins. This branch declares selector-facing result content without running method-family registration or `G.5-3 Select`; non-Method members never enter those method-family operations.

For ordinary method-family dispatch, open `G.5` when two or more already admitted Methods are live under grounded selector rows for the same declared task and the current question is the selector-facing set result: which candidates remain admissible, whether the emitted result may truthfully order them, or whether it must be a shortlist, narrowed handoff, abstain, or escalation. If the live question is still one local choice among available options, first constitute the exact C.11 choice assertion under its predicate. Reuse already grounded method-family rows when they exist; do not rebuild a registry on every run. Create a new reusable row only when the grouping itself must recur, carry family-level policy, be versioned, or be published. Crossing, evidence/reliance, assurance, stable public identity, and actual publication are conditional branches, not an entry fee.



Before opening G.5 for Method dispatch, resolve every selectable `MethodRef` to an exact `U.Method` already admitted under A.3.1. A `MethodFamilyId` names the continuing selector-row lineage for one declared grouping; it does not by itself select an exact edition. `MethodFamilyRowRef := <MethodFamilyId, rowEdition>` designates one immutable row edition, which cites the exact Methods it groups and the independently established classification claim, membership relation, or local grouping criterion used for this selector. Neither the row, its label, a family card, a `U.MethodDescription`, an eligibility or maturity record, a policy, an evidence pin, a shortlist, nor a publication makes a candidate a Method or makes family membership obtain. Where no exact ontic-family or membership predicate is defined, keep the row as a project-local selector grouping under its declared criterion. If only labels, descriptions, cards, or unresolved references are available, state the blocker and use A.3.1, C.2.1, or the exact family-relation subject pattern only as a locator before selection.

Also say whether the current claim is only a reusable registry, selector, policy, template, or result-content declaration, or whether an actual selection and publication occurred. An actual selection first requires every precise performer's A.13 core and an independently A.15.1-admitted dated Work, plus the actual A.6.1 `Select` application with effective argument and `SelectionSlot` bindings under A.19.SelectorMechanism. Add F.6 only when the current selection claim also needs exact assignment-bound attribution through the same obtaining A.13 assignment. Any persisted result episteme, A.10 evidence-provenance relation, B.3 assurance claim, authorization, and E.24.PUB publication occurrence remain separate. A row, declaration, record, telemetry pin, or selected-set label supplies none of them by appearance.



- several method families or generator families can admissibly act on the same declared task family or work target
- you need one selector to return a `Shortlist`, `RankedShortlist`, `JointUseSet`, one `SpecialistHandoff`, one other narrowed handoff plan, or one abstain outcome without pretending that there is always one scalar winner or that all set results are alternatives
- the declared result must carry enough basis pins for its named downstream use—for example, later comparison, handoff, or escalation—without changing its declared outcome kind or any applicable public selected-set label

