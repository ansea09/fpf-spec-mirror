---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Method-Family Registry, Dispatch and Selected-Set Result Declaration"
section_id: "G.5:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__002_use-this-when.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "G.5 — Method-Family Registry, Dispatch and Selected-Set Result Declaration"
  - "G.5:0 — Use this when"
line_start: 113025
line_end: 113042
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
  - "JointUseSet"
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
  - "selected-set result declaration"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:0 - Use this when
When loop-engineering work retains several already identified candidates for downstream use—for example, loop candidates, harness variants, method families, workflow-store entries, or DPF framework candidates—or when several already identified values are all included for one named use, use `G.5` only when the live claim is the selector-facing declaration of that set result. The declared result states the outcome kind, members or keyed member entries, ordering status, named use when applicable, and basis pins. It does not prove that any member improved, that work occurred, that a local choice has been made, or that the result is available to an audience.

Use `Shortlist` or `RankedShortlist` for alternatives retained for later choice. Use `JointUseSet` only when every named member is included for one bounded use. This joint-use branch consumes exact member identities under their own rules; it does not require `MethodRef`, a method-family registry row, or Method classification for framework editions or other non-Method values.

When an earlier choice or other current inclusion basis has already fixed the exact members, use `G.5-6 DeclareSetResult` with those member refs, the named use, inclusion conditions, ordering, and sufficient basis pins. This branch declares selector-facing result content without running method-family registration or `G.5-3 Select`; non-Method members never enter those method-family operations.

For ordinary method-family dispatch, open `G.5` when two or more already admitted Methods are live under grounded selector rows for the same declared task and the current question is the selector-facing set result: which candidates remain admissible, whether the emitted result may truthfully order them, or whether it must be a shortlist, narrowed handoff, abstain, or escalation. If the live question is still one local choice among available options, first constitute the exact C.11 choice assertion under its predicate. Reuse already grounded method-family rows when they exist; do not rebuild a registry on every run. Create a new reusable row only when the grouping itself must recur, carry family-level policy, be versioned, or be published. Crossing, evidence/reliance, assurance, stable public identity, and actual publication are conditional branches, not an entry fee.


For Method dispatch, resolve each exact A.3.1 Method and the row's independent grouping basis under S1 (§4.2). An unresolved member or grouping basis blocks that row. If the claim concerns actual selection, use S3's application and Work-admission conditions; a result declaration alone supplies no such occurrence. S5 governs any separately needed result episteme, public identity and publication claim.

Typical selector situations include:

- Methods or generators from several families are admissible for the same declared task family or work target
- you need one selector to return a `Shortlist`, `RankedShortlist`, `JointUseSet`, one `SpecialistHandoff`, one other narrowed handoff plan, or one abstain outcome without pretending that there is always one scalar winner or that all set results are alternatives
- the declared result must carry enough basis pins for its named downstream use—for example, later comparison, handoff, or escalation—without changing its declared outcome kind or any applicable public selected-set label

