---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:9"
section_title: "Conformance Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__011_conformance-checks.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:9 — Conformance Checks"
line_start: 92967
line_end: 92991
dependencies:
  - "A.15.1"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "F.0.1"
  - "F.1"
  - "F.1-F.17"
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

Use these checks before a durable name enters a pattern or `UnifiedTermSheet`.

| Check | Passing condition |
| --- | --- |
| Governed value | The named value is recoverable and belongs to a direct governing pattern. |
| Interpretation | The effective `U.ReferenceScheme` is carried by value and the local sense is named; model-use structure, claim scope, project work, and other locality relations remain separate. |
| Kind | The kind is stated as governed value kind, not inferred from spelling. |
| Candidate set | Rejected plausible labels are visible with reasons. |
| Role boundary | Role, role assignment, holder, capability, method, work, evidence, and status claims are not collapsed. |
| Relation-object boundary | Predicate-definition episteme, admitted relation kind, obtaining occurrence, representation element, and designator are named only after their separate governing settlements; relation slot, interface, port, and signature names cite direct governing patterns. |
| Public row | `F.17` is used only for term-row publication; the row is not the value. |
| Bridge | `F.9` governs exact cross-context sense correspondence and admitted use, not governed-value identity; cross-scheme interpretation alone does not create an F.9 Bridge. |
| Lineage | Renames, aliases, splits, merges, and retirements are recorded under `F.13`. |
| Reader use | A practitioner can tell what to say, what not to infer, and where to go if the name is not enough. |
| Work-name boundary | An action nominal remains a morphology cue: a hidden claim-bearing function-like use goes through `A.6.F`, while an already recovered method, method description, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, or other value is named only under its direct pattern. A WBS/Work Package label remains plan- or assignment-episteme content, and a performed-work name is accepted only for one occurrence grounded under `A.15.1`; neighboring production claims, measurement results, evaluation results, decisions, delivery occurrences, and acceptance verdicts stay under their direct governors. |

Regression checks:

- When the effective reference-scheme edition changes, re-check local sense and bridge claims.
- When a role description changes, re-check role name and any holder-assignment name.
- When a method, capability, work, evidence, or status pattern changes, re-check any name that borrowed morphology from that area.
- When repeated reader errors occur, reopen candidate comparison instead of adding aliases indefinitely.

