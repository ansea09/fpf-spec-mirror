---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:16"
section_title: "Authoring and Review Guidance"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__017_authoring-and-review-guidance.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:16 — Authoring and Review Guidance"
line_start: 51792
line_end: 51822
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

### C.25:16 - Authoring and Review Guidance

#### C.25:16.1 - For authors

Begin with *what would make this claim false?* Then:

1. identify the exact bearer and the quality-family label used in the claim;
2. if one measure on one declared Scale carries the claim, state that Characteristic and stop;
3. otherwise add only the differently typed contributors that jointly carry the claim;
4. omit scope, window, mechanisms, status, or evidence when changing that slot would change neither the claim nor the receiving action;
5. identify the enclosing C.2.1 episteme through its claim content, bearer, and effective ReferenceScheme; and
6. add a proxy, gate, publication, evidence relation, or assurance result only when its own receiving question is current.

The schema remains available for a demanding case; it is not the authoring order for every bundle.

#### C.25:16.2 - For assessors

A checking reader should ask:

- whether the chosen endpoint shape is admissible,
- whether any scope slot has been smuggled into scalar language,
- whether mechanism presence has been mistaken for a metric,
- whether the window is truly optional or actually load-bearing,
- and whether any summary proxy is trying to replace the underlying bundle.

In practice, most defects are visible as soon as the checking reader asks what exactly one reported number stands for.

#### C.25:16.3 - For gate designers and assurance leads

Resist a guard such as *resilience must be high*. Cite the exact quality-claim episteme or addressed claim and name only the slots the decision actually uses—for example one scope, one measure threshold, a load-bearing window, or a required mechanism. Do not require an absent slot merely because the source claim uses Q-Bundle-shaped content.

