---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:9"
section_title: "Conformance Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__011_conformance-checks.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:9 — Conformance Checks"
line_start: 96869
line_end: 96894
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.PUB"
  - "F.0.1"
  - "F.1"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:9 - Conformance Checks

Use these checks before a durable name is reused in a pattern. If an F.17 row is current, run its own row checks after the section 4.4 gate; these F.18 checks neither create that row nor establish a publication occurrence for it.

| Check | Passing condition |
| --- | --- |
| Governed value | The named value is recoverable and belongs to a direct governing pattern. |
| Interpretation | The effective `U.ReferenceScheme` is carried by value and the local sense is named; model-use structure, claim scope, project work, and other locality relations remain separate. |
| Kind | The kind is stated as governed value kind, not inferred from spelling. |
| Candidate set | The smallest set covers at least two live head families and every plausible neighbouring-object reading; any forced untested exception is explicit in `CandidateCoverage` and `RefreshCondition`. |
| Role boundary | Role, role assignment, holder, capability, method, work, evidence, and status claims are not collapsed. |
| Relation-object boundary | Predicate-definition episteme, admitted relation kind, obtaining occurrence, representation element, and designator are named only after their separate governing settlements; relation slot, interface, port, and signature names cite direct governing patterns. |
| Public row | A durable local card is enough unless public, Core-facing, durable-across-context, or cross-context reuse is current. The section 4.4 gate passes before any F.17 row is cited; the row is neither the value nor the publication occurrence. |
| Bridge and bounded use | `F.9` governs an exact sense relation only between different `<ReferenceScheme, LocalSenseClaim>` projections. Same projection plus another expression is designation; same scheme plus another claim can open F.9; scheme difference opens only the question; no current correspondence use creates no Bridge or use claim. A separate C.2.1 claim says whether an obtaining Bridge suits the named naming use, and A.10 or B.3 governs reliance. None authorizes or proves that reuse occurred. |
| Local-plain non-use | A one-off claim about whether an exact Bridge suits a named use stays in ordinary wording. No `NameCard`, public claim kind, or durable CamelCase name is created unless an independent later reuse need reopens F.18. |
| Lineage and reopen | Rename, alias, split, merge, and retirement history is recorded under `F.13`, and the card names the smallest value, scheme, sense, owner, use, or reader-error change that reopens this settlement. |
| Reader use | A practitioner can tell what to say, what not to infer, and where to go if the name is not enough. |
| Work-name boundary | An action nominal remains a morphology cue: a hidden claim-bearing function-like use goes through `A.6.F`, while an already recovered method, method description, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, or other value is named only under its direct pattern. A WBS/Work Package label remains plan- or assignment-episteme content, and a performed-work name is accepted only for one occurrence grounded under `A.15.1`; neighboring production claims, measurement results, evaluation results, decisions, delivery occurrences, and acceptance verdicts stay under their direct governors. |

Regression checks:

- When either the effective reference-scheme edition or the `LocalSenseClaim` changes, compare the resulting semantic-context projections. Re-check any obtaining Bridge, the separate claim about the named use between different projections, and that claim's current reliance; same-projection expression changes stay with designation, and no current correspondence use creates no Bridge or use claim.
- When a role description changes, re-check role name and any holder-assignment name.
- When a method, capability, work, evidence, or status pattern changes, re-check any name that borrowed morphology from that area.
- When repeated reader errors occur, reopen candidate comparison instead of adding aliases indefinitely.

