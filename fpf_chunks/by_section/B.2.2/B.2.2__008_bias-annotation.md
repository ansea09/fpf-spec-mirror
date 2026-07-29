---
chunk_kind: "child"
pattern_id: "B.2.2"
pattern_title: "Meta-System Transition - System Specialization of MHT"
section_id: "B.2.2:5.1"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.2/B.2.2__008_bias-annotation.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "B.2.2 — Meta-System Transition - System Specialization of MHT"
  - "B.2.2:5.1 — Bias-Annotation"
line_start: 37854
line_end: 37863
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2.1"
  - "A.2.2"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "B.1.2"
  - "B.2"
  - "B.2.5"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
keywords:
---

### B.2.2:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Named aggregate as system | A fleet, platform, or cell name is treated as system recognition. | Apply B.2 to one exact candidate; require the complete A.1 criterion and the direct `U.System` criterion. |
| Component evidence transfer | Component certificates are read as assurance for the candidate system. | Re-test each claim against the candidate and use exact evidence or assurance relations; do not transfer support by label. |
| Coordination as whole | A controller, protocol, or coordination relation is treated as automatic system MHT. | Recover the obtaining relation, then require B.2 whole reidentification plus complete A.1 and `U.System` recognition; keep any support separate. |
| Description as system | Dashboard, simulation, model, twin, or bill is treated as the operating system. | Use episteme, publication, source-use, and architecture-description owners for description objects. |
| Transformation as containment | An external system changes a holon and is treated as its super-holon. | Use A.12, A.3.4, A.15.1, B.2.5, and part-whole owners separately. |

