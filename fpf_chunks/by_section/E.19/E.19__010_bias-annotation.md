---
chunk_kind: "child"
pattern_id: "E.19"
pattern_title: "Pattern Quality Gates: Review and Refresh Profiles"
section_id: "E.19:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.19/E.19__010_bias-annotation.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "E.19 — Pattern Quality Gates: Review and Refresh Profiles"
  - "E.19:6 — Bias-Annotation"
line_start: 88518
line_end: 88534
dependencies:
  - "A.15.1"
  - "A.6.P"
  - "E.10"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
  - "(see H-8)"
  - "inside the predicate)"
  - "under E.8 H-8 and CC-SG.4"
  - "where a non-deontic Invariant: predicate is required)"
---

### E.19:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** (applies to all patterns and all clusters).

Bias risks and mitigations:

* **Governance bias (Gov):** reviewers may over-prioritize compliance signals and under-prioritize teaching value.
  *Mitigation:* PCP‑BASE checks didactic grounding and internal coherence and prioritizes ontology and semantics.
* **Architecture bias (Arch):** internal package architecture can displace the problem-owning domain or practice.
  *Mitigation:* test EntityOfConcern, narrowed branch, and practical payoff against the domain/practice question and relevant SoTA under `CC-E19-7`.
* **Epistemic monoculture (Onto/Epist):** SoTA‑Echoing can become single-tradition name-dropping.
  *Mitigation:* use multiple traditions when the question or claimed breadth requires them; make substantive disagreement visible. Use F.18 for neutral durable naming when its use condition applies.
* **Pragmatic bias (Prag):** a pattern can be “correct” yet unusable.
  *Mitigation:* consequences and anti-patterns remain mandatory sections, surfacing material costs or limitations and grounded misuse or application boundaries under `E.8`; an already established boundary may be referenced.
* **Didactic bias (Did):** narrative quality can be mistaken for truth.
  *Mitigation:* conformance and SoTA‑Echoing sections bind claims to explicit requirements and lineage.

