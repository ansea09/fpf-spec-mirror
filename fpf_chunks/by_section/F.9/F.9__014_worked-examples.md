---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:12"
section_title: "Worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__014_worked-examples.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:12 — Worked examples"
line_start: 89997
line_end: 90022
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
keywords:
  - "A.10/B.3 reliance"
  - "LocalSenseClaim> projections"
  - "different <ReferenceScheme"
  - "exact F.17 SchemeSenseCell endpoints"
  - "inverse/composition checks"
  - "obtaining Bridge"
  - "optional CL evidence-strength shorthand"
  - "optional card"
  - "quantum/coarsening exit"
  - "relation-semantic profile"
  - "separate C.2.1 bounded-use claim"
---

### F.9:12 - Worked examples

#### F.9:12.1 - Service target and monitoring observation

A service team resolves two exact cells: the ITIL sense of an availability target and the SOSA sense of an availability observation. Profile `P-SLO-OBS-v2` states a `Measurement-evidence-for` semantic relation: the observation sense concerns a measured availability quantity relevant to the target sense, while observation and target remain different kinds of claim. The profile names the endpoint readings, direction of the semantic relation, applicability to the cited editions, Boolean condition, and required quantity-definition dependency. Current meanings satisfy it, so Bridge `b-slo-obs` obtains.

The team next proposes use `u-slo-check`: compare one observation result with the target. Direction `d-slo` is observation-to-target; rule `r-slo` requires the same quantity kind, aligned windows, and the stated unit conversion; tolerance `t-slo` permits the named rounding loss but no quantity-kind change. A C.2.1 claim with EntityOfConcern `b-slo-obs` states affirmative polarity for `<u-slo-check,d-slo,r-slo,t-slo>`.

Because this is an ordinary bounded evidence use below the B.3 threshold and no assurance claim is made, the team recovers the exact A.10 evidence-provenance graph relation for the observation record and states `RelianceDisposition=pass` only for `u-slo-check`. That supports relying on the claim within its boundary. It does not make the SLO fulfilled, authorize acceptance, or prove that comparison Work occurred. Those claims remain with their direct owners.

#### F.9:12.2 - Behavioral participant and access role

An exact `Partial-overlap` Bridge obtains between a BPMN participant sense and a named RBAC role sense when the profile's overlap and difference conditions are satisfied. A separate bounded-use claim proposes the label "actor" for one glossary row, in the stated direction, under a rule that preserves assignment moment, enforcement locus, multiplicity, and accountability differences, with zero tolerance for reading the label as a role assignment. Current evidence can support that label use under A.10.

If a project later says an RBAC role counts for a work step, it must recover an exact `U.RoleAssignment` under A.2.1 or F.6. The Bridge, affirmative label-use claim, and passing evidence disposition establish no assignment and no performed-work attribution.

#### F.9:12.3 - Subtype notions in one structural row

The endpoint senses are `OWL2:SubClassOf` under a cited OWL profile and curated-taxonomy `is-a` under one named taxonomy edition. The Bridge profile states `Equivalence` and makes its direct relation predicate true only when both endpoint meanings use compatible class-level reasoning and satisfy the stated acyclicity and anti-symmetry conditions. When those facts and dependencies are current, the exact Bridge obtains.

A second premise is still required. The C.2.1 claim names the proposed type-structure row, its source-to-receiving direction, the rule that preserves the three invariants, and zero material-loss tolerance. Only an affirmative current claim with passing A.10 reliance, or the positive B.3 assurance branch when that pattern is triggered, supports relying on the row. A contradicted relation invariant makes the Bridge predicate false; a use-specific tolerance failure can instead make the bounded-use claim negative while the Bridge remains unchanged.

#### F.9:12.4 - Setpoint versus service target

`CTRL:setpoint` and `ITIL:target` share a familiar word but usually have only `Partial-overlap` or are `Disjoint` under the exact readings. A proposed substitution in a control calculation receives a negative bounded-use claim because its rule and tolerance cannot preserve the physical-reference meaning. A didactic comparison may receive a different affirmative claim. Neither claim changes which Bridge obtains.

