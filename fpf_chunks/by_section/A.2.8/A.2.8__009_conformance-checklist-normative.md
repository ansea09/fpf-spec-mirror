---
chunk_kind: "child"
pattern_id: "A.2.8"
pattern_title: "U.Commitment (Deontic Commitment Object)"
section_id: "A.2.8:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8/A.2.8__009_conformance-checklist-normative.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "A.2.8 — U.Commitment (Deontic Commitment Object)"
  - "A.2.8:7 — Conformance Checklist (normative)"
line_start: 5151
line_end: 5163
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.2.6"
  - "A.6.B"
  - "A.6.C"
  - "A.7"
  - "E.8"
  - "U.PromiseContent"
  - "U.Work"
keywords:
  - ") but makes the structure explicit"
  - "BCP‑14 (RFC 2119/8174)"
  - "adjudication hooks"
  - "commitment"
  - "deontics"
  - "evidenceRefs"
  - "modality normalization"
  - "obligation"
  - "permission"
  - "prohibition"
  - "scope+validity window"
---

### A.2.8:7 - Conformance Checklist (normative)

1. **CC‑A.2.8‑1 (Accountable subject).** A normative `U.Commitment` **MUST** name an accountable `subject` (role assignment, role enactor, or party) and **MUST NOT** use a specification episteme, interface-description episteme, or document-carried episteme as subject.

2. **CC‑A.2.8‑2 (Explicit modality).** A normative `U.Commitment` **MUST** specify `modality` as `DeonticModalityToken` (with any RFC-keyword synonyms normalized to it).

3. **CC‑A.2.8‑3 (Scope & validity explicit).** A normative `U.Commitment` **MUST** specify `scope` (`U.ClaimScope`) and `validityWindow` (`U.QualificationWindow`), or explicitly cite the context policy that supplies defaults (do not rely on “implied defaults”).

4. **CC‑A.2.8‑4 (Referents present and by ID).** `referents` **MUST** be non‑empty. If the bound content exists as claim IDs, the commitment **SHOULD** reference those IDs in `referents` rather than restating their content.

5. **CC‑A.2.8‑5 (Auditable commitments have hooks).** If the commitment is intended to be auditable, it **SHALL** include `adjudication.evidenceRefs` referencing the evidence claims (typically `E-*`) that make adjudication possible.
6. **CC‑A.2.8‑6 (Evidence separation).** If an `E-*` claim is referenced only for measurement/verification, it **SHALL** appear in `adjudication.evidenceRefs` (not in `referents`).

