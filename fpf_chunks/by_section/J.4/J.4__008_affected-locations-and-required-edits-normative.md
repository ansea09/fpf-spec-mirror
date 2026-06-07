---
chunk_kind: "child"
pattern_id: "J.4"
pattern_title: "First Practical Entry Neighborhood Index"
section_id: "J.4:section-007"
section_title: "Affected locations and required edits (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/J.4/J.4__008_affected-locations-and-required-edits-normative.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "J.4 — First Practical Entry Neighborhood Index"
  - "J.4:section-007 — Affected locations and required edits (normative)"
line_start: 82190
line_end: 82223
dependencies:
keywords:
---

### Affected locations and required edits (normative)

Editors SHALL apply the following replacements:

1. **Part C.2.2 (F–G–R).**

   * Replace any internal definition of “Generality” with a normative reference to **A.2.6 §6.3** (*Claim scope (G)*).
   * Where “abstraction level” is mentioned as G, replace with “Claim scope (where the claim holds)”; keep **AT** (AbstractionTier) only as optional didactics (non‑G).
   * Ensure composition examples use **intersection/SpanUnion** for G, not ordinal “more/less general”.

2. **Part C.2.3 (Formality F).**

   * No change to F itself.
   * Any example that implies “raising F widens G” MUST be rephrased: F changes expression form; G changes only via **ΔG**.

3. **Part A.2.2 (Capabilities).**

   * Replace “capability envelope/applicability” with **`U.WorkScope`**.
   * Method–Work gates MUST test **Work scope covers JobSlice**, with **measures** and **qualification windows** bound.

4. **Part B (Bridges & CL).**

   * Add a note: **CL penalties apply to R**, not to **F/G**; mapping MAY recommend **narrowing** the mapped scope (best practice).

5. **Part E (Lexicon).**

   * Add entries for **Claim scope (G)**, **Work scope**, **Scope** (mechanism).
   * Mark listed deprecated terms as **deprecated aliases** allowed only in explanatory notes.

6. **ESG & Method–Work templates.**

   * Replace any “applicability”/“envelope” guard phrasing with **ScopeCoverage** (see §10).
   * Require explicit **`Γ_time`** selectors in all scope‑sensitive guards.

