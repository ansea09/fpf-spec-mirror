---
chunk_kind: "child"
pattern_id: "C.21"
pattern_title: "Field Health & Structure (Discipline-CHR)"
section_id: "C.21:9"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.21/C.21__010_conformance-checklist-normative.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "C.21 — Field Health & Structure (Discipline-CHR)"
  - "C.21:9 — Conformance Checklist (normative)"
line_start: 41382
line_end: 41400
dependencies:
  - "A.17"
  - "A.18"
  - "A.2.6"
  - "B.3"
  - "C.16"
  - "C.2"
  - "C.20"
  - "E.10"
  - "F.9"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.12"
  - "G.2"
  - "G.5"
  - "G.9"
  - "U.Discipline"
keywords:
  - "alignment"
  - "discipline"
  - "disruption"
  - "field health"
  - "reproducibility"
  - "standardisation"
---

### C.21:9 - Conformance Checklist (normative)

**CC-C.21-1 (CHR typing).** Every DHC slot **MUST** declare **Characteristic + Scale/Unit/Polarity**, with CSLC legality proved before any aggregation.
**CC-C.21-2 (Freshness).** Published values MUST carry Γ_time selector and freshness window; stale rows escalate to {degrade|abstain} in **G.4 Acceptance**.
**CC-C.21-3 (Plane).** ReferencePlane declared; cross‑plane re‑use publishes **CL^plane** (policy id) alongside CL; both penalties route to **R_eff**.
**CC‑C.21‑4 (DesignRunTag).** Every DHC row SHALL declare **DesignRunTag ∈ {design, run}**; design‑ and run‑characteristics **not mixing** in one value/aggregate.
**CC-C.21-5 (Lane tags).** Each value **MUST** tag **TA/VA/LA** lanes of contributing evidence.
**CC-C.21-6 (Ordinal discipline).** **StandardisationLevel** is ordinal; **no means**, **no z-scores**.
**CC-C.21-7 (Scope).** All computations declare **TargetSlice**; **USM** membership is decidable and deterministic.
**CC-C.21-8 (Bridges).** Cross-Context comparisons/publishers **MUST** cite **Bridge id + CL**; penalties route to **R\_eff**, never to F/G.
**CC-C.21-9 (UTS).** Publish DHC rows as **UTS Name Cards** with **twin labels** (Tech/Plain).
**CC‑C.21‑10 (Registry).** DHC methods are table-backed; silent method changes are forbidden (**bump `DHCMethodSpecRef.edition` + RSCR trigger**).
**CC-C.21-11 (Unknowns).** Unknown inputs propagate tri-state {pass|degrade|abstain} to Acceptance; **no `unknown→0` coercion**.
**CC-C.21-12 (No tool/vendor tokens).** Core narrative follows **E.5.1** (Lexical Firewall).
**CC-C.21-13 (CG‑Spec citation).** Any numeric operation (comparison/aggregation) in DHC **MUST** refer to **CG‑Spec** (characteristics, **ScaleComplianceProfile (SCP)**, **Γ‑fold**, MinimalEvidence).
**CC-C.21-14 (Φ‑policies).** **Φ(CL)** and **Φ_plane** — **monotone** and **table‑backed**; published by policy id.
**CC‑C.21‑15 (Ref discipline).** Any edition pinning **SHALL** appear as `…Ref.edition` on the relevant reference field (DHCPack/MethodSpec/DistanceDef/DHCMethodRef); bare `…Edition` fields are non‑conformant.
**CC‑C.21‑16 (Role kit, informative).** Use standard roles from F.4: `DisciplineStewardRole` (governs DHCPack), `DHCMethodAuthorRole`, `DHCSeriesPublisherRole`. Roles are **design‑time**; values are **run‑ or design‑stance** per slot and must declare **ReferencePlane**.

