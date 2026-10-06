---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:7"
section_title: "Decision trees (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__008_decision-trees-informative.md"
commit_sha: "94b6c708eadc1a572f7db7788ed2e74df4053b2d"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:7 — Decision trees (informative)"
line_start: 53095
line_end: 53125
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2.6"
  - "C.2.2"
  - "C.2.3"
  - "C.3"
  - "C.3.1-C.3.5"
keywords:
  - "ESG"
  - "Method-Work"
  - "assurance"
  - "declaration compatibility"
  - "exact candidate judgment"
  - "guard refusal"
  - "regulatory"
  - "true/false/unknown"
---

### C.3.A:7 - Decision trees (informative)

**D1 — Admit a quantified claim.**

1. Pin the quantified claim kind, receiving kind, and both exact signature editions.
2. Require the receiving kind to be identical to or a subkind of the claim kind, or establish the receiving use's required correspondence between distinct kinds through the exact source-claim to target-receiving KindBridge relation and assertion.
3. Check Claim scope against the exact TargetSlice and `Gamma_time`.
4. Apply R consequences and freshness/threshold checks.
5. Return the separate action disposition. Do not ask for a candidate unless the receiving use applies the claim to one.

**D2 — Apply the claim to a candidate.**

1. Identify the candidate under its direct governor.
2. Complete D1 steps 1–3: declarations, kind compatibility, and Scope/time.
3. Check receiving admissibility. On `not-applicable`, refuse without a judgment; otherwise evaluate the four-input target judgment.
4. On `true`, use the established order or bridge for the claim-kind consequence and complete D1's R, freshness, and threshold checks before allowing use; on `false`, refuse as known failure; on `unknown`, refuse and retain the non-settlement reason.

**D3 — Compose or cross a context.**

1. Pin source and target declarations.
2. Recover declaration compatibility through identity, the required subkind relation, or an obtaining KindBridge with its separate assertion; recover Scope Bridge separately when Scope translation is required.
3. Check the serial or translated scope.
4. If an actual output/candidate is current, check admissibility and evaluate it under the target declaration only when admissible.
5. Apply R consequences and decide separately.

**D4 — Publish a union.**

1. Complete the relevant D1/D2 checks per line.
2. Demonstrate support-line independence.
3. Publish only the supported union; retain line-specific classifications and bridge consequences.

