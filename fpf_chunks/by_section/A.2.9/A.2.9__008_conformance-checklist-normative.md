---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Object)"
section_id: "A.2.9:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__008_conformance-checklist-normative.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Object)"
  - "A.2.9:7 — Conformance Checklist (normative)"
line_start: 5512
line_end: 5521
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
  - "act≠utterance≠carrier"
  - "approval/authorization/publication/revocation"
  - "communicative work"
  - "institutes"
  - "judgement context"
  - "provenance"
  - "speech act"
  - "window/freshness"
---

### A.2.9:7 — Conformance Checklist (normative)

1. **CC‑A.2.9‑1 (Accountable performer).** A normative `U.SpeechAct` record **MUST** identify `performedBy` as an accountable `RoleAssignmentRef` and **MUST NOT** use a specification episteme, interface-description episteme, or document-carried episteme as performer.
2. **CC‑A.2.9‑2 (ActTypes declared).** A `U.SpeechAct` record **MUST** include at least one `SpeechActTypeRef` recognized in its judgement context.
3. **CC‑A.2.9‑3 (Window explicit).** A `U.SpeechAct` record **MUST** have an explicit `window` (or inherit a window from its parent work record) so freshness and gating can be evaluated.
4. **CC‑A.2.9‑4 (Observable when used for gating/provenance).** If a speech act is cited by a checklist/guard or by `U.Commitment.source.speechActRef`, it **SHALL** have at least one `utteranceRef` or `carrierRef` that supports observation/audit in the given context; evidence‑critical uses **SHOULD** anchor at least one carrier via SCR/RSCR per A.10.
5. **CC‑A.2.9‑5 (Effects by reference).** If the act is intended to institute/update commitments/roles or statuses, those effects **SHOULD** be referenced in `institutes.*` by stable IDs.
6. **CC‑A.2.9‑6 (Bridge-only cross-context use).** If a `SpeechActRef` is interpreted for gating/provenance in a different bounded context than the act’s judgement context, the referencing object **MUST** cite the Bridge/policy that licenses that cross-context interpretation (no “same label implies same force”).


