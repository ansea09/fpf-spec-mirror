---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:10"
section_title: "Selector Fields And Evidence Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__012_selector-fields-and-evidence-relations.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:10 — Selector Fields And Evidence Relations"
line_start: 48083
line_end: 48088
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
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:10 - Selector Fields And Evidence Relations

*Inputs.* `ProblemProfile` (...Description), CG-Spec ids, Evidence Graph Ref (A.10), D.CTX; CharacteristicSpaceRef, ArchiveConfig, and EmitterPolicyRef configs when QD is live; GeneratorIntent when OEE is live.
*Produces.* One `TaskSignature@Context` value, declared as the Context-local `U.Signature` species specified in C.22:5.2. When a receiving use is current, C.22 also produces one separate `TaskSignatureAssignmentRelation@Context` relating that signature edition to the exact problem-side episteme and receiving-use description. `TaskSignature@Context` is neither a new root U-kind nor a record kind: SubjectBlock, Vocabulary, Laws, and Applicability determine its semantic edition, while carrier and serialization remain outside its identity. Optional QD, archive, generator, `PortfolioMode`, and telemetry vocabulary appears only when current.
*Used by.* **G.5** (Eligibility and Selection kernel), **G.4** (Acceptance and Evidence), **C.23** (admit, degrade, and abstain rules and method-family maturity checks).

