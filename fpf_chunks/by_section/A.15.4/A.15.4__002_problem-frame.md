---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__002_problem-frame.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:1 — Problem Frame"
line_start: 23657
line_end: 23676
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.16.0"
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
  - "generated explanation"
  - "project-side claim/effect reference"
  - "publication face"
  - "reliance appearance"
  - "required claim before use"
  - "required instituted effect before use"
  - "work or reliance use"
---

### A.15.4:1 - Problem Frame

Dashboards, credential views, generated explanations, copied approvals, provenance labels, green tiles, schema wording, API wording, and composed source-relation chains often look ready for work or reliance before the record or relation that carries the claim is visible. The practical problem is to decide what an engineer-manager may do now without turning appearance into approval, gate passage, evidence, assurance, performed work, role-assignment currentness, role-state or credential-status currentness, or release authorization.

**Plain recognition line.** Let the dashboard tile, credential view, copied approval, generated explanation, publication face, API response, or pointer lead to the governing pattern position that must be checked. Do not let the reliance appearance become the relation, slot filler, or project-side reference that authorizes work or reliance.

**Reliance-appearance and claim/effect-position discipline.** In this pattern, `source` is not a generic kind. The governing value for the work or reliance use is the concrete slot, direct relation record, decision record, state/status/currentness record, work plan, work occurrence, or project-side reference that carries the required claim or instituted effect before use. Source-finding pointers, publication faces, publication carriers, renderings, dashboards, copied wording, generated explanations, and weak indications remain reliance appearances unless they expose that governing position, relation, or project-side reference. If no governing pattern position can be named, keep the reliance appearance at orientation, source-finding, cue-pack preservation, repair request, or bounded-probe use.

**Ontological unpacking of the local repair relation.** `A.15.4` does not introduce `U.Source`, `U.RequiredValue`, `WorkReliancePremise`, a generic cue head, or a generic visible-thing kind. It governs one dependent repair relation among already-governed values:
- `RelianceAppearanceRef` names the dashboard tile, credential view, copied wording, generated explanation, publication face, carrier, display, API wording, source-finding pointer, or low-articulation indication whose appearance is tempting the work or reliance use. Its actual kind is named separately in `RelianceAppearanceKind`, so the record can distinguish an episteme, episteme publication, publication face, carrier, display, copied wording, generated explanation, API wording, source-finding pointer, or low-articulation indication without making them one kind. If the live value is a preserve-worthy early cue, use `U.PreArticulationCuePack` under `A.16.1`.
- `WorkOrRelianceUseKind` and `WorkOrRelianceUseRef` name the use being justified: intended work, reliance on a claim, reliance on performed work, a work-relevant P2W claim, or a P2W chain position. These fields select the current branch; they do not create a durable kind.
- `RequiredClaimBeforeUseRef` is filled when the governing pattern must carry a claim before the work or reliance use is admissible.
- `RequiredInstitutedEffectBeforeUseRef` is filled when the governing pattern must carry an effect before the work or reliance use is admissible, such as a gate passage, role-state change, commitment, or speech-act effect.
- `ClaimOrEffectPatternRef`, `ClaimOrEffectPositionKind`, `ClaimOrEffectPositionRef`, and `ProjectSideClaimOrEffectRef` name the direct FPF pattern, the position kind in that pattern, the exact position or relation to inspect, and the project-side reference required by that pattern.
- `AllowedUseNow` states what use remains admissible after repair, such as orientation, source-finding, bounded reversible probe, narrowed reliance, or proceed-inside-recovered-relation.
- `AppearanceOverreadBlocked` names the false use that the reliance appearance would create by appearance, for example treating a dashboard color as gate passage or a copied approval as a current speech act.
- `RecoveryOrStopCondition` names what blocks the work or reliance use and what newly exposed or repaired governing pattern value would reopen it.

Here `evidence relation`, `attestation relation`, and `currentness relation` mean `A.10` evidence-provenance, attestation, or currentness relations named by value. They are not work-procedure elements and do not carry authorization by their wording.

