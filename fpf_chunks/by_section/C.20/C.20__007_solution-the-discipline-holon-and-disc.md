---
chunk_kind: "child"
pattern_id: "C.20"
pattern_title: "Composition of U.Discipline (Discipline‑CAL)"
section_id: "C.20:4"
section_title: "Solution — the Discipline holon and Γ_disc"
source_path: "FPF-Spec.md"
output_path: "by_section/C.20/C.20__007_solution-the-discipline-holon-and-disc.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "C.20 — Composition of U.Discipline (Discipline‑CAL)"
  - "C.20:4 — Solution — the Discipline holon and Γ_disc"
line_start: 46524
line_end: 46555
dependencies:
  - "A.19"
  - "C.2"
  - "C.21"
  - "C.22"
  - "C.23"
  - "E.10"
  - "F.17-F.18"
  - "F.9"
  - "G.0"
  - "G.2"
  - "G.5"
  - "U.BoundedContext"
keywords:
  - "U.AppliedDiscipline"
  - "U.Transdiscipline"
  - "discipline"
  - "episteme corpus"
  - "institutions"
  - "standards"
  - "Γ_disc"
---

### C.20:4 - Solution — the **Discipline holon** and Γ_disc

#### C.20:4.1 - U-kind settlement and registers
* **`U.Discipline`** — a **Holon** that composes an **EpistemeCanon**, **Standards/Practices**, and **Organisational Carriers** into a durable field-level EntityOfConcern.
* **`U.AppliedDiscipline`**, **`U.Transdiscipline`** — C.3-governed subkind values under `U.Discipline`; they are not separate root ontics.
* **Tradition and lineage values** — auxiliary holon-like values that organise variants or editions within a `U.Discipline`; write them without `U.` unless a direct governing pattern admits `U.Tradition` or `U.Lineage` by E.24.UK settlement.

**Placement and naming.** `U.Discipline` is governed by this pattern as the direct root durable U-kind. Its subkinds follow C.3/C.3.1 and F.5 naming discipline, E.10/F.17 register discipline, and A.11 parsimony. C.20 does not treat discipline names as candidate U-kinds merely because they appear in discipline-composition prose; a discipline kind needs the C.20 settlement plus ordinary U-kind admission evidence.

#### C.20:4.2 - What a `U.Discipline` is / is not
* A `U.Discipline` is **not** a `U.BoundedContext` and **not** a **Domain**. **Domain** remains a *catalog label* (stitched to D.CTX + UTS): **Discipline ≠ Domain** is enforceable via **E.10 LexicalCheck**; any cross-domain or cross-context reuse cites a **Bridge (F.9)** with **CL** and loss notes; penalties apply to **R** only; **F** and **G** remain invariant (USM/KD‑CAL).
* **Comparability** of a discipline is carried **only by** the discipline’s **CG-Spec** entries (no ad-hoc formulas).
* Cross-context or cross-tradition reuse uses **Bridges** with **CL** and loss notes; **CL penalties apply to R** (KD-CAL/B.3); **F** and **G** remain invariant.
* Public names obey **LEX** (EntityOfConcern, Description, specification-use, twin labels, banned heads); “discipline column” is **didactic only** and **carries no semantics** (enforced by LexicalCheck).

#### C.20:4.3 - Constructor **Γ_disc** (CAL export)
*Signature.*
`Γ_disc : ⟨EpistemeCanon, StandardsSet, OrgCarriers, {Bridges}, Policy⟩ → U.Discipline`
*Intent.* Fold the three constituents into a `U.Discipline`, **preserving provenance**, publishing UTS cards, and enabling admissible comparability via referenced **CG‑Spec** rows.
*Obligations.*
1) **Provenance & lanes.** Each imported episteme/standard declares **A.10 anchors** and lane tags **{TA, VA, LA}**; freshness windows are recorded.
2) **Assurance fold.** Use KD‑CAL weakest‑link on R with **Φ(CL)** (and, where applicable, **Φ_plane** for ReferencePlane crossings) **table‑backed and monotone**; publish policy ids. For any independent justification line **P**, compute **`R_eff(P) = max(0, min_i R_i − Φ(CL_min(P)))`**; for parallel independent lines to the *same* claim take **`R(Γ) = max_P R_eff(P)`**; **`F(Γ)=min`** along the used lines. No thresholds inside CHR/CAL (Acceptance‑only). Unknowns propagate as {pass|degrade|abstain} to Acceptance.
3) **CG-Spec guard.** Any numeric comparison or aggregation in Discipline reports **MUST** cite the discipline’s **CG-Spec** with **ScaleComplianceProfile (SCP)**, **Γ-fold**, and **MinimalEvidence**; units, scale, and polarity admissibility via **MM-CHR/CSLC** precedes aggregation.
4) **Scale, unit, and polarity admissibility.** Before any comparison/aggregation, **establish admissibility via MM‑CHR/CSLC** and cite **CG‑Spec characteristic ids** used in the fold (A.17–A.19).
5) **ReferencePlane guard.** When crossings touch the world, concept, or episteme plane, apply **CL_meta** penalties to **R** only; record **plane** on the UTS row.
6) **Edition discipline.** Changes to canons or standards that alter computed ⟨F,G,R⟩ **create a new edition**; the rationale belongs in the edition-continuity record, and UTS records the transition.
7) **No stealth globalisation.** Cross-context mappings are **by Bridge only**; “by-name reuse” is forbidden even with similar labels.

#### C.20:4.4 - Discipline ESG (informative state view)

Export a **Discipline.ESG** with named states and guarded transitions (e.g., *Emerging → Consolidating → Codified → Fragmenting*), where **guards reference C.21 metrics** (CHR‑typed; **Scale/Unit/Polarity + freshness windows**) and cite **CG‑Spec ids**; **all thresholds live only in AcceptanceClauses** (G.4). ESG is **descriptive**; all gating remains in CHR/CAL/LOG packs.

