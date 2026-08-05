---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation - Windowed Role-State Recognition and Work Admission"
section_id: "A.2.5:10"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__013_consequences.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.2.5 — RoleStateRelation - Windowed Role-State Recognition and Work Admission"
  - "A.2.5:10 — Consequences"
line_start: 4700
line_end: 4718
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:10 - Consequences

Benefits:

- one assignment can support several separately identifiable state episodes;
- simultaneous predicates remain expressible without pretending every case is a single-state automaton;
- state truth, state assertion, evidence use, and work admission can change independently and be repaired locally;
- method and gate patterns receive an exact current relation instead of a status label;
- physical, social, organizational, and computational role-state cases use the same relation discipline.

Costs and limits:

- load-bearing state predicates must be written by value, including temporal semantics;
- consequence-bearing use needs evidence currentness and an explicit direct consumer;
- cross-taxonomy reuse may need a bridge rather than label matching;
- A.2.5 does not define every subject-domain state predicate, measurement method, authorization relation, or state-change method.

Reopen or lower only the affected claim when the assignment episode, by-value predicate, actual role-state extent, receiving-use evaluation window, effective scheme, evidence relevance, direct consumer rule, or interpretation-changing model-use selection changes. Do not rewrite the role value or assignment when only one role-state episode changes.

