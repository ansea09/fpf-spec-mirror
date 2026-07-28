---
chunk_kind: "child"
pattern_id: "E.19"
pattern_title: "Pattern Quality Gates: Review and Refresh Profiles"
section_id: "E.19:5"
section_title: "Archetypal Grounding — Tell–Show–Show: System / Episteme"
source_path: "FPF-Spec.md"
output_path: "by_section/E.19/E.19__009_archetypal-grounding-tell-show-show-system-episteme.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "E.19 — Pattern Quality Gates: Review and Refresh Profiles"
  - "E.19:5 — Archetypal Grounding — Tell–Show–Show: System / Episteme"
line_start: 84253
line_end: 84260
dependencies:
  - "A.15.1"
  - "A.6.P"
  - "E.10"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
  - "(see H-8)"
  - "MUST NOT modify modeled-world entities (e.g"
  - "and (if needed) reference them from CC items"
  - "inside the predicate)"
  - "where a non-deontic Invariant: predicate is required)"
  - "“Earth”"
  - "“RoleAssignment”"
  - "“Role”"
  - "“holon”) — express those as Invariant: / Well‑formedness constraint: predicates instead"
---

### E.19:5 - Archetypal Grounding — Tell–Show–Show: System / Episteme

| Scenario | U.System grounding | U.Episteme grounding |
|---|---|---|
| **Tell** | A safety-critical engineering team proposes a new pattern describing how to gate a subsystem before deployment. The draft looks polished, but it quietly imports domain terms, assumes cross-team equivalences, and introduces requirements that are not listed in the pattern checklist. | A research group refreshes an older pattern that summarizes how to evaluate evidence-sufficiency class. The pattern still appears clear, but its SoTA references and terminology no longer match current practice, and its Relations point to patterns that were renamed or superseded. |
| **Show (failure without PQG)** | Reviewers focus on whether the idea is good and whether the template exists. The pattern is admitted, but later users disagree on what it requires because the Conformance Checklist is incomplete and key constraints are only in prose. | The pattern remains unchanged because “nothing looks broken”. Over time, it becomes a conceptual fossil: newcomers treat it as current guidance, but it encodes an outdated stance and stale vocabulary. |
| **Show (repair with PQG profiles)** | PCP‑BASE finds missing internal coherence (requirements in prose not reflected in CC). PCP‑TERM finds naming drift and scope-smuggling in new terms. PCP‑BRIDGE finds implicit cross-context identity claims without explicit alignment. The same work repairs and rechecks all three defects before admission; the final CC becomes the canonical conformance body. | Independent review records the outdated SoTA‑Echoing, excess scope, and stale Relations as findings with repair direction. The author updates the Solution and evidence, limits historical material to historical lineage, repairs Relations, and returns the changed pattern for focused verification. |

