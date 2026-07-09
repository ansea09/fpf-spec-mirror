---
chunk_kind: "child"
pattern_id: "E.11"
pattern_title: "First-Practical Entry and Pattern-Use Discoverability Discipline"
section_id: "E.11:4.1"
section_title: "readme First-Entry Scenario Rule"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11/E.11__007_readme-first-entry-scenario-rule.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "E.11 — First-Practical Entry and Pattern-Use Discoverability Discipline"
  - "E.11:4.1 — readme First-Entry Scenario Rule"
line_start: 71305
line_end: 71458
dependencies:
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.19"
  - "E.21"
  - "E.8"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
  - "Public first-entry explanation or durable pattern semantics"
  - "dependencies"
  - "query phrases"
---

### E.11:4.1 - readme First-Entry Scenario Rule

The public first-entry scenario set starts from working project questions and stabilizing results.

A conforming first-entry scenario has this shape:

```text
FirstEntryScenario:
  projectQuestion:
  practicalUse:
  typicalFirstResults:
  firstPatternFamily:
  blockedOverreadOrBoundary:
```

The public scenario text may be prose rather than a visible form. It should still make those fields recoverable. `typicalFirstResults` may name one ordinary result for a simple entry case, but the schema does not require one input record to become one output record; a scenario may start from several accepted records, source packs, or current structures and expose several admissible first results or next uses.

Good scenario heads name recognizable project work:

- develop or review architecture;
- write rules, methods, and work-process documents;
- compare alternatives and make a local choice;
- turn a vague situation into a usable problem statement;
- define what "better" means and run improvement;
- prepare a costly or hard-to-reverse action;
- account for timing, freshness, rhythm, and action windows;
- use causal explanations, interventions, responsibility, and model outputs for action;
- compare descriptions, dashboards, explanations, and views of the same described object;
- give project objects, relations, and claims better names;
- clarify wording that drives work;
- decide whether a mathematical model or formal declaration would help;
- build a state-of-the-art or option portfolio;
- build a domain or local FPF-grounded framework.

Action-driving wording may be one scenario. It must not dominate the public first-entry set. FPF should not look like a commission for checking admissible technical speech when it is also a framework for architecture, problem shaping, work-method publication, comparison, evidence, mathematics, quality, and improvement.

#### E.11:4.1a - Entry-Unfolding Seed Descriptions

When a first-entry scenario needs to show how the first move continues without becoming a required workflow, write a compact `EntryUnfoldingSeedDescription@Readme` or make its fields recoverable in prose.

```text
EntryUnfoldingSeedDescription@Readme:
  entryProblemPhrase:
  firstGoverningPatternSet[]:
  firstRecordToWrite:
  likelyFamilyCueRefs[]?:
  directGoverningPatternSet[]:
  governingPatternMap?:
  firstCandidateLoci[]:
  blockedOverread:
  governingPatternReturn:
  nextReadableOutputs:
```

The seed is a public description episteme, not the project's unfolding structure. It says: "from this recognizable project question, the likely first governed record or small candidate record set is here, with these candidate loci, returns to governing patterns, and next readable outputs." It must not prescribe a universal FPF procedure or create a second navigation authority beside the pattern bodies.

`likelyFamilyCueRefs[]?` may cite promoted core cue examples such as `UF.P2S`, `UF.IMP`, or `UF.REFRESH`, or a DPF or project-local cue when that package defines one. These cues are optional recognition aids. They are not membership in a maintained list, not conformance, not a promise that FPF core lists every local unfolding structure, and not the governing route for the entry. The authoritative route for an entry is `directGoverningPatternSet[]` plus `governingPatternMap?`.

The compact seed's problem-side and starting fields are entry-level cues, not admitted CGUS slots by themselves. A fuller `ConstraintGovernedUnfoldingStructure@Context` may later cite admitted records through `acceptedStartingRecordRefs[]` and already-current structures through `acceptedStartingStructureRefs[]`. In E.11 they remain public-entry cues; acceptance and stronger use still belong to the direct governing pattern for the record or structure.

