---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Unified Comparison Mechanism (CPM)"
section_id: "A.19.CPM:0"
section_title: "At a glance (didactic, informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__002_at-a-glance-didactic-informative.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "A.19.CPM — Unified Comparison Mechanism (CPM)"
  - "A.19.CPM:0 — At a glance (didactic, informative)"
line_start: 34093
line_end: 34126
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

**What this buys.** The practitioner gets one set-valued comparison outcome that downstream selection can consume. The actual `Compare` application keeps the profile pair, comparator, claim scope and selected context slices, optional A.19 predicate, reference plane, evaluation window, policies, and output binding recoverable. Partial order, incomparability, missing evidence, and scale limits remain explicit instead of becoming a hidden scalar winner.

**First output.** Read the by-value set bound to `ComparisonResultSlot`: only the relation or poset tokens. Read comparator, comparison scope, predicate when used, plane, window, eligibility value, and evidence use from the actual operation application and their direct neighboring relations; they are not fields hidden inside the output.

**Manager quick checklist (before you trust a comparison):**
* **Comparator is explicit:** do we have a `ComparatorSpecRef`, and is it admitted by `CG‑Spec.ComparatorSet`?
* **Admissibility is declared:** do we cite `CG‑Spec` (and `SCP` when numeric ops exist) and treat violations as `degrade|abstain`?
* **Evidence is not faked:** are missing or unknown inputs treated as `degrade|abstain` under the effective MinimalEvidence policy (never as `pass`)?
* **Partiality is preserved:** are we willing to accept incomparability and ties as first‑class outcomes (set‑valued result), rather than forcing a winner?

* **Suite stage:** `compare` (pipeline order lives in `A.19.CHR:4.5`, not in the `mechanisms[]` enumeration).
* **Input (conceptual):** left profile, right profile, `CN-Spec`, `CG-Spec`, an explicit `ComparatorSpec`, one `U.ClaimScope` with selected A.2.6 `U.ContextSlice` members, an optional A.19 `CharacteristicSpacePredicate` when the comparison depends on one, effective reference plane, explicit evaluation window, and optional explicit `MinimalEvidence` override.
* **Output (conceptual):** the by-value `ComparisonResultSlot` set of relation or poset tokens. It is not a score, selected set, result episteme, work-result relation, evidence record, or container for replay metadata.
* **Planned slot fillings:** concrete `ComparatorSpecRef.edition` and policy ids are planned fillers only under the exact A.15.3 planned-filling declaration and are carried by `SlotFillingsPlanItem` rows (A.15.3 plus `A.19.CHR:4.7.2`). CPM's declaration does not fill project-specific slots. A dated comparison `U.Work` has separately governed occurrence-parameter bindings; an actual A.6.1 `Compare` operation application binds the set-valued result to `ComparisonResultSlot`; and its A.10 evidence-provenance path records the evidence and source-currentness basis used for replay.
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

