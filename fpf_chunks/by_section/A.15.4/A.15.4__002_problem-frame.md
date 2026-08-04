---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__002_problem-frame.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:1 — Problem Frame"
line_start: 25656
line_end: 25673
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

### A.15.4:1 - Problem Frame

Dashboards, credential views, generated explanations, copied approvals, provenance labels, green tiles, schema wording, API wording, and composed source-relation chains often look ready for work or reliance before the record or relation that carries the claim is visible. The practical problem is to decide what an engineer-manager may do now without turning appearance into approval or permission, gate passage, evidence, assurance, performed work, role-assignment currentness, role-state or credential-status currentness, or release authorization.

**Plain recognition line.** Let the dashboard tile, credential view, copied approval, generated explanation, publication face, API response, or pointer lead to the governing pattern position that must be checked. Do not let the reliance appearance become the relation, slot filler, or project-side reference that authorizes work or reliance.

**Reliance-appearance and claim/effect-position discipline.** In this pattern, `source` is not a generic kind. The governing value for the attempted use is the direct object selected by its owner: an actual relation occurrence, owner-defined decision/finding/status result, plan, Work occurrence, or claim about that object. A project record may be a `U.Episteme` that names the direct object, and a publication relation may expose that record; neither the record nor its display makes the direct object obtain. If no typed reference and owner-defined test can be recovered, keep the appearance at orientation, source-finding, cue-pack preservation, repair request, or bounded-probe use.

**Ontological unpacking of the local repair relation.** `A.15.4` does not introduce `U.Source`, `U.RequiredValue`, `WorkReliancePremise`, a generic cue head, or a generic visible-thing kind. It governs one dependent repair relation among already-governed values:
- `RelianceAppearanceRef` names the dashboard tile, credential view, copied wording, generated explanation, publication face, carrier, display, API wording, source-finding pointer, or low-articulation indication whose appearance is tempting the work or reliance use. Its actual kind is named separately in `RelianceAppearanceKind`, so the record can distinguish an episteme, episteme publication, publication face, carrier, display, copied wording, generated explanation, API wording, source-finding pointer, or low-articulation indication without making them one kind. If the live value is a preserve-worthy early cue, use `U.PreArticulationCuePack` under `A.16.1`.
- `WorkOrRelianceUseKind` and `WorkOrRelianceUseRef` name the use being justified: intended work, reliance on a claim, reliance on performed work, a work-relevant P2W claim, or a P2W chain position. These fields select the current branch; they do not create a durable kind.
- `RequiredPositionEntries` is the sole prerequisite set and contains one row per independently required direct object. Every row states `DirectOwnerPatternRef`, `DirectObjectKind`, the owner's native `ProjectSideObjectRef`, `RequiredPostureOrCurrentness`, and `DependencyOnAttemptedUse`. One row may point to a required claim, another to an instituting speech act, grant, conflict finding, gate decision, assignment, evidence/currentness relation, plan, or other direct object; the row set creates none of them and never turns a claim into an instituted effect.
- `AllowedUseNow` states what use remains admissible after repair, such as orientation, source-finding, bounded reversible probe, narrowed reliance, or proceed-inside-recovered-relation.
- `AppearanceOverreadBlocked` names the false use that the reliance appearance would create by appearance, for example treating a dashboard color as gate passage or a copied approval as a current speech act.
- `RecoveryOrStopCondition` names the first failed prerequisite and what must change. Before reopening, follow every typed ref and verify that the relation obtains or the result passes its owner-defined criterion, is current, covers the attempted beneficiary/action/target/scope/window, and has the evidence or source relation required for this reliance. When a relevant conflict exists, its separate `PermissionNormConflictFinding@Context` row must carry a current owner-defined disposition; an `unresolved` or norm-selecting result blocks the affected use without changing grant currentness. A named or complete-looking record is not enough.

Here `evidence relation`, `attestation relation`, and `currentness relation` mean `A.10` evidence-provenance, attestation, or currentness relations named by value. They are not work-procedure elements and do not carry authorization by their wording.