The compact seed should be enough for most public readme entries. If it is not enough, open a fuller `FirstEntryUnfoldingExpansion@FPFReadme` under this E.11 custody rather than stuffing the README with record fields.

```text
FirstEntryUnfoldingExpansion@FPFReadme:
  entryId:
  publicScenarioHead:
  declaredProblemSideRecordCues:
  intendedPractitionerRoleRefs:
  startingRecordOrStructureCues:
    - startingKindOrCue:
      startingReadiness:
      contextGrounding:
  likelyFamilyCueRefs[]?:
  directGoverningPatternSet[]:
  unfoldingLoci:
    - locusName:
      governingPatternRef:
      expectedRecordOrResult:
      governingPatternBoundary:
  typicalFirstResults:
  nextPossibleResults:
  governingPatternMap:
    claimOrRelationKind -> governingPatternRef
  blockedOverreads:
  returnOrReopenCondition:
  patternFamilyRefs:
  DRRRefs:
  entryUnfoldingExplicitness:
  remainingUnfoldingCarryThroughWork:
```

`FirstEntryUnfoldingExpansion@FPFReadme` is for entry disambiguation and didactic support. It may point to `DemonstrativeUnfoldingSlice@Context` records when a first-use example is needed, but it does not become a pattern body, a table of contents, or a mandatory public card.

`likelyFamilyCueRefs[]?` in an expansion record uses the same optional recognition cues as the compact seed. If no promoted core or local cue helps the reader, leave the field empty and rely on `directGoverningPatternSet[]` and `governingPatternMap`. Do not add a core `UF.*` cue merely because a public README entry exists.

#### E.11:4.1b - Current First-Practical Entry Seed Set

`CurrentFirstPracticalEntrySeedSet@Readme` is the E.11 custody record for the current public first-practical entries in `host-readme`. It is not a second public front door and not a technical `UF.*` list. It preserves the entry set as a reviewable disambiguation table: if the README wording changes, this table is the place to check whether the first useful result, governing pattern map, blocked overread, and return condition still match.

