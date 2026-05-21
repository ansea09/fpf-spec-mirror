---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:5"
section_title: "Solution — RoleMask (overview)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__006_solution-rolemask-overview.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:5 — Solution — RoleMask (overview)"
line_start: 37156
line_end: 37179
dependencies:
  - "C.3.1"
  - "C.3.2"
keywords:
  - "RoleMask"
  - "constraints"
  - "context-local adaptation"
  - "subkind promotion"
---

### C.3.4:5 - Solution — **RoleMask** (overview)

A **RoleMask** is a **named, versioned binding** `U.RoleMask(kind, Context)` that:

1. **Adds constraints** (entity‑level predicates only),
2. **Binds vocabulary/notation** (aliases, field maps) for the Context/process,
3. **May declare context expectations** (selectors over `U.ContextSlice`, e.g., jurisdiction, API version). **These are enforced via USM Scope guards** (A.2.6) and **do not** change mask membership.
4. **May narrow membership**: `Extension_mask(k, s) ⊆ Extension(k, s)` (entity‑level narrowing only),
5. **Never creates a new kind**; identity stays with `k`.
6. **Is guard‑addressable** and **deterministic** (no “latest”).

**Mask types (declared):**

* **Constraint mask** — adds constraints; may narrow membership;
* **Vocabulary mask** — aliases only; no membership change;
* **Composite mask** — both.

**Separation discipline.**

* **Entity‑level predicates** (e.g., “hasABS(x)”) → **mask membership** (narrowing).
* **Context conditions** (e.g., “jurisdiction=EU”, “API=v2.3”) → **USM Scope** guards (intersection), **not** mask membership.
  Masks **may carry both kinds** of information, but guards must route them into the **right channel**.


