---
chunk_kind: "child"
pattern_id: "C.32.ADA"
pattern_title: "Architecture Decision Adequacy Scales"
section_id: "C.32.ADA:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADA/C.32.ADA__006_archetypal-grounding.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "C.32.ADA — Architecture Decision Adequacy Scales"
  - "C.32.ADA:5 — Archetypal Grounding"
line_start: 84877
line_end: 84886
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2.1"
  - "A.2.6"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.25"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.13"
  - "E.17"
  - "E.21"
  - "E.22"
  - "E.24.PUB"
keywords:
  - "ArchitectureDecisionAdequacyEvaluation@Project"
  - "E.21 labels"
  - "architecture decision adequacy"
  - "complete coordinate set"
  - "declared use"
  - "method docking"
  - "no average"
  - "publication projection"
  - "repair target"
---

### C.32.ADA:5 - Archetypal Grounding

**Developer-work readiness.** A service decision explains the candidate and trade-off, but the instruction “teams should use events” leaves the event boundary, Method, required capabilities and start conditions open. Its `MethodAndWorkDockingAdequacy` for the intended implementers is `2 partiallyExpressedForDeclaredUse`. The decision can prescribe how a future shift should implement a change before its members are assigned. For an instruction to start now, establish who can and may perform it. If the report goes on to claim actual Work or its performance under a particular assignment, establish those occurrences under A.13/A.15.1 and F.6 as applicable. Any claim of responsibility has its own domain predicate.

**ADR-publication readiness.** The manufacturing trade-study memo omits status and supersession, so its readers cannot establish which instruction is in force from this copy. For that use the projection merits `2 partiallyExpressedForDeclaredUse`. Open the decision or another authoritative record if the task also asks how adequately the underlying decision sets out its reopen conditions. A complete decision with an incomplete memo and a decision that itself lacks those conditions require different repairs. Until the relevant decision content is available, leave its coordinate unresolved. When it is available, assess that content and repair the memo through C.32.ADR.

**Architecture review.** A method-family architecture decision has candidate options and Method instructions, but no declared architecture characteristics. ADA gives `ArchitectureCharacteristicTradeoffAdequacy = 0 absent`. The repair states the missing characteristic assertions using C.32.ACS and C.25 before review can judge the decision.

**Governance enforcement.** A toolchain-product correspondence decision depends on team and tool structures. ADA evaluates `TransformerTransformedCorrespondenceAdequacy`; if the correspondence refs are absent, the repair states the missing correspondence assertion using C.32.CONWAY before institutional governance can constrain Method use.

