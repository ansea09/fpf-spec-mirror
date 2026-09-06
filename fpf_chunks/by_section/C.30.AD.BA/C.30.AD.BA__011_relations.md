---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:8"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__011_relations.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:8 — Relations"
line_start: 60023
line_end: 60034
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "F.18"
  - "G.11"
keywords:
---

### C.30.AD.BA:8 - Relations

- **Specializes:** `C.30.AD` for built-asset architecture-description use.
- **Uses architecture and structure patterns:** `C.30`, `C.30.ASV`, `A.22`, `A.6.F`, `A.6.M`, `C.30.TFS-REL`, and `C.30.LCA`.
- **Uses description, view, representation, and publication patterns:** `C.2.1`, `A.7`, `E.17.0`, `E.17`, `E.24.PUB`, and `C.29`.
- **Uses relation, naming, and currentness patterns:** the exact designation/reference predicate and assertion; `A.6.P` for precision repair; `A.6.RCD` only for a demonstrated missing reusable predicate; `A.6.REL` only after the relation kind is admitted, current facts satisfy its obtaining predicate, and occurrence identity matters; `F.18`; and `G.11`.
- **Uses lifecycle information-management source discipline from:** exact published `ISO 19650-1:2018` and `ISO 19650-3:2020` editions through source-to-use, edition, currentness, source-return, and admissible-use boundaries, without ontology or authority import.
- **Records design/run separation in:** one local `BuiltAssetDesignRunSeparationUse` over exact C.2.1 descriptions, `A.15.1` Work, source-use paths, `G.11` currentness, directly governed correspondence or coupling, and A.3.4 transformation refs; the local classification admits no kind or relation.
- **Use for auxiliary-view claims:** `C.16` for characteristic measurement, `A.15.1` for operation or maintenance Work, `C.27.TA` for positive temporal aspects, `C.27` for action-guiding temporal-claim adequacy, `C.28` when an intervention, maintenance action, simulation, telemetry change, or claimed effect is used causally, `A.10` for evidence or material reliance, `B.3` for assurance, and `G.11` for currentness and reopen conditions.
- **Use for gate- and release-looking claims:** `A.21` when a named gate must decide a bounded action or its `GateDecisionResult` is being relied on; the display remains a cue until the required result is established. Route a release action or other performed Work to `A.15.1`, work-entry readiness to `A.15.5`, a permission result or exercise to `A.2.8.PER`, an instituting or revoking grant act to `A.2.9`, and a subject-release claim to its named predicate and participants or `A.6.RCD missing-governor`; none of these claims entails another.
- **Use for other claims:** `A.3.4` and the direct transformation, evaluation, evidence, assurance, Work, decision, acceptance, or project-use pattern named by the claim.

