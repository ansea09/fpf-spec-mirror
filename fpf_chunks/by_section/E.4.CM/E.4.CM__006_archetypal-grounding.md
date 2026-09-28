---
chunk_kind: "child"
pattern_id: "E.4.CM"
pattern_title: "Develop Composite Methods as Framework Contributions"
section_id: "E.4.CM:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.CM/E.4.CM__006_archetypal-grounding.md"
commit_sha: "a8fc704270e4bef9d97953190a52d683db1d9e66"
heading_path:
  - "E.4.CM — Develop Composite Methods as Framework Contributions"
  - "E.4.CM:5 — Archetypal Grounding"
line_start: 80251
line_end: 80286
dependencies:
  - "B.1.5.EW"
  - "B.1.5.RS"
  - "C.39.RO"
  - "E.11"
  - "E.11.PFP"
  - "E.19"
  - "E.21"
  - "E.4"
  - "E.8"
  - "F.19"
keywords:
---

### E.4.CM:5 - Archetypal Grounding

#### E.4.CM:5.1 - Assemble a comparison that another reader can use

A team has two public operations: grouping records and comparing paired observations. Its receiving question requires each error/non-error pair to share both setup and temperature. The existing grouping uses only setup.

The available data are T1=(error, S1, warm), T2=(acceptable, S1, cool), T3=(error, S2, warm), T4=(acceptable, S2, warm). Grouping by setup offers T1–T2 and T3–T4. Only the latter satisfies the comparison's precondition.

The author locates a composition difficulty: the producer's grouping key is weaker than the receiver's eligibility rule. The repair groups by setup and temperature, returns T3–T4 as eligible and makes the missing S1 comparison explicit. Comparison then uses the eligible pair; it cannot claim a result for S1. A request for another record is warranted only if that unresolved use matters.

This is already developed in C.40.CD:5.1. E.4.CM therefore selects reuse of that explanation rather than another pattern for these same operations. If a proposed card merely lists grouping and comparison, it should point to the available construction instead of asking the reader to invent the missing key.

Now change the receiving rule to require a shared instrument revision too. Temperature matching alone no longer answers eligibility. If revisions are present, extend the key; if absent, return the unavailable comparison rather than treating omission as a match. This change illustrates what the public explanation must teach: derive the joining rule from the receiving condition and preserve partial results. It does not establish causality from one matched pair.

#### E.4.CM:5.2 - A larger contribution survives subtraction

Suppose an author has explanations for probing an unfamiliar device, comparing architecture alternatives and retaining a shared way of working. A practitioner still needs to turn an unexpected response into a repeatable delivery use.

The necessary connection is not “do all three.” A response supports only a bounded claim; the intended use determines whether that claim is sufficient. If it is insufficient, the next probe must distinguish the relevant alternatives. A chosen use then determines which preparation and environmental support to preserve, and a receiving participant's attempt can reopen the arrangement rather than the original causal question.

C.40.CU develops this whole. Its suppliers remain useful, but subtracting their individually supplied operations leaves the selection and return relations above. A normal FPF pattern is appropriate because those relations recur across constructs and uses.

The whole has both dimensions. Horizontally, a supported fixed-task response can permit use while an unfamiliar-task claim remains unknown and calls for another probe; these are conditioned continuations, not a compulsory inquiry sequence. Vertically, guide inspection and loading are constituent actions of delivery, and the delivery deadline constrains their combined performance. Ontologically, the tested configuration's success remains distinct from the controller's independently held capability. Each distinction changes the construction.

A short entry can say “take the response, bound the claim, construct a useful arrangement, and reproduce it under the receiving conditions.” That sentence is a reminder, not the complete explanation.

#### E.4.CM:5.3 - Integrate overlapping checks without losing either use

An intake Method accepts a reading when its unit is °C and its value lies from 0 through 100. A calibration-use Method repeats that same check and also requires a current calibration. The two Methods consume the same immutable reading version and use the same meanings of unit, endpoints and rejection. Under those conditions the common check can be performed once and its result supplied to both uses.

For the readings R1=(42, °C, current), R2=(42, °F, current), R3=(120, °C, current), R4=(60, °C, expired) and R5=(60, °C, current), the common check accepts R1, R4 and R5. Intake retains all three. Calibration use additionally tests calibration currentness, retaining R1 and R5. Sharing the check does not permit removing that additional condition or imposing it on intake.

Now the calibration use changes its upper limit to 50 °C. Use B.1.5.RS to follow the replacement through both receiving uses. Retain the shared 0–100 check for intake and add the narrower condition on the calibration branch; that branch now retains only R1. Changing the common threshold to 50 would incorrectly remove R4 and R5 from intake. Alternatively, keep separate checks when different observation versions, meanings or required failure responses prevent sharing their result.

The constructive choice is to identify the identical predicate and input, preserve each distinct obligation, and reconnect their results to the two receivers. It integrates the overlap without flattening the Methods into one stronger admission rule. No additional pattern is needed merely to give these checks a second name.

