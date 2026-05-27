---
chunk_kind: "child"
pattern_id: "C.20"
pattern_title: "Composition of U.Discipline (Discipline‑CAL)"
section_id: "C.20:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.20/C.20__008_conformance-checklist-normative.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "C.20 — Composition of U.Discipline (Discipline‑CAL)"
  - "C.20:7 — Conformance Checklist (normative)"
line_start: 42628
line_end: 42645
dependencies:
  - "A.19"
  - "C.2"
  - "C.21"
  - "C.22"
  - "C.23"
  - "E.10"
  - "F.17"
  - "F.18"
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

### C.20:7 - Conformance Checklist (normative)
| ID | Requirement | Purpose |
|---|---|---|
| **CC‑C20‑1 (CG‑Spec linkage).** | A `U.Discipline` **SHALL** declare the **CG‑Spec** ids and **CHR characteristic ids** behind any comparison/aggregation; thresholds live only in **Acceptance** clauses referenced by those CG‑Specs. | Auditable comparability; no illegal ops. |
| **CC‑C20‑2 (Bridge‑only reuse).** | Any cross‑Context/Tradition use **SHALL** cite **Bridge id + CL + loss notes**; penalties **route to R only**; **F/G invariant**. | Prevent silent globalisation; align with KD‑CAL. |
| **CC‑C20‑3 (ReferencePlane).** For any crossing touching `world|concept|episteme`, **publish plane** and apply **Φ(CL)** (and **Φ_plane**, where applicable) — both **MUST** be **monotone, bounded, table‑backed**; **unknowns** propagate as **{pass|degrade|abstain}** into **Acceptance** with **SCR note**; **no silent `unknown→0`**. |
| **CC‑C20‑4 (Γ_disc integrity).** | `Γ_disc` **MUST** record lane tags and freshness windows for all imported evidence; **Φ(CL)** **MUST** be monotone and table‑backed per policy. | Deterministic assurance; hygiene of penalties. |
| **CC‑C20‑5 (Edition & DRR).** | Discipline editions **SHALL** be recorded via **UTS edition-continuity records** with DRR links; no silent rewrites or renames. | Traceable evolution. |
| **CC‑C20‑6 (LEX/I‑D‑S).** | `U.Discipline` names **SHALL** follow **LEX** (twin labels; registers; banned heads). **Domain** mentions are catalog‑only. | Register hygiene; avoid “Domain = Discipline”. |
| **CC‑C20‑7 (Crossing visibility hooks).** | Any **cross‑stance / cross‑Context / cross‑plane** reference in Discipline materials **SHALL** publish a **CrossingBundle** for the crossing (**E.18**; Bridge+UTS through **F.9**, **F.17**, **E.17**, and **E.18**) and expose it via `Expose_CrossingHooks` (**G.10‑3**). Published crossings **MUST** be checkable for **LanePurity** (CL→R only; F/G invariant; Φ tables present) and **Lexical SD** (**E.10**) under the active GateProfile / GateChecks (**A.21**). | Prevents implied crossings; makes provenance auditable & replayable. |
| **CC‑C20‑8 (Discipline column is didactic).** | Any use of a “discipline column” in tables is **didactic only**; semantics are carried by **UTS rows + Bridges**; **Domain** remains a catalog stitch (**E.10/F.17**). |  |
| **CC‑C20‑9 (Lexical firewall).** | Normative sections remain **notation/tool‑neutral**; vendor/tool tokens are avoided (see **E.5.1**). |  |

#### C.20:7.1 - Canonical rewrites (anti‑ambiguity)
* “TDD discipline” → **`Tradition: Test‑Driven`** *(Plain twin keeps “Tradition”)*.
* “Safety Discipline Owner” → **`Holder#DisciplineStewardRole:Safety‑Context`**.
* “ClinicalSafetyDomain Governance” → **`DisciplineSpec: Clinical‑Safety`** with comparability in **CG‑Spec**; the **Domain** mention remains a **D.CTX + UTS** catalog stitch.

