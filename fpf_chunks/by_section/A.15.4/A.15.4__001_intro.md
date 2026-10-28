---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__001_intro.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:intro — Intro"
line_start: 30259
line_end: 30316
dependencies:
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.16.0"
  - "A.2.1"
  - "A.2.5"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "E.10.MOVE"
  - "E.17"
  - "E.17.EFP"
  - "F.6"
keywords:
  - "allowed or blocked use"
  - "appearance-based reliance"
  - "copied approval"
  - "credential"
  - "dashboard"
  - "exact attempted use"
  - "generated explanation"
  - "governing pattern and direct object"
  - "independent required-position rows"
  - "orientation and source-finding"
  - "project-side reference"
  - "publication face"
---

## A.15.4 - Work-Relevant Appearance-Based Reliance Repair

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `A.15.4` when a display, copied approval or generated explanation is about to justify work or reliance, but the prerequisite for that use is unclear. Ask three questions: **What am I about to do or rely on? Which fact, relation, decision, or result would warrant that use? Can I check that it holds for this case and time?** Keep the appearance at the lightest safe use until that prerequisite can be checked.

**Use this when.** Use this pattern only while appearance hides the direct object and test needed for one attempted use. If the direct question and the pattern that defines or tests it are already known, apply that pattern directly.

**First output.** Start with one ordinary sentence:

> This green tile points to `GateDecision-42`, but its link is stale. Use the tile only to find the current decision; do not deploy `Release-42` until that decision says `pass` for this release, target, scope, and window.

That sentence is a complete first result for this one-prerequisite use: it identifies the attempted use, appearance, missing prerequisite, allowed use now and return condition. If the prerequisite is recovered immediately, omit the note and apply its direct rule.

When a short worksheet is useful, unpack the same result without adding ontology:

```text
Attempted use:
Appearance:
Missing prerequisite:
Safe use now:
Blocked overread:
Return when:
```

Keep each independently required object, its subject pattern and test, required posture or currentness, and dependency on the attempted use separately recoverable. Keep a native reference when its governing rule or the receiving use requires one; an ordinary statement may identify its participants directly. Retain a sufficient existing note or accessible source account. Use `RequiredPositionEntries` when rows help compare or inspect the prerequisites; in that layout, use one row per direct object:

```text
RequiredPositionEntries:
  - SubjectPatternLocator:
    DirectObjectKind:
    ProjectSideObjectRef:
    RequiredPostureOrCurrentness:
    DependencyOnAttemptedUse:
```

These rows represent prerequisites defined by their subject patterns. When the analysis needs a separately referable claim, identify the C.2.1 episteme whose EntityOfConcern and ClaimGraph carry it; use an existing sufficient account when available. Split claims with different entities of concern. For a separated handoff, include the interpretation and source return the recipient would otherwise lose; a link is sufficient when that recipient can access and use it.

**First repair use in practice.** Choose the sufficient supported continuation: orientation or source finding, preservation of an early cue under A.16.1, ordinary planning, a bounded reversible probe, narrowed reliance, or a stop on the unsupported use. Admit WorkPlan content under A.15.2 only when that coordination claim is made.

**What goes wrong if missed.** The appearance is treated as proof of approval, gate passage, evidence, assurance, performed Work, currentness, or release authorization. Work then proceeds or stops while the relation or result that must support the claim is missing, stale, revoked, or contradicted.

**Subject of the repair in plain terms.** The pattern handles one attempted-use question. The appearance, attempted use, direct prerequisites, safe current use, and blocked overread retain the kinds and relations supplied by their own patterns.

**First repair checks.**
1. Name the appearance by its actual kind without treating it as the required relation or result.
2. Name the exact attempted use and the subject that use concerns.
3. Name the first missing prerequisite and the pattern that defines or tests it. A note stopping the unsupported use can finish there; a decision to proceed still requires every prerequisite consumed by that use.
4. Keep each independently required claim, instituted effect, relation occurrence, result, decision, assignment, evidence relation, currentness relation, or plan separately recoverable. Choose typed rows when their arrangement helps comparison or inspection.
5. Before allowing the attempted use, establish each required relation or result under its own criterion and match its applicable participants, scope, time and reliance basis to this case. Reuse an applicable established result; recheck what is changed, missing or expired.
6. A relevant permission or norm conflict, gate decision, or work-entry-readiness result remains a separate prerequisite. An unresolved conflict blocks only the affected use and does not make an independently obtaining grant cease.

**Not this pattern when.** Stay in A.15 when the question is only separation among the acting System, local system-role kind, classification judgment, direct `U.SystemRoleAssignment` species, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work`. Stay in `A.15.2` for WorkPlan construction, `A.15.3` for declaration-local planned-filling content, and `A.15.5` for full-kit condition or work-entry readiness. Stay in `A.16.1` and `C.2.4` for pre-articulation cue preservation, `C.16.Q` for a dynamic-quality claim, `A.6.A` for an action invitation, and E.17 for publication-face exposure. When the direct evidence, gate, constraint, boundary, permission, authority, Work, or other claim is already known, use the pattern and test selected by the §3 lookup instead of A.15.4.

**What this buys.** The practitioner can keep a useful source-finding or limited-use continuation while withholding an unsupported stronger conclusion. Repeated ambiguity can then be repaired in the source or presentation that causes it.

