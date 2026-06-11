---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
section_id: "A.10:10a"
section_title: "Evidence carriers for quantum-like statements"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__012_evidence-carriers-for-quantum-like-statements.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.10 — Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
  - "A.10:10a — Evidence carriers for quantum-like statements"
line_start: 18937
line_end: 18970
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.8"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "B.1"
  - "B.1.1"
  - "B.3"
  - "B.4"
  - "C.16"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
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

### A.10:10a - Evidence carriers for quantum-like statements

Use A.10 when a quantum-like statement needs evidence rather than only a local modeling note. The practical question is not "is this quantum-like source impressive?" but "which carrier evidences which minimal claim, under which time window and method?"

Evidence-relation checks:

1. State the minimal state, probe, export, or viability claim being evidenced.
2. Pin the concrete carriers: source, trace, dashboard export, report, observation, metric, work result, model output, interview, survey, or incident record.
3. State the evidence-producing role and method: who or what produced the carrier, by which method, probe, measurement, or work act.
4. State the time window, decay condition, and reopen condition.
5. State what the carrier does not show, including the most relevant rival explanation that remains plausible.
6. Choose the next pattern: stay in A.10 for carrier evidence relation, apply `B.3` for assurance claims, apply `C.16` for measurement legality, apply `F.9` for bridge or export loss, or apply a `C.26.*` pattern for the remaining probe, state, or envelope question.

For probe-coupled, distributed-state, bridge-loss, measurement-frame, or viability-envelope statements, include at least:

| Field | Required content |
| --- | --- |
| Claim | The minimal state, probe, export, or viability claim being evidenced |
| Evidence carrier | The concrete evidence carrier or carrier class |
| Evidence source or carrier kind | Source publication, witness statement, measurement result, report publication, trace record, dashboard display, work-result record, or human-statement carrier |
| Method or probe | The measurement, work act, survey, dashboard query, API query, workshop, model, or trace query that produced the carrier |
| Time window | When the evidence was produced and how long it remains fit for the intended inference |
| Confidence bounds and limits | What the carrier does not show, and what rival explanation remains plausible |
| Reopen trigger | When decision, assurance, audit, work use, or reliance use requires additional evidence |

Useful outputs:

- a local evidence note when the claim only guides discussion;
- an EPV-DAG / SCR / RSCR entry when the claim enters a published assertion;
- a B.3 assurance tuple when the claim will feed readiness, audit, release, compliance, or comparative assurance;
- a neighboring-pattern note when the carrier shows only ordinary measurement, bridge loss, or work enactment.

Do not let the label `quantum-like` carry evidence weight by itself. The evidence graph carries the claim; the math lens only explains what representational mistake the evidence is being used to avoid.

