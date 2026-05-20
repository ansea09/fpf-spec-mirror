---
chunk_kind: "child"
pattern_id: "G.1"
pattern_title: "CG‑Frame‑Ready Generator"
section_id: "G.1:10"
section_title: "Rationale (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.1/G.1__011_rationale-informative.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "G.1 — CG‑Frame‑Ready Generator"
  - "G.1:10 — Rationale (informative)"
line_start: 68617
line_end: 68623
dependencies:
  - "A.10"
  - "A.15.3"
  - "A.19"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.Core"
keywords:
  - "CGFrameLibraryId"
  - "CGKitId manifest"
  - "RSCR linkage surfaces"
  - "RefreshReadinessCardId"
  - "ShortlistId"
  - "SoTA_SetId"
  - "UTS/Name Cards"
  - "VariantPoolId"
  - "and set-surface scaffold"
  - "edition pins"
  - "generator"
  - "generator chassis"
  - "selector"
  - "set-return selection"
  - "set-surface outcome"
  - "shipping and refresh boundaries"
  - "six-card kit (M1-M6)"
---

### G.1:10 - Rationale (informative)

* **Why six cards?** It matches the minimal decomposition needed to keep scope, harvesting, generation, selection, publication, and refresh **explicitly separable** (and thus auditable and evolvable).
* **Why “kit/index” rather than “pack”?** A CG‑Frame authoring effort must stay modular; shipping is a separate governing boundary (`G.10`).
* **Why push method content into Extensions?** It prevents conflating (i) universal invariants, (ii) frame‑specific kit surfaces, and (iii) method/generator families—supporting Phase‑2 universalisation goals.
* **Why working‑model first?** Many CG‑Frames fail due to premature formalism; a chassis with didactic micro‑examples improves correctness of pins, names, and boundaries before deep formalisation.

