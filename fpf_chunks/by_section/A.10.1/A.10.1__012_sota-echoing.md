---
chunk_kind: "child"
pattern_id: "A.10.1"
pattern_title: "Revalidate Affected Uses When a Relied-on Source Changes"
section_id: "A.10.1:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10.1/A.10.1__012_sota-echoing.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "A.10.1 — Revalidate Affected Uses When a Relied-on Source Changes"
  - "A.10.1:11 — SoTA-Echoing"
line_start: 23327
line_end: 23336
dependencies:
  - "A.10"
  - "A.10.1"
  - "A.11"
  - "B.3"
  - "C.2.1"
  - "E.15"
  - "G.11"
  - "G.6"
keywords:
---

### A.10.1:11 - SoTA-Echoing

| Current problem-solving claim | Practice and source | A.10.1 alignment and working implication | Adoption |
| --- | --- | --- | --- |
| Reverify only the slice that can affect the checked property, and reuse an unchanged prior result when its actual dependency is outside the change. | Dependency-aware incremental build practice distinguishes actual from declared dependencies ([Bazel dependency concepts](https://bazel.build/concepts/dependencies)); change-aware model checking reuses prior results through property-relevant dependency slices (Li, Chen, Huang, and Ding, [2024](https://doi.org/10.1002/smr.2626)). | Sections 4.3–4.4 require actual receiving-use inspection, action-changing closure, and explicit reuse conditions. A build or program graph is only an analogy: it cannot establish prose meaning or reliance. | **Adopt and adapt.** Adopt dependency-bounded reverification and result reuse; adapt the dependency test to exact claim use and independently governed subject results. |
| Traceability, heterogeneous-model links, and automated analysis can lower the cost of candidate impact discovery, but conflict and semantic judgment remain explicit. | A systems-engineering change-impact case connects heterogeneous model semantics, traceability, conflict handling, and versioning (Wu et al., [2025](https://doi.org/10.1016/j.aei.2025.103490)); `SYSE.19` supplies the current FPF-aligned engineering host. | Section 4.3 uses traces and tools for source-outward discovery, pairs them with receiver inspection, and treats gaps and `unresolved` candidates as results rather than hiding them. The calibration case in section 5.1 shows the practical boundary. | **Adapt.** Use tools to find candidates and coverage limits; retain direct-use and subject-authority tests. |
| Full rerun and pure reachability are conservative only in appearance: they spend effort on unaffected uses while still missing undeclared reliance. | Broad rerun and graph-fanout are serious rival practices when the change is genuinely system-wide, but neither is an adequate default impact test at comparable effort. | Sections 4.2–4.7 take the cheap stop, bound the frame, add receiver-oriented discovery, and widen only when actual dependent reach or an unresolved coverage gap requires it. | **Reject as defaults.** Retain broad replay only for a genuinely broad frame or when the direct subject pattern requires it. |

The practical SoTA contribution is the combination of claim-sized comparison, bounded bidirectional discovery, actual-use classification, dependency-closed reach, reuse of unaffected results, and an acyclic subject-application/result sequence. No one graph, repository, or status vocabulary substitutes for that combination.

