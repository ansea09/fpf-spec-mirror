---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Relation"
section_id: "B.2.5:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__007_archetypal-grounding-worked-cases.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Relation"
  - "B.2.5:5 — Archetypal Grounding (Worked Cases)"
line_start: 41751
line_end: 41782
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
  - "A.6.RCD"
  - "B.1"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30.LCA"
  - "E.10"
  - "F.19"
  - "G.6"
keywords:
---

### B.2.5:5 - Archetypal Grounding (Worked Cases)

#### B.2.5:5.1 - Robotic Swarm

A fleet controller C supervises drone d1. In this illustrative protocol R1, each control tick requires a same-tick range report received by C and a returned command received by d1. The command is generated from that report: reduce speed when the reported obstacle distance is below 2 m; otherwise maintain speed. These protocol predicates govern reporting, command delivery and their coupling for this case; they do not establish sensor accuracy or safety.

| Case facts under R1 | Compound result |
| --- | --- |
| At tick 10, C receives d1's 1.2 m report, generates `reduce speed` from it under R1, and d1 receives that command. | All three conjuncts hold for {d1} at tick 10. |
| At tick 11, C receives telemetry, but the only delivered command is an unrelated scheduled broadcast. | The known command has no R1 coupling to that report; it does not satisfy this feedback predicate. |
| At tick 12, the report arrives but the complete tick trace shows no returned command. | The return conjunct fails. Reporting remains an independently supported fact. |
| At tick 13, the link breaks and the complete trace shows no same-tick report or return. | The claim covering every tick 10–13 fails under R1. A supervisor assignment may still continue under its own rule. |
| At tick 14, the link reconnects and a new report, R1-based command and delivery are established. | The tick-14 claim is supported from those new facts; the earlier interval does not become uninterrupted. |

If the tick-13 trace is unavailable, the corresponding conclusion is unresolved instead of negative. If R1 changes to R2, use R2's actual coupling test for the new interval. Adding d2 requires d2's own report, return and coupling facts before asserting feedback for {d1,d2}.

A C.30.LCA description consumes the report and command relation references plus the compound assertion. It need not invent a single feedback occurrence to draw the supported connection. Claims about convergence, delay tolerance, disturbance damping, evidence, assurance or safety use their subject patterns.

#### B.2.5:5.2 - Scientific Theory Revision

A theory is revised when labs publish findings and a research community reviews anomalies and accepted revisions.

B.2.5 can state feedback around review and revision when the reviewed object is independently admitted as a Holon and the report, returned revision influence and coupling rule are established. Otherwise retain the independently supported review or source-use claims. Recover the exact admitted System that performs the review or revision, whether it is a research community, standards body, lab, review board, or tool-mediated group; any local system-role kind and assignment are separate claims. The theory remains the reviewed or revised episteme.

For publication channels, journals, datasets, reports, and review records, keep each object's identity distinct from its current publication or source-use relation; recover content, form, representation, or carrier only when the case depends on that distinction.

#### B.2.5:5.3 - Product Platform Policy

A product platform constrains component teams through interface rules and release gates. B.2.5 states the component reports, returned constraints and rule coupling those constraints to the reports for the admitted platform or governance system; a system-role kind or assignment is added only when separately current.

Work alignment uses `A.15`; a separate work-authority claim needs its own direct pattern. Gate passage uses `A.21`; `A.6.M` restores interface wording before the exact commitment claim returns to its direct pattern; architecture view uses `C.30.LCA` when the control structure is described.

