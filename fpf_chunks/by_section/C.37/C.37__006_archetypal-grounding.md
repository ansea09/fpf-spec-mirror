---
chunk_kind: "child"
pattern_id: "C.37"
pattern_title: "Select and Use Representations for One Action"
section_id: "C.37:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.37/C.37__006_archetypal-grounding.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "C.37 — Select and Use Representations for One Action"
  - "C.37:5 — Archetypal Grounding"
line_start: 76039
line_end: 76066
dependencies:
  - "A.10"
  - "A.2.4"
  - "A.22"
  - "A.6.3.RT"
  - "C.11"
  - "C.13"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.29"
  - "E.17.0"
  - "E.24.PUB"
keywords:
  - "co-use"
  - "diagram"
  - "exposure"
  - "loss"
  - "model"
  - "plan"
  - "receiving action"
  - "record"
  - "representation selection"
---

### C.37:5 - Archetypal Grounding

#### C.37:5.1 - Qualified premises for a bounded-trial decision

`MethodEngineer-ME1` must select or decline `MethodChange-MC7` as the proposed Method edition for one bounded trial in planned Work item `WP4`. This one decision is the receiving use for all three rows.

In this constructed case, the options are to prepare and run the MC7 trial or retain the current Method edition. WP4 provides a one-hour trial slot. The stipulated setup estimate for MC7 is four additional hours, while the applicable total setup-and-trial ceiling is three hours. Retaining the current edition is feasible within that ceiling. These case facts are additional planning inputs; WorkRecord-W19 does not establish the setup estimate or predict the benefit of MC7.

C.11 result CR7 is `choose now`: ME1 selects retaining the current edition and declines MC7 for this WP4 use because 4 + 1 hours exceeds the three-hour ceiling. The selected comparison criterion is compliance with that current total budget; the earlier rework record supplies motivation, not permission to exceed it. Reopen CR7 if the setup estimate, budget, options or trial conditions materially change. The decision makes no claim that the planned trial occurred.

| Candidate | Direct result, reliance, and receiving result | Exposed and withheld | Disposition and return |
| --- | --- | --- | --- |
| Workflow diagram in `MethodDescription-MD5`, edition 5 | A.3.2 identifies the episteme as a MethodDescription about `Method-M2`. A.2.4 may classify its intended evidence use. A.10 path `P-MD5` carries the premise “edition 5 states the proposed MC7 action order,” its source/currentness window, direct decision-use relation, and `RelianceDisposition=pass`. Receiving result: CR7, defined above. | Exposes proposed sequence and handoff; withholds actual effort, achieved result, and future performer availability. | `select` for proposed-way claims only; return if the edition, intended Method, path, or reliance window changes. |
| `WorkPlan-WP4` trial item | A.15.2 identifies the schedule-of-intent episteme and its planned performer, interval, and capability conditions. A.2.4 may classify the intended use. A.10 path `P-WP4` carries the premise “WP4 currently provides the named trial slot and conditions,” source/currentness, direct decision-use relation, and `RelianceDisposition=pass`. Receiving result: CR7, defined above. | Exposes a bounded trial slot and intended conditions; withholds actual occurrence, performance, and result. | `select` for the stated trial-slot availability and intended conditions only; return if the plan, performer, interval, capability condition, path, or disposition changes. |
| `WorkRecord-W19` about actual `Work-W19` | A.15.1 admits the dated Work independently; C.2.1 identifies the record episteme. A.2.4 may classify its intended use. A.10 path `P-W19` carries the premise “WorkRecord-W19 reports the stated rework and effort under the named earlier conditions,” its provenance and decision-use relation, and `RelianceDisposition=degrade` to that comparability-limited premise. Receiving result: CR7, defined above. | Exposes observed breakdown and effort under the earlier edition and conditions; withholds proof that MC7 fixes the breakdown or that the trial planned in WP4 will reproduce those observations. | `select` only for the narrowed comparability-qualified premise; return if the observed conditions, path, currentness, disposition, or relevance to MC7 changes. |

The completed account retains two pass premises and the comparability-limited degrade premise as inputs to CR7. Declining MC7 for WP4 does not make those representations unusable as decision premises; it states the result obtained using them and the additional budget facts. None of the three rows proves that MC7 improves the Method. If the same diagram is later used for a tailoring choice or WorkRecord-W19 for a learning decision, start another account.

#### C.37:5.2 - Failed diagram use

A release team receives a polished architecture diagram and wants to authorize deployment. E.24.PUB establishes that the diagram edition is available through a current carrier. C.2.P.DR repairs one route-shaped arrow that had been read as operational authority. Neither result establishes view conformance, a representation correspondence, runtime structure, evidence reliance, or deployment permission. Until the needed direct subject result, A.10 path and disposition, and permission or gate result are available, the row is `unresolved`; visual polish and provenance cannot upgrade it. If the direct release gate or permission pattern instead returns a negative result because its required basis is absent, the row is `decline`; classification, publication, provenance, and repair facts cannot override that direct result.

#### C.37:5.3 - One decision now and a later reader's need

In section 5.1, the engineer completes the current comparison using the three independently qualified inputs and the stated budget facts. The direct receiving result and material limits are already clear: the description supplies proposed order, the plan supplies intent rather than performed Work, and the earlier record supplies only its comparability-limited observation. If no later use needs another account of this comparison, the answer is complete without a standalone C.37 record. Required source and receiving-result evidence remain under their own governors.

Now suppose a later trial reviewer must reconstruct why those particular inputs were usable for WP4. That use needs the exact claims, source and reliance boundaries, losses, dispositions and receiving result—not merely “MC7 selected.” Retain the complete basis in the existing same-use decision account if it can carry it, otherwise in one identifiable account. A new receiving decision still requires its own use-bounded selection; the retained earlier basis is not authority for the new action.

