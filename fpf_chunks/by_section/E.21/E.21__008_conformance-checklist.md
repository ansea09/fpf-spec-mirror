---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__008_conformance-checklist.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:7 — Conformance Checklist"
line_start: 67128
line_end: 67190
dependencies:
  - "A.17-A.19"
  - "A.19.ECS"
  - "A.6.P"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.10"
  - "E.11"
  - "E.19"
  - "E.2.DA"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "J.4"
keywords:
  - "and admissibility predicates are not written as duties"
  - "definitions"
  - "invariants"
  - "state agent obligations only"
  - "typing rules"
---

### E.21:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| **CC-E21-1 (No single score).** | A pattern-quality read **SHALL NOT** collapse the active characteristics into one arithmetic score, percentage, average, or hidden total order. | Preserves multi-characteristic truth and scale legality. |
| **CC-E21-2 (Bundle scope declared).** | A `PatternQualityQBundle` **SHALL** declare `PatternVersionRef`, `ClaimScope`, `WorkingReaderScope`, `IntendedUse`, and `QualificationWindow`. | Prevents unscoped quality claims. |
| **CC-E21-2a (Question purpose explicit or floor-defaulted).** | A nontrivial `E.21` read **SHALL** state the requested quality-read purpose or cite an `E.22` `QualityReadQuestionFrame`. If omitted, the read is `floorRead` under the declared or receiving-pattern floor, not `exceptionalImprovementRead`. | Prevents blocker audits from masquerading as exceptional-improvement reads and prevents maximal rewrite pressure when only readiness was requested. |
| **CC-E21-3 (Eligibility before dominance).** | The active `EligibilitySet` **SHALL** be checked before dominance, tie-breaker, or front comparison. | Prevents hard blockers from being averaged away. |
| **CC-E21-4 (Status value set).** | The result **SHALL** use one `PatternQualityStatus` value from `E.21:4.1` or explicitly define a local extension with a narrower meaning. | Keeps outcomes portable and non-vague. |
| **CC-E21-5 (Declared coordinates).** | The active `DominanceSet` **SHALL** name the selected characteristics and their ordinal floors. | Makes the quality space inspectable. |
| **CC-E21-6 (Measurement legality).** | Any comparison, coordinate, threshold, or telemetry reading **SHALL** follow `C.16`, `A.17`, `A.18`, and applicable `A.19`/`C.25` discipline. | Blocks illegal scalarization and ordinal arithmetic. |
| **CC-E21-6a (Coordinate/state separation).** | A pattern-quality read **SHALL NOT** assign coordinate values from review completion, landing state, monolith placement, release state, steward acceptance, or other administrative state. | Prevents administrative proxies from replacing content measurement. |
| **CC-E21-6b (No reputation or adoption medals).** | A pattern-quality read **SHALL NOT** raise or lower coordinate values from popularity, adoption, awards, steward praise, reviewer praise, prior use, absence of use, completed external review, number of reviews, landing, monolith placement, release inclusion, or absence of those signals. A signal may affect a coordinate only after it is rewritten into replayable pattern-content evidence for the exact pattern version, reader/use/scope/window, and coordinate. | Prevents reputation and usage proxies from replacing pattern-property readings. |
| **CC-E21-7 (Neighbour authority).** | A pattern-quality read **SHALL** cite exact neighbouring FPF patterns for evidence, assurance, measurement, naming, work, gate, decision, publication, causal, bridge, release, and refresh claims when those claims are live. | Prevents shadow authority. |
| **CC-E21-8 (SoTA content-bearingness).** | SoTA grounding **SHALL** follow the E.8 definition of SoTA as current best-known problem-solving practice for the governed problem, state what the pattern adopts, adapts, or rejects, and state which `Solution`, checklist, relation, boundary, or worked case changes because of that stance. Official status, source recency, broad popularity, citation volume, institutional adoption, or familiar terminology do not raise `SoTABindingAndCurrentness` by themselves. | Blocks decorative citation and prestige-source substitution. |
| **CC-E21-9 (Action guidance survives).** | If semantic or lexical repair improves type precision, the read **SHALL** check that a remaining admissible reader move still exists or that a named neighbouring pattern now carries the live claim. | Prevents type-correct but inert patterns. |
| **CC-E21-10 (Bounded non-use).** | Remaining weaknesses **SHALL** narrow use or name a receiving pattern; they **MUST NOT** be hidden behind "later", "deferred", or vague future research language inside the pattern-quality claim. | Makes stopping honest. |
| **CC-E21-11 (Front discipline).** | When several variants are live, the selected version **SHOULD** be on the `PatternQualityFront`; choosing a dominated variant requires an explicit reason such as legacy, regulation, or reader-continuity cost. | Preserves open-ended search without endless perfectionism. |
| **CC-E21-12 (Apparatus fit).** | A pattern-quality read **SHALL** add front/archive/telemetry/support fields only when the live claim requires them. | Prevents bureaucracy from masquerading as quality. |
| **CC-E21-13 (Telemetry boundaries).** | Telemetry signals **SHALL** reopen or calibrate the quality read only for the claim they can support; retrieval or review telemetry is not project certification. | Keeps evidence use scoped. |
| **CC-E21-14 (Accepted-basis carry-through).** | Accepted basis obligations governing the pattern **SHALL** be expressed, intentionally absent, inherited, or assigned by value to a named receiving pattern or support document before claiming `admissibleForDeclaredUse`. | Prevents source loss across drafting. |
| **CC-E21-15 (Stop condition explicit).** | A stop decision **SHALL** cite the active `StopCondition` and state whether it is satisfied for the declared scope. | Replaces "looks good enough" with an inspectable end condition. |
| **CC-E21-16 (Cost coordinates not hidden).** | Reader, author, reviewer, maintainer, migration, evidence, neighbour-integration, entry/projection, retrieval, durable-name, relation, and corpus-ecology cost **SHALL** be active coordinates when they can change admissible use; they **SHALL NOT** be hidden as tie-breakers while live. | Prevents affordability, maintainability, entry, and corpus-ecology loss from being optimized away. |
| **CC-E21-17 (Proxy-for-value check).** | Before a stop decision, the read **SHALL** ask what became worse after coordinate improvement; if rubric satisfaction displaces practical pattern-use value, the `DominanceSet`, status, or scope **MUST** be revised. | Blocks Goodhart substitution. |
| **CC-E21-18 (First-pass affordability).** | A first-pass pattern-quality read **SHALL NOT** require `PatternQualityFront`, `PatternImprovementArchive`, `TelemetrySet`, full `CoordinateEvidenceRef` cards, or a complete coordinate-menu read unless the declared `ClaimScope` makes them live. | Keeps ordinary pattern evaluation usable and prevents review apparatus from becoming the first action. |
| **CC-E21-18a (Repeated improvement locus).** | When a pattern-quality read becomes part of repeated improvement, the repeated method **SHALL** be governed by `E.23`; `E.21` continues to supply coordinates, values, protected trade-offs, status, and stop meanings. | Prevents `E.21` from becoming the full improvement-loop method while keeping exceptional pattern improvement available. |

