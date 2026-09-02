---
chunk_kind: "child"
pattern_id: "E.15"
pattern_title: "Pattern Change, Edition Continuity, and Impact Analysis"
section_id: "E.15:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.15/E.15__012_sota-echoing.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "E.15 — Pattern Change, Edition Continuity, and Impact Analysis"
  - "E.15:11 — SoTA-Echoing"
line_start: 81106
line_end: 81120
dependencies:
  - "C.18"
  - "C.19"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.8"
  - "E.9"
  - "F.0.1"
  - "F.1"
  - "F.15"
  - "F.9"
keywords:
---

### E.15:11 - SoTA-Echoing

The selected method combines exact edition comparison with dependency-aware incremental reverification and optional design-space search. No one source supplies the complete FPF procedure.

| Practice or research line | Status and contribution | Limit or rejected overread | Change to E.15 |
| --- | --- | --- | --- |
| [Git diff documentation](https://git-scm.com/docs/git-diff), current official documentation | **Adopt:** compare exact endpoints and keep historical values recoverable. | A textual or blob diff locates change but does not prove semantic preservation or actual consumer impact. | Exact predecessor/candidate recovery is mandatory; semantic probes remain separate. |
| [Semantic Versioning 2.0.0](https://semver.org/) | **Adapt as established release practice:** immutable released contents and explicit compatibility communication are useful. | SemVer depends on a declared public API and its labels do not decide FPF semantic continuity. It is not the current method for impact analysis. | Version syntax is optional and follows, rather than supplies, the Delta-Class decision. |
| [Current Bazel action-graph and incremental-build practice](https://bazel.build/about/intro) and its [actual-versus-declared dependency distinction](https://bazel.build/concepts/dependencies) | **Adapt:** trace changed inputs through actual dependencies and reuse unaffected work. This advances the effort-to-reliability frontier over full reruns when change is local. | A build graph is not an ontology of pattern meaning, and declared references can miss or overstate semantic dependence. | Inspect actual and declared consumers; reopen only affected conclusions. |
| Li, Chen, Huang, and Ding, [“Change-aware model checking for evolving concurrent programs based on Program Dependence Net”](https://doi.org/10.1002/smr.2626), 2024 | **Adopt the current research move by analogy:** use prior verified results and property-relevant dependency slices rather than rechecking an entire changed system. | Software paths and LTL properties do not transfer as FPF kinds or sufficient evidence for prose semantics. | Result reuse requires an unchanged conclusion and a justified outside-impact dependency. |
| MAP-Elites and quality-diversity search, with current FPF C.18/C.19 machinery | **Retain as optional lineage and method family:** useful when several materially different candidates and diversity itself matter. | Candidate multiplicity and archive coverage do not improve an understood local repair and do not select a winner across heterogeneous qualities. | Alternative generation is conditional; E.21/E.22 and intended use decide among non-dominated candidates. |
| Full rerun of every authoring, source, assurance, and review activity | **Reject as the default rival:** broad reruns can be appropriate after a genuinely broad Δ-3 change. | At comparable correctness, they spend more effort on unaffected premises and encourage ceremonial records. | Scope verification from actual change and dependencies, while preserving the explicit broad-change branch. |

The non-dominated contribution is therefore not a new authoring trace or scoring system. It is the combination of a cheap direct-repair path, actual-delta classification, independent predecessor preservation, actual-consumer reach, and whole-pattern practitioner-language verification, with stronger search and checking opened only by their real use.

