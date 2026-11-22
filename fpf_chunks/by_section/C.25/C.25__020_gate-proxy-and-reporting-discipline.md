---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Express a Quality Claim as One Characteristic or a Structured Bundle"
section_id: "C.25:19"
section_title: "Gate, Proxy, and Reporting Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__020_gate-proxy-and-reporting-discipline.md"
commit_sha: "a9845e2c1029313e518c91a459ff7fab39e2831e"
heading_path:
  - "C.25 — Q-Bundle: Express a Quality Claim as One Characteristic or a Structured Bundle"
  - "C.25:19 — Gate, Proxy, and Reporting Discipline"
line_start: 68623
line_end: 68633
dependencies:
  - "A.15"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.16.Q"
  - "C.26.3"
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

### C.25:19 - Gate, Proxy, and Reporting Discipline

#### C.25:19.1 - Report-only summary proxy
Apply the report-only proxy rule in section 14.4 to the exact source episteme or addressed claims.

#### C.25:19.2 - Gate binding rule
When a gate uses a quality family, take its acceptance conditions from the receiving decision. Cite the quality-claim episteme or its addressed claims and identify which conditions each supports, such as a measure in a specified window or a required mechanism. Reuse other evidence for any condition the supplied claim leaves open. The gate's own rule determines what to do with a known failure or an unresolved condition.

#### C.25:19.3 - Roll-up caution
A roll-up is a separate claim-bearing episteme. Cite the exact source epistemes or ClaimAddresses and explain how their claims support the property the recipient needs. A direct observation of the service may already establish the property. When drawing a conclusion from the parts, identify how their states or contributions determine the property in question. Suppose a service can accept a request precisely when both stages are available. Each stage was available on 99 of the same 100 request opportunities. If their outages coincided the service was available on 99 opportunities. If they occurred separately it was available on 98. These records settle a target of at least 98. To decide a target of 99, establish whether the outages coincided or use records of service availability itself. When a summary is used for local engineering action, return to the source claims and the Q-Bundle slots that action depends on.

