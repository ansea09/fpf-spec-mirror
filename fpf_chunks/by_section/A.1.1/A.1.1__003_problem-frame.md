---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "Bounded Model-Use Structure and DDD Bounded-Context Recovery"
section_id: "A.1.1:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__003_problem-frame.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "A.1.1 — Bounded Model-Use Structure and DDD Bounded-Context Recovery"
  - "A.1.1:1 — Problem frame"
line_start: 1943
line_end: 1954
dependencies:
  - "A.1"
  - "A.14"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.17.0"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
---

### A.1.1:1 - Problem frame

**Use this when.** Use this pattern when a current decision depends on the organization of three distinguishable facts about one exact model edition: where it applies, how it is actually used in assigned Work, and whether maintained expression content remains coherent with it. Physical location, team ownership, a document title, or the word *context* is not enough.

**First useful move.** State the decision, model, and use locus; recover only the direct relation that answers the question and stop when it suffices. Select the wider structure only when several already governed relations, applied constraints, and one exact selection-use frame together change the decision.

**What goes wrong if missed.** Systems, Work, epistemes, and publications are merged into a context-shaped proxy. One subsystem under two models is treated as one context by location, while one model used coherently across several loci is split by an implementation boundary. Local vocabulary, rules, units, status, or evidence use is also forced into a context object even when a direct semantic-locality pattern answers the question.

**What this buys.** Actual participants retain their identities. Applicability, use, and fixed-content coherence remain inspectable direct relations; their decision-relevant organization can be selected as `U.Structure`; and ordinary semantic locality is stated through its exact value and relation assertion, with the subject pattern kept only as a locator.

**Not this pattern when.** If only a term sense, local system-role-kind value, system-role-assignment occurrence, relation among system-role kinds, rule or invariant, admissible inference, unit or measurement basis, status, evidence use, claim scope, description, publication, or direct relation is current, use the A.1.1:4.4 triage and stop at that direct result. Do not select `BoundedModelUseStructure` unless the relation organization itself changes the decision.

