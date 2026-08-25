---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:17"
section_title: "Acceptance tests"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__019_acceptance-tests.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:17 — Acceptance tests"
line_start: 92661
line_end: 92690
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "C.3"
  - "E.10.ROLE"
  - "E.17.ID.CR"
  - "E.24.PUB"
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

### F.9:17 - Acceptance tests

#### F.9:17.1 - Static conformance

* **SCR-F9-S01 (Well-typed direct relation).** Each actual Bridge has exactly two resolved F.17 `SchemeSenseCell` endpoints and one exact relation-semantic profile.
* **SCR-F9-S02 (Different semantic contexts).** The endpoint `<ReferenceScheme, LocalSenseClaim>` projections differ; same-context aliases stay with designation resolution.
* **SCR-F9-S03 (Profile boundary).** The profile contains only kind, symmetry or orientation, endpoint readings, relation condition, applicability and as-of basis, Boolean truth condition, and stop dependencies.
* **SCR-F9-S04 (Obtaining).** Current endpoint facts satisfy the exact profile and all required dependencies are present. Scheme difference, spelling, implementation, evidence score, card, registry, or publication alone fails this test.
* **SCR-F9-S05 (Separate bounded use).** Every use claim identifies exact Bridge `b`, names `u`, `d`, `r`, `t`, polarity, and an effective ReferenceScheme under C.2.1.
* **SCR-F9-S06 (Reliance branch).** The same bounded use has the exact A.10 relation plus a passing local disposition or, when an actual named assurance claim is current, its exact B.3 `AssuranceResult`; only `supported-for-use` supports the attempted assurance use, while `narrowed` supports only its stated narrower use.
* **SCR-F9-S07 (No authorization overread).** Semantic fit, A.10 reliance, and B.3 assurance are not described as legal, policy, or deontic permission.
* **SCR-F9-S08 (Receiving-object boundary).** A named proposed use is never treated as performed Work, assertion, publication, relation, or operation application.
* **SCR-F9-S09 (Card truthfulness).** An actual card concerns an already individuated occurrence; a candidate or negative card concerns the admitted relation kind and has no positive occurrence ref.
* **SCR-F9-S10 (Plain action).** A practitioner can tell what relation to test, what use is proposed, what would stop reliance, and which downstream claim still needs an applicable pattern.
* **SCR-F9-S11 (Non-optional identity and recurrence).** The declaration states `BridgeOccurrenceIdentityRule`, asymmetric ordering or symmetric canonicalization, and the non-recurrence of one fixed endpoint/profile tuple; a later basis changes the profile before another candidate is admitted.
* **SCR-F9-S12 (Description and publication boundary).** Every actual description/Card concerns an already individuated occurrence under C.2.1; every modal proposal has no positive occurrence ref; E.24.PUB publication, form, carrier, and registry identity establish neither.
* **SCR-F9-S13 (No adjacent fact by Bridge).** No Bridge creates a local system-role kind or assignment, Work, evidence authority, status transfer, U-kind admission, publication, model-use crossing, or another subject relation.

#### F.9:17.2 - Regression checks

* **RSCR-F9-E01 (Same Bridge, changed use).** Reversing direction, changing the use rule, or changing tolerance reidentifies the C.2.1 claim, not the Bridge.
* **RSCR-F9-E02 (Same claim, changed evidence).** Stale or stronger evidence changes the A.10 relation or disposition, or the B.3 branch, without reidentifying the fixed claim.
* **RSCR-F9-E03 (Required but missing assurance claim).** If a direct domain rule requires an assurance claim and none is current, return `RelianceDisposition=assurance-needed` or block the use. Do not manufacture a positive claim or a generic safety-case record.
* **RSCR-F9-E04 (Profile change).** A changed relation condition or endpoint reading identifies another profile and occurrence candidate.
* **RSCR-F9-E05 (Packaging change).** A changed card, registry entry, publication, form, or carrier leaves the Bridge and fixed bounded-use claim unchanged unless their own discriminators changed.
* **RSCR-F9-E06 (Positive proposal versus occurrence).** An affirmative claim with passing reliance proves no comparison Work, assertion, publication, direct relation, or operation application.
* **RSCR-F9-E07 (Polarity versus reliance).** Negative claim polarity and a non-passing reliance disposition remain different facts.
* **RSCR-F9-E08 (Reliance versus authorization).** A.10 `pass` or B.3 `supported-for-use` does not imply permission.
* **RSCR-F9-E09 (No inverse or composition).** Neither an asymmetric inverse nor a direct A-to-C Bridge follows without its own profile and obtaining test.

