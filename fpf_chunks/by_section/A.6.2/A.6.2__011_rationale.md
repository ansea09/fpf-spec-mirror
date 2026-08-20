---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
section_id: "A.6.2:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__011_rationale.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.6.2 — U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
  - "A.6.2:10 — Rationale"
line_start: 13302
line_end: 13322
dependencies:
  - "A.1"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### A.6.2:10 - Rationale

**Why a separate EFEM pattern (A.6.2) instead of folding into A.6.1 or C.2.1?**

* A.6.1 defines **Mechanism** declarations—operations with AdmissibilityConditions, Γ_time, transport and Bridges—which are too operational for the pure episteme transforms needed here.
* C.2.1 fixes episteme identity through claim content, exact EntityOfConcern, and effective ReferenceScheme and keeps neighboring direct relations separate, but does not define morphisms. EFEM is a morphism-level pattern over those values and relations.

This split mirrors how Signature (A.6.0) separates “what is declared” from “how it is realised”: C.2.1 says what an episteme is; A.6.2 says what an admissible episteme-to-episteme transform is.

**Why insist on EntityOfConcernChangeMode?**

Because almost all subtle errors in multi‑view reasoning show up as **silent retargeting**: a transform that appears to keep the same EntityOfConcern actually changes it (e.g., from “component assembly” to “function bundle”) without naming the bridge or invariant. By forcing every species to declare `preserve` vs `retarget`, EFEM makes those decisions explicit and reviewable.

**Why name actual values and relation effects instead of informal fields?**

FPF distinguishes actual participants and their references from the declaration-local SlotKinds used in a reusable `RelationSignature`. Reusing that distinction here:

* aligns episteme morphisms with the framework's direct-relation architecture;
* enables checks that an EFEM species changed only the identity values and neighboring relations it declared; and
* avoids minting another generic parameter, field, or relation-role vocabulary.

