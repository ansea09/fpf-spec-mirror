---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__001_intro.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:intro — Intro"
line_start: 22357
line_end: 22395
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.20"
  - "A.21"
  - "A.6.5"
  - "A.6.7"
  - "B.3"
  - "C.27.TA"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.19"
  - "E.20"
  - "E.24"
  - "G.11"
  - "G.6"
  - "U.RelationSlotDiscipline"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "P2W seam"
  - "WorkPlanning"
  - "edition pins"
  - "guard pins"
  - "planned baseline"
  - "planned filler"
  - "slot-bearing description"
  - "variance trail"
  - "Γ_time selector"
---

## A.15.3 - SlotFillingsPlanItem

> **Tech-name:** `SlotFillingsPlanItem`
> **Plain-name:** planned slot-fillings baseline item
> **Short code:** `SFPI`
> **Type:** Definitional WorkPlanning pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part A -> A.15 work family
> **Builds on:** `A.15.2 U.WorkPlan`, `A.15.1 U.Work`, `A.6.5 U.RelationSlotDiscipline`, `E.10.D2`, `E.17`, `E.18.1`, `E.20`, and `E.24`
> **Used by:** P2W work-planning slices, suite or kit planned baselines, work-entry readiness checks, Part G planned-baseline references, and performed-work variance records
> **One-line purpose:** name one planned baseline item that states which planned fillers are intended for which SlotKinds of one slot-bearing description before performed work occurs.

**At a glance.** Use `SlotFillingsPlanItem` when a `U.WorkPlan` needs more than a date, budget, or intended method: it needs a reproducible planned baseline saying which planned fillers are intended for one slot-bearing description's SlotKinds.

**Use this when.** Use this pattern when a P2W, work-planning, or work-entry-readiness slice needs planned references, policy pins, method-description refs, edition pins, evidence-reference pins, guard-preparation refs, or crossing-policy refs to stay fixed before performed `U.Work`.

**First output.** One `SlotFillingsPlanItem` naming exactly one `target_slot_bearing_description_ref`, one `bounded_context_ref`, the EntityOfConcern under planning, a time selector or time rule, authoritative planned-filling rows, and any guard-preparation, evidence-reference, readiness-preparation, edition, or crossing-policy refs needed before performed work.

**Working use order.**

1. Confirm that the current claim is a planned baseline inside a `U.WorkPlan`, not the slot-bearing description itself and not performed work.
2. Name the target slot-bearing description and use its SlotSpecs from the governing description pattern, with A.6.5 slot discipline.
3. Name the EntityOfConcern under planning and the bounded context; add a grounding holon only when the current claim needs one.
4. Write planned-filling rows from SlotKind to planned filler, with ByValue or concrete RefKind mode and edition pins when reproducibility depends on them.
5. Keep projections, views, evidence-reference pins, guard-preparation refs, and crossing-policy refs as secondary references. They do not add rows, create evidence, pass a gate, or finalize launch values.

**Ordinary use.** For a minimal baseline, use context, time selector, target slot-bearing description, EntityOfConcern ref, and planned-filling rows.

**Reliance-bearing use.** Use the fuller record when reproducibility, launch-guard preparation, crossing expectations, suite or kit reuse, Part G universalization, publication-view projection, or P2W carry-through depends on the baseline.

**Stop condition.** Stop once the planned rows are explicit enough for the work-planning use, or lower the claim to a plan cue, source-gap note, relation governed by another FPF pattern, or blocked kind-definition gap without claiming a conforming planned baseline.

**What goes wrong if missed.** Teams hide planned choices in mechanism prose, suite descriptions, generated cards, "latest" references, local checklists, or execution logs. Later nobody can tell what was planned, what was performed, which edition changed, or which variance belongs to performed work.

**What this buys.** A small planned-baseline record that lets later performed work cite the intended slot fillings and record variance without rewriting the plan after the fact.

**Not this pattern when.** Not this pattern when the current claim is the slot-bearing description itself (`A.6.5` plus the governing description pattern), a mechanism definition (`A.6.1` or `E.20`), a performed work occurrence (`A.15.1`), an ordinary work plan without slot-filling rows (`A.15.2`), work-entry readiness or full-kit condition (`A.15.5`), evidence or assurance (`A.10` or `B.3`), a gate or constraint decision (`A.20` or `A.21`), publication-use behavior (`E.17`), or a declarative representation overread as work control (`C.2.P.DR`).

