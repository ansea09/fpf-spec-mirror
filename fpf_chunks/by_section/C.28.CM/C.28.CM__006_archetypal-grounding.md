---
chunk_kind: "child"
pattern_id: "C.28.CM"
pattern_title: "Construct and Challenge a Causal Model"
section_id: "C.28.CM:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28.CM/C.28.CM__006_archetypal-grounding.md"
commit_sha: "becbad541e7cc23731542d1e14370b3b4e423a65"
heading_path:
  - "C.28.CM — Construct and Challenge a Causal Model"
  - "C.28.CM:5 — Archetypal Grounding"
line_start: 64230
line_end: 64280
dependencies:
  - "A.15.9"
  - "B.5.2"
  - "B.5.FM"
  - "C.11.DUA"
  - "C.16"
  - "C.27"
  - "C.28"
  - "C.28.MR"
  - "C.29"
keywords:
---

### C.28.CM:5 - Archetypal Grounding

The following constructed cases demonstrate reasoning under stated premises. They do not report field effects.

#### C.28.CM:5.1 - Separate an omission, its record and the incident sample

Four incident tickets mention missing order identifiers after a reporting-template change. A planner asks whether supplying the identifier before import would remove manual matching. All four tickets came from problematic reports; the frequency among all reports is unknown.

Choose M for an actually missing identifier and Y for manual matching after import. X denotes template use and L high process load. One account proposes X → M → Y, with load affecting template deployment and identifier omission. A second account proposes that load produces both missing identifiers and an additional wrong join key K; K causes matching work even after the identifier is supplied. The second account has L → M and L → K → Y without an M → Y mechanism.

These accounts make different conditional predictions. If missing identifiers are the operative joining failure and supplying one changes no other input, supplying it removes that modeled obstacle. If K remains wrong, the same correction leaves the K-related work. A report with its identifier restored but the same failed join can challenge the first account's claim of sufficiency. It does not establish the second account merely by eliminating one rival.

Now recover the observing process. Let R be a log saying the identifier is missing. A logging defect can make R=1 while M=0. Inspecting the submitted report and the importer’s actual inputs can therefore resolve a recording question before further causal research is useful.

Let S=1 mean a report entered the incident sample, either because R=1 or because matching work was severe. The structure R → S ← Y means that analyzing only S=1 conditions on a collider. The four tickets cannot by themselves establish the population association or the effect of correcting identifiers. Obtain the needed comparison cases if they could change the decision; retaining a qualified unresolved answer is also possible.

The first return is specific: determine which joining inputs were actually missing or wrong, then distinguish the two modeled failure mechanisms. If all retained accounts support a cheap temporary manual check under the decision's own conditions, using it does not establish which account caused the incident.

**Onset, persistence and amplification.** Suppose a queue began during a specialist's absence. After their return, ten new items and capacity for ten items arrive each day. Under the simplified balance B(t+1)=max(0, B(t)+A(t)+R(t)−C(t)), with backlog B(0)=12, A=10, R=0 and C=10, the backlog remains 12. Two daily rework items, R=2, increase it by two per day. The absence explains the initial loss of service; the present flow balance explains persistence; rework explains growth under these premises. Restoring attendance alone need not clear the backlog. A different arrival pattern, capacity or feedback from delay to rework reopens the corresponding part of the model.

#### C.28.CM:5.2 - Construct the measurement and device mechanisms separately

An idealized regulated supply has command C=12 volts and a fixed 6-ohm resistive load. Its display reads D=14 volts. The practical question is whether correcting the display can reduce the load current.

Construct separate variables for delivered voltage V, display D and current I. Use the load relation I=V/6. Two accounts fit the displayed value:

| Account | Proposed mechanisms | Current implied by the account |
| --- | --- | --- |
| Display bias | V=C; D=V+2. | V=12 and I=2 amperes. |
| Supply offset | V=C+2; D=V. | V=14 and I=7/3 amperes. |

Setting the displayed number to 12 replaces the display mechanism in either model. It leaves V and I unchanged. Changing C to 6 instead gives V=6, I=1 in the first model and V=8, I=4/3 in the second, if the stated offsets and load relation remain valid. The observation D=14 alone does not choose between the accounts.

A separately qualified voltage or current observation can discriminate these idealized models. The need is a measurement of the physical quantity with a suitable independent basis, not another copy of the same display.

Change the situation: the displayed value is fed into an automatic controller for the next command. The earlier absence of a display-to-device path no longer applies over that horizon. Add D(t) → C(t+1) → V(t+1) and obtain the controller law before predicting the later current. The current instant and later controlled behavior are different questions. C.28.MR then performs the chosen replacement in the model actually constructed.

#### C.28.CM:5.3 - Separate AI assistance from assignment and selection

A team reports that AI-assisted tasks had a higher success rate. The question is the effect of actually using assistance A on success Y for the same eligible task population. Let D denote pre-existing task difficulty and H the worker's prior skill.

One model contains A → Y, D → A, D → Y, H → A and H → Y. The rival keeps the assignment and difficulty/skill relations but omits A → Y: the observed difference could arise through who used assistance and on which tasks. Success rates alone do not settle that difference.

The models permit different intervention consequences even when they fit the same aggregate report. Under the explicit assumption that D and H suffice to block common-cause paths, with comparable treatment versions and adequate overlap, adjustment might identify the chosen effect. Those conditions are additional premises, not results of drawing D and H. If workers choose assistance using an unmeasured expectation of difficulty, preserve that possible influence and return the identification gap.

Suppose inclusion in the showcase S depends on both use of assistance and success. A → S ← Y adds a selection path; conditioning on showcased tasks opens it. Reconstruct the eligible set and inclusion process before using the selected comparison for the population question.

Now randomize an offer Z while leaving actual use A voluntary. The offer's effect is a different estimand from the effect of A. If the offer also teaches a technique used without the AI, Z has a route to Y outside A. Using the offer as an instrument to learn the effect of actual use would require it to affect success only through use, among other assumptions. The additional route violates that requirement. The model returns the exact identification question and keeps observed performance descriptive until the required result is available.

The useful return can be a revised comparison population, a retained unmeasured cause, or a direct-effect route that invalidates a proposed design. A larger benchmark or more detailed simulation does not resolve those missing premises by itself.

