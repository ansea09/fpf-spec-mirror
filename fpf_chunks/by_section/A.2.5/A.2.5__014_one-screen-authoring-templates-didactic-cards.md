---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "U.RoleStateGraph: The Named State Space of a Role"
section_id: "A.2.5:13"
section_title: "One‑screen authoring templates (didactic cards)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__014_one-screen-authoring-templates-didactic-cards.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.2.5 — U.RoleStateGraph: The Named State Space of a Role"
  - "A.2.5:13 — One‑screen authoring templates (didactic cards)"
line_start: 3755
line_end: 3805
dependencies:
  - "A.15"
  - "A.2.1"
  - "A.2.3"
  - "B.3"
  - "E.10.D1"
  - "F.9"
  - "U.RoleAssignment"
  - "U.RoleDescription"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:13 - One‑screen authoring templates (didactic cards)

Keep each RSG **teachable on one screen**. Use the following **notation‑neutral** templates when drafting RoleDescriptions (A.2.3).

#### A.2.5:13.1 - RSG card (per Role, per Context)

```
RSG for: <RoleName>   Context: <ContextName/Edition>
RCS characteristics (gist): <characteristic1>, <characteristic2>, …
States (◉ = enactable):
  - [◉] <StateName> — checklist gist; typical admission/maintenance/exit
  - [  ] <StateName> — …
  - …
Green‑Gate: step requiring <RoleName> is enactable iff holder asserts any ◉ state at Window.
Role algebra hooks: specialization (≤ … ), incompatibility (⊥ … ), bundles (⊗ … ).
```

#### A.2.5:13.2 - State checklist snippet (per State)

```
State <StateName> (enactable? yes/no)
Checklist (all must hold at Window):
  - <Observable criterion 1>  (e.g., CalibrationAge ≤ 30d)
  - <Observable criterion 2>  (e.g., exists SpeechAct(Approval) age ≤ 30d)
Maintenance (optional): <predicate> (e.g., EnvRangeOK)
Evidence Graph Ref: <Observation/Evaluation ids>
```

#### A.2.5:13.3 - Specialization refinement map (R' ≤ R)

```
Refinement map π : S(R') → S(R)
R' state        π(state in R)   entailment note (why Checklist_R' ⇒ Checklist_R)
-----------     -------------    -----------------------------------------------
<Ready+>        Ready            adds stricter fatigue & independence thresholds
<Authorized+>   Authorized       requires same approval + extra duty segregation
…
```

#### A.2.5:13.4 - SoD focus (⊥) — enactable pairs

```
Incompatibility ⊥ (applies when both sides enactable at same Window):
  <RoleA.StateX>  ⊥  <RoleB.StateY>
  <RoleA.(any ◉)> ⊥  <RoleB.(any ◉)>   // default if not refined
Rationale: <one‑line reason>
```

> **Didactic cue.** If your “template” spills beyond a screen, you’re drifting into **method-order description**. Pull back to **eligibility** (RSG) and **recognition** (checklists).


