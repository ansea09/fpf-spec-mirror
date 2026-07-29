---
chunk_kind: "child"
pattern_id: "A.6.3.CR"
pattern_title: "ConservativeRetextualization: EntityOfConcern-Preserving Textual Re-Expression"
section_id: "A.6.3.CR:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CR/A.6.3.CR__008_conformance-checklist.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "A.6.3.CR — ConservativeRetextualization: EntityOfConcern-Preserving Textual Re-Expression"
  - "A.6.3.CR:7 — Conformance Checklist"
line_start: 13765
line_end: 13783
dependencies:
  - "A.15"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.7"
  - "B.5.2"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "F.18"
  - "F.9"
keywords:
---

### A.6.3.CR:7 - Conformance Checklist

1. **CC-CR-1 — Same EntityOfConcern remains explicit.**
   The case preserves `entityOfConcernRef` without special pleading.
2. **CC-CR-2 — Textual re-expression remains the right family.**
   The result stays a textual re-expression rather than explanation or representation shift.
3. **CC-CR-3 — Loss, provenance, pinning, and reliability are explicit or inherited by pinned reference.**
   The case states these explicitly or inherits them through already-pinned content that remains visible to review.
4. **CC-CR-4 — Direct vs correspondence split is explicit.**
   The direct-vs-correspondence split is explicit and justified.
5. **CC-CR-5 — Correspondence witness is named where needed.**
   If correspondence-mediated, `CorrespondenceModelRef` is declared.
6. **CC-CR-6 — Local conservativity witness remains satisfied.**
   The reviewed case does not silently widen modality, remove caveats, raise reliability assessment, import bridge or substitution licence, or collapse declared alternatives beyond stated loss notes.
7. **CC-CR-7 — Governing pattern is explicit on failure.**
   If the case fails any of the checks above, the governing pattern for the changed claim is named explicitly (ExplanationFaithfulnessProfile, RepresentationSchemeTransition, A.6.4, B.5.2, or another governing pattern).
8. **CC-CR-8 — Working-model first remains intact.**
   Ordinary same-entity rewrites stay lightweight; fuller explicit review records are reserved for claim-bearing cases.

