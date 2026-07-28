---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
section_id: "A.2.9:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__010_conformance-checklist-normative.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
  - "A.2.9:7 — Conformance Checklist (normative)"
line_start: 6562
line_end: 6572
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.6.C"
  - "A.7"
  - "U.Work"
keywords:
  - "actual communicative occurrence"
  - "admitted speech-act Work kind"
  - "authority-grounding assignment"
  - "evidence carrier"
  - "institutional target and effect"
  - "optional SpeechActRecord"
  - "performing U.System"
  - "publication relation"
  - "utterance description"
---

### A.2.9:7 — Conformance Checklist (normative)

1. **CC‑A.2.9‑1 (Occurrence, performer, and assignment).** One actual Work individual is admitted as `SA : U.SpeechAct`; its performer is an admitted accountable `U.System`, and the exact covering `U.RoleAssignment` has that system as holder. Any `SpeechActRecord` states those as claims and **MUST NOT** make the assignment, role value, organizational label, episteme, or carrier the performer.
2. **CC‑A.2.9‑2 (Act-type predicate).** The actual occurrence satisfies at least one context-local `SpeechActTypeRef`; merely writing a token into `SpeechActRecord.actTypes` is insufficient.
3. **CC‑A.2.9‑3 (Actual extent versus timestamp claim).** The occurrence has an actual temporal extent. A record's `window` must truthfully state that extent at the required precision; it does not create it.
4. **CC‑A.2.9‑4 (Observable relied-on occurrence).** If a checklist, guard, commitment, or grant cites the occurrence, one `SpeechActRecord` identifies it and cites an applicable utterance, carrier, or direct evidence relation. Evidence-critical uses **SHOULD** cite at least one carrier through A.10.
5. **CC‑A.2.9‑5 (Typed world-side effects, separate claims).** A record's `institutes.*` branch references only an exact commitment or obtaining relation occurrence through its declared RefKind. A grant uses `GrantedPermissionRelationRef@Context`; publication uses `EpistemePublicationRelationRef`; a subject-specific status uses its direct relation type. A status claim and its evidence stay separate, and no record field makes any effect obtain.
6. **CC‑A.2.9‑6 (Bridge-only cross-context use).** A receiving claim that interprets a `SpeechActRef` or `SpeechActRecord` in another bounded context cites the Bridge/policy that licenses that interpretation.
7. **CC‑A.2.9‑7 (No fabricated method anchor).** If the occurrence's actual `enactsMethod -> U.Method` relation cannot be recovered, the record names the unresolved claim and source-gap provenance, remains `observationOnly`, and is not used for gate or deontic provenance. A placeholder `U.MethodDescription` never closes the gap.
8. **CC‑A.2.9‑8 (Subject, target, and effect stay distinct).** A record uses `utteranceSubjectRefs` for aboutness and `institutionalTargetRefs` only for a policy-selected target. It claims actual change or institutional effect only through the exact direct relation; an informative act needs no changed target.

