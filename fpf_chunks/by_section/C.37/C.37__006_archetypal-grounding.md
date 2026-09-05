---
chunk_kind: "child"
pattern_id: "C.37"
pattern_title: "Use-Bounded Representation Selection and Co-Use"
section_id: "C.37:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.37/C.37__006_archetypal-grounding.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "C.37 — Use-Bounded Representation Selection and Co-Use"
  - "C.37:5 — Archetypal Grounding"
line_start: 68114
line_end: 68131
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
---

### C.37:5 - Archetypal Grounding

#### C.37:5.1 - Method change selected for one bounded trial

`MethodEngineer-ME1` must select or decline `MethodChange-MC7` as the proposed Method edition for one bounded trial in planned Work item `WP4`. This one decision is the join key for all three rows. A C.11 `ChoiceResult`, or the corresponding direct Method Engineering decision result, owns the selection.

| Candidate | Direct result, reliance, and receiving result | Exposed and withheld | Disposition and return |
| --- | --- | --- | --- |
| Workflow diagram in `MethodDescription-MD5`, edition 5 | A.3.2 identifies the episteme as a MethodDescription about `Method-M2`. A.2.4 may classify its intended evidence use. A.10 path `P-MD5` carries the premise “edition 5 states the proposed MC7 action order,” its source/currentness window, direct decision-use relation, and `RelianceDisposition=pass`. The C.11 result alone selects or declines MC7. | Exposes proposed sequence and handoff; withholds actual effort, achieved result, and future performer availability. | `select` for proposed-way claims only; return if the edition, intended Method, path, or reliance window changes. |
| `WorkPlan-WP4` trial item | A.15.2 identifies the schedule-of-intent episteme and its planned performer, interval, and capability conditions. A.2.4 may classify the intended use. A.10 path `P-WP4` carries the premise “WP4 currently provides the named trial slot and conditions,” source/currentness, direct decision-use relation, and `RelianceDisposition=pass`. The C.11 result alone selects or declines MC7. | Exposes a bounded trial slot and intended conditions; withholds actual occurrence, performance, and result. | `select` for planned-trial feasibility only; return if the plan, performer, interval, capability condition, path, or disposition changes. |
| `WorkRecord-W19` about actual `Work-W19` | A.15.1 admits the dated Work independently; C.2.1 identifies the record episteme. A.2.4 may classify its intended use. A.10 path `P-W19` carries the premise “W19 reports the stated rework and effort under the named earlier conditions,” its provenance and decision-use relation, and `RelianceDisposition=degrade` to that comparability-limited premise. The C.11 result alone selects or declines MC7. | Exposes observed breakdown and effort under the earlier edition and conditions; withholds proof that MC7 fixes the breakdown or that WP4 will reproduce W19. | `select` only for the narrowed comparability-qualified premise; return if the observed conditions, path, currentness, disposition, or relevance to MC7 changes. |

The resulting account does not say that three rows jointly prove MC7. It says which bounded premises the receiver may use, what each leaves out, and which C.11 result follows under those limits. If the same diagram is later used for a tailoring choice or W19 for a learning decision, start another account.

#### C.37:5.2 - Failed diagram use

A release team receives a polished architecture diagram and wants to authorize deployment. E.24.PUB establishes that the diagram edition is available through a current carrier. C.2.P.DR repairs one route-shaped arrow that had been read as operational authority. Neither result establishes view conformance, a representation correspondence, runtime structure, evidence reliance, or deployment permission. Until the needed direct subject result, A.10 path and disposition, and permission or gate result are available, the row is `unresolved`; visual polish and provenance cannot upgrade it. If the direct release gate or permission pattern instead returns a negative result because its required basis is absent, the row is `decline`; classification, publication, provenance, and repair facts cannot override that direct result.

