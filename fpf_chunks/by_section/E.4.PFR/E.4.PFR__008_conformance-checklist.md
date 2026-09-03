---
chunk_kind: "child"
pattern_id: "E.4.PFR"
pattern_title: "Pattern-Framework Relation and Edition Discipline"
section_id: "E.4.PFR:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFR/E.4.PFR__008_conformance-checklist.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "E.4.PFR — Pattern-Framework Relation and Edition Discipline"
  - "E.4.PFR:6 — Conformance Checklist"
line_start: 72228
line_end: 72248
dependencies:
  - "A.10"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.P"
  - "A.6.RCD"
  - "B.3"
  - "C.2.1"
  - "C.32.PAD"
  - "C.33"
  - "C.33-C.35"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.11.PUR"
  - "E.17"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFAD"
  - "E.5.3"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
  - "G.5"
keywords:
---

### E.4.PFR:6 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-PFR.1 Assertion first | Every load-bearing claim has an exact subject, relation function, defining or constraining ClaimGraph, polarity, and current basis; a PFR row is optional. |
| CC-PFR.2 Named row receiver | Every row names a framework-maintenance, impact, comparison, repair, or refresh use that changes action; otherwise delete the row and retain the assertion. |
| CC-PFR.2a Smallest receiver form | A cross-relation consumer uses the generic PFR row; a dependency-impact or refresh consumer uses the dependency-specific record. Both forms appear only when one named receiver needs both, cite the same subject assertion, link explicitly, derive overlapping values from that assertion, and share one refresh rule. |
| CC-PFR.3 No owner field | No generic subject-pattern relation, owner field, pattern agency, authority, receiver, or destination is asserted. |
| CC-PFR.4 Function before label | Relation function is selected by what the claim does, not by word similarity, adjacency, table position, or graph direction. |
| CC-PFR.5 Dependency separated | Framework-edition dependency remains separate from compatibility, specialization, publication, recommendation, preservation, derivation, and evaluation. |
| CC-PFR.5a One direct dependency per record | Each `FrameworkEditionDependencyRecord` names one dependent edition, one relied-on edition, and that dependency's content refs, use, direction, reason, and refresh conditions together. Several dependencies use separate or keyed records; any aggregate is a derived projection, never parallel lists or a second maintained truth. |
| CC-PFR.5b Dependency predicate recoverable | Each positive dependency assertion names the dependent edition, relied-on edition, exact relied-on content, named use, and the case fact that makes the content required: removing it or relevantly changing it invalidates the dependent content/result or reopens the use. The assertion and any record cite the E.4.PFR:3.4 predicate. |
| CC-PFR.6 Stable direction | E.5.3 constrains allowed dependency direction and Core acyclicity only after dependency is identified; it cannot establish the relation. G.11 supplies currentness and refresh only. |
| CC-PFR.7 Compatibility independent | A positive compatibility claim names the exact pair, overlapping use, difference or interface, impact, and reopen condition. Insufficient basis yields no positive compatibility claim. |
| CC-PFR.7a Optional link only | A dependency record cites `compatibilityClaimRefs` only for a named maintenance consumer and only after the pairwise compatibility assertion exists independently; the ref creates neither claim. |
| CC-PFR.8 Carrier meanings preserved | Publication, access, preservation, admission, source, Work/tool, evidence, assurance, and currentness claims keep their exact patterns and identities. |
| CC-PFR.9 Actual-use truth | `derivedUsingRuleContent` or `evaluatedAgainstRuleContent` cites the exact actual-use claim and satisfies its strict truth condition. |
| CC-PFR.10 Analysis threshold | Candidate-family analysis exists only for a named comparison, replay, same-subject conflict, or reliance receiver and includes only candidates, axes, pairs, conflicts, and receiving-edition distinctions whose resolution can change the exact cell disposition or named receiver action. |
| CC-PFR.11 Analysis closure | The candidate universe, in-scope axes, required pairwise results, temporal cells, established family, and exactly one disposition are recomputed together for every cell whose disposition or named receiver action can change. |
| CC-PFR.12 Non-permissive boundary | A basis answer supplies no authority, permission, gate passage, Work, actual use, evidence, assurance, or reliance by implication. |

