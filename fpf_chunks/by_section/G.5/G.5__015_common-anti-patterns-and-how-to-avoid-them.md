---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher and MethodFamily Registry"
section_id: "G.5:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__015_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "G.5 — Multi‑Method Dispatcher and MethodFamily Registry"
  - "G.5:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 104228
line_end: 104262
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

### G.5:8 - Common Anti-Patterns and How to Avoid Them

* **Anti‑pattern: “Selector as a shadow spec.”**
  *Symptom:* local acceptance or admissibility rules appear in selector prose or code, diverging from CN, CG, and CAL.
  *Avoid:* govern constraint semantics through `CNSpecRef` and `CGSpecRef` plus pinned CAL records; keep G.5 core as a boundary.

* **Anti‑pattern: “Implicit crossings.”**
  *Symptom:* reuse across distinct source-local meanings is claimed from a shared label, Bridge or CL pin, registry row, policy, DRR or SCR line, `GateCrossing`, or `CrossingBundle` without the required relation, use, and reliance facts.
  *Avoid:* resolve the exact F.17 endpoint senses; establish the F.9 Bridge; state the separate C.2.1 `<u,d,r,t,polarity>` claim; require the matching A.10 disposition or B.3 assurance branch; and keep authorization and actual selector use separate. Materialize or cite a bundle only when its named downstream use requires that durable package.


* **Anti‑pattern: “Hidden scalarisation.”**
  *Symptom:* partial orders are flattened into single winners “for convenience”.
  *Avoid:* return declared sets; make dominance regimes explicit; keep telemetry report‑only unless promoted by explicit policy.

* **Anti‑pattern: “Method specifics in the selector head.”**
  *Symptom:* QD, OEE, or preference models become mandatory for basic dispatch.
  *Avoid:* keep them in `G.5:Ext.*` blocks with explicit pins and `Uses`.

* **Anti‑pattern: “Churn by meaning.”**
  *Symptom:* a continuing family id silently resolves different members, grouping basis, or selection pins after a row changes.
  *Avoid:* keep the lineage id only for the continuing declared grouping, publish a new immutable row edition, and carry its exact row ref through selection, result basis, refresh, and deprecation notices.

* **Anti‑pattern: “Result declaration hidden in upstream reasoning.”**
  *Symptom:* the retained alternatives or all-member result exist only as one implication inside `C.11`, `C.19`, or `C.24`, while `G.5` never names the declared result kind.
  *Avoid:* declare the selected-set result directly, with its result kind, applicable members or keyed entries, ordering, named use where required, and basis pins instead of leaving it implicit upstream.

* **Anti-pattern: “Shortlist used for complementary members.”**
  *Symptom:* every named member is needed for one use, but the result calls them alternatives in a `Shortlist`.
  *Avoid:* use `JointUseSet`, name the joint use, and key one entry per exact member; keep direct member relations and actual selection separate.

* **Anti‑pattern: “Declared result missing required content.”**
  *Symptom:* a `Shortlist`, `JointUseSet`, narrowed handoff, or abstain result is named, but the emitted result still omits its members or keyed member entries, ordering, named use where required, or basis pins.
  *Avoid:* state the result kind, retained members or keyed joint-use entries, ordering, named use where required, abstain or escalation condition, and basis pins directly in `G.5`.

