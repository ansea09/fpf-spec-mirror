---
chunk_kind: "child"
pattern_id: "A.15.4"
pattern_title: "Work-Relevant Appearance-Based Reliance Repair"
section_id: "A.15.4:4"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.4/A.15.4__009_conformance-checklist.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "A.15.4 — Work-Relevant Appearance-Based Reliance Repair"
  - "A.15.4:4 — Conformance Checklist"
line_start: 25959
line_end: 25968
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

### A.15.4:4 - Conformance Checklist

| ID | Requirement (Normative Predicate) | Purpose and Rationale |
| :--- | :--- | :--- |
| **CC-A15.4-1 (One attempted use; typed prerequisite entries)** | Before an appearance guides work or reliance, a conforming use names one exact `WorkOrRelianceUseRef` and one `RequiredPositionEntries` row per independently required object. Every row supplies the direct owner, exact direct-object kind, native project-side ref, required posture/currentness, and dependency on the attempted use. A one-position repair has one row; a multi-prerequisite repair never stores comma-separated patterns, kinds, or refs and never coerces them into a generic `U.EntityRef` list. If any required row is absent or fails its posture, `AllowedUseNow` stays at the safe narrowed use. | Keeps every field fillable and every prerequisite under its direct owner. |
| **CC-A15.4-2 (P2W publication use boundary)** | A principle scheme, functional diagram, scenario, screen, or explanation that exposes a P2W chain guides only the `A.15` work or planning kind selected by the project use: method-family selection, selected method, `U.WorkPlan`, dated `U.Work`, work-result record, or result measurement. Claims outside that selected use require their own governing pattern position or source relation named by value. | Keeps P2W publication use tied to the work use under repair instead of turning publication form into project authority. |
| **CC-A15.4-3 (Lowering and refresh)** | When the governing pattern, governing pattern position, source-currentness relation, revocation relation, affected work target, relying context, or time window cannot be recovered, the disposition for the work or reliance claim is orientation, source-finding, contested use, bounded reversible probe, repair request, or blocked unsupported claim. The record states the return or refresh condition for changes to source currentness, revocation, governing decision, evidence relation, role-state register, credential-status register, context-state record, copied-source relation, generated-source relation, or publication relation. | Keeps A.15.4 useful without admitting source as a new kind. |
| **CC-A15.4-4 (Exact reopening judgment)** | Naming is only the first recovery step. Before `AllowedUseNow` permits the attempted use, follow every typed ref and verify that its relation obtains or its owner-defined result says pass/ready, is current, covers the beneficiary/action/target/scope/window, and has evidence/source support required for this reliance. A relevant `PermissionNormConflictFinding@Context` has its own row and current owner-defined disposition; an `unresolved` or norm-selecting result blocks the affected use but does not make a separately obtaining grant cease. Any separately required A.21 gate and A.15.5 work-entry-readiness relation is current and passes its own criterion. A named, recorded, but revoked or mismatched grant keeps the use blocked. | Prevents explicit records and green displays from substituting for current world-side or institutional conditions. |
| **CC-A15.4-5 (Register source is not the effect)** | A register-backed reliance keeps the register-entry episteme, its publication relation, constitutive rule, authorized entry-producing Work, actual exercised Work or evaluation Work when current, direct relation/finding, and evidence/currentness relation separate. The entry is authoritative source only for the exact claim or effect governed by the named rule. An institutional effect needs the authorized Work that the rule makes constitutive; exercise needs dated matching Work; a non-violation finding needs its owner-defined evaluation. Inscription establishes none of them. | Prevents record-as-world and record-as-Work overread. |

