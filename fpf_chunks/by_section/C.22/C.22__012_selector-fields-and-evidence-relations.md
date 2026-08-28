---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Task Typing and TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:10"
section_title: "Selector Fields And Evidence Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__012_selector-fields-and-evidence-relations.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "C.22 — Task Typing and TaskSignature Assignment (Problem-CHR)"
  - "C.22:10 — Selector Fields And Evidence Relations"
line_start: 51149
line_end: 51154
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:10 - Selector Fields And Evidence Relations

*Inputs.* `ProblemProfile` (...Description) and CG-Spec ids; an A.10 evidence-use or provenance relation only when the receiving use relies on it; D.CTX only when that separate context relation is current; CharacteristicSpaceRef, ArchiveConfig, and EmitterPolicyRef configurations only when QD is live; GeneratorIntent only when OEE is live.
*Produces.* One `TaskSignature` episteme, declared as the `U.Signature` species specified in C.22:5.2. When a receiving use is current, C.22 also produces one separate `TaskSignatureAssignmentRelation` among that signature, the exact problem-side episteme, and exact receiving-use episteme. TaskSignature is neither a new root U-kind nor a record kind: its A.6.0/C.2.1 identity tuple and declaration content determine its semantic edition, while publication, carrier, and serialization remain outside identity. Optional QD, archive, generator, `PortfolioMode`, and telemetry vocabulary appears only when current.
*Used by.* **G.5** (Eligibility and Selection kernel), **G.4** (Acceptance and Evidence), **C.23** (admit, degrade, and abstain rules and method-family maturity checks).

