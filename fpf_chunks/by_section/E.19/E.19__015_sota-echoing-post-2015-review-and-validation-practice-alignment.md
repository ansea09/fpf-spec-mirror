---
chunk_kind: "child"
pattern_id: "E.19"
pattern_title: "Pattern Quality Gates: Review & Refresh Profiles"
section_id: "E.19:11"
section_title: "SoTA-Echoing — post-2015 review and validation practice alignment"
source_path: "FPF-Spec.md"
output_path: "by_section/E.19/E.19__015_sota-echoing-post-2015-review-and-validation-practice-alignment.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "E.19 — Pattern Quality Gates: Review & Refresh Profiles"
  - "E.19:11 — SoTA-Echoing — post-2015 review and validation practice alignment"
line_start: 63696
line_end: 63709
dependencies:
  - "A.6.P"
  - "C.2.P"
  - "E.10"
  - "E.8"
  - "E.9"
  - "F.18"
keywords:
  - "(see H-8)"
  - "MUST NOT modify modeled-world entities (e.g"
  - "and (if needed) reference them from CC items"
  - "inside the predicate)"
  - "where a non-deontic Invariant: predicate is required)"
  - "“Earth”"
  - "“RoleAssignment”"
  - "“Role”"
  - "“holon”) — express those as Invariant: / Well‑formedness constraint: predicates instead"
---

### E.19:11 - SoTA-Echoing — post-2015 review and validation practice alignment

**Evidence binding note.** If a SoTA Synthesis Pack exists for review and validation discipline or refresh discipline in your Context, cite it and keep this section consistent with it; otherwise treat the table below as a provisional seed that should not be duplicated elsewhere without an explicit update record.

| Claim (E.19 need)                                                      | SoTA practice (post‑2015)                                                                                   | Primary source (post‑2015)                                                                  | Alignment with E.19                                                                       | Adoption status                                                                                              |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Reviews need explicit criteria, not informal taste.                    | Move from folklore validation to explicit validation methods and documented criteria.                       | Riehle et al. (2020), “Pattern Discovery and Validation Using Scientific Research Methods”. | PCPs make criteria explicit; CC coherence is enforced.                                    | **Adopt.** Keep methods lightweight but explicit.                                                            |
| A stable structure improves comparability and reduces ambiguity.       | Standards specify required viewpoints, concerns, and consistency rules for descriptions.                      | Joint ISO, IEC, and IEEE 42010:2022 (architecture description).                                         | PCP‑BASE includes structural integrity and internal consistency.                          | **Adopt and adapt.** Adopt conformance mindset; adapt to pattern-language template and didactic grounding.       |
| Pattern writing benefits from explicit guidance plus critique culture. | Pattern-language communities emphasize clear template usage, consequences, and critique for quality.        | Iba (2021), “How to Write Patterns …” (PLoP 2021).                                          | Baseline checks enforce meaningful sections; anti-patterns make critique concrete.        | **Adopt.** Directly supports admission quality.                                                              |
| “Living” guidance needs refresh discipline.                            | Reporting and review guidance is updated and versioned; reviewers track changes and report deltas clearly. | Page et al. (2021), PRISMA 2020 statement and explanation papers.                           | Runs require explicit decisions and deltas in SoTA‑Echoing. | **Adapt.** Use the “versioned guidance + explicit deltas” principle without importing implementation or process mandates. |
| Retrieval-facing entry changes need selected evidence dimensions, not universal benchmarks. | RAG evaluation practice separates context relevance, answer faithfulness, answer relevance, and support quality. | Es et al. (2023), `RAGAS`; Saad-Falcon et al. (2023), `ARES`. | `PCP-ENTRY-E4` and related evidence modes select tiny retrieval fixtures only when retrieval-facing behavior or observed misretrieval is live; the row does not authorize a universal benchmark for every pattern entry. | **Adopt lightly.** Keep hit, support, authority, and faithfulness dimensions only when retrieval-facing behavior is live; ordinary entry prose remains prose-only. |

Action result from the pattern-review and validation practice basis: an `E.19` pass, caution, return-for-repair result, narrower-use result, clean checklist, or clean retrieval-entry check does not become project certification, project evidence, safety support, gate input, release justification, compliance support, assurance material, work authority, publication truth, or project refusal/approval. The local E.19 result is a pattern-quality review or refresh claim over the named target pattern, selected profile, defects found or cleared, admission, refresh, narrower-use, repair-return, or selected pattern-quality boundary. Reopen the pattern-quality result when the reviewed text, accepted-basis decision, SoTA support, related exact pattern, selected support reading, profile trigger, target boundary, or attempted project-side reuse changes.

