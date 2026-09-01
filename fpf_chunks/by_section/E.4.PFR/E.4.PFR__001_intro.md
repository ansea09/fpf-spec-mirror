---
chunk_kind: "child"
pattern_id: "E.4.PFR"
pattern_title: "Pattern-Framework Relation and Edition Discipline"
section_id: "E.4.PFR:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFR/E.4.PFR__001_intro.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "E.4.PFR — Pattern-Framework Relation and Edition Discipline"
  - "E.4.PFR:intro — Intro"
line_start: 71645
line_end: 71662
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
  - "C.33-C.35"
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

**Use this when.** Use E.4.PFR when a named framework-maintenance, edition-impact, comparison, publication/dependency-repair, or refresh task needs a stable relation-specific row across patterns, framework editions, publication or access carriers, source packs, decisions, generated carriers, or quality results.

**First useful move.** State the exact subject assertion in ordinary C.2.1 form: name the subject or claim, exact relation function, exact defining or constraining ClaimGraph, polarity, and the current fact or condition. Stop there unless an identified maintainer or tool consumes standardized relation form.

**Primary working object.** One already identified subject assertion, optionally represented by one `PatternFrameworkRelationRecord@Context` for a named framework-maintenance use. The assertion, relation row, pattern description, relation kind or occurrence, framework edition, publication occurrence, form, carrier, access route, source use, Work, evidence, assurance, and currentness result remain distinct.

**Primary working reader.** A framework author or maintainer who must state one relation or edition claim now and decide whether a named maintenance use justifies a reusable row. A tool may consume that row; it is neither the reader nor an actor in the claim.

**What this buys.** Ordinary authoring stays light, while real edition and framework-maintenance consumers can still compare relation functions, inspect compatibility and dependency effects, preserve blocked stronger readings, and reopen only affected uses.

**Not this pattern when.** If a readable subject assertion closes the task, use C.2.1 and stop. Use E.11.PUR for pattern-use recommendations, E.17 and E.24.PUB for publication, G.2 for source selection and use, C.33-C.35 for carrier capture/preservation/admission, and the exact subject pattern for the direct relation. E.4.PFR does not define a generic governance relation, pattern owner, mandatory relation-record layer, workflow, runtime route, API call, build dependency, or performed Work.

