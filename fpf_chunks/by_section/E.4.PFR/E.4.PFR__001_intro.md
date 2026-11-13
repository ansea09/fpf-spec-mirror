---
chunk_kind: "child"
pattern_id: "E.4.PFR"
pattern_title: "Pattern-Framework Relation and Edition Discipline"
section_id: "E.4.PFR:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFR/E.4.PFR__001_intro.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.4.PFR — Pattern-Framework Relation and Edition Discipline"
  - "E.4.PFR:intro — Intro"
line_start: 100760
line_end: 100785
dependencies:
  - "A.10"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.P"
  - "A.6.RCD"
  - "B.3"
  - "C.2.1"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.11.PUR"
  - "E.17"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFAD"
  - "E.5.3"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
  - "G.5"
keywords:
---

## E.4.PFR - Pattern-Framework Relation and Edition Discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

**Use this when** a named framework-maintenance, edition-impact, comparison, publication/dependency-repair, or refresh task needs a stable row for a specific relation across patterns, framework editions, publication or access carriers, source packs, decisions, generated carriers, or quality results.

**Begin with the assertion.** State the subject assertion in ordinary C.2.1 form. Name the subject or claim, identify the relation function and the ClaimGraph that defines or constrains it, and give the polarity and current fact or condition. Stop there unless an identified maintainer or tool consumes standardized relation form.

**Primary object.** One already identified subject assertion, optionally represented by one `PatternFrameworkRelationRecord@Context` for a named framework-maintenance use.

The assertion, relation row, pattern description, relation kind or occurrence, framework edition, publication occurrence, form, carrier, access route, source use, Work, evidence, assurance, and currentness result remain distinct.

**Primary reader.** A framework author or maintainer who must state one relation or edition claim now and decide whether a named maintenance use justifies a reusable row. A tool may consume the row. That fact alone does not make the tool an actor in the subject claim represented by the row.

Ordinary authoring stays light. Edition and framework-maintenance consumers can compare relation functions, inspect compatibility and dependency effects, preserve blocked stronger readings, and reopen only affected uses.

**When to stop or use another method.** If a readable subject assertion closes the task, use C.2.1 and stop.

Use E.11.PUR for pattern-use recommendations, E.17 and E.24.PUB for publication, C.33 and C.34 for selected-structure capture and preservation, C.35 for exact-result admission to an intended architecture use, and the exact subject pattern for the direct relation.

For direct source reliance or bounded source selection and synthesis, use the source route in E.4.DPF:4. Use G.2 only for a broad, refreshable CG-Frame pack.

E.4.PFR does not define a generic governance relation, pattern owner, mandatory relation-record layer, workflow, runtime route, API call, build dependency, or performed Work.

