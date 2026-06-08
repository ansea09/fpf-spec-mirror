---
chunk_kind: "child"
pattern_id: "J.4"
pattern_title: "First Practical Entry Pattern-Comparison Index"
section_id: "J.4:0"
section_title: "Compact Front-Door Rows"
source_path: "FPF-Spec.md"
output_path: "by_section/J.4/J.4__002_compact-front-door-rows.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "J.4 — First Practical Entry Pattern-Comparison Index"
  - "J.4:0 — Compact Front-Door Rows"
line_start: 82880
line_end: 82912
dependencies:
keywords:
---

### J.4:0 - Compact Front-Door Rows

Rows are retained only when they are likely first practical entries, common wrong first guesses, or retrieval-facing cues that materially change the first pattern choice. A pattern does not need a `J.4` row merely because it exists.

The compact table has two reader families. Project and practitioner rows are the primary family: they help a user apply `FPF` to a working project, project-side claim, relation, boundary, comparison, architecture, publication, or improvement question. `FPF`-artifact rows are a small secondary family: they help a user apply `FPF` to an `FPF` artifact such as a pattern or `DRR`. Do not use an `FPF`-artifact row as project-side evidence, assurance, gate, decision, work, release, or certification.

#### Project or Practitioner First Entries

| Working problem or first-entry cue | Apply first | If the question is actually... |
|---|---|---|
| "We have a messy situation, concern, complaint, or opportunity, and do not yet know what problem-side material is accepted before work starts." | `C.22.2` | Use `E.18.1` only after accepted problem-side material needs first-principles-to-work carry-through. Use `A.15`, `A.15.2`, or `A.15.3` when the issue is responsibility, method, plan, or performed work rather than problem-side material. |
| "A serious cue or emerging idea is too important to ignore but too early to publish as a settled claim, requirement, or work record." | `C.2.2a` | Use `C.2.P` when the cue's wording must be restored before stronger use, and use the endpoint pattern only when the cue has matured into that endpoint's governed claim. |
| "A first-principles distinction should change what work, method, or modeling move is tried next." | `E.18.1` | Use `C.29` when the live move is mathematical-lens use, `A.6.0` when a `U.Signature(profile=FormalSubstrate)` declaration must be written, and `A.6.1` when mechanism realization or import is being claimed. |
| "Responsibilities, roles, methods, plans, performed work, and source use are being mixed in the project conversation." | `A.15` | Use `A.1.1` for bounded responsibility context, `A.15.2` or `A.15.3` for plan and work separation, `A.15.4` for work-relevant source use, and `B.5.1` when the alignment frame itself is being made. |
| "We need to compare alternatives, keep a shortlist honest, decide locally, or publish a selected set without hiding the comparison logic." | `A.19` and `C.19` | Use `C.11` for a local choice, `C.18` for portfolio or archive context, and `G.5` when a selector or set-return claim is being made. |
| "The first deliverable is a reusable search, generator, SoTA harvest, novelty-diversity archive, or exploration portfolio rather than one recommendation." | `G.0` | Use `G.1`, `G.2`, and `G.5` for generator and set-return claims; use `C.18` and `C.19` when the archive or selected-set publication is central; use `A.19` when the characteristic space already governs comparison. |
| "We need to say what better means before evaluating, comparing, or improving an object." | `A.19.ECS` | Use `C.16` for measurement construction, `C.25` for an existing Q-Bundle, `E.22` when a suitable evaluation exists but the evaluation question needs framing, and `E.23` when repeated improvement is needed. |
| "Evidence, test gaps, assurance, gate validity, or decision permission must be made explicit before commitment." | `A.10` and `B.3` | Use `A.20` for internal constraint validity, `A.21` for gate decisions, `C.11` for local choice, and `A.15` when the claim being made is performed work or planned work. |
| "We need to describe or change the architecture of some holon, selected structure, or architecture-relevant characteristic." | `C.30` | Use `A.22` or `C.30.ASV` for selected-structure and structural-view questions, `C.30.AD` when the object under repair is an architecture description, and `C.30.STRAT`, `C.30.LCA`, or `C.30.ILC` when stratification, control, or interlevel residuals are live. |
| "Function, module, interface, port, platform, reusable structure, or scale preference is central to the project move." | `A.6.F` and `A.6.M` | Use `C.31` for modularity or reusable-structure characteristics, `C.31.RSA` for reusable-structure accounting, `C.31.ASAP` for scale-amenability preference, and `C.30.TGA-FLOW-REL` when a TGA flow relation changes an architecture claim. |
| "Different audiences need aligned descriptions, explanations, screens, summaries, or renderings without changing the underlying EntityOfConcern." | `E.17` | Use `E.17.0` for description discipline, `E.17.AUD` for same-publication-unit use, `E.17.EFP` for explanation-facing rendering, `E.17.ID.CR` for bounded comparative interpretation, and `A.6.3.*` for same-EntityOfConcern episteme morphisms. |
| "Timing, freshness, delay, cadence, throughput, rate, recovery, effort, or resistance changes what can be claimed or done." | `C.27` | Use `C.16` for characteristic or measurement admission, and the work, comparison, quality, mechanism, evidence, or decision pattern when the temporal cue only modifies that claim. |
| "A correlation, explanation, scenario, model output, or comparison is being used as if it justified intervention, responsibility, or counterfactual choice." | `C.28` | Use `A.10` for evidence-path use, `B.3` for assurance, `C.16` for measurement, `C.27` for temporal adequacy, and `A.15` for performed work when those claims are live. |
| "Agreement, API, boundary, protocol, compliance, SLA, acceptance, or permission wording mixes rules, gates, duties, evidence, quality, or action." | `A.6` | Use `A.6.B` for boundary claims, `A.6.C` for claim routing, `A.10` for evidence, `B.3` for assurance, `A.20` for internal constraint validity, `A.21` for gate decisions, and `A.15` for work. |
| "Vocabulary is breaking down: a word or phrase hides the FPF kind, relation, source-use disposition, value meaning, or admissible move." | `E.10` and `E.10.ARCH` | Use the repair pattern after the kind is recovered: `F.19` for phrase apparatus, `F.18` for naming, `A.19.SPR` for state-family wording, `C.16.P` or `C.16.Q` for characteristic, scale, or quality wording, `E.10.D2` for EntityOfConcern, description, or specification-use wording, `A.6.P`, `C.2.P`, `C.30.P`, `C.30.STRAT`, `A.6.F`, `A.6.M`, or another governing pattern. |

#### FPF-Artifact Author First Entries

| Working problem or first-entry cue | Apply first | If the question is actually... |
|---|---|---|
| "We need to evaluate or improve an FPF artifact without reducing quality to one score." | `E.22` | Use `E.21` for one pattern version, `E.9.DA` for one `DRR`, `E.2.DA` for FPF-level quality, and `E.23` when repeated improvement is being made. Use `A.19.ECS` first only when the needed evaluation characteristic space does not yet exist or is inadequate. |
| "We need to publish an accepted evaluation CharacteristicSpace as an FPF pattern." | `E.8.ECSPF` | Use `A.19.ECS` while constructing or repairing the evaluation characteristic space itself. Use `E.21`, `E.9.DA`, or `E.2.DA` when applying an existing evaluation to a pattern, `DRR`, or FPF-level object. |

