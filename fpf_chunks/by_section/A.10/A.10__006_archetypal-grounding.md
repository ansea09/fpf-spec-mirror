---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
section_id: "A.10:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__006_archetypal-grounding.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "A.10 — Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
  - "A.10:5 — Archetypal Grounding"
line_start: 23115
line_end: 23122
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.PROD"
  - "A.19"
  - "A.2-family"
  - "A.2.4"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.10.ROLE"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
  - "G.11"
  - "G.4"
keywords:
  - "RelianceDisposition"
  - "actual-use relation"
  - "bounded use"
  - "carrier"
  - "claim/result episteme"
  - "currentness"
  - "dated work"
  - "direct relation"
  - "evidence-provenance path"
  - "relied-on claim"
  - "rival explanation"
  - "source publication"
  - "unsupported overread"
---

### A.10:5 - Archetypal Grounding

**Runtime acceptance from a measurement result.** C.16 dated measurement work obtains a pressure measurement result with uncertainty under a named model and calibration; a distinct C.2.1 episteme states it. If the claim that this Work first constituted that episteme is current, A.15.PROD recovers one local entity-inception claim. Separate evaluation work applies the declared G.4 pressure clause through A.6.1 bindings and obtains `unknown`; another C.2.1 episteme states that verdict. Later C.11 decision work uses the verdict episteme as a premise and defers. A.10 can trace the source publications, calibration and measurement work, result episteme, evaluation work, clause declaration, exact bindings, provenance, and any currentness or live rival that affects reliance. The supplied G.4 `unknown` and C.11 deferral are separate results, not an A.10 disposition. The bounded claim/use and the evidence basis needed by §4.5's seven-value rule are not specified here, so the A.10 reliance classification remains unresolved. Select that claim and use and recover their required basis before classifying them; neither `unknown` nor deferral fills the gap. No ledger edge establishes measurement, verdict, decision, or use.

**Meta-analysis.** Source study publications, datasets, analysis code, inclusion work, statistical method, and synthesis work are recovered by their direct relations. The application of the statistical method and the result relation establish the pooled estimate and uncertainty; the relied-on claim in the result's C.2.1 episteme states that pooled estimate and uncertainty. A.10 records source identity, transformations, coverage, provenance, currentness, and the bounded clinical or policy use, not a generic `validatedBy` relation.

**Credential display.** A credential view can support credential currentness when the issuer or trust-root object and relation, verifier, relying use, and applicable verification facts are recoverable. Retain validity limits when present or required, status-source/register and revocation facts when the mechanism is present or the selected verification/use policy requires them, and holder binding when that claim or regime requires it. A bearer credential need not identify its holder, and a holder need not be the credential subject; neither case relaxes the actual selected policy. Permission remains with A.2.8.PER, commitment with A.2.8, an issuing act with A.2.9, and an exact system-role-assignment occurrence with A.2.1. A status assertion requires its direct status pattern; an entry predicate requires its defining pattern and A.6.B boundary classification; gate passage remains with A.21. Display presence creates none of them.

