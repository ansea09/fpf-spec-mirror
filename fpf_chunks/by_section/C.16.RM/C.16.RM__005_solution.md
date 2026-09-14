---
chunk_kind: "child"
pattern_id: "C.16.RM"
pattern_title: "Repair a Measurement Model or Arrangement"
section_id: "C.16.RM:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.RM/C.16.RM__005_solution.md"
commit_sha: "b6bc6961903d9196811f71f561c1877fd3feec07"
heading_path:
  - "C.16.RM — Repair a Measurement Model or Arrangement"
  - "C.16.RM:4 — Solution"
line_start: 53126
line_end: 53193
dependencies:
  - "B.5.MPC.R"
  - "B.5.RR"
  - "C.11.DUA"
  - "C.16"
  - "C.16.IR"
  - "C.16.MR"
  - "C.28"
  - "C.29.2"
keywords:
---

### C.16.RM:4 - Solution

Follow the disagreement from the wanted result through the indication-producing relations. Compare changes at the contribution that matters, choose a sufficient available repair, and use the revised relation to obtain the result needed by the work.

**Align the question and observations → locate the consequential contribution → compare a model, computation or arrangement change → carry through the selected repair → determine what the revised result supports.**

The starting point can be a known fault, an unexplained discrepancy or a proved inability to distinguish the needed cases.

#### C.16.RM:4.1 - Align the comparison and target

State the quantity or distinction sought, its subject and operating conditions. Put the expected result and obtained indication on a comparable basis: same quantity, time interval, units and relevant preparation. If the expectation concerns an unconnected source but the reading concerns a loaded source, retain that difference in the relation.

Recover how the indication was produced and interpreted. Separate an observed disagreement from an assumed explanation. A temperature-dependent response may come from the subject, sensor or their interaction; the correlation alone leaves those contributions to be distinguished.

Use C.16.MR when the measurement relation itself is missing. Use C.16.IR to find which alternatives fit an available relation and which distinction remains unresolved. A sufficient bound may already answer the question and end the repair attempt.

#### C.16.RM:4.2 - Locate the contribution that could change the answer

Follow the target-to-indication relation far enough to identify the consequential influence or incompatible operation. Ask what each candidate explanation would require changing and what present information bears on it.

| Possible repair location | What to inspect | A useful change |
| --- | --- | --- |
| Subject model | Which interaction, boundary or varying condition is omitted from the predicted quantity? | Include a background contribution or the dependence on the actual preparation. |
| Instrument model | How does the instrument respond in the range and conditions used? | Include loading, offset, saturation or a calibrated nonlinear response. |
| Computation | Does the implemented operation evaluate the intended relation with its units, domains and required accuracy? | Correct a unit conversion, retained branch, numerical approximation or aggregation interval. |
| Subject arrangement | Can a relevant condition be controlled while retaining the target or a usable relation to it? | Shield an unwanted input or hold a consequential condition stable. |
| Measuring arrangement | Can a different interaction or indication distinguish the needed alternatives? | Change the input resistance, operating range, observation timing or reference measurement. |

The table locates choices; the domain Method supplies the physical law or diagnosis that makes one choice appropriate. A common influence can cross several rows. For example, a change in illumination can alter both the subject response and the detector response.

For a suspected computational fault, run a supplied or constructed input whose answer follows from the intended relation. Compare intermediate values, units and branch choices until the divergence is located. A successful calculation on that input checks implementation of the relation. Compare the relation with the actual subject separately when its adequacy is in question.

#### C.16.RM:4.3 - Compare changes by their predicted contribution

For each serious available repair, change the corresponding part of the relation and determine what would become knowable. An added parameter can represent a missing effect while introducing an unknown that one reading cannot determine. A physical change can remove the effect or make its influence small enough to bound.

A difference measurement is useful when the target changes between two observations in a known way while the influences being cancelled remain sufficiently stable. A larger input resistance is useful when the loading relation shows how much it reduces the consequential error. Repeating an unchanged observation needs its own error or dynamics account to support a narrower conclusion.

Prefer an already available comparison or a small reversible change when it can settle the repair choice. If several explanations predict the same result of a proposed test, that test cannot select among them. Use C.11.DUA to compare the gain from an attainable further observation with its effort and delay.

The needed conclusion sets the reach of diagnosis. Replacing a defective assembly and obtaining the required response may restore the measurement without identifying which internal component failed. Retain the unresolved cause if later reliability, maintenance or causal explanation depends on it. Use C.28 when the required result is a causal attribution.

#### C.16.RM:4.4 - Carry the selected repair through the measurement

Keep the target and receiving question fixed while revising the selected contribution. If an alternative target or operating condition is acceptable, make that change part of the receiving decision and derive the relation for the new use.

For a model repair, include the consequential influence and obtain its value, range or relation from available information. An added correction term earns its use through that basis. Carry any remaining uncertainty into the sought result.

For a computation repair, correct the operation and recalculate the affected results from retained inputs. Reuse observations whose meaning and conditions still fit. Identify outputs that depended on the incorrect operation so that subsequent comparisons use the repaired result.

For an arrangement change, derive how preparation, interaction, indication and calibration are affected. An attenuator can move a detector out of saturation while introducing an attenuation factor and its uncertainty. A shield can remove ambient light while changing alignment. Retain the conditions that make the new relation appropriate.

A planned change supports a conditional result. Once performed, use the resulting observations and conditions to interpret that measurement. Older observations can still answer their original question or be reinterpreted through a supported revised relation; changing a model now does not supply a new past observation.

#### C.16.RM:4.5 - Test the repaired contribution at the needed scope

Choose a comparison capable of exposing the defect the repair addresses. For computation, compare with an independently obtained result for the same mathematical input. For an omitted influence, use a relevant reference condition, intervention or already available contrast. For a claimed operating range, include the range boundary or change of behavior on which the claim depends.

Read the result through the repaired measurement relation. Propagate the uncertainty that could change the receiving answer, and use C.16.IR when compatible alternatives or an outer bound require interpretation. A closer numerical match can still leave a consequential ambiguity.

When the comparison leaves the needed answer unresolved, return to the remaining contribution. A further repair may be justified, or the useful result may be a narrower claim, a changed use or a stop. Do not expand a successful local comparison into a wider range claim without the corresponding basis.

#### C.16.RM:4.6 - Return the usable result

Give the corrected value or comparison, the conditions under which it applies and the consequence for the receiving work. Keep the reason for a changed interpretation where another user could otherwise continue using the old one.

Stop when the result is adequate for that use. Further investigation may have value for another question, such as broader operating conditions or the origin of the fault; it is a separate continuation whose gain should be clear.

