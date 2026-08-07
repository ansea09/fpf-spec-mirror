---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__001_intro.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:intro — Intro"
line_start: 25587
line_end: 25636
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.16.0"
  - "A.2.1"
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

**At a glance.** Use `A.15.4` when a dashboard tile, credential view, copied approval, generated explanation, publication face, API response, source pointer, or weak indication is about to justify one exact work or reliance use, but a prerequisite for that use is not yet recoverable. Name the attempted use first. Then add one `RequiredPositionEntries` row for each independently required direct object; a one-position repair has one row, while a use with several prerequisites keeps them in separate rows. Each row names its `SubjectPatternLocator`—the pattern whose content defines, constrains, or tests the prerequisite—plus the direct-object kind, native project-side reference, required posture or currentness, and dependency on the attempted use. The repair record does not turn appearances or prerequisite rows into a new umbrella kind.

**Use this when.** Use this pattern when an acting user is ready to plan, start, continue, stop, or rely because a visible or copied appearance looks approved, current, safe, evidenced, delegated, released, or ready, but one exact attempted use still lacks one or more required relations or results. Record every independently required prerequisite as its own `RequiredPositionEntries` row; do not place several patterns, kinds, or project refs into one field.

**First output.** One compact `A.15.4` local repair record:

```text
A.15.4 local repair record:
  RelianceAppearanceRef:
  RelianceAppearanceKind:
  WorkOrRelianceUseKind:
  WorkOrRelianceUseRef:
  RequiredPositionEntries:
    - EntryId:
      SubjectPatternLocator:
      DirectObjectKind:
      ProjectSideObjectRef:
      RequiredPostureOrCurrentness:
      DependencyOnAttemptedUse:
  AllowedUseNow:
  AppearanceOverreadBlocked:
  RecoveryOrStopCondition:
```

`RequiredPositionEntries` is a local row set, not a new record kind, prerequisite U-kind, or generic `U.EntityRef` list. Each `SubjectPatternLocator` names the pattern whose content defines, constrains, or tests that row's `DirectObjectKind`; `ProjectSideObjectRef` then uses the native reference form required for that object. A navigation or proxy pattern does not substitute for that rule or test, and heterogeneous prerequisites remain separate rows.

**First repair use in practice.** Name what the encountered display, publication face, copied text, credential view, API response, pointer, or indication may safely do now: keep attention oriented, help find the required relation or result and its test in the §3 prerequisite lookup (including the permission and authority branch when that is the live claim), preserve a weak indication through `A.16.1`, support planning only through a `U.WorkPlan`, proceed inside a recovered relation, or block only the unsupported work or reliance claim.

**What goes wrong if missed.** The reliance appearance starts acting as if it already proves approval, gate passage, evidence, assurance, performed work, currentness, or release authorization. Work then proceeds or stops while the relation or result that must support the claim is missing, stale, revoked, or contradicted.

**Primary EntityOfConcern in plain terms.** One local repair relation for one exact attempted work or reliance use. It connects the reliance appearance and that attempted use to the smallest set of independent prerequisites, plus the safe current use and blocked appearance overread. The entries point to existing direct objects; they are not one new umbrella object.

**First repair checks.**
1. Name the reliance appearance's actual kind and publication position without treating its appearance as the required relation, result, or source relation itself.
2. Decide the live working moment: early attention to preserve, intended work to plan, reliance on already-performed work or a decision, or another operative relation for action now.
3. Fill `WorkOrRelianceUseKind` and `WorkOrRelianceUseRef`: the use being justified can be intended work, reliance on a claim, reliance on a performed-work occurrence, a work-relevant P2W claim, or a P2W chain position.
4. Create one `RequiredPositionEntries` row for each independently required direct object. This typed row set is the sole prerequisite set: a claim, instituted effect, gate decision, role assignment, evidence/currentness relation, plan, or other prerequisite each receives its own row. If permission or authority is current, first choose its exact object in the §3 branch, then fill `SubjectPatternLocator`, the direct-object kind, native project-side ref, required posture/currentness, and dependency on the attempted use. Never put comma-separated patterns, kinds, or refs into one field.
5. Follow dependencies through those direct objects. For permission or authority, use the dependency stated by the selected §3 row. An instituting act, enduring grant, conflict finding, gate decision, and work plan remain separate prerequisites; none substitutes for another row or inherits another row's posture.
6. Before allowing the attempted work or reliance, open every prerequisite through its typed reference. Check that the referenced relation actually obtains or the referenced result satisfies the criterion defined for it; that it is current and covers this beneficiary, action, target, scope, and time window; and that any evidence or source relation required for this reliance is present. When a relevant permission/norm conflict exists, give its exact `PermissionNormConflictFinding@Context` a separate row: an `unresolved` or norm-selecting disposition blocks this use but does not make the grant cease to obtain. When policy separately requires an A.21 gate or A.15.5 work-entry-readiness relation, give each its own row and require a current passing or ready result. Naming a record is only the first recovery step. If any check fails, keep `AllowedUseNow` at the safe narrowed use.

**Not this pattern when.** Stay in A.15 when the question under repair is only `U.Role`, holder, context, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation. Stay in `A.15.2` for WorkPlan construction, `A.15.3` for planned slot-filling baselines, and `A.15.5` when the question is full-kit condition or work-entry readiness rather than a reliance appearance being used as a reason for work or reliance. Stay in `A.16.1` and `C.2.4` when the honest current value is pre-articulation cue preservation and articulation level. Stay in `C.16.Q` when dynamic-quality or evaluative wording is the current claim. Stay in `A.6.A` when the current claim is action invitation. Stay in E.17 when the question under repair is only publication-face exposure or multi-view publication. When the direct evidence, gate, constraint, boundary, permission/authority, work, or other claim is already known, use the pattern and test selected by the §3 lookup instead of A.15.4.

**What this buys.** The acting engineer-manager can keep work moving without trusting appearances: use the reliance appearance for orientation or source-finding when that is all it can carry, proceed only inside the recovered relation when that relation exists, and turn repeated ambiguity into source-relation repair work rather than repeated manual reconstruction.

