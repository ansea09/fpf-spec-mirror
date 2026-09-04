---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Constraint Validity for Transformation Steps"
section_id: "A.20:7"
section_title: "Check the ordinary local result"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__009_check-the-ordinary-local-result.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.20 — Constraint Validity for Transformation Steps"
  - "A.20:7 — Check the ordinary local result"
line_start: 35092
line_end: 35111
dependencies:
  - "A.10"
  - "A.15"
  - "A.21"
  - "A.6.1"
  - "A.6.4"
  - "B.3"
  - "C.2.1"
  - "C.27"
  - "E.17"
  - "E.18"
  - "E.20"
  - "F.9"
  - "G.11"
keywords:
---

### A.20:7 - Check the ordinary local result

For an ordinary A.20 use, check only these five points:

1. **Subject and constraint (`CC-A20-1`).** Name the exact subject and the exact constraint and edition being applied.
2. **Case and applicability (`CC-A20-2`).** State the assumptions, case facts, scope, evaluation window, and why the constraint is `required`, `optional`, or `notApplicable`.
3. **Evaluation and outcome (`CC-A20-2`).** Record `evaluated` or `notRun`. For an evaluated applicable constraint, record `satisfied`, `violated`, `unknown`, or `error` under the constraint's own outcome rule.
4. **Support (`CC-A20-1`).** Give the witness, counterexample, missing-information reason, or error reason that supports that result.
5. **Complete summary (`CC-A20-3`).** Use `ConstraintValiditySummary=satisfied` only when every constraint in the complete declared required set was evaluated and satisfied.

A specialist constraint such as a stability bound, return-shape condition, or retargeting invariant is present only when its trigger in section 4.3 applies (`CC-A20-4`).

#### A.20:7.1 - Extensions only when another use is current

| Trigger | Additional check | Direct pattern |
| --- | --- | --- |
| A gate consumes the result | Keep every applicable GateFit result independently recoverable; an A.20 failure changes only the A.21 aggregate under its current rule (`CC-A20-5`). A deferred required check remains `notRun` (`CC-A20-6`). | `A.21` |
| The exact proposition in an A.6.4 bounded-use assertion q is the named internal constraint | Apply A.20 to that proposition for the stated case and return only its `ConstraintValidityResult`; keep r, q, any operation application, and the A.6.4 current-case judgement separate. A Bridge or reversibility claim enters only when separately current (`CC-A20-8`). | `A.6.4`; add `F.9` only for a separate semantic-correspondence claim |
| Publication, structure, time, refresh, evidence, assurance, or Work is current | Keep those claims in their own result or relation and follow the direct pattern (`CC-A20-9`). A.20 adds no publication-face, path, slice, scheduler, gate-profile, or gate-algebra fields (`CC-A20-7`). | `E.17`, `E.18`, `C.27`, `G.11`, `A.10`, `B.3`, or `A.15`, as applicable |

