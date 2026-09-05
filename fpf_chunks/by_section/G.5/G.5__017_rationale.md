---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__017_rationale.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:10 — Rationale"
line_start: 104241
line_end: 104249
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "C.35"
  - "E.17"
  - "E.24.PUB"
  - "E.4.PFR"
  - "G.0"
  - "G.11"
  - "G.2"
  - "G.2-G.4"
  - "G.5"
  - "G.6"
  - "G.9-G.11"
  - "G.Core"
keywords:
  - "RankedShortlist"
  - "SelectorOutcomeKind"
  - "Shortlist"
  - "ShortlistId"
  - "SpecialistHandoff"
  - "abstain/escalation result"
  - "are forbidden in registry"
  - "assurance"
  - "basis pins"
  - "dispatcher"
  - "eligibility"
  - "generator-family registry"
  - "in core registry and eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set publication"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:10 - Rationale

* **Why registries?** Dispatch requires stable, auditable family objects with explicit eligibility and assurance records; otherwise selection collapses into ad-hoc tooling.
* **Why separation via Extensions?** QD, OEE, preference-learning, and similar families are fast-moving and method-specific; making them part of the selector head would force a universal semantics and violate strict distinction.
* **Why set-return?** Partial orders are common and often the only admissible representation under heterogeneous scales; set-return preserves semantics and makes tie criteria explicit.
* **Why explicit defaults with one declared source?** Defaults are unavoidable; single-source indexing prevents competing defaults from silently diverging across patterns.
* **Why selected-set result declaration here?** Once the current question is to state retained alternatives or an all-member result for downstream use, the selector should declare that result directly instead of leaving it implicit in local choice, pool-policy, or enactment notes written for other purposes.
* **Why `JointUseSet`?** A shortlist preserves alternatives for later choice; an all-member result says that removing one member changes the result for the named use. G.5 mints `JointUseSet` only as a local `SetResultFamily` value and reuses the existing outcome schema and member identities. `G.5-3 Select` may emit it only over exact Method candidates admitted through that kernel; `G.5-6 DeclareSetResult` covers exact already grounded members without retyping them as Methods. Neither branch mints a new U-kind, Method kind, relation kind, or registry kind. `CoUseSet` is less plain, `ComplementarySet` would imply a relation among the members, and `Bundle` would misname a package form.

