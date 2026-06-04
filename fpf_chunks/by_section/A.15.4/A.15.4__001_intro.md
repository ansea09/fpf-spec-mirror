---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Source Restoration"
section_id: "A.15.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__001_intro.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "A.15.4 — Work-Relevant Source Restoration"
  - "A.15.4:intro — Intro"
line_start: 20561
line_end: 20591
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

**At a glance.** This A.15 cluster member tells an engineer-manager which exact project-side FPF kind, relation, and reference must be recovered before an encountered episteme, episteme publication, display, credential view, generated explanation, copied statement, provenance mark, dashboard tile, schema wording, API wording, or composed source chain may justify a work claim or reliance claim.

**Use this when.** Use this pattern when a visible item is about to guide a work move, reliance move, or work-relevant P2W claim by appearance, and the acting user must recover the exact project-side FPF kind and reference before proceeding.

**First output.** One compact restoration note: encountered item; live work claim, reliance claim, work-relevant P2W claim, or P2W chain position; governing FPF pattern; exact project-side FPF kind and reference needed; admissible next project move now; and blocked overread.

**What goes wrong if missed.** Teams treat a visible dashboard, credential view, copied approval, generated explanation, provenance mark, schema wording, API wording, publication, display, or cue as if it already carried approval, permission, gate passage, evidence, engineering justification, performed work, release permission, role relation, or status relation. Work then proceeds or stops on appearance while the governing FPF pattern and exact project-side FPF kind and reference that actually carry the claim or effect are missing, stale, revoked, or contradicted.

**Primary EntityOfConcern in plain terms.** One source-restoration relation for one live work claim, reliance claim, work-relevant P2W claim, or P2W chain position: encountered item, live claim or effect, governing FPF pattern, exact project-side FPF kind and reference needed, admissible next project move now, and blocked overread. It is not a new `authoritySourceRef`, evidence source, gate record, engineering-justification record, work occurrence, or generic publication kind.

**First admissible project move in plain terms.** Recover or name the receiving FPF pattern, exact project-side FPF kind and reference, and live relation before allowing the encountered item to guide work or reliance. When that relation is absent or insufficient, narrow the move, reopen or refresh the source, run only a bounded reversible probe under a work plan, or block the unsupported claim or effect.

**Recognition block vs assurance block.** Read **At a glance**, **Use this when**, **First output**, **What goes wrong if missed**, **Primary EntityOfConcern**, **First admissible project move**, **Working action path**, **Not this pattern when**, and **What this buys** as the primary recognition block. Read the field tables, lookup table, lint cues, stress cases, conformance checklist, SoTA alignment, and relations below as assurance blocks and companion material that tighten the same source-restoration claim; they do not widen this pattern into an evidence, gate, engineering-justification, speech-act, commitment, boundary, or work-occurrence pattern.

**Working action path.**
1. Name the encountered source kind and publication position without treating its appearance as the source relation itself.
2. Name the live work claim, reliance claim, work-relevant P2W claim, or P2W chain position and the claim or effect that would be carried.
3. Recover the governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect.
4. Choose the lightest admissible project move now: proceed inside the recovered exact relation, narrow the move, run a bounded reversible probe under `U.WorkPlan`, reopen or refresh the source, ask the accountable role assignment to expose or repair the missing source episteme, publication, register entry, or project record, or block only the unsupported claim or effect.
5. Return to `A.15` only when the remaining live question is `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation.

**Not this pattern when.** Stay in A.15 when the live problem is only `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation. Stay in E.17 when the live problem is only publication-face exposure or multi-view publication. Stay in A.10, B.3, A.20, A.21, A.2.8, A.2.9, A.6, or A.15.1 when evidence, currentness, engineering justification, gate validity, constraint validity, commitment, speech act, boundary claim, or work occurrence already governs the live claim or effect directly.

**What this buys.** The acting engineer-manager can keep work moving at the lightest admissible level: proceed inside the recovered exact relation, narrow the move, run a bounded reversible probe under a work plan, reopen the needed exact project-side FPF kind and reference, ask the role assignment accountable for that source to expose or repair it, or block only the unsupported claim or effect while preserving narrower admissible use.

