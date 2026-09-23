---
chunk_kind: "child"
pattern_id: "A.1.RI"
pattern_title: "Reidentifying an Object across Observations"
section_id: "A.1.RI:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.RI/A.1.RI__006_archetypal-grounding.md"
commit_sha: "4ddaf71557d4159e988cc61d2bd3088bfc1d2803"
heading_path:
  - "A.1.RI — Reidentifying an Object across Observations"
  - "A.1.RI:5 — Archetypal Grounding"
line_start: 2110
line_end: 2148
dependencies:
  - "A.1"
  - "A.3.3.PI"
  - "A.3.3.TR"
  - "B.5.RR"
  - "B.5.TC"
  - "B.5.TU"
  - "C.11.DUA"
  - "C.16.IR"
  - "C.16.MR"
  - "C.2.1"
keywords:
---

### A.1.RI:5 - Archetypal Grounding

#### A.1.RI:5.1 - Associate two moving objects and retain an unresolved alternative

Consider two persistent point objects with independent motion on one axis; their paths may cross. Each object is observed once at each end of a one-second interval. Positions are assumed known in one common frame. Initially A is at 0 cm and B at 10 cm. Later R is at 1 cm and S at 9 cm.

The motion account limits speed to 2 cm/s. Construct the complete associations:

| Association | Required displacement magnitudes | Result under the speed bound |
| --- | --- | --- |
| A to R; B to S | 1 cm each | Admissible; the two straight paths give a joint realization. |
| A to S; B to R | 9 cm each | Excluded; each exceeds the permitted displacement. |

Under these premises, R observes the continuing A and S the continuing B. A's displacement is +1 cm and B's is -1 cm.

Now allow speed up to 10 cm/s. Both associations have admissible straight paths. The observations leave A's displacement as either +1 or +9 cm; choosing the shorter path adds a preference absent from the speed-bound premise.

Suppose the next question is instead the mean position of these two objects. It was 5 cm and is still 5 cm under both associations. That calculation can proceed without another observation. If a following action must address A individually, look for a discriminator that matters to that action or use an explicitly permitted provisional association.

If the motion premise changes again to a bound below 1 cm/s, neither complete association fits. Reconsider the bound or the observation account before asserting an identification.

#### A.1.RI:5.2 - Test associations together

Keep the one-second, independent, persistent-point and complete-detection premises. Initially A is at 0 cm and B at 1 cm; later R is at 2 cm and S at 3 cm. Each displacement is at most 2 cm.

The admissible pairs are A-R, B-R and B-S. B's nearest detection is R. Assigning it first leaves A without a permitted observation. The joint association A-R with B-S satisfies every constraint and uses each later observation once. It is the only complete association under these premises.

The common Method contributes the joint comparison. The supplied motion bound and complete-detection rule determine which associations it tests. If missed or repeated detections become possible, revise those premises and reconstruct the affected alternatives.

#### A.1.RI:5.3 - Separate a process run from a reused number

An operator wants to compare resource use in two reports carrying the same process number. The object of interest is one process run. Both reports concern the same machine boot and PID naming scope; their fields are assumed to describe the indicated process consistently.

The first report gives start time 1,000 ticks after boot; the second gives 2,400 ticks. Linux exposes such a start-time field in `/proc/pid/stat`. The changed start time excludes continuation of the earlier run, despite the repeated number. Keep the two runs' resource totals separate; subtracting the earlier total from the later one would not measure one run's interval use.

If the reports contain only the number and executable name, they can fit either continuation or termination followed by reuse. An available lifecycle event may distinguish them. For ongoing supervision, a retained process reference such as a Linux PID file descriptor can make a fresh number-based inference unnecessary.

This case resolves run continuity. A question about a service continuing through replacement processes uses the service's own continuation criterion.

