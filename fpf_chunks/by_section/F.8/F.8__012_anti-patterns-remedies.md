---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
section_id: "F.8:10"
section_title: "Anti‑patterns & remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__012_anti-patterns-remedies.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "F.8 — Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
  - "F.8:10 — Anti‑patterns & remedies"
line_start: 71659
line_end: 71673
dependencies:
  - "A.11"
  - "A.7"
  - "A.8"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "decision lattice"
  - "minting new types"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:10 - Anti‑patterns & remedies

| #         | Anti‑pattern               | Symptom                                                                            | Why it harms thinking                              | Remedy (conceptual move)                                                                                                                         |
| --------- | -------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **AP‑1**  | **Row‑less sameness**      | Declaring “these mean the same” across Contexts without citing a **Concept‑Set row**. | Imports meaning implicitly; no CL guard.           | If Cross‑context reuse is desired, **reuse an existing row** at a declared **scope** (F.7), else **publish the contrast** and apply F.9 Bridges only when the bridge relation is live. |
| **AP-2**  | **Scope creep**            | Using a **Naming-only** row to justify **Assignment-eligibility** or structural inferences. | Over-claims sameness; breaks τ(scope).             | Respect **scope thresholds** (τ). Upgrade only when **Row CL(min) ≥ τ(new scope)**; otherwise stay Naming-only.                                  |
| **AP‑3**  | **Alias with payload**     | Introducing an Alias that subtly changes intent or senseFamily.                          | Hides semantics behind wording; confuses senseFamilies.   | Aliases (F.5) are **style only**. If semantics change, choose **row reuse** or **Role Description** instead.                                         |
| **AP-4**  | **Role-Description-to-row anchoring** | Role Description points to a **row** rather than a **single SenseCell**.       | Masks locality; **assignments** become cross-context by stealth. | Role Descriptions **must anchor to one SenseCell** (F.4). Use rows only in prose or aggregated views.                                                |
| **AP‑5**  | **Kernel inflation**       | Proposing a new **U.Type** because a convenient label is missing.                  | Duplicates the kernel; violates parsimony.         | Apply A.8: require **≥ 3 domain families** and **irreducibility**; otherwise **Alias** or **row**.                                               |
| **AP‑6**  | **senseFamily mixing**           | One name that conflates Role, Status, Measurement, or Type‑structure.              | Collapses A.7 Strict Distinction.                  | **Split by senseFamily** first (Q0). Decide **per senseFamily**.                                                                                             |
| **AP‑7**  | **Bridge‑by‑string**       | Treating identical lexical forms as equivalent senses across Contexts.                | Homonym trap; ignores local sense.                 | Equivalence only via **F.9 Bridge** + **row**; never by string.                                                                                  |
| **AP‑8**  | **Row without loss notes** | Publishing a row where Bridges indicate mismatches, but row text is silent.        | Readers assume full equivalence.                   | Include **counter‑example** and **loss sketch** in the row’s narrative (F.7).                                                                    |
| **AP‑9**  | **CL laundering**          | Citing a high-scope row based on old high `CL` while the relevant Bridge `CL` has since dropped.    | Invalidates downstream claims.                     | When `CL` falls below `τ(scope)`, **downgrade row scope** (e.g., to Naming-only) or **split row**.                                                   |
| **AP‑10** | **Global normal form**     | Seeking one canonical wording across all Contexts **as if** meaning were global.      | Erases locality; fuels hidden merges.              | Keep normalisation **per Context** (F.2/F.3). Cross‑context sameness lives in **rows** with scope.                                                     |

