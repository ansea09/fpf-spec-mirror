---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:3"
section_title: "Shared recovery algorithm"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__009_shared-recovery-algorithm.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:3 — Shared recovery algorithm"
line_start: 77403
line_end: 77430
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
  - "C.2.1"
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
  - "E.10.DEV"
  - "E.10.MOVE"
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

### E.10.ARCH:3 - Shared recovery algorithm

Use this five-step object-preserving order only for the ontology question that remains after the normal `F.19` and compact `E.10` pass:

1. **Bound the wording and use.** Name the exact text span or publication unit, the recurring wording, its sentence function and register, and the working claim or use that makes it consequential. Keep `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily` as author-facing routing coordinates rather than as candidate project ontology.
2. **Recover the exact subject and claim.** Identify the exact governed entity, value, or episteme; the obtaining direct relation and its actual participants when that is the claim; or the exact claim-bearing episteme when the encountered row, report, or card states the claim. When representation is current, identify both the represented object and the representation use without treating the representation as obtaining. When metonymy or compression is plausible, keep both the literal and intended candidates explicit until their defining or testing rules and exact relations or claims distinguish the uses or rule one out; shared wording does not license premature single-referent closure.
3. **Bypass restoration when the subject and predicate are clear.** Once the object, relation, assertion, description, publication, representation, work, result, structure, or architecture claim has a clear predicate and `ClaimGraph`, state or use that subject claim under its defining or constraining rule and stop the restoration detour. Use the PatternID to locate the rule. If actual authoring or repair Work is part of the claim, recover each exact performer through A.13 and let A.15.1 independently admit the dated Work. Add A.2.1 and F.6 only when this architecture account also consumes precise assignment-bound attribution. Work admission is decided independently under A.15.1; F.6 supplies the additional precise attribution. State Method, MethodDescription, and responsibility claims separately only when they matter.
4. **Add only receiver-needed apparatus.** Add a reusable `RelationSignature` and A.6.5 `SlotSpec` values, relation-occurrence identity, participant designations, designators, references, publication forms, or C.29 representation elements only when a named later use needs that additional object. Keep each item under the rule that defines its identity or use, and cite the pattern containing that rule. Use an E.24 `onticSlotRelation` only after durable ontic settlement makes that exact relation current. If the same entity participates in several direct relations, is designated in several assertion or occurrence-description epistemes, or corresponds to several representation elements, keep those uses distinct under their separate predicates; shared entity identity does not merge the relations, epistemes, designations, or representation correspondences.
5. **Write the shortest usable sentence.** State the governed object, direct relation or claim, and admissible action-facing use so the working reader need not consult the applicability row. Add a guard only when the `F.19` plausible-intended-reader test warrants it. A type-correct but inert sentence is not a completed repair.

Perform a terminology-source audit only when source ontology can change the governed object, direct relation kind, participant meaning, actual participant kind, declaration-local `SlotSpec`, assertion-side participant designation, exact use, admissible use, or the defining or testing rule selected for the claim. Stable ordinary prose remains ordinary. A source tuple or argument place remains representation-side until an explicit correspondence to a declared `SlotSpec` is current.

#### E.10.ARCH:3.1 - Method, work, and P2W claim-rule constellation in wording restoration

Use this branch when one source label, project handle, or project concern points to changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern` rather than to one typed FPF value.

Do not name a new recovery object. Recover each current value and claim separately: one locally used `U.Method`; a `U.MethodDescription` episteme that describes that method; exact method-side relations and, only when a named use depends on their organization, the A.22-selected structure locally designated `MethodRelationStructure`; a mechanism or formal-substrate declaration; a mathematical-lens or other representation use; a `U.WorkPlan`; dated `U.Work`; an actual transformation; a production, inception, or completion claim; a changed-referent relation; a measurement, evaluation, choice, or decision result; an evidence, source, gate, publication, temporal, delivery, or acceptance relation; a selected structure; an obtaining C.30 `ArchitectureRelation` with its actual holon and structure participants; a separate `ArchitectureClaim` episteme; an architecture-description episteme only when that use is current; or another object named under its defining or testing rule. A.15 keeps system-role classification, assignment, Method, MethodDescription, WorkPlan, dated Work, and F.6 attribution separate. Unresolved *role* wording still uses `E.10.ROLE`.

When wording concerns a relation among methods or method families, recover the relation itself—for example, serial or parallel composition, guarded choice, iteration, refinement, substitution, decomposition, parameterization, family membership, selection, or fallback. Use `A.3.1`, `G.5`, or the rule that defines or constrains that relation. If a named use depends on how several such relations are organized, use A.22's criterion to select the structure and call it `MethodRelationStructure` locally; that name creates neither a U-kind nor another relation. A graph, algebra, tuple, or other notation is a C.29 representation or mathematical-lens use of the structure, not itself a Method. A claim-bearing episteme that describes the relation remains separate from it. `U.MethodDescription` still means an episteme that describes one Method. Do not classify one value as both `U.Method` and `U.Mechanism` unless the defining rules for those two kinds independently admit both claims.

The authoring note may record the affected entity; the exact source or practice boundary, effective scheme, model-use structure, situation, scope, or frame when it changes the claim; a change or maintained-condition claim; any current state or delta predicate; and the exact objects and relations exposed by the wording together with the rules that define or constrain them. This is a wording-repair note. Keep each project-side value under its own defining or testing rule and preserve its identity separately; the pattern ID remains a locator.

Treat `input`, `raw material`, epistemic `source data` or `source material`, `output`, `result`, `outcome`, `deliverable`, `handoff`, and work-name wording as triggers only while their exact relation is hidden. Once clear, bypass E.10.ARCH: use `A.3.2` only for a description episteme about one exact method; `A.15.2` for an intended participant or use in planned work; `A.15.1` and the exact resource or participation pattern for a dated Work occurrence; `A.3.4.P` and the direct transformation pattern for an actual transformation participant; `A.15.PROD`, the measurement or evaluation pattern, or the delivery or acceptance pattern for the exact result claim; and `C.29` when the word names only an argument, tuple component, graph element, or other representation place. Use `C.2.P` first for an epistemic source expression and source-to-use relation. Keep physical material under its direct physical governor.

If the exact method/work-boundary relation is still hidden after generic relation recovery, apply `A.6.P.WMR`. Its result remains exactly one family: a positive or governed-negative direct subject-relation claim; an exact `A.6.1` operation-application binding; an exact local `A.15.PROD` or `A.6.RCD` claim; or reason-specific non-assertability as `factually unsupported`, `missing-information`, or `missing-governor`. A failed known predicate such as `EpistemeUsedByReviewWorkAsReference` is `factually unsupported`; an unavailable ETL receiving-use fact under a known rule is `missing-information`; an absent relation kind and defining ClaimGraph or declaration for the health-effect claim between `Patient_8472` and `HE-8472` is `missing-governor`. Only the last names an affected receiving use and a needed future relation rule or declaration. Classification, a generic result label, a type-correct designation, planned use, or inferred opposite polarity does not close the branch.

Durable naming follows the governed value. `F.18` may name a performed Work occurrence only after its A.15.1 occurrence basis is established, and it names neighboring production, measurement, evaluation, delivery, and acceptance results separately. If a proposed `U.*` name merely repeats a declaration-local `SlotSpec` label or a participant meaning stated in a direct-relation rule, keep it local unless E.24 supplies durable identity, action-facing gain, and the exact relation involved. If repeated Method, Work, or process material is proposed as durable ontology, its E.24 ontic decision and, for any public `U.*` kind, `E.24.UK` admission plus the pattern containing the kind's defining rule must precede current citation.

