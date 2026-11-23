---
chunk_kind: "child"
pattern_id: "C.2.2a"
pattern_title: "Language-State Chart over U.CharacteristicSpace"
section_id: "C.2.2a:13"
section_title: "Worked Examples"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2a/C.2.2a__015_worked-examples.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "C.2.2a — Language-State Chart over U.CharacteristicSpace"
  - "C.2.2a:13 — Worked Examples"
line_start: 55618
line_end: 55641
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.19"
  - "A.6.A"
  - "B.4.1"
  - "C.16.Q"
  - "C.2.3"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.10"
  - "E.17.1"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
  - "articulation"
  - "characteristic space"
  - "closure"
  - "episteme publication"
  - "formality"
  - "language-state chart"
  - "local thresholds"
  - "partial coordinates"
  - "position claim"
  - "representation"
  - "source and use conditions"
---

### C.2.2a:13 - Worked Examples

#### C.2.2a:13.1 - Inquiry cue before endpoint capture
An inquiry note says that two meters gave different readings under the same recorded operating conditions. It identifies the meters and their units. It names calibration drift and a sampling-time difference as possible causes, with no observation yet to distinguish them. A reader can recover a diagnostic question and two live explanations. The display uses names and numbers. If the comparison concerns the code inside either meter, its distribution across internal units is still unknown. Use the established readings for the diagnostic inquiry. Entry to a pattern that needs a specific relation or causal conclusion depends on that pattern’s own conditions.

#### C.2.2a:13.2 - Routed operator alert note
Use `Pump-alert-21` from C.2.LS:13.1 to compare the three stated diagnostic alternatives before selecting a check. The alert names Pump P7, its indicated pressure of 70 kPa, the alarm condition `p_indicated(P7,t21) < 90 kPa`, and the contrasting implications of sensor bias, low supply, and an open bypass. Its chart readings and separate use condition are:

- `F`: the pressure variables and units are defined, the alarm predicate is explicit, and the question and diagnostic contrasts are expressed in prose;
- `AE = AE4`: the diagnostic question has the participants, conditions, and bounds needed for this comparison;
- `CD = CD1`: the three alternatives have explicit contrasts, but none has yet been excluded and no diagnostic route has been selected;
- use condition under C.2.6: the console connects the alert to the operator's acknowledgement and diagnostic-check selection; this is stated beside the coordinates;
- `RepresentationFactorBundle = {local, sparse, symbolic}` for the alert's indicator-code component only: one of eight named units is active, the fixed decoder gives its report label, and the active fraction `1/8` meets the example's local sparse criterion. C.2.LS:13.1 supplies the unit order, decoder, and criterion.

If an accepted reference-gauge reading of 72 kPa for the same sample t21 excludes sensor bias under the stated case rule while the other two alternatives remain, update `CD` to `CD2`. The question remains fully stated and the code, expression properties, and operator-loop connection are unchanged.

Keep the live responses explicit in the route-bearing seam publication. Before publishing an endpoint-subject-qualified work record or reliance record, test the applicable downstream pattern's conditions; these chart readings do not decide that result.

#### C.2.2a:13.3 - Viewpoint-bound adequacy note
A review note asks whether the architecture description specifies who acknowledges a storage fault. The cited edition names two possible responders and leaves their assignment open. A reviewer can identify the unresolved choice and the evidence still needed. Before assigning a closure level, check whether either responder has been ruled out or chosen and what would allow that choice to be reopened. Compare the note with an observation report on the same chart only for facets assessed on the same basis. Keep the source of each assessment available.

#### C.2.2a:13.4 - Polished prose is not closure
A prose rewrite may look cleaner, more compact, or more manager-readable than the source cue and still remain low in closure or articulation explicitness. If the underlying slot values, uncertainty, and route plurality remain unchanged, then publication polish changes the rendering or carrier lane, not the chart position by itself.

