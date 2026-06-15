---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:6"
section_title: "Proof obligations (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__007_proof-obligations-normative.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:6 — Proof obligations (normative)"
line_start: 30831
line_end: 30850
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "C.2"
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
2. **PO‑SYN‑OBJ.** The **Object** MUST be identified (single subject via LCA or explicit `U.CompositeEntity`) with declared **mappings** and their **CL**.
3. **PO‑SYN‑CL.** All **mapping edges** that bridge semantics/units MUST carry **CL**; the chosen penalty **Φ** MUST be monotone in CL (lower CL ⇒ higher penalty). Thresholds for marking **provisional** MUST be stated.
4. **PO‑SYN‑R.** `R_eff` MUST be computed as **min over justification paths** of (claim reliabilities along the path **minus** `Φ(CL_min(path))`). No arithmetic mean is allowed for reliability.
5. **PO‑SYN‑CONFLICT.** Contradictions MUST be either (i) separated by context/scope, (ii) marked as **provisional** with explicit conflict edges, or (iii) escalated to **MHT** if resolution yields new explanatory closure.
6. **PO‑SYN‑ORDER.** If order matters, the **OrderSpec** MUST be recorded and Γ\_ctx **NC‑1..3** (determinism, context hash, partial‑order soundness) MUST hold.
7. **PO‑SYN‑NOWORK.** Resource spending, yields, and dissipation MUST NOT be computed here; instead, attach references to the aligned **Γ\_work** composition.

**At compilation (Γ\_epist^compile):**

1. **PO‑COMP‑CTX.** The target **bounded context** MUST be declared; all active concepts MUST be mapped with **CL**; context vocabulary/units recorded.
2. **PO‑COMP‑ASSUR.** The assurance tuple (F/G/R) MUST be recomputed **in the target context** with the applied **CL penalties**.
3. **PO‑COMP‑REL.** A **release‑grade SCR** (hashes, versions, dates) MUST be produced.
4. **PO‑COMP‑MHT.** If the compilation re‑anchors **boundary**, **objective**, or **identity** (e.g., from compendium to explanatory theory), an **MHT (Context Reframe)** MUST be declared with a Promotion Record (B.2).
5. **PO‑COMP‑ORDER/TIME.** If derivational order or a specific time slice is essential, the **OrderSpec** and the **Γ\_time** slice MUST be referenced.