| **CC-E21-19 (First action before control).** | A pattern-quality read **SHALL** recover the pattern version's first admissible action-guiding move from `Problem frame` and `Solution` before adding checklist, telemetry, archive, or high-assurance support. If the first move is absent or only appears in the checklist, the read may close as `repairBeforeUse` or `admissibleWithNarrowerUse`. | Prevents conformance checks and control apparatus from replacing pattern guidance. |
| **CC-E21-20 (SoTA mutation test).** | Every live SoTA row **SHALL** state which `E.21` field, eligibility condition, coordinate, worked slice, relation, conformance item, non-use boundary, or stop/reopen condition changes because of the adopted/adapted/rejected stance. A source that changes no content-bearing text is rationale support, not SoTA binding. | Prevents decorative SoTA and keeps `SoTABindingAndCurrentness` content-bearing. |
| **CC-E21-21 (SoTA currentness and lineage split).** | A foundational, official, popular, or lineage source **MAY** remain in `E.21:11`, but a current-practice claim **SHALL** either cite a current SoTA anchor under E.8 or explicitly mark the older or official source as lineage-only, current-standard reference, rationale-only, or rejected-popular-practice material. | Prevents old standards, fresh standards, classic papers, and popular practice from masquerading as present SoTA. |
| **CC-E21-22 (Evaluation non-certification).** | A pattern-quality evaluation **SHALL NOT** be used as safety, security, compliance, release, project assurance, or gate certification. When such a claim is live, the read **SHALL** open the exact receiving FPF pattern and state the supported and unsupported use. | Blocks audit-theatre and compliance-by-checklist overread. |
| **CC-E21-23 (Activated retrieval evidence only).** | Retrieval, RAG, search, or misentry telemetry **SHALL** be used only when retrieval-facing pattern entry or observed misretrieval is live; it **SHALL NOT** become a universal benchmark requirement for ordinary pattern drafts. | Keeps modern retrieval evaluation useful without adding review bureaucracy. |
| **CC-E21-24 (First-pass content slice).** | A conforming first-pass pattern-quality read **SHALL** be able to close on the smallest slice that identifies pattern version, reader/use/window, first admissible move evidence, activated blockers, minimal dominance coordinates, status, and next admissible repair or bounded non-use. | Keeps `E.21` usable as content guidance rather than review bureaucracy. |
| **CC-E21-25 (Status payload).** | Every `PatternQualityStatus` **SHALL** state the exact use, scope, reader boundary, blocker, reopen trigger, or architecture-decision question that makes the status true. | Prevents status labels from becoming vague maturity tags. |
| **CC-E21-26 (Ordinal-reading boundary).** | A coordinate value **SHALL** be treated as an ordinal content reading unless a `C.16` measurement basis is explicitly declared. | Prevents accidental pseudo-measurement. |
| **CC-E21-27 (Claim-triggered activation).** | Coordinates and eligibility rows **SHALL** be activated by the live claim force of the pattern version or quality claim; inactive rows **SHALL NOT** be treated as hidden failures or waived passes. | Keeps the complete characteristic space from becoming a universal audit grid. |
| **CC-E21-28 (Kind settlement).** | Every durable or FPF-force-bearing `E.21` head **SHALL** be classified as an existing FPF kind specialisation, local field, value set, local evidence-reference record, or scoped support construct. A head with no recovered kind **SHALL NOT** be used in a stop decision. | Prevents `E.21` from minting a parallel quality ontology. |
| **CC-E21-29 (No gate/status overread).** | `PatternQualityStatus`, `EligibilitySet`, coordinate floors, and `StopCondition` **SHALL NOT** be described as gate passage, release status, role state, assurance level, work authority, or project approval. | Keeps `E.21`, `E.19`, `A.21`, `B.3`, and release/work patterns distinct. |
| **CC-E21-30 (Local name-card sufficiency).** | `E.21:4.11` local name-precision cards are sufficient for ordinary `E.21` use. A full `F.18` Name Card is required only when a head is reused outside `E.21`, collides with an existing head, enters durable cross-pattern vocabulary, or changes naming authority. | Preserves naming discipline without turning ordinary pattern-quality reading into naming bureaucracy. |
| **CC-E21-31 (Coordinate-head scope).** | Coordinate heads in `PatternQualityEvaluationCharacteristicSpace` **SHALL** remain local ordinal characteristic heads for pattern-quality reads unless a neighbouring `C.16`/`A.17`/`A.18`/`A.19` declaration promotes a specific coordinate into a measurement or broader characteristic claim. | Prevents accidental metrics, maturity dimensions, and pseudo-measurement. |
| **CC-E21-32 (Neighbour-governed claim boundary).** | A conforming `E.21` read **SHALL** state or preserve the governing-pattern boundary between `E.21` and live neighbouring patterns when authoring, review, measurement, naming, evidence, assurance, gate, release, work, or project-side claims are involved. | Prevents `E.21` from becoming a central quality-governance subsystem. |
| **CC-E21-33 (Layer activation).** | A conforming `E.21` read **SHALL** use the lowest activation layer sufficient for the declared claim. Front, archive, telemetry, and full support-card apparatus **SHALL NOT** be required for a first-pass read unless the claim makes them live. | Preserves affordability and prevents bureaucracy. |
| **CC-E21-34 (Replayable quality read).** | A `PatternQualityQBundle` **SHALL** be replayable from its pinned pattern version, reader/use/scope/window, active eligibility rows, active coordinates, evidence refs, status payload, and stop/non-stop reason, without relying on chat memory or administrative placement state. | Preserves auditability without requiring a process log. |
| **CC-E21-35 (No neighbour substitution).** | `E.21` **SHALL NOT** absorb the governed object of `E.8`, `E.19`, `C.25`, `C.16`/`A.17`/`A.18`/`A.19`, `F.18`/`E.10`/`A.6.P`, or project-side evidence, assurance, gate, work, and release patterns. When such a claim is live, `E.21` **SHALL** name the exact receiving pattern application by value. | Preserves modularity and composability. |
| **CC-E21-36 (Smallest live reopen).** | A refresh or telemetry signal **SHALL** reopen the smallest affected locus: source stance, neighbour relation, coordinate reading, worked case, name, eligibility row, status payload, or stop condition. The whole quality read reopens only when that local change can change status or stop. | Preserves evolvability without whole-pattern churn. |
| **CC-E21-37 (Status is not authority).** | `PatternQualityStatus` **SHALL** remain an admissible-use posture for the pattern-quality claim and **SHALL NOT** be used as project approval/refusal, gate decision, release state, assurance level, compliance verdict, safety certificate, or work authority. | Preserves scope safety and trust calibration. |
| **CC-E21-38 (No quality veto without content locus).** | A blocking pattern-quality finding **SHALL** name the exact activated eligibility row, coordinate, status payload, or stop-condition clause, plus content evidence and the first admissible repair or bounded non-use. | Prevents pattern-quality review from becoming reviewer authority theatre. |
| **CC-E21-39 (Self-application closure).** | `E.21` self-application **SHALL** use the lowest sufficient activation layer and **SHALL NOT** require recursive quality bundles evaluating quality bundles. | Prevents infinite regress and keeps `E.21` usable. |
| **CC-E21-40 (Thin echo boundary).** | ToC rows, `J.4` rows, README notes, dashboards, generated summaries, and retrieval snippets **SHALL NOT** replace the governed `PatternQualityQBundle`; they may only echo it by value and scope. | Prevents projection authority and RAG/snippet overread. |
| **CC-E21-41 (No forced winner).** | When multiple candidates are non-dominated and no receiving action requires one selected candidate, a conforming read **SHALL NOT** force a single winner. | Preserves NQD/front discipline and blocks hidden scalarization. |
| **CC-E21-42 (Bounded non-use as valid outcome).** | `admissibleWithNarrowerUse` **SHALL** be used when a pattern is not ordinary-use admissible but remains useful for a named narrower reader/use/scope. | Prevents unnecessary rewrite churn and preserves useful legacy/support material. |
| **CC-E21-43 (High-value falsifiability hook).** | Coordinate values `4` or `5`, and any coordinate supporting `admissibleForDeclaredUse` or `StopCondition`, **SHALL** state a lowering condition or content discovery that would reopen or lower the read. | Makes high quality claims falsifiable without adding a full harness. |
| **CC-E21-44 (Support retention test).** | Support material **SHALL** remain active only when the read states what quality breakage would return if that material were absent. | Prevents support material from becoming folklore, hidden authority, or permanent reader cost. |
| **CC-E21-45 (Pattern text vs pattern application).** | `E.21` **SHALL NOT** be used to certify that a project correctly applied a pattern. It reads the quality of the pattern version; project/application claims remain under exact receiving patterns. | Preserves FPF-side and project-side boundaries. |
| **CC-E21-46 (High-assurance separation).** | High-assurance support **SHALL NOT** make the ordinary pattern body harder to use unless the ordinary use itself changes. | Keeps ordinary action guidance alive while allowing additional support material where live. |
| **CC-E21-47 (Activation-normalized coordinates).** | `PatternQualityEvaluationCharacteristicSpace` **SHALL NOT** be used as one flat always-on audit grid. Each coordinate **SHALL** state its activation class, and inactive coordinates **SHALL NOT** count as pass, waiver, or hidden failure. | Prevents characteristic bloat and hidden checklist control. |
| **CC-E21-48 (Hard blockers stay out of dominance).** | `firstMoveRecoverability`, hard measurement illegality, shadow neighbour authority, administrative proxy use, and live mission/pillar conflict **SHALL** be treated as eligibility blockers when activated, not weak coordinate values. | Prevents hard failures from being averaged or front-compared away. |
| **CC-E21-49 (No evidence-as-coordinate substitution).** | `CoordinateEvidenceRefs`, evidence kinds, support cards, review findings, and telemetry signals **SHALL** justify, reopen, or calibrate coordinate readings; they **SHALL NOT** become coordinates by themselves. | Keeps the quality space about pattern properties, not support artefact volume. |
| **CC-E21-50 (No hidden double weighting).** | When two quality concerns are directly coupled, the pattern **SHALL** either merge them into one coordinate with explicit subreadings or explain why the two coordinates can fail independently and require different repairs. | Prevents the number of coordinate rows from acting like a hidden weighting scheme. |
| **CC-E21-51 (Formal-claim activation).** | Measurement, score, comparison, threshold, aggregation, mathematical-lens, causal-lens, QL-lens, simulation, representation, or learned-lens checks **SHALL** activate `FormalClaimLegalityAndLensFit`; absence of such a claim **SHALL NOT** create an ordinary coordinate obligation. | Prevents ordinary pattern reads from becoming formal-method bureaucracy. |
| **CC-E21-52 (Projection and corpus activation).** | External entry, publication projection, retrieval, RAG, dashboard, durable-name, relation, or corpus-ecology coordinates **SHALL** activate only when the pattern version or candidate edit changes those surfaces or is known to be misentered or overread through them. | Keeps corpus safety without universal projection bureaucracy. |
| **CC-E21-53 (High-value lowering condition).** | Coordinate values `4` or `5`, `admissibleForDeclaredUse`, and stop claims **SHALL** state a concrete lowering or reopen condition unless the declared use is only first-pass repair triage. | Makes high-value pattern-quality claims falsifiable without requiring a test harness. |

