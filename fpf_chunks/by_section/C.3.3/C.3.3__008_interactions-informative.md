---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge & CL^k — Cross‑context Mapping of Kinds"
section_id: "C.3.3:7"
section_title: "Interactions (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__008_interactions-informative.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "C.3.3 — KindBridge & CL^k — Cross‑context Mapping of Kinds"
  - "C.3.3:7 — Interactions (informative)"
line_start: 45247
line_end: 45275
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

### C.3.3:7 - Interactions (informative)

#### C.3.3:7.1 - With USM Scope bridges (two channels)

When using a claim across Contexts, expect **two concurrent bridges**:

* **Scope Bridge (USM):** the exact scope-bridge occurrence supports translation of G; its separate assessment supplies CL and the `Φ(CL)` consequence to R.
* **KindBridge (this pattern):** the obtaining direct relation connects exact source and target kinds; its separate bridge assertion supplies `CL^k`, loss, and the `Ψ(CL^k)` consequence to R.

**Discipline:** compute both; **do not** collapse them into one “interoperability score.”

 See **Annex C.3.A §5 (E‑01)** for the normative evaluation order in guards.

#### C.3.3:7.2 - With target classification (C.3.2)

After an obtaining KindBridge relates source kind `k` to independently identified target kind `k'`, evaluate the exact target judgment `J(candidate, k', targetSignatureEdition, TargetSlice)`. If a mapping rule motivates another target `KindSignature`, a system authors and identifies that declaration episteme separately; the bridge relation and its assertion do not construct it. A source judgment may be evidence for the receiving reliance claim but never substitutes for the target judgment.

#### C.3.3:7.3 - With Role masks (C.3.4)

A cross-context masked use requires an obtaining KindBridge relation between exact source and target kinds, the separate bridge assertion, a target RoleMask declaration episteme, and a `MaskAdapter` declaration episteme when constraints or bindings differ. The target context evaluates its exact `J_mask`; source masked results are not target truth. Any justified bridge penalties affect R only, and a stable target refinement requires an independently identified local kind and obtaining `U.SubkindOf` relation.

#### C.3.3:7.4 - With guards (Annex C.3.A)

Use the **`Guard_XContext_Typed`** macro (Annex C.3.A), which requires **both bridges** and applies **both penalties** to **R**:

* find Scope bridge (CL≥threshold), translate **G**, check coverage;
* establish the exact KindBridge relation and its bridge assertion, recover the independently identified target kind and signature edition, and evaluate the exact target judgment;
* apply **Φ(CL)** and **Ψ(`CL^k`)** to **R**; keep **F/G** untouched.

