---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent (Promise Content)"
section_id: "A.2.3:12"
section_title: "Didactic quick distinctions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__019_didactic-quick-distinctions.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.2.3 — U.PromiseContent (Promise Content)"
  - "A.2.3:12 — Didactic quick distinctions"
line_start: 4304
line_end: 4313
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8"
  - "A.2.9"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "F.12"
  - "F.9"
  - "U.Capability"
  - "U.ClaimScope"
  - "U.Episteme"
  - "U.Method"
  - "U.MethodDescription"
  - "U.SystemRoleAssignment"
  - "U.Work"
  - "U.WorkPlan"
  - "U.WorkScope"
keywords:
  - "SLA"
  - "SLO"
  - "Work evidence"
  - "acceptance specification"
  - "access specification"
  - "claim scope"
  - "promise content"
  - "promised outcome"
  - "provider and consumer system-role kinds"
---

### A.2.3:12 - Didactic quick distinctions

* **Promise content.** A consumer-facing episteme stating the promised outcome, any eligibility predicate, effective reference scheme, claim scope, and acceptance specification; its optional `accessSpec` describes the access method.
* **Method and method description.** `U.Method` is the semantic way of doing. `U.MethodDescription` is an episteme describing that method; neither is delivery work.
* **Delivery work, affected subject, and effect Delta.** A provider holder system performs `U.Work`. Exact affected-referent, actual-change, production, delivery, or acceptance claims state what happened under their own governors; the selected effect Delta is a mathematical-lens expression over the affected referent and its pre-work and post-work states.
* **Evidence and evaluation.** Evidence relations support delivery and satisfaction claims. A separately performed evaluation occurrence has an actual operation application with a declared result binding; any verdict episteme is separately constituted and governed.
* **Provider and consumer participation.** The promise-content fields typed by `U.KindRef` identify local provider and consumer system-role kinds. Assignment occurrences identify admitted holder Systems and assignment extents; their declared `U.SystemRoleAssignment` species define the participant meanings. The assignment does not itself perform Work.
* **Measures.** `U.Measure` claims such as availability or lead-time readings derive from selected work facts through named characteristics, C.16 measurement templates, A.10 evidence relations, aggregation rules, and temporal policies; when a particular measurement method matters, its `U.MethodDescription` is cited.
* **Structure boundary.** Promise content is not a structural part. The systems that expose access or perform delivery retain their own parts, selected structures, and `ArchitectureOf@Context` relations.

