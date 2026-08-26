---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus"
section_id: "B.3:5"
section_title: "Proof obligations"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__006_proof-obligations.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "B.3 — Trust and Assurance Calculus"
  - "B.3:5 — Proof obligations"
line_start: 38223
line_end: 38244
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.2.6"
  - "A.21"
  - "A.22"
  - "A.6.1"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.10"
  - "G.11"
  - "G.6"
keywords:
---

### B.3:5 - Proof obligations

#### B.3:5.1 - Common obligations

Every positive or narrowed B.3 result:

1. identifies the exact target claim and named assurance use;
2. cites only basis results and relations that actually bear on that use;
3. states assumptions, limitations, and unsupported stronger uses;
4. keeps target fact, claim, evidence, assessment, result, record, publication, and later use distinct;
5. names a reopen condition;
6. uses the direct domain rule for every safety, permission, access, status, release, responsibility, or controlled-action premise;
7. avoids aggregation unless its model and assumptions are explicit.

#### B.3:5.2 - Additional obligations for a calculated result

A calculated result also names every bearer, characteristic, scale, unit, dependency, calibrated mapping, aggregation rule, and calculation. It shows at least one assumption whose failure changes the result. If a rival rule is plausible at comparable effort, show why the selected rule fits the declared dependency structure.

#### B.3:5.3 - Additional obligations for replay

A replayable result adds only the Work and performance facts needed by the receiving use. Identify the assessment Work, the System that performed it, and any Method, assignment, application binding, witness, or timing fact on which competence, independence, reproducibility, contest, or redress actually depends. No record field stands in for an obtaining relation.

