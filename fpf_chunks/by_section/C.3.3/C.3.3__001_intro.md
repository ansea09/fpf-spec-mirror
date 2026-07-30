---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge & CL^k — Cross‑context Mapping of Kinds"
section_id: "C.3.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__001_intro.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "C.3.3 — KindBridge & CL^k — Cross‑context Mapping of Kinds"
  - "C.3.3:intro — Intro"
line_start: 45226
line_end: 45245
dependencies:
  - "A.2.6"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
  - "F.9"
keywords:
  - "CL^k"
  - "KindBridge direct relation"
  - "R penalty"
  - "bridge assertion episteme"
  - "loss"
  - "target judgment"
---

## C.3.3 - KindBridge & CL^k — Cross‑context Mapping of Kinds

> **One-line summary.** Defines **`KindBridge`** as the direct cross-context relation between one exact source local kind and one exact target local kind under pinned reference-scheme editions and a declared mapping predicate. A separate C.2.1 bridge-assertion episteme states direction, paired `KindSignature` editions, order preservation or collapse, `CL^k`, loss notes, definedness, evidence, and admitted use. Target classification is always a fresh four-input C.3.2 judgment; a source result or bridge assertion never creates target truth. `CL^k` affects only the receiving reliance value R, while F and Claim scope G remain with their own owners.

**Status.** Normative in **Part C**. Identifier **C.3.3**.
**Audience.** Engineering managers, architects, assurance leads, editors.

**Depends on.**

* **C.3.1 — U.Kind & SubkindOf (Core):** kinds are context-local `U.Kind` values; `U.SubkindOf` is an obtaining direct relation under an exact effective reference scheme; kinds carry no Scope.
* **C.3.2 — Kind intent, judgment, and extension:** `KindSignature` is a declaration episteme; `J(candidate, kind, signatureEdition, slice)` returns `true`, `false`, or `unknown`; an optional pinned-edition `KindExtension` is only a representation of true candidates.
* **A.2.6 — USM (Context slices & Scopes):** Claim scope (**G**) and Work scope live on claims/capabilities; scope bridging and **CL** penalties are defined there.
* **C.2.2 — F–G–R:** weakest‑link; penalties land in **R**, not **F/G**.
* **C.2.3 — U.Formality (F):** signature rigor.

**Non‑goals.**
— No repository/notation mandates; conceptual only.
— No Scope mapping here (that’s USM); **KindBridge** maps **kinds**, not scopes.
— No new arithmetic on `CL^k`; it reuses the **ordinal anchor semantics** of CL (Part B) but applies to kinds.

