---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:13"
section_title: "Decision Test: Single Characteristic or Bundle?"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__014_decision-test-single-characteristic-or-bundle.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:13 — Decision Test: Single Characteristic or Bundle?"
line_start: 51628
line_end: 51664
dependencies:
  - "A.10"
  - "A.15"
  - "A.16.0"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.26.3"
  - "C.33"
  - "C.34"
  - "C.35"
  - "F.9"
  - "F.9.1"
keywords:
  - "admissible quality-family use"
  - "characteristic plus scope"
  - "endpoint classification"
  - "failure mode"
  - "ility"
  - "mechanism/status slots"
  - "proxy metric"
  - "quality bundle"
  - "quality family"
  - "viability envelope"
---

### C.25:13 - Decision Test: Single Characteristic or Bundle?

The most common authoring failure is not in the bundle syntax itself; it is in choosing the wrong endpoint shape. The quickest useful test is to ask what would make the quality claim false.

#### C.25:13.1 - Use one `U.Characteristic` when

A quality claim should terminate in one admissible CHR characteristic only when all of the following hold together:

- one measurable aspect is actually doing the evaluative work,
- one declared scale is enough to compare relevant cases,
- the bearer and scope are already clear without introducing extra quality slots,
- mechanism or status presence is not itself part of the core quality head,
- and downstream gates can read the claim without needing a bundle decomposition.

Examples include a narrowly declared `AvailabilityRatio[%]`, a specific latency percentile, or one response-time threshold under one fixed window.

#### C.25:13.2 - Use a `Q-Bundle` when

A quality claim belongs in `C.25` when one family label is standing over several distinct typed concerns, for example:

- several measures are needed together,
- scenario or claim scope is load-bearing,
- mechanism presence or certification state constrains admissibility,
- qualification windows alter the reading materially,
- or one scalar head would hide which part of the family is actually failing.

The bundle is not a fallback for laziness. It is the explicit authoring form for claims whose truth conditions are already composite.

#### C.25:13.3 - Borderline cases

Some quality families contain both a bundle-shaped form and a narrow single-characteristic form. For example, a service team may use:

- one CHR characteristic for a very narrow uptime commitment, and
- one Q-Bundle for the broader service-availability family that includes scope, windows, failover mechanisms, and evidence.

This is legitimate as long as the text states clearly which head is currently in play. The single-characteristic form does not replace the broader family; it selects one evaluative slice of it.

