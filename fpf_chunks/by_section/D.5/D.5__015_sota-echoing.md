---
chunk_kind: "child"
pattern_id: "D.5"
pattern_title: "Bias Audit and Ethical Assurance"
section_id: "D.5:10"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/D.5/D.5__015_sota-echoing.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "D.5 — Bias Audit and Ethical Assurance"
  - "D.5:10 — SoTA-Echoing"
line_start: 97814
line_end: 97819
dependencies:
  - "A.10"
  - "B.3"
  - "C.11.DUA"
  - "C.16"
  - "C.28"
  - "D.1"
  - "D.2"
  - "D.3"
  - "D.4"
  - "E.13"
  - "E.17"
  - "E.5.4"
keywords:
---

### D.5:10 - SoTA-Echoing

For deciding what a fairness result supports, **adapt** C.16’s measurement interpretation and C.28:4.6’s claim-specific identification and estimation conditions. Against the aggregate-accuracy inference in :6, :2–4 retain the qualified metric result and obtain the additional causal basis only for a conclusion that needs it. Section :3.1 reuses an adequate audit account and selects further work from the reliance, while a missing required basis leaves the stronger conclusion unsupported. B.3 supplies any assurance relation and D.4 its ethical decision use. Reopen the affected basis when the population, intended use, claimed effect, evidence conditions or binding requirement changes.

Kearns, Neel, Roth and Wu show how a classifier can meet a parity condition for each of several predefined groups while violating it for a subgroup defined by a combination of attributes. Section 2 uses that distinction to select the group a claim concerns. Which criterion matters and which population it covers still come from the receiving use. [Preventing Fairness Gerrymandering (2018)](https://proceedings.mlr.press/v80/kearns18a.html)

