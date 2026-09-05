---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Task Typing and TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:10"
section_title: "Selector Fields And Evidence Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__012_selector-fields-and-evidence-relations.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.22 — Task Typing and TaskSignature Assignment (Problem-CHR)"
  - "C.22:10 — Selector Fields And Evidence Relations"
line_start: 51963
line_end: 51968
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

*Inputs.* One stabilized problem-side episteme and CG-Spec ids; a `ProblemProfile` (...Description) only when C.22:5.0b's replay need is current; an A.10 evidence-use or provenance relation only when the receiving use relies on it; D.CTX only when that separate context relation is current; the QD values or references named by CharacteristicSpaceRef, ArchiveConfig, and EmitterPolicyRef only when QD is live; GeneratorIntent only when OEE is live.
*Produces.* Declare one `TaskSignature` episteme as the `U.Signature` species specified in C.22:5.2. When that signature is actually adopted for the problem-side episteme and receiving use, one separate `TaskSignatureAssignmentRelation` obtains among that signature, the exact problem-side episteme, and exact receiving-use episteme under C.22:5.2. TaskSignature is neither a new root U-kind nor a record kind: its A.6.0/C.2.1 identity tuple and declaration content determine episteme identity; signature membership and edition continuity follow C.22:5.2, while publication, carrier, and serialization remain outside identity. Optional QD, archive, generator, `PortfolioMode`, and telemetry vocabulary appears only when current.
*Used by.* **G.5** (Eligibility and Selection kernel), **G.4** (Acceptance and Evidence), **C.23** (admit, degrade, and abstain rules and method-family maturity checks).

