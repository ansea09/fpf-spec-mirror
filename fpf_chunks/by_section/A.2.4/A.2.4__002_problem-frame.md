---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__002_problem-frame.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:1 — Problem Frame"
line_start: 4661
line_end: 4682
dependencies:
  - "A.10"
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10.D2"
  - "E.10.ROLE"
  - "E.17"
  - "F.10"
  - "G.11"
  - "G.6"
  - "U.SystemRoleAssignment"
keywords:
  - "claim"
  - "episteme"
  - "evidence-use relation"
  - "provenance"
  - "role-shaped source phrase"
  - "source-use wording"
  - "status-use relation"
---

### A.2.4:1 - Problem Frame

Use this pattern when an episteme, such as a report's content, is being used as evidence, source, status bearer, assurance input, or causal-use input for a claim.

Use it when the working question is:

* which episteme is being used;
* which claim, theory statement, status assertion, use, or causal-use question the episteme is being used for;
* which effective source scheme (when interpretation depends on it), ClaimScope, grounding holon, polarity, relevance window, assurance use, weight model, and provenance constraints are current;
* whether source wording such as "evidence role", "status role", "standard role", or "the report plays a role" hides an evidence-use, status-use, source-use, publication-use, assurance-use, gate-use, or causal-use relation;
* whether the evidence-use or status-use relation is sufficiently specified for the intended reliance, or only enough for orientation, source-finding, a reversible probe, or a narrowed use.

**Primary EntityOfConcern.** The `EntityOfConcern` is the evidence-use relation or status-use relation around an episteme.

**First useful move.** Name the exact episteme and the claim or governed status for which it is being used. Then point outward, when current, to the dated producing/evaluating work and actual bindings, domain-local result and direct governor, C.2.1 result episteme, A.10/G.6 provenance, G.11 currentness, receiving work and direct use relation, local `RelianceDisposition`, and B.3 assurance boundary.

**What goes wrong if missed.** Producing or evaluating work is attributed to the document itself, a dataset is treated as if it were classified under a work-facing system-role kind, a dashboard status is used as permission, a proof is used outside its theory-version fence, or a simulation-only counterfactual output is relabelled as realized causal evidence.

**What this buys.** A cheap first-use classification that identifies the episteme and its evidence-use or status-use relation. The further questions in §4.6 are answered through their direct patterns.

**Not this pattern when.** Use A.13 to identify the actual performer and A.15.1 to admit performed Work independently. If the current result must also identify the assignment under which that Work was performed, check it separately through F.6. Use A.6.1 for actual bindings, and use the exact formal, measurement, causal, diagnostic, conformance, comparison, selection, acceptance, gate, permission, commitment, system-role-kind, assignment, or decision pattern for its local result. Use C.2.1 for the result episteme, A.10/G.6 for provenance and bounded reliance, G.11 for currentness, B.3 for assurance, F.10 or another direct status pattern for status, and E.17 for publication. A.2.4 classifies only the episteme's first evidence-use or status-use.

