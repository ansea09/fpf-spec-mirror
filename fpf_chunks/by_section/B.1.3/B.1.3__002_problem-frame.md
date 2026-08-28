---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__002_problem-frame.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:1 — Problem frame"
line_start: 36145
line_end: 36154
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

### B.1.3:1 - Problem frame

* **Holonic foundation.** In the FPF, a `U.Episteme` is a holon whose identity is **knowledge-bearing** (A.1). It can be a **statement/claim**, a **model**, a **theory**, a **specification**, a **dataset with semantics**, or a **compiled claim-bearing synthesis**.
* **Strict Distinction (A.15).** We separate:
  **structure** (what the episteme comprises), **order** (argument flow), **identity and history** (C.2.1 identities and edition relations), **proper temporal restriction** (A.14), **work** (what was spent to produce/validate it), and **values** (objectives/criteria). Γ\_epist stays in the **structure/semantics** lane and calls out to Γ\_ctx/Γ\_time/Γ\_work only after their direct inputs are recovered.
* **Mereology (A.14).** For knowledge composition we primarily use **ConstituentOf** (logical or semantic parts), **UsageOf** or **ReferenceTo** (external reliance), and each collection's own belongs-to rule for collections such as anthologies or corpora. We do **not** use **ComponentOf** (physical) in Γ\_epist.
  `PhaseOf` may restrict the **same unchanged episteme** to a proper interval when its complete C.2.1 identity triple remains fixed. Distinct labelled versions or revisions require distinct C.2.1 identities when a discriminator changes and an independently obtaining `EpistemeEditionRelation` for any claimed historical continuation. Knowledge does not act and acquires neither a work-facing local system-role kind nor an assignment. Ordinary prose may say, for example, "the researcher synthesized the sources". If the receiving use does not identify that action as one particular dated `U.Work` occurrence, stop with the ordinary sentence. If it does, recover each actual performer's A.13 core and independently admit the occurrence under A.15.1. Add F.6 only when the receiving use also needs precise assignment-bound attribution; a short local projection may omit an unused assignment identifier only when every consumed relation remains recoverable.
* **Assurance (B.3).** Knowledge carries **F**, **G**, **R** (Formality, ClaimScope, Reliability). Integration edges carry **CL** (congruence level) that penalizes poor fit. Γ\_epist **must** preserve provenance and apply **conservative** bounds: no “truth averaging,” no silent context hops. **Obligations here are mode/assurance‑gated per C.2.1.**  # [M‑0]
* **Order/time flavours.** Argument sequences may need **Γ_ctx** (non-commutative ordering of premises to conclusion). Knowledge evolution first uses C.2.1 to identify exact epistemes and any obtaining edition relations; B.1.4/**Γ_time** may then aggregate already recovered temporal restrictions, relation order, deprecation, or update windows for a bounded use. The aggregation creates neither identity nor continuity. Open B.2 only if the synthesis leaves a genuine whole-reidentification question after the existing-whole explanation check and identifies an exact candidate new whole; new wording or explanatory gain alone is not MHT.

