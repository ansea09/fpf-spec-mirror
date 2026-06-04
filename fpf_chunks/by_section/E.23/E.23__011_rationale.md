---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__011_rationale.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:10 — Rationale"
line_start: 69327
line_end: 69344
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.19.1"
  - "C.22.1"
  - "C.24"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.23:10 - Rationale

Quality improvement is not the same problem as quality review. A review can answer one framed question about one object version under improvement. Improvement changes the object under improvement and then asks whether the changed object version is better under the declared object-under-improvement evaluation.

The separation keeps the first pass affordable. `A.19.ECS` constructs or repairs a missing object-under-improvement evaluation `CharacteristicSpace`; `E.22` frames the read; `E.21`, `E.9.DA`, `E.2.DA`, `F.18`, `C.25`, or another evaluation supplies values; `E.23` governs repetition, absorption, re-read, cost and risk account, method-family selection, and stopping.

Classical cycles and agentic loops become useful when treated as candidate method families rather than as universal law. POOGI optimizes throughput and constraint selection; PDCA and PDSA optimize learning and stabilization against declared measures; OODA optimizes orientation quality under changing conditions; Ralph-like loops approximate a broad adaptive agent repeatedly working from specification, feedback, verification, and memory. `E.23` asks whether the method family fits the object-under-improvement evaluation and whether the next pass is still worth its cost.

The method also protects against over-optimization. Improvement is multi-characteristic optimization by changes that produce non-dominated gains or explicitly accepted trade-offs, not one scalar quality score.

The `NQD` connection gives a precise reading of "space of characteristics" when open-ended improvement is live: those characteristics can be the declared `Q` components of the comparison. `E.23` can then govern repeated object changes that move one candidate or declared transduction result against an externally declared comparison set, accepted `SoTA` line, or current front. That does not make `E.23` the generator, archive, selector, parity, or refresh pattern.

This also distinguishes `SoTA` from loop-internal improvement. `SoTA` names the working external front at the time of the read. A loop can try to reach that front, maintain it as sources change, or test a front-improving proposal by combining several accepted source or practice lines into one `SourceComposedResultClaim` that the single lines did not already provide. The claim is only admissible when the object-under-improvement evaluation can read that result claim and the protected characteristics together.

`E.23` applies that rule to loops that use it. A loop's source composition can be multi-stratum: classical improvement cycles contribute explicit learning and stop discipline; BLP contributes cost and general-method preference; agentic-loop practice contributes optional operation families; SkillOpt-like work contributes fixed-performer object-version-under-improvement optimization; MCDA and Goodhart lines contribute protected trade-off and proxy checks; OEE/NQD contributes `Q`-side comparison, fronts, and proposal portfolios. The combined result is an improvement-loop method instance that remains cheap for floor reads, useful for externally assigned `SoTA` reach or maintenance, and bounded by neighbours.

The stop rule is deliberately local. Reaching all `5` values or the current non-dominated front means the current loop has no better admissible move under the named object-under-improvement evaluation, `Q` components, externally declared comparison basis, protected trade-offs, and cost boundary. It does not say development is complete forever. It says the next improvement question needs a changed use, changed comparison, changed source, changed `SoTA`, changed cost boundary, or another exact reason to reopen.

