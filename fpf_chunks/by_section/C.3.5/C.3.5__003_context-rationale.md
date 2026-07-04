---
chunk_kind: "child"
pattern_id: "C.3.5"
pattern_title: "KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
section_id: "C.3.5:2"
section_title: "Context & Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.5/C.3.5__003_context-rationale.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "C.3.5 — KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
  - "C.3.5:2 — Context & Rationale"
line_start: 41528
line_end: 41553
dependencies:
  - "C.3.1"
keywords:
  - "K0-K3"
  - "KindAT"
  - "abstraction tier"
  - "informative facet"
  - "planning"
---

### C.3.5:2 - Context & Rationale

#### C.3.5:2.1 - The orthogonality we preserve

* **G (Claim scope)** is **where** a claim holds (A.2.6).
* **Kinds** give **what** a claim is about (C.3.1/3.2).
* **R** is assurance (evidence, freshness, penalties).
* **F** is expression rigor (C.2.3).

Teams often **conflate abstraction with applicability** (“sounds general ⇒ applies broadly”) or **over‑engineer proofs** where **slice‑checks** suffice. AT separates these concerns.

#### C.3.5:2.2 - Why a facet, not a Characteristic

Per **MM‑CHR**, **Characteristics** (e.g., F, G) carry algebra and appear in guards/composition. **KindAT** is only a **tag** on `U.Kind`:

* **No algebra, no thresholds**, not used in guards.
* **Editorial placement** only: on kinds, not on claims.
* **Planning signal**: what ΔF and ΔR typically pay off; what bridge style to expect.

This keeps AT **useful** without risking a “second G” or back‑door quality scores.

#### C.3.5:2.3 - Design choice recap (moved from C.3 §15.2)

* Making AT a Characteristic would **duplicate** G’s role and encourage gating.
* As a **facet**, AT remains a **catalog/navigation and planning device**, not an assurance dimension.

