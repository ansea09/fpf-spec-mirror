---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Source Restoration"
section_id: "A.15.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__001_intro.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.15.4 — Work-Relevant Source Restoration"
  - "A.15.4:intro — Intro"
line_start: 22145
line_end: 22184
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.8"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.2.1"
  - "E.17"
  - "E.17.EFP"
  - "U.Flow.ConstraintValidity"
  - "U.Work"
keywords:
  - "P2W load and position"
  - "admissible next project move"
  - "approval-looking display"
  - "blocked overread"
  - "copied statement"
  - "credential view"
  - "dashboard display"
  - "generated explanation"
  - "provenance mark"
  - "required project-side FPF kind and reference"
  - "work-relevant source restoration"
---

## A.15.4 - Work-Relevant Source Restoration

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `A.15.4` when an encountered source candidate is about to guide work or reliance before the claim-carrying source has been recovered. The source candidate may be a dashboard tile, credential view, copied approval, generated explanation, provenance mark, schema wording, API wording, publication face, or composed source chain.

**Use this when.** Use this pattern when the acting user is ready to proceed because something looks approved, current, safe, evidenced, delegated, released, or ready, but the work claim or reliance claim still needs its governing project source named by value.

**First output.** One compact source-restoration note:

```text
SourceRestorationNote:
  EncounteredSourceCandidate:
  WorkOrRelianceClaimUnderRepair:
  ClaimOrEffectNeeded:
  GoverningSourceNeeded:
  RelationGovernedMoveNow:
  BlockedOverread:
  StopOrReopenCondition:
```

**First move in practice.** Name what the encountered source candidate may safely do now: orient the user, help find a source, allow a bounded reversible probe under `U.WorkPlan`, proceed inside a recovered relation, or block only the unsupported work or reliance claim.

**What goes wrong if missed.** A dashboard, credential view, copied approval, generated explanation, provenance mark, schema wording, API wording, publication, display, or cue starts acting as the work or reliance source relation. Work then proceeds or stops while the gate decision, evidence path, speech act, commitment, role assignment, status record, work occurrence, source episteme, or source publication that would carry the claim is missing, stale, revoked, or contradicted.

**Primary EntityOfConcern in plain terms.** One source-restoration relation for one work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair. The relation connects the encountered source candidate, the needed claim or effect, the source that must carry that claim, the next relation-governed move, and the blocked overread.

**First restoration checks.**
1. Name the encountered source-candidate kind and publication position without treating its appearance as the source relation itself.
2. Name the work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair.
3. Name the claim or effect that would be carried: gate passage, release reliance, evidence relation, assurance claim, speech act, commitment, role relation, status currentness, work occurrence, source currentness, boundary claim, or another claim named by value.
4. Recover the source that must carry that claim: the governing FPF pattern plus the reference named by value.
5. Choose the lightest relation-governed disposition now: proceed inside the recovered relation, narrow the move, run a bounded reversible probe under `U.WorkPlan`, reopen or refresh the source, ask the accountable role assignment to expose or repair it, or block only the unsupported claim or effect.

**Not this pattern when.** Stay in A.15 when the question under repair is only `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation. Stay in E.17 when the question under repair is only publication-face exposure or multi-view publication. Stay in A.10, B.3, A.20, A.21, A.2.8, A.2.9, A.6, or A.15.1 when evidence, currentness, engineering justification, gate-passage claim, `ConstraintValidity` status, commitment, speech act, boundary claim, or work occurrence already governs the claim or effect directly.

**What this buys.** The acting engineer-manager can keep work moving without trusting appearances: use the source candidate for orientation or source-finding when that is all it can carry, proceed only inside the recovered relation when that relation exists, and turn repeated ambiguity into source-system repair work rather than repeated manual reconstruction.

