---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:23"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__025_rationale.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:23 — Rationale"
line_start: 93007
line_end: 93012
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.17.ID.CR"
  - "E.24.PUB"
  - "F.0.1"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
keywords:
  - "A.10/B.3 reliance"
  - "LocalSenseClaim> projections"
  - "different <ReferenceScheme"
  - "exact F.17 SchemeSenseCell endpoints"
  - "inverse/composition checks"
  - "obtaining Bridge"
  - "optional CL evidence-strength shorthand"
  - "optional card"
  - "quantum/coarsening exit"
  - "relation-semantic profile"
  - "separate C.2.1 bounded-use claim"
---

### F.9:23 - Rationale

Cross-context comparison is unavoidable, but the truth of a semantic relation and the suitability of one action are different claims. Putting direction, a use rule, and tolerated loss into `BridgePredicateProfile` would reidentify the relation whenever the proposed use changed. Putting them in a separate C.2.1 claim lets one Bridge remain fixed while several uses are affirmed, rejected, narrowed, or reopened independently.

The same separation keeps evidence honest. A.10 or B.3 can reopen reliance without erasing the relation. A card can travel without becoming the relation. A proposed use can be warranted without being authorized or performed. These boundaries preserve practical reuse and make each failure local and repairable.

