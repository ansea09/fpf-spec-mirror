---
chunk_kind: "child"
pattern_id: "E.13"
pattern_title: "Pragmatic Utility and Value Alignment"
section_id: "E.13:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/E.13/E.13__002_use-this-when.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "E.13 — Pragmatic Utility and Value Alignment"
  - "E.13:0 — Use This When"
line_start: 79941
line_end: 79966
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "E.12"
  - "E.14"
  - "E.19"
  - "E.2"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
keywords:
  - "Campbell"
  - "Goodhart"
  - "minimally viable value slice"
  - "pragmatic utility"
  - "proxy-to-value alignment"
  - "surrogation"
---

### E.13:0 - Use This When

Use this pattern when a project treats a visible measure, score, proxy, benchmark, dashboard, quality value, review result, release posture, or evidence volume as if it were the practical value or objective itself.

Typical moments:

- a metric improves, but the team cannot say what intended value improved;
- a quality score, all-`5` posture, assurance level, citation count, source count, or review pass becomes the target;
- a proxy is used as a gate, incentive, resource-allocation signal, reputation signal, or release argument;
- a model, method, pattern, or system is formally better while users, operators, safety, maintainability, learning, or decision quality get worse;
- an evaluation loop adds apparatus to satisfy the evaluator instead of improving the object of concern.

**First useful move.** Name the intended value or objective, name the proxy or visible measure, and state how that proxy is being used now: measure, target, incentive, gate, release argument, decision driver, reputation signal, repair target, or orientation cue.

**What goes wrong if missed.** The team optimizes the proxy and loses the value. It can produce a better score, cleaner review proof, larger source packet, or more complete record while practical utility gets worse.

**What this buys.** FPF can keep measurement, evaluation, and quality loops useful without letting their visible outputs replace the value they were meant to serve.

**Not this pattern when.**

- If the question is whether a measurement scale is admissible, use `C.16`.
- If the question is ordinary pattern quality, use `E.21`; use `E.13` only when a visible quality value is being treated as the practical value.
- If the question is DRR adequacy, use `E.9.DA`; use `E.13` only when DRR marks become a surrogate for decision usefulness.
- If the question is whole-FPF Pillar adequacy, use `E.2.DA`; use `E.13` only when Pillar values become the target.
- If the question is assurance, gate passage, evidence sufficiency, or decision authority, use the governing pattern for that claim before treating the visible proxy as value.

