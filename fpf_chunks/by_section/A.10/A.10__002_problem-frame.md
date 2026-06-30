---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
section_id: "A.10:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__002_problem-frame.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.10 — Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
  - "A.10:1 — Problem frame"
line_start: 19962
line_end: 19984
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.4"
  - "A.2.8"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6"
  - "B.1.1"
  - "B.3"
  - "B.4"
  - "C.16"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "E.17"
  - "E.17.EFP"
  - "F.9"
keywords:
  - "SCR/RSCR"
  - "authority-reliance evidence path"
  - "claim support"
  - "evidence"
  - "evidence carrier"
  - "exact authority reference"
  - "generated-explanation source support"
  - "probe/distributed/export/causal evidence"
  - "provenance"
  - "register excerpt"
  - "status register"
  - "traceability"
---

### A.10:1 - Problem frame

Use this pattern when a claim, metric, model result, dashboard tile, confidence badge, review note, credential, provenance label, quantum-like statement, causal-use statement, or generated explanation starts acting as evidence while the evidence carrier, evidence-producing work, method trace, time window, source-currentness relation, or rival explanation is still implicit.

**Primary EntityOfConcern.** The `EntityOfConcern` is the claim-bound evidence-provenance graph relation: the path in the evidence-provenance graph that links one named claim or effect to concrete carriers, evidence-producing or evidence-interpreting work occurrences, role assignment when current, method trace or work trace, time stance, and admissible evidence use.

**First useful move.** Write the smallest because-graph that can answer: which claim or effect, which carriers, which evidence-producing or evidence-interpreting work occurrence and role assignment when current, which method or work trace, which time window, which evidence relation, and which bounded use?

**What goes wrong if missed.** Claims become weightless, dashboards become authority, provenance becomes truth, credentials become permission, generated explanations become evidence, method descriptions get mixed with work traces, and part-whole structure is mistaken for evidence.

**What this buys.** One bounded evidence relation that can be replayed, contested, refreshed, narrowed, or used by a neighboring governing pattern without making evidence pretend to be approval, permission, gate passage, performed work, assurance, causal authority, or part-whole structure.

**Ordinary use.** For routine source-finding, orientation, bounded reversible probes, and low-stakes evidence use, keep the evidence relation small: claim, carrier, producer or source-maintenance role assignment, method trace or work trace when relevant, time window, bounded evidence use, unsupported attempted use, and reopen trigger.

**Reliance-facing use.** Expand the evidence relation only when consequence severity, reuse, contestability, cross-context movement, source-currentness risk, credential reliance, provenance reliance, gate use, release use, assurance use, work use, causal-use claim, or privacy boundary makes the extra field decide the current claim.

**Not this pattern when.** Not this pattern when the current claim is authorization, commitment, performed work, gate decision, assurance, causal identification, measurement construction, representation-scheme transition, explanation faithfulness, or source publication use itself. In those cases, use the neighboring governing pattern and let A.10 supply only the evidence-provenance graph relation it needs.

Use `A.2.4` first when the immediate question is only whether an episteme is being used as evidence or status for a claim, before a full evidence-provenance graph relation is needed. A.2.4 keeps episteme evidence-use and status-use relation slots distinct from `U.RoleAssignment`; A.10 then owns the full claim-bound evidence-provenance graph relation when the carrier, producer, method trace, work trace, time window, and provenance relation must be replayable.

Here `path` means a path in the evidence-provenance graph, not a route for actions to follow.


