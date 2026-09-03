---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:9"
section_title: "Conformance Checks"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__011_conformance-checks.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:9 — Conformance Checks"
line_start: 100354
line_end: 100379
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
| Governed value | The named value is recoverable and belongs to a subject pattern. |
| Interpretation | The effective `U.ReferenceScheme` is carried by value and the local sense is named; model-use structure, claim scope, project work, and other locality relations remain separate. |
| Kind | The kind is not inferred from spelling, source, or practice. A system-role kind is already recoverable through its candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule. |
| Candidate set | The smallest set covers at least two live head families and every plausible neighbouring-object reading; any forced untested exception is explicit in `CandidateCoverage` and `RefreshCondition`. |
| System-role boundary | System-role kind, classification, assignment, holder, capability, Method, Work, evidence, status, participant meaning, declaration place, and representation position are not collapsed. |
| Relation-object boundary | Predicate-definition episteme, admitted relation kind, obtaining occurrence, representation element, and designator are named only after their separate settlements; relation slot, interface, port, and signature names cite the applicable direct patterns. |
| Public row | A durable local card is enough unless public, Core-facing, durable-across-context, or cross-context reuse is current. The section 4.4 gate passes before any F.17 row is cited; the row is neither the value nor the publication occurrence. |
| Bridge and bounded use | Apply the F.9 predicate only to exact local senses whose `<ReferenceScheme, LocalSenseClaim>` projections differ. Same projection plus another expression is designation; same scheme plus another claim can open the F.9 question; scheme difference opens only the question; no current correspondence use creates no Bridge or use claim. A separate C.2.1 claim says whether an obtaining Bridge suits the named naming use, and A.10 or B.3 supplies the reliance rule. None authorizes or proves that reuse occurred. |
| Local-plain non-use | A one-off claim about whether an exact Bridge suits a named use stays in ordinary wording. No `NameCard`, public claim kind, or durable CamelCase name is created unless an independent later reuse need reopens F.18. |
| Lineage and reopen | Rename, alias, split, merge, and retirement history is recorded under `F.13`, and the card names the smallest value, scheme, sense, subject pattern, use, or reader-error change that reopens this settlement. |
| Reader use | A practitioner can tell what to say, what not to infer, and where to go if the name is not enough. |
| Work-name boundary | An action nominal remains a morphology cue: a hidden claim-bearing function-like use goes through A.6.F, while an already recovered Method, MethodDescription, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, or other value is named only under its direct pattern. A WBS or Work Package label remains plan- or assignment-episteme content. A performed-Work name is accepted only for one occurrence whose exact actual performers have A.13 cores and which A.15.1 independently grounds. Add assignment and F.6 refs only when the naming record or receiving use expressly represents precise assignment-bound attribution; missing or failed F.6 leaves the Work name intact. Neighbouring production claims, measurement results, evaluation results, decisions, delivery occurrences, and acceptance verdicts stay under their direct patterns. |

Regression checks:

- When either the effective reference-scheme edition or the `LocalSenseClaim` changes, compare the resulting semantic-context projections. Re-check any obtaining Bridge, the separate claim about the named use between different projections, and that claim's current reliance; same-projection expression changes stay with designation, and no current correspondence use creates no Bridge or use claim.
- When a system-role-kind description changes in a way that may alter the C.3 candidate domain, membership distinction, member/non-member boundary, continuity, or the naming settlement's reader meaning, re-check the local kind name and any assignment name that depends on it. A provenance-only edit does not split the kind.
- When a method, capability, work, evidence, or status pattern changes, re-check any name that borrowed morphology from that area.
- When repeated reader errors occur, reopen candidate comparison instead of adding aliases indefinitely.

