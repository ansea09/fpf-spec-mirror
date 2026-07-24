---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:7"
section_title: "Subject-pattern thin-pointer rule"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__013_subject-pattern-thin-pointer-rule.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:7 — Subject-pattern thin-pointer rule"
line_start: 74181
line_end: 74205
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.SPR"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.F"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.25"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.P"
  - "C.30.STRAT"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.18"
  - "E.19"
  - "E.2"
  - "E.20"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

### E.10.ARCH:7 - Subject-pattern thin-pointer rule

Subject patterns keep at most one local first-use cue when the EntityOfConcern under repair, relation, claim, or field is hidden, then name the selected precision-restoration pattern as a pattern through ordinary references or `Relations`. They do not turn that reference into local reference boilerplate, and they do not copy:

- the full `E.10` wording-recognition table;
- this shared algorithm;
- the `WordingUseRestorationApplicabilityTable`;
- broad false-friend lists whose only job is first-stage repair;
- past placement or repair history written in place of current architecture prose.

A thin pointer is acceptable when it helps the working reader choose the right first move, for example:

- use `C.30.P` when architecture or structure wording hides whether the use under repair is selected structure, architecture-description use, structural-view use, source, model, diagram, graph, dashboard, or ordinary prose;
- use `C.30.STRAT` when `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, `gate`, or a close source label hides whether the use under repair is a control-layer relation, module-interface relation, architecture-to-`TransformationFlowStructure` relation, scale or coarse-graining relation, publication relation set, gate relation, neighboring use named by value, ordinary source label, quote-only cue, or blocked use;
- use `C.16.P` when metric, score, axis, dimension, feature, property, indicator, strong, weak, robust, level, coordinate, threshold, or comparison wording hides characteristic or scale construction;
- use `C.16.Q` when quality or evaluative characterization wording hides Q-bundle, pattern-quality coordinate, relation construction, action-invitation, bridge, or characterization use named by value;
- use `A.19.SPR` when state, status, posture, readiness, stance, currentness, or a local state-like field hides bearer, state frame, value set, admissible use, or governing pattern;
- use `C.2.P` when source, publication, publication form, face, `PublicationUnit`, dashboard, documentation, or text-work wording hides source-currentness relation or project-side reliance;
- use `A.3.1` when method, algorithm, program, proof, solver, workflow, process, procedure, access-path, query-plan, control-strategy, method-algebra, method-graph, selector-calculus, or programming-paradigm wording hides whether the current slot is method, method relation structure, method description, formal substrate, mathematical-lens use, mechanism, work plan, dated work, evidence relation, or quote-only source wording;
- use `A.6.RSIR` when relation, signature, interface, role, assignment, enactment, slot, field, parameter, argument, endpoint, port, API, protocol, connector, capability, affordance, method, function, concern, or interest wording hides the current governed object or claim kind and no direct governing pattern is yet clear;

- use `A.6.P.WMR` when input, raw-material, source-data, source-material, output, result, outcome, deliverable, handoff, or work-name wording hides one exact work/method-boundary relation-bearing claim; use `C.2.P` first for the epistemic source side, and return one of the four truthful WMR exits rather than classification or actual-slot fallback;
- use `C.2.P.DR` when a declarative representation, graph relation, evidence-path wording, publication face, checklist predicate, query, dashboard, or pattern relation is being overread as an imperative route, call, dispatch, work sequence, permission, release, evidence result, or pattern application;
- use the direct governing pattern, with `A.19.SPR` only when hidden state-family wording remains, when admissibility-like, legal, lawful, validity, pass-looking, fail-looking, readiness, conformance, or authority wording already recovers its bearer, claim kind, source relation, value frame, and admissible use.

