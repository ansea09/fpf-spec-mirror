---
chunk_kind: "child"
pattern_id: "C.2.2a"
pattern_title: "U.LanguageStateSpace - Language-state chart over U.CharacteristicSpace"
section_id: "C.2.2a:13"
section_title: "Worked Examples"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2a/C.2.2a__015_worked-examples.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "C.2.2a — U.LanguageStateSpace - Language-state chart over U.CharacteristicSpace"
  - "C.2.2a:13 — Worked Examples"
line_start: 52393
line_end: 52422
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
  - "anchoring"
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
---

### C.2.2a:13 - Worked Examples

#### C.2.2a:13.1 - Inquiry cue before endpoint capture
A position claim for a research cue note may state:

- `F`: the terms needed for the inquiry are defined, while the proposed inferences remain in prose,
- low articulation explicitness,
- low closure,
- `AM.EmbodiedFelt` or `AM.TraceAnchored`, according to the cue's actual anchor,
- and mixed representation factors.

Keep these readings explicit when testing entry into `A.6.P` or `C.25`; the note should remain upstream while the relevant receiving pattern's entry conditions remain unmet, even if its prose happens to look polished.

#### C.2.2a:13.2 - Routed operator alert note
Use `Pump-alert-21` from C.2.LS:13.1 to compare the three stated diagnostic alternatives before selecting a check. The alert names Pump P7, its indicated pressure of 70 kPa, the alarm condition `p_indicated(P7,t21) < 90 kPa`, and the contrasting implications of sensor bias, low supply, and an open bypass. Its chart readings are:

- `F`: the pressure variables and units are defined, the alarm predicate is explicit, and the question and diagnostic contrasts are expressed in prose;
- `AE = AE4`: the diagnostic question has the participants, conditions, and bounds needed for this comparison;
- `CD = CD1`: the three alternatives have explicit contrasts, but none has yet been excluded and no diagnostic route has been selected;
- `LanguageStateAnchoringMode = AM.OperatorLoop`: the alert is connected to the operator's console acknowledgement and diagnostic-check selection;
- `RepresentationFactorBundle = {local, sparse, symbolic}` for the alert's indicator-code component only: one of eight named units is active, the fixed decoder gives its report label, and the active fraction `1/8` meets the example's local sparse criterion. C.2.LS:13.1 supplies the unit order, decoder, and criterion.

If an accepted reference-gauge reading of 72 kPa for the same sample t21 excludes sensor bias under the stated case rule while the other two alternatives remain, update `CD` to `CD2`. The question remains fully stated and the code, expression properties, and operator-loop connection are unchanged. Keep the live responses explicit in the route-bearing seam publication. Before publishing an endpoint-subject-qualified work record or reliance record, test the applicable downstream pattern's conditions; these chart readings do not decide that result.

#### C.2.2a:13.3 - Viewpoint-bound adequacy note
A document-mediated adequacy note about an architecture description may state an explicit vocabulary and predicates for its claims, with articulation sufficient for the described comparisons, mid-level closure, document-mediated anchoring and symbolic representation. That position remains within the same language-state chart even though its carrier lane differs from an embodied inquiry cue.

#### C.2.2a:13.4 - Polished prose is not closure
A prose rewrite may look cleaner, more compact, or more manager-readable than the source cue and still remain low in closure or articulation explicitness. If the underlying slot values, uncertainty, and route plurality remain unchanged, then publication polish changes the rendering or carrier lane, not the chart position by itself.

