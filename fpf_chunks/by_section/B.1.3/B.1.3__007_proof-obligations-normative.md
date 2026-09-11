---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:6"
section_title: "Proof obligations (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__007_proof-obligations-normative.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:6 — Proof obligations (normative)"
line_start: 37242
line_end: 37261
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.PROD"
  - "A.6.1"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.11"
  - "C.19.2"
  - "C.2"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
  - "F.9"
  - "U.Work"
keywords:
  - "KD-CAL"
  - "epistemic"
  - "knowledge aggregation"
  - "provenance"
  - "trust"
---

### B.1.3:6 - Proof obligations (normative)

**At synthesis (Γ\_epist^synth):**

1. **PO‑SYN‑PROV.** The **provenance/evidence graph** MUST be preserved (union with de‑duplication); every retained claim is traceable to sources/methods in the **SCR**.
2. **PO-SYN-OBJ.** The result **MUST** name one exact EntityOfConcern already identified under its direct pattern. If the synthesis depends on several inputs as a joint subject, its collection, relation, or whole identity **MUST** be independently governed; a list, graph, label, or mapping is insufficient. Every semantic mapping used by the fold **MUST** be declared with its **CL** evidence summary.
3. **PO-SYN-CL.** Every mapping used in the support account **MUST** retain its CL evidence summary and actual use limitation. A numerical loss **MUST** have a receiving model establishing its meaning, scale, derivation or calibration, and assumptions; ordinal ranks and monotonicity alone are insufficient. The summary neither establishes an F.9 Bridge nor grants use.
4. **PO‑SYN‑R.** The result **MUST** distinguish indispensable premises, sufficient alternatives, complementary support, scope slices, and counterevidence where present. An aggregate R **MUST** have warranted input meanings, scales, dependencies, and an operation under B.3/C.2.2. Otherwise retain separate support and a reasoned bounded synthesis. Neither F nor a mode tag supplies an R conversion.
5. **PO-SYN-CONFLICT.** The result **MUST** retain credible contrary evidence and distinguish an established scope or interpretation difference from an unresolved conflict. Narrow, qualify, or withhold the affected conclusion accordingly. B.2 applies only to a separately grounded whole-reidentification question.
6. **PO‑SYN‑ORDER.** If order matters, the **OrderSpec** MUST be recorded and Γ\_ctx **NC‑1..3** (determinism, context hash, partial‑order soundness) MUST hold.
7. **PO‑SYN‑NOWORK.** Resource spending, yields, and dissipation MUST NOT be computed here; instead, attach references to the aligned **Γ\_work** composition.

**At compilation (Γ\_epist^compile):**

1. **PO-COMP-SCHEME.** The exact target reference scheme **MUST** be declared. Every active concept and unit **MUST** have an explicit mapping; a cross-context meaning use **MUST** name the exact F.9 Bridge, separate bounded-use claim, permitted loss, and any relied-on A.10 or B.3 result.
2. **PO-COMP-ASSUR.** The formal basis, scope, and support account **MUST** be re-expressed in the target scheme without losing their limitations. Any recalculated R or loss **MUST** satisfy the receiving model; otherwise preserve the separate support and bounded conclusion.
3. **PO-COMP-SCR.** The compiled episteme **MUST** retain an SCR with the hashes, versions, and dates required to reconstruct the application. This obligation does not assert release or publication.
4. **PO-COMP-ID.** The output **MUST** be identified through its C.2.1 claim content, exact EntityOfConcern, and effective target scheme. A changed discriminator identifies another episteme. B.2 is opened only for an independently current existing-whole versus candidate-new-whole question, never as a substitute for this identity rule.
5. **PO‑COMP‑ORDER/TIME.** If derivational order is essential, the **OrderSpec** MUST be referenced. If temporal selection is essential, name the exact C.2.1 episteme identity and reference the already recovered proper restriction, edition-relation order, applicability window, and B.1.4/**Γ\_time** aggregation actually consumed.