| Entry | First useful result or record | Main seed shape | Direct governing-pattern map | Blocked overread | Return or reopen condition |
| --- | --- | --- | --- | --- | --- |
| 1 Architecture | `ProblemToStructureArchitecturingFlowCard@Project` or first architecture question note | architecture-relevant pressure to candidate, selected, expected, or actual structures | `C.32.P2S`, `C.30`, `C.32`, `C.32.PAD`, `C.30.TFS-REL`, `C.33`, `C.34`, `C.35`, work and refresh patterns when current | diagram, view, ADR, score, or P2S card as architecture plus decision plus realization | Return when decision, description, work, eval, currentness, or actual-structure feedback becomes the current claim. |
| 2 Rules, methods, work-process documents | working-document outline, method-description record, work-plan seed, readiness note, or call-plan record | governed object and document pressure to method, method description, interface, work, role, gate, permission, publication, or tool-use planning pattern | `A.6`, `A.15`, `A.15.1`, `A.15.2`, `A.15.3`, `A.15.4`, `E.18.1`, `C.24`, `E.8`, `E.19` | one document as method, plan, permission, evidence, gate, publication, and work at once | Return when a stronger work, gate, evidence, role, publication, or tool-use claim is made. |
| 3 Compare alternatives | comparison frame, archive/front/pool, selected set, or local-choice record | candidate or option field to comparison and selection relation | `A.19`, `A.19.ECS`, `C.11`, `C.18`, `C.19`, `G.5` | selected set as scalar winner or ungoverned preference | Return when decision, publication, refresh, or local-choice authority is claimed. |
| 4 Vague situation to problem | `ProblemCard@Context`, problem portfolio, cue set with candidate downstream governing-pattern alternatives, or abductive prompt | cue, anomaly, opportunity, or pressure to problem-side admitted record and downstream entry | `C.22.2`, `B.4.1`, `B.5.2`, `A.16.*`, downstream pattern named by the live claim | cue, prompt, or route-shaped publication form treated as an admitted problem record, downstream governing-pattern recommendation, method, work, architecture claim, evidence claim, or decision authority | Return when method, work, architecture, evidence, decision, or hypothesis/evidence status is claimed. |
| 5 Better and improvement | evaluation frame, first evaluation result, or quality-improvement loop record | object version to evaluation, repair candidates, re-evaluation, and stop or continue decision | `E.22`, `E.23`, `C.16`, `C.25`, `E.21`, `E.9.DA`, `E.2.DA`, `A.22.CGUS` when unfolding structure is current | retry loop or all-5 target as improvement | Return when a source-currentness relation, release, gate, work, evidence, or decision claim leaves improvement governance. |
| 6 Commitment-ready action | commitment-readiness note, smaller-experiment option, action-mode note, or work-or-architecture follow-up note | costly or hard-to-reverse action to action mode and direct governing-pattern exit | `A.10`, `B.3`, `A.20`, `A.21`, `C.11`, `C.28`, current work or architecture pattern | checklist or gate-looking path as work authorization | Return when the project can act on a named basis, narrow the claim, test cheaply, or must enter evidence, assurance, gate, decision, work, or architecture governance. |
| 7 Timing and freshness | timing note, temporal claim, currentness window, freshness limit, action-window note, or refresh record | object whose timing matters to affected decision, work, publication, comparison, or refresh pattern | `C.27`, `G.11`, `A.10`, `A.20`, `A.21`, `C.11`, pattern governing the timed object | stale timing cue as current authority | Return when freshness, decay, telemetry, or timing changes the admissible use. |
| 8 Causality and model outputs | causal-use, counterfactual-use, responsibility, model-output-use note, or smaller-study frame | causal explanation, intervention, responsibility, or generated output to next action and responsibility boundary | `C.28`, `A.10`, `B.3`, `A.20`, `A.21`, `C.11`, domain governing pattern | model output, causal story, or responsibility label as evidence or action authority | Return when study, work, decision, evidence, or stop condition becomes current. |
| 9 Descriptions, dashboards, explanations, and views | description-use, view-use, narrative-rendering, correspondence, or representation-transition note | described EntityOfConcern to description, view, narrative, correspondence, publication, role concern, or transition relation | `E.17`, `E.17.0`, `E.17.EFP`, `A.6.2`, `A.6.3.NAR`, `A.6.3.RT`, `A.6.3.CSC`, `A.6.4`, `C.30.AD`, `C.30.TFS-REL`, `C.33`, `C.34`, `C.35` | description, dashboard, narrative, or view as the described object, evidence, decision, or work | Return when stronger evidence, architecture, decision, work, assurance, or publication-use claim is made. |
| 10 Naming | name card or bounded naming decision | object, kind, relation, or use needing a better name to contexts, candidates, and publication boundary | `F.17`, `F.18`, `F.19`, `E.10`, `E.10.ARCH`, subject governing pattern | name change as kind change or work authorization | Return when bridge, UTS, publication, or subject-domain claim becomes current. |
| 11 Action-driving wording | repaired paragraph, claim register row, term-sheet row, or use-boundary note | wording that may change action to recovered kind, relation, use, and changed text | `E.10`, `E.10.ARCH`, `F.18`, `F.19`, `A.6.P`, `C.2.P`, `B.3.5`, `C.13`, `C.3`, subject precision pattern | lexical replacement as ontology repair | Return when action, work, evidence, architecture, proof, or publication claim is stronger than wording repair. |
| 12 Mathematical model or formal declaration | lens candidate, formal-substrate declaration, preserved/lost structure note, payoff note, or validation-limit note | project difficulty to candidate mathematical lens or formal substrate | `C.29`, `A.6.0`, `A.6.1`, `E.18.1`, `B.3.5`, `C.13`, `C.3`, `C.16`, `C.27`, architecture/domain pattern | mathematical prestige as evidence, architecture adequacy, or work authority | Return when validation, measurement, formal claim, downstream use, or P2W carry-through is current. |
| 13 SoTA or option portfolio | current-front question, reference harvest, archive/front/pool, comparison, or publication record | scope and current-front question to options and refresh | `G.0`, `G.1`, `G.2`, `G.5`, `G.11`, `C.18`, `C.19`, `A.19`, `A.19.ECS` | reference list as current authority or selected set | Return when a source-currentness relation, reference-edition state, comparison, publication, or refresh condition changes. |
| 14 Domain or local framework | PFAD, PFR, DPF seed, `G.2` source pack, quality-improvement path or loop record, publication or access carrier, or call plan | local context and domain references to framework authoring spine | `E.4`, `E.4.FPF`, `E.4.PFAD`, `E.4.DPF`, `E.4.DPF.DA`, `E.4.PFR`, `G.2`, `C.24`, `E.8`, `E.11`, `E.17`, `F.18`, `G.11` | all-in-one framework file or source pack as admitted framework | Return when framework architecture, relation record, source-currentness relation, publication, access carrier, or tool-use planning is current. |

