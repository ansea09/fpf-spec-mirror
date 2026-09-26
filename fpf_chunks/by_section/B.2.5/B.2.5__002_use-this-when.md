---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Relation"
section_id: "B.2.5:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__002_use-this-when.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Relation"
  - "B.2.5:0 — Use This When"
line_start: 41624
line_end: 41653
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

### B.2.5:0 - Use This When

Use this pattern when a holon is supervised, regulated, steered, corrected, constrained, or coordinated through a two-sided feedback relation between one supervising acting system and one or more supervised holons. If the supervision is conditioned by a local system-role kind or assignment, recover that classification and exact assignment separately.

The first useful move is to recover the facts supporting the feedback claim:

```text
Which holons are supervised?
Which admitted system supervises these holons for this feedback use, under which policy and during which time window, and which local supervisor system-role kind and exact assignment obtain when that classification matters?
What observation, report, signal, publication, or source relation carries state?
What influence, constraint, objective, mode, or work change returns?
Which rule and case facts couple that return to the observation for each supervised holon?
Which transformation, work, architecture, evidence, assurance, timing,
or causal claim is being made in addition to the relation?
```

**What goes wrong if missed.** A control diagram, policy note, dashboard, publication channel, or supervisor word starts carrying part-whole, agency, safety, assurance, timing, gate, or architecture claims that belong elsewhere.

**What this buys.** B.2.5 gives a readable compound claim: for each named holon, this system receives the stated observation and returns an influence coupled to it under the applicable rule. The observation, influence and coupling facts remain separately governed; the assertion can support a control description without introducing a fused feedback occurrence.

**Not this pattern when.**

- If the question is a control-structure view, use `C.30.LCA`.
- If the question is architecture or selected structure, use `C.30`, `A.22`, and `C.30.ASV`.
- If the question is reusable dynamics, timing, rate, or temporal validity, use `A.3.3` and `C.27`.
- If the question is causal use, use `C.28`.
- If the question is evidence, provenance, assurance, or a gate decision, use `A.10`, `G.6`, `B.3`, or `A.21` respectively. Use `A.20` for its internal-constraint test in a transformation-flow structure; other constraint claims need their direct pattern.
- If module or interface wording hides the exact claim, use `A.6.M` to recover it; use the direct pattern for an already precise allocation or commitment claim.
- If the question is whole reidentification, use `B.2`.

