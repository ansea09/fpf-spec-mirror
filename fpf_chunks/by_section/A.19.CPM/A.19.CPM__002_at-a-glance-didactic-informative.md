---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Unified Comparison Mechanism (CPM)"
section_id: "A.19.CPM:0"
section_title: "At a glance (didactic, informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__002_at-a-glance-didactic-informative.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.19.CPM — Unified Comparison Mechanism (CPM)"
  - "A.19.CPM:0 — At a glance (didactic, informative)"
line_start: 32373
line_end: 32406
dependencies:
keywords:
  - "ComparatorSet"
  - "ComparatorSpecRef"
  - "comparator"
  - "comparison"
  - "partial order"
  - "set-valued comparison outcome"
  - "tri-state admissibility (pass"
---

### A.19.CPM:0 - At a glance (didactic, informative)

CPM is the CHR comparison kernel: it compares two admitted profiles under an explicit, admissibility‑gated comparator and returns a **set‑valued** comparison outcome.

**One-screen purpose (manager-first).** CPM answers: "Given two admitted profiles and an explicit comparator, what relation holds under the declared admissibility frame?" It does **not** answer: "Which one should we pick?" (selection) nor "What is the score?" (scoring).

**Use this when.** Use CPM when the current project question is comparison under one declared comparator, not scoring, folding, selection, publication, or work authorization.

**What this buys.** The practitioner gets a comparison relation that can be audited and later consumed by selection without turning partial order, incomparability, missing evidence, or scale limits into a hidden scalar winner.

**First output.** Write or cite one `ComparisonResultSlot` carrying the relation or poset tokens, comparator ref, admissibility frame, and evidence and currentness pins needed for replay.

**Manager quick checklist (before you trust a comparison):**
* **Comparator is explicit:** do we have a `ComparatorSpecRef`, and is it admitted by `CG‑Spec.ComparatorSet`?
* **Admissibility is declared:** do we cite `CG‑Spec` (and `SCP` when numeric ops exist) and treat violations as `degrade|abstain`?
* **Evidence is not faked:** are missing or unknown inputs treated as `degrade|abstain` under the effective MinimalEvidence policy (never as `pass`)?
* **Partiality is preserved:** are we willing to accept incomparability and ties as first‑class outcomes (set‑valued result), rather than forcing a winner?

* **Suite stage:** `compare` (pipeline order lives in `A.19.CHR:4.5`, not in the `mechanisms[]` enumeration).
* **Input (conceptual):** left profile, right profile, `CN‑Spec`, `CG‑Spec`, an explicit `ComparatorSpec`, context slice; optional explicit `MinimalEvidence` override.
* **Output (conceptual):** `ComparisonResultSlot` as a **set of relation or poset tokens** (not a single scalar, and not an embedded selection decision).
* **Planned slot fillings:** concrete `ComparatorSpecRef.edition` and any policy ids are planned fillers **only** under the `A.15.3` planned slot-filling ontic and are carried by `SlotFillingsPlanItem` rows (A.15.3 + `A.19.CHR:4.7.2`). CPM's kernel does **not** fill project-specific slots; executions record the **effective** refs and pins in `Audit`.
* **Reproducible comparisons:** for parity and benchmark style runs that require a stable run package plus report record (editions, windows, parity pins), use `G.9` (Parity and Benchmark Harness). CPM stays kernel-only.
* **What CPM does not do (strict distinction):**

  * does **not** normalize (`UNM`);
  * does **not** choose indicators (`UINDM`);
  * does **not** score (`USCM`);
  * does **not** fold or aggregate (`ULSAM`);
  * does **not** select (“pick best”) — that is `SelectorMechanism`.
* **Core safety commitments:** admissibility gate via `CG-Spec.ComparatorSet` + `CG-Spec.SCP` + CSLC; tri-state admissibility (`pass|degrade|abstain`); unknown never coerces to “pass” or to a fabricated outcome; no silent scalarization or totalization.
* **Where method details live:** in editions of `ComparatorSpec` and their SoTA wiring (Part G packs and extensions), not inside CPM’s kernel semantics.
* **Quick rule of thumb:** if you need **numbers**, that’s `USCM`; if you need a **selection or selected-set result**, that’s `SelectorMechanism`. CPM’s job is only: **compare → relation tokens**.

