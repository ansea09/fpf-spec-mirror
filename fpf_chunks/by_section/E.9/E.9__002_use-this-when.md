---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design‑Rationale Record (DRR) Method"
section_id: "E.9:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__002_use-this-when.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "E.9 — Design‑Rationale Record (DRR) Method"
  - "E.9:0 — Use this when"
line_start: 71179
line_end: 71187
dependencies:
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.22"
  - "E.23"
  - "E.5.4"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.19"
keywords:
---

### E.9:0 - Use this when

- one proposed normative change needs an explicit by-value account of what FPF should say, why this decision is preferred, and which neighboring patterns or selected non-pattern FPF kind-reference pairs it affects
- several patterns or selected non-pattern FPF kind-reference pairs must move together and one external decision record is needed to keep one bounded coordinated change set (one mutually dependent change set) semantically complete while enduring Core text is redistributed
- one bounded content decision question would otherwise force authors to decide the same load-bearing answer separately across several patterns or selected non-pattern FPF kind-reference pairs
- one deprecation, narrowing, or cross-pattern amendment must stay reviewable without reconstructing intent from patch history, chat memory, or scattered notes

**Not this pattern when.** Do not use `E.9` as the permanent location of normative Core law, as a campaign or process brief, or as the main vehicle for purely editorial `Delta-0` or `Delta-1` cleanup that fits the lightweight variant in `CC-DRR.5`. Use `E.9.DA` when one concrete `DRR` already exists and the question is whether its selected answer, selected-locus obligations, source use, lexical closure, and drafting actionability are adequate for a declared downstream authoring use.

