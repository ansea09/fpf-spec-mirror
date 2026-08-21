---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Relation"
section_id: "B.2.5:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__002_use-this-when.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Relation"
  - "B.2.5:0 — Use This When"
line_start: 37377
line_end: 37405
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15.1"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.3.4"
  - "A.6.M"
  - "B.1"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.13"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30.LCA"
  - "G.6"
keywords:
---

### B.2.5:0 - Use This When

Use this pattern when a holon is supervised, regulated, steered, corrected, constrained, or coordinated through a two-sided feedback relation between one supervising acting system and one or more supervised holons. If the supervision is conditioned by a local system-role kind or assignment, recover that classification and exact assignment separately.

The first useful move is to recover the relation:

```text
Which holons are supervised?
Which admitted system supervises these holons for this feedback use, under which policy and during which time window, and which local supervisor system-role kind and exact assignment obtain when that classification matters?
What observation, report, signal, publication, or source relation carries state?
What influence, constraint, objective, mode, or work change returns?
Which transformation, work, architecture, evidence, assurance, timing,
or causal claim is being made in addition to the relation?
```

**What goes wrong if missed.** A control diagram, policy note, dashboard, publication channel, or supervisor word starts carrying part-whole, agency, safety, assurance, timing, gate, or architecture claims that belong elsewhere.

**What this buys.** B.2.5 gives a small relation record: supervised holons, supervising acting system, optional exact system-role kind and assignment, medium or publication relation, observation or report side, influence or constraint side, and the patterns that define any stronger claim.

**Not this pattern when.**

- If the question is a control-structure view, use `C.30.LCA`.
- If the question is architecture or selected structure, use `C.30`, `A.22`, and `C.30.ASV`.
- If the question is reusable dynamics, timing, rate, or temporal validity, use `A.3.3` and `C.27`.
- If the question is causal use, use `C.28`.
- If the question is evidence, assurance, gate, or constraint validity, use `A.10`, `G.6`, `B.3`, `A.20`, or `A.21`.
- If the question is module allocation or interface commitment, use `A.6.M`.
- If the question is whole reidentification, use `B.2`.

