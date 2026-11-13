---
chunk_kind: "child"
pattern_id: "B.4.1"
pattern_title: "Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)"
section_id: "B.4.1:13"
section_title: "Worked Route Sets"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4.1/B.4.1__014_worked-route-sets.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "B.4.1 — Publish Candidate Routes for a Stabilized Cue (RoutedCueSet)"
  - "B.4.1:13 — Worked Route Sets"
line_start: 48026
line_end: 48051
dependencies:
  - "A.15"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.6.A"
  - "A.6.P"
  - "B.4"
  - "B.5.2"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.22.1"
keywords:
---

### B.4.1:13 - Worked Route Sets

#### B.4.1:13.1 - Multi-route operator case
An operator alert note records a service-latency rise after a configuration change and a response-time clause whose applicability to this service is unresolved. The operator may publish a route set containing:

- `ActionInvitationRoute`,
- `ProblemAbductionRoute`,
- and `RequirementCommitmentRoute`.

Keep the live routes explicit and state any selection with its grounds. The missing discriminator for `RequirementCommitmentRoute` is whether the clause covers this service and incident window. If it does, use `A.2.8` for the question of a duty; the latency cue can support intervention and explanatory inquiry.

#### B.4.1:13.2 - Inquiry case
A conceptual mismatch may route simultaneously toward:

- explanatory inquiry,
- probe design,
- and later lexical repair.

This is admissible only if the route rationale states the plurality.

#### B.4.1:13.3 - Invalid jump
It is invalid to treat a routed cue set as if it were a hypothesis, a gate, or a work plan. The route-bearing publication form records candidate continuations; the subject pattern governs the downstream result.

#### B.4.1:13.4 - Specialization-route and nonhuman-utility split
A routed cue set for a new task family may keep `ProblemAbductionRoute`, `TaskFamilySpecializationRoute`, and `NonHumanUtilityRoute` live together. The point is to preserve the declared task family, utility target, any qualifying budget conditions, any unresolved facts needed for use or selection, and any relevant corridor-entry conditions without presenting those candidates as a justified prompt, selector, or policy choice.

