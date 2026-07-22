---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__001_intro.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:intro — Intro"
line_start: 25305
line_end: 25353
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
  - "U.Work"
keywords:
  - "allowed use now"
  - "appearance overread blocked"
  - "appearance-based reliance"
  - "claim/effect position"
  - "copied approval"
  - "credential view"
  - "dashboard display"
  - "exact permission-result relation or finding"
  - "generated explanation"
  - "project-side claim/effect reference"
  - "publication face"
  - "reliance appearance"
  - "required claim before use"
  - "required instituted effect before use"
  - "work or reliance use"
---

## A.15.4 - Work-Relevant Appearance-Based Reliance Repair

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `A.15.4` when work or reliance is about to proceed from a dashboard tile, credential-status view, copied approval, generated explanation, provenance mark, API response, publication face, source-finding pointer, or weak indication, but the FPF position that would actually carry the required claim has not yet been named. That position is not another generic item: it is a governing pattern position such as a slot, relation record, exact permission-result relation or finding ref, gate decision, evidence or currentness relation, speech-act ref, commitment ref, role-state or credential-status relation, `U.WorkPlan`, or dated `U.Work` occurrence. First decide which working moment is live: preserve an early cue, plan intended work, rely on a claim that work or a decision already happened, or use an operative relation now. Then write the local repair record with the reliance appearance, its actual kind, the work or reliance use being justified, the required claim or instituted effect before use, the FPF pattern and concrete claim/effect-carrying position, the project-side claim/effect reference, the allowed use now, and the appearance overread being blocked. The record does not make dashboards, copied approvals, generated explanations, credentials, publications, pointers, or weak indications one kind.

**Use this when.** Use this pattern when the acting user is ready to plan, start, continue, stop, or rely because a dashboard, credential view, copied text, generated explanation, publication face, API response, or similar publication/display/credential/source-finding case looks approved, current, safe, evidenced, delegated, released, or ready, but the work still needs a concrete governing position and project-side reference named by value. Typical recovered positions are exact permission-result relation or finding refs, gate decisions, evidence or currentness relations, role-assignment refs, role-state or credential-status records, speech-act refs, commitment refs, `U.WorkPlan`, and dated work occurrences; the local fields `ClaimOrEffectPositionKind`, `ClaimOrEffectPositionRef`, `ClaimOrEffectPatternRef`, and `ProjectSideClaimOrEffectRef` state which FPF position is current.

**First output.** One compact `A.15.4` local repair record:

```text
A.15.4 local repair record:
  RelianceAppearanceRef:
  RelianceAppearanceKind:
  WorkOrRelianceUseKind:
  WorkOrRelianceUseRef:
  RequiredClaimBeforeUseRef:
  RequiredInstitutedEffectBeforeUseRef:
  ClaimOrEffectPatternRef:
  ClaimOrEffectPositionKind:
  ClaimOrEffectPositionRef:
  ProjectSideClaimOrEffectRef:
  AllowedUseNow:
  AppearanceOverreadBlocked:
  RecoveryOrStopCondition:
```

**First repair use in practice.** Name what the encountered display, publication face, copied text, credential view, API response, pointer, or indication may safely do now: keep attention oriented, help find the concrete governing record or relation—exact permission-result relation/finding ref, gate, evidence/currentness, speech act, commitment, role state, credential status, plan, or dated work occurrence—preserve a weak indication through `A.16.1`, support planning only through a `U.WorkPlan`, proceed inside a recovered relation, or block only the unsupported work or reliance claim.

**What goes wrong if missed.** The reliance appearance starts acting as if it already proves approval, gate passage, evidence, assurance, performed work, currentness, or release authorization. Work then proceeds or stops while the governing pattern position that should carry the claim is missing, stale, revoked, or contradicted.

**Primary EntityOfConcern in plain terms.** One local repair relation for one claim that is being used to guide intended work or reliance. This field names the current branch of the repair problem, not one new umbrella kind. The relation connects the reliance appearance, the work or reliance use being justified, the concrete FPF position that must carry the required claim or instituted effect before use, the project-side claim or effect reference, the safe current use, and the blocked appearance overread.

**First repair checks.**
1. Name the reliance appearance's actual kind and publication position without treating its appearance as the governing pattern position or source relation itself.
2. Decide the live working moment: early attention to preserve, intended work to plan, reliance on already-performed work or a decision, or another operative relation for action now.
3. Fill `WorkOrRelianceUseKind` and `WorkOrRelianceUseRef`: the use being justified can be intended work, reliance on a claim, reliance on a performed-work occurrence, a work-relevant P2W claim, or a P2W chain position.
4. Name `RequiredClaimBeforeUseRef` when the governing pattern must carry a claim before the work or reliance use is admissible.
5. Name `RequiredInstitutedEffectBeforeUseRef` when the governing pattern must carry an instituted effect, such as gate passage, role-state change, commitment, speech-act effect, or a strong grant validly instituted by an exact policy-recognized act. Leave it empty when no instituted effect is being relied on.
6. Fill `ClaimOrEffectPatternRef`, `ClaimOrEffectPositionKind`, and `ClaimOrEffectPositionRef`: the position kind is one of the already-governed positions such as slot, exact permission-result relation or finding ref, project reference, source-currentness relation, gate decision, evidence relation, speech-act ref, commitment ref, or work-occurrence ref. All five permission-side objects route by value to `A.2.8.PER`; only a strong grant may be an instituted effect under exact policy, while non-prohibition/non-violation findings, an exercise relation, and a conflict finding are not thereby instituted effects. For those, `RequiredClaimBeforeUseRef` names the claim required before use and the position fields cite the exact relation or finding.
7. Fill `ProjectSideClaimOrEffectRef` with the project-side reference that must be named by value for the work or reliance use.
8. Choose the lightest relation-governed disposition now: proceed inside the recovered relation, narrow the recovered use, preserve a cue pack, run a bounded reversible probe under `U.WorkPlan`, return to the source-currentness or governing pattern when freshness is the live claim, ask the holder, work-performing system, or project role holder identified by the relevant `RoleAssignmentRef` to expose or repair the missing position, or block only the unsupported claim or effect.

**Not this pattern when.** Stay in A.15 when the question under repair is only `U.Role`, holder, context, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation. Stay in `A.15.2` for WorkPlan construction, `A.15.3` for planned slot-filling baselines, and `A.15.5` when the question is full-kit condition or work-entry readiness rather than a reliance appearance being used as a reason for work or reliance. Stay in `A.16.1` and `C.2.4` when the honest current value is pre-articulation cue preservation and articulation level. Stay in `C.16.Q` when dynamic-quality or evaluative wording is the current claim. Stay in `A.6.A` when the current claim is action invitation. Stay in E.17 when the question under repair is only publication-face exposure or multi-view publication. Stay in A.10, B.3, A.20, A.21, A.2.8, A.2.8.PER, A.2.9, A.6, or A.15.1 when evidence, currentness, engineering justification, gate-passage claim, `ConstraintValidity` status, commitment, exact permission result, speech act, boundary claim, or work occurrence already governs the current use directly.

**What this buys.** The acting engineer-manager can keep work moving without trusting appearances: use the reliance appearance for orientation or source-finding when that is all it can carry, proceed only inside the recovered relation when that relation exists, and turn repeated ambiguity into source-relation repair work rather than repeated manual reconstruction.

