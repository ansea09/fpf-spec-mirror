---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Method-Family Registry, Dispatch and Selected-Set Result Declaration"
section_id: "G.5:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__012_rationale.md"
commit_sha: "ea8c54542bf017f36659167f36e816fad4de88cb"
heading_path:
  - "G.5 — Method-Family Registry, Dispatch and Selected-Set Result Declaration"
  - "G.5:10 — Rationale"
line_start: 128868
line_end: 128876
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
  - "JointUseSet"
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
  - "selected-set result declaration"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:10 - Rationale

* **Why registries?** Stable row editions preserve the grouping and eligibility basis for later dispatch. Assurance records enter when required by the declared use or public-registration contract.
* **Why separation via Extensions?** QD, OEE and preference-learning have different method semantics. Extensions let a selector use those semantics only for the task that needs them.
* **Why set-return?** Partial orders are common and often the only admissible representation under heterogeneous scales; set-return preserves semantics and makes tie criteria explicit.
* **Why explicit defaults with one declared source?** Indexing each default by its governing definition lets consumers use and revise the same rule.
* **Why selected-set result declaration here?** Once the current question is to state retained alternatives or an all-member result for downstream use, the selector should declare that result directly instead of leaving it implicit in local choice, pool-policy, or enactment notes written for other purposes.
* **Why `JointUseSet`?** A shortlist preserves alternatives for later choice; an all-member result says that removing one member changes the result for the named use. `JointUseSet` is a local `SetResultFamily` value using the existing member identities. `G.5-3 Select` may emit it only over exact Method candidates admitted through that kernel. `G.5-6 DeclareSetResult` covers already identified members with a current inclusion basis, including framework editions, without retyping them as Methods or asserting a relation among them.

