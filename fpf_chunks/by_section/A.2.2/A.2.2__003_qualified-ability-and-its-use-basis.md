---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "System Capability: Conditions, Measures and Fit"
section_id: "A.2.2:2"
section_title: "Qualified Ability and Its Use Basis"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__003_qualified-ability-and-its-use-basis.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.2.2 — System Capability: Conditions, Measures and Fit"
  - "A.2.2:2 — Qualified Ability and Its Use Basis"
line_start: 4170
line_end: 4190
dependencies:
  - "A.1"
  - "A.15"
  - "A.2.3"
  - "A.2.6"
  - "C.2.1"
  - "E.23.CDI"
keywords:
  - "attained bounds"
  - "capability fit"
  - "currentness"
  - "holder ability"
  - "qualification"
  - "support"
  - "work conditions"
---

### A.2.2:2 - Qualified Ability and Its Use Basis

The positive claim is that a named holder can perform the named work or produce the named result under the stated conditions and attained bounds. If its truth depends on time, include that time in the claim. A reference to the holder identifies its subject; the other values qualify the proposition rather than identify another individual.

Use these values when the receiving comparison needs them:

| Value | Contribution |
|---|---|
| `capabilityHolderRef` | The independently admitted `U.System` whose ability is claimed. |
| `WorkFamilyOrResultClassRef` | What the holder can do or produce. A particular Method or independently admitted MethodDescription may constrain this claim when the use requires it. |
| `CapabilityEnvelope` | The inputs, environment, resources, configuration, version, calibration state, staffing and other conditions under which the ability is claimed. Its set-valued work-condition basis is `U.WorkScope` under A.2.6. |
| `CapabilityMeasureSet` | The attained bounds claimed for the holder, with units, scales, tolerances and success predicates. Keep the demanded bounds on the other side of the fit comparison. A Characteristic, Q-Bundle slot or architecture criterion can supply a measure without becoming the ability. |
| Capability statement | An assertion of that proposition; use a C.2.1 episteme when the account itself needs identity. Recording it does not make it true. |
| Evidence and source-use relations | The tests, prior work, simulations, standards or other sources that warrant the assertion or constrain its use under their direct governors. |
| Qualification policy and currentness assessment | The rule for relying on that support now, and its dated assessment. A qualification window may expire while actual ability remains unchanged. |
| Capability-fit predicate | The receiving comparison of demanded work conditions and bounds with the qualified holder claim. This is distinct from the ability proposition and its support. |

WorkScope describes work conditions, even when an episteme states them. That episteme's ClaimScope concerns its claims; the two scopes do not become interchangeable. Quantitative bounds and qualification policy remain separate from WorkScope membership. A time condition belongs in WorkScope only when it actually changes which work slices are covered; an evidence-age rule belongs in qualification.

These distinctions permit ordinary capability use without `U.Capability` as an additional kind. A separate kind question arises only if a concrete receiving use needs another individual's continuity or a useful stable classification beyond the holder and these claims; E.24.UK then requires that question's actual identity and membership facts.

