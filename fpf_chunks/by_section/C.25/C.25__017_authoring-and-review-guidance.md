---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:16"
section_title: "Authoring and Review Guidance"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__017_authoring-and-review-guidance.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:16 — Authoring and Review Guidance"
line_start: 43442
line_end: 43481
dependencies:
  - "A.15"
  - "A.16.0"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "A.6.Q"
  - "B.3"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.26.3"
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

Authors should begin with the question: *what is the actual head of this quality claim?* If the truthful answer is "several measures plus scope plus mechanism constraints," start with a bundle and narrow only if a later slice genuinely deserves one CHR head.

A useful authoring order is:

1. name the family label,
2. identify the bearer,
3. publish scope,
4. publish measures,
5. add mechanism/status slots,
6. publish qualification window,
7. bind evidence,
8. and only then consider whether a report-only summary proxy is needed.

#### C.25:16.2 - For assessors

A checking reader should ask:

- whether the chosen endpoint shape is lawful,
- whether any scope slot has been smuggled into scalar language,
- whether mechanism presence has been mistaken for a metric,
- whether the window is truly optional or actually load-bearing,
- and whether any summary proxy is trying to replace the underlying bundle.

In practice, most defects are visible as soon as the checking reader asks what exactly one reported number stands for.

#### C.25:16.3 - For gate designers and assurance leads

Gate designers should resist writing guards against vague family labels such as *resilience must be high*. A conforming gate should instead name the relevant bundle slots:

- coverage over the target slice,
- threshold satisfaction on declared measures,
- qualification-window validity,
- and any required mechanism or status slots.

This keeps the gate auditable and prevents later disputes about what the family label was supposed to mean.

