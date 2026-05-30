---
chunk_kind: "child"
pattern_id: "A.6.3.CR"
pattern_title: "ConservativeRetextualization — same-described-entity textual re-expression"
section_id: "A.6.3.CR:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CR/A.6.3.CR__008_conformance-checklist.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "A.6.3.CR — ConservativeRetextualization — same-described-entity textual re-expression"
  - "A.6.3.CR:7 — Conformance Checklist"
line_start: 10924
line_end: 10942
dependencies:
  - "A.15"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CSC"
  - "A.6.4"
  - "A.7"
  - "B.5.2"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.ID.CR"
  - "F.18"
  - "F.9"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
keywords:
  - "direct vs correspondence-mediated rewrite"
  - "filtering"
  - "report rewrite"
  - "retextualization"
  - "same-described-entity textual re-expression"
  - "source tether"
  - "summary"
  - "translation"
---

### A.6.3.CR:7 - Conformance Checklist

1. **CC-CR-1 — Same described entity remains explicit.**
   The case preserves `describedEntityRef` without special pleading.
2. **CC-CR-2 — Textual re-expression remains the right family.**
   The result stays a textual re-expression rather than explanation or representation shift.
3. **CC-CR-3 — Loss, provenance, pinning, and reliability are explicit or inherited by pinned reference.**
   The case states these explicitly or inherits them through already-pinned content that remains visible to review.
4. **CC-CR-4 — Direct vs correspondence split is explicit.**
   The direct-vs-correspondence split is explicit and justified.
5. **CC-CR-5 — Correspondence support is named where needed.**
   If correspondence-mediated, `CorrespondenceModelRef` is declared.
6. **CC-CR-6 — Local conservativity witness remains satisfied.**
   The reviewed case does not silently widen modality, remove caveats, raise reliability posture, import bridge or substitution licence, or collapse declared alternatives beyond stated loss notes.
7. **CC-CR-7 — Handoff path is explicit on failure.**
   If the case fails any of the checks above, the handoff target is explicit (`ExplanationFaithfulnessProfile`, `RepresentationTransduction`, `A.6.4`, `B.5.2`, or another governing pattern).
8. **CC-CR-8 — Working-model first remains intact.**
   Ordinary same-entity rewrites stay lightweight; fuller explicit review records are reserved for load-bearing cases.

