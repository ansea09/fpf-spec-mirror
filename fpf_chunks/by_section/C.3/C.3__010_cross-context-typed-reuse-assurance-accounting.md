---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent/Extent, and Typed Reasoning (Kind‑CAL)"
section_id: "C.3:8"
section_title: "Cross‑context typed reuse & assurance accounting"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__010_cross-context-typed-reuse-assurance-accounting.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "C.3 — Kinds, Intent/Extent, and Typed Reasoning (Kind‑CAL)"
  - "C.3:8 — Cross‑context typed reuse & assurance accounting"
line_start: 36072
line_end: 36113
dependencies:
  - "A.1"
  - "A.2.6"
keywords:
  - "classification"
  - "extension"
  - "intension"
  - "kind"
  - "subkind"
  - "type"
  - "typed reasoning"
  - "vocabulary"
---

### C.3:8 - Cross‑context typed reuse & assurance accounting

#### C.3:8.1 - The **two‑bridge rule** (mandatory)

When any part of the use crosses Contexts:

1. **Scope Bridge** (USM/Part B) with **CL** → penalty **Φ(CL)** to **R**.
2. **KindBridge** (C.3.3) with **`CL^k`** → penalty **Ψ(`CL^k`)** to **R**.

Both bridges carry **loss notes**; neither changes **F** or **G**. See **C.3.A Guard\_XContext\_Typed**.


#### C.3:8.2 - Narrowing after mapping (best practice)

If a bridge’s loss notes indicate material mismatch (dropped invariants, collapsed subkinds):

* **Narrow the mapped Scope** to areas where those losses are benign.
* **Or** introduce an **adapter** (plus evidence) that restores the needed properties in the target Context.
* Document the decision; the penalties still land in **R**.


#### C.3:8.3 - Typical Cross‑context patterns (manager’s catalog)

* **Name‑level overlap only (low `CL^k`).**
  Expect significant Ψ penalty. Limit quantification, add local checks, or refuse reuse until the kind mapping is improved.

* **Up‑to‑iso mapping (high `CL^k`).**
  Often seen for K3 kinds. Ψ penalty is small; treat as “shape‑preserving” transfer. Still apply the appropriate **Φ(CL)** for Scope.

* **Mask‑to‑subkind evolution.**
  If receivers repeatedly use the same **RoleMask** to make a transfer safe, promote it to an explicit **subkind** and update the bridge to preserve that link.


#### C.3:8.4 - Decision pattern (fast path)

1. **Typed pre‑check:** `k_A ⊑ k_B` (same Context) **or** `KindBridge(k_A → k′_B)` with acceptable **`CL^k`**.
2. **Scope coverage:** `translate(Scope_A)` covers `TargetSlice_B`.
3. **Apply penalties:** **Φ(CL\_scope)** and **Ψ(`CL^k`)** to **R**.
4. **Freshness:** windows/decay for all bound evidence.
5. **Publish:** a short “Bridge and Loss Notes” box; include any **narrowing** or **adapters** used.