Use `EntryUnfoldingExplicitness` as an internal discoverability signal when reviewing a first-entry row:

| Value | Meaning |
| ---: | --- |
| 0 | no recoverable unfolding structure; only a topic or slogan |
| 1 | problem phrase plus pattern list |
| 2 | first result or result set named but governing-pattern map missing |
| 3 | unfolding family and governing-pattern map recoverable |
| 4 | starting records or structures, next uses, unfolding loci, governing-pattern map, and return are recoverable |
| 5 | worked slices, relation records, DRR carry-through, and refresh condition have been tested |

The scale is not public bureaucracy. It helps decide whether the README line is enough, whether an E.11 expansion is needed, or whether the relevant pattern body must carry more of the solution structure.

#### E.11:4.1.1 - First-Time Engineer Readability Rule

Public first-entry text is tested against a first-time engineer, engineer-manager, or assisting agent who has not studied FPF.

The title and first sentence must name a recognizable working problem before FPF taxonomy, pattern ids, internal kind names, quality or projection vocabulary, or conformance vocabulary appears. The first practical result must be something the reader could imagine producing or asking for in the project: an architecture question note, regulation outline, comparison note, problem card, quality-and-improvement note, commitment-readiness note, timing note, causal-use note, description-use note, naming card, repaired paragraph, modeling note, or option portfolio.

FPF precision remains required. It is introduced after the plain recognition hook and stays recoverable through the pattern ids and later wording. If the same sentence cannot be translated into ordinary engineering Russian or ordinary engineering English without FPF slang, it is probably not public first-entry text yet.

#### E.11:4.1.2 - Public Value Claim And Grounding Rule

A first-entry scenario may state substantial project value, but that value claim must be grounded. The scenario is not bare marketing copy. It should let an unfamiliar practitioner or assisting agent recognize a project situation, imagine a first useful result, and see the substantive FPF mechanism behind that value claim.

A conforming public first-entry scenario therefore:

- starts from a concrete project need in ordinary engineering language;
- names the first useful written result or decision aid before it names internal FPF apparatus;
- names the first pattern family as the means, not as the headline;
- shows at least one substantive distinction, object, comparison, or decision that FPF will make usable;
- avoids cards, forms, pattern ids, quality vocabulary, projection vocabulary, and conformance vocabulary until the working use is already recognizable;
- keeps wording repair and description repair visible but below half of the public scenario set, so FPF does not present itself mainly as speech policing.

When a public first-entry scenario must mention boundary or checking terms such as `evidence`, `assurance`, `gate`, `validity`, `admissible`, `blockedOverread`, `permission`, or `compliance`, place them after the working use and the first useful result. They should act as addresses to governing patterns, not as the public reason to open FPF.

The public first-entry set should read like "here are typical ways FPF can help a working project first", not like "here is the internal topology of FPF" and not like "here are slogans about better thinking."

