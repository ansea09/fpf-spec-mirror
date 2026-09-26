---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Naming and Semantic Unification"
section_id: "F.15:15"
section_title: "Closure conditions"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__019_closure-conditions.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Naming and Semantic Unification"
  - "F.15:15 — Closure conditions"
line_start: 107764
line_end: 107778
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.6"
  - "A.2.7"
  - "A.22"
  - "A.6.1"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.24.PUB"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.6"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
  - "Bridge"
  - "NameCard"
  - "RSCR"
  - "SCR"
  - "SchemeSenseCell"
  - "UnifiedTermRow"
  - "exact versions"
  - "finite naming slice"
  - "regression"
  - "result reuse"
  - "static conformance"
---

### F.15:15 - Closure conditions

A finite slice is locally admissible for its named receiving use only when:

1. every scope member and exact version resolves under its identity rule and PatternID locator;
2. every triggered static rule has an exact current C.2.1 `pass` result for the named receiving use; a `fail` or `undetermined` result leaves the affected use unadmitted;
3. every changed member has an exact prior/later pair and a current passing RSCR result supporting the stated continuity/change, admitted losses and receiving use;
4. every failed subject claim needed by the use is repaired and re-evaluated under its defining or testing rule, and the affected F.15 rule then passes before reuse;
5. witness refs and any relied-on A.10/B.3 path are current for the exact result and use, without becoming the result;
6. the optional record cites, but does not replace, applications/work, result claims, evidence, Bridge occurrences, descriptions, publication, or currentness;
7. tempting non-admitted uses—system-role assignment, performed work, source or publication authority, status transfer, evidence use, equivalence, assurance, gate passage, and authorization—are explicit; and
8. the closure statement names the exact slice versions, rule set, currentness basis, and receiving use.

Closure is local. A later change reopens only the affected rule results and their dependents after contradiction checks. It does not authorize a full rerun by habit or a global claim that all names, rows, relations, evidence, and publications conform.

