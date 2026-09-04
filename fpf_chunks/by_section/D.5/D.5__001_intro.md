---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__001_intro.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:intro — Intro"
line_start: 69287
line_end: 69300
dependencies:
  - "A.10"
  - "B.3"
  - "C.16"
  - "C.28"
  - "D.1"
  - "D.2"
  - "D.3"
  - "D.4"
  - "E.13"
  - "E.17"
  - "E.5.4"
keywords:
---

## D.5 - Bias Audit and Ethical Assurance

> **Type:** D-family bias-audit and ethical-assurance boundary pattern
> **Status:** Stable
> **Pattern role:** This compact pattern owns bias, fairness, impact-audit, causal-fairness audit consumption, and ethical-assurance boundary use; it does not replace D.1 through D.4.

**Use this when.** Use this pattern when a model, metric, policy, publication, decision system, recommendation, method, work plan, system, holon, or FPF claim may create bias, unfairness, human or group impact, causal-fairness overclaim, or ethical assurance risk.

**Not this pattern when.** If the ethical value frame is missing, use `D.1`. If the current question is multilevel ethics entry, use `D.2`. If the current question is to describe the sides and tension of an interlevel ethical conflict, use `D.3`. If the current question is mediation or decision use of that conflict, use `D.4`. If the current question is only evidence, causality, assurance, measurement, or architecture residual without bias, fairness, human or group impact, or ethical assurance, use the direct owner.

**What goes wrong if missed.** A model, metric, policy, publication, or decision system passes ordinary evidence or assurance checks while representation, proxy, visibility, metric, language, or human-impact bias remains hidden.

**What this buys.** Bias, fairness, human-impact, causal-fairness, and ethical-assurance concerns become auditable without replacing `D.1` through `D.4`, evidence, causal, measurement, or architecture owners.

