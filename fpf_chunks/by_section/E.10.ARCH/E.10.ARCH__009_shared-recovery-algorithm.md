---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:3"
section_title: "Shared recovery algorithm"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__009_shared-recovery-algorithm.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:3 — Shared recovery algorithm"
line_start: 74731
line_end: 74758
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

### E.10.ARCH:3 - Shared recovery algorithm

Use this five-step object-preserving order for every E.10.ARCH authoring case:

1. **Bound the wording and use.** Name the exact text span or publication unit, the recurring wording, its sentence function and register, and the working claim or use that makes it consequential. Keep `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily` as author-facing routing coordinates rather than as candidate project ontology.
2. **Recover the exact subject and claim.** Identify the exact governed entity, value, or episteme; the obtaining direct relation and its actual participants when that is the claim; or the exact claim-bearing episteme when the encountered row, report, or card states the claim. When representation is current, identify both the represented object and the representation use without treating the representation as obtaining. When metonymy or compression is plausible, keep both the literal candidate and the intended candidate explicit until their direct owners and exact relations or claims either distinguish the two uses or rule one out; shared wording does not license premature single-referent closure.
3. **Bypass restoration when the owner is clear.** Apply the direct governing pattern immediately once it can carry the recovered object, relation, assertion, description, publication, representation, work, result, structure, or architecture claim. Use E.10.ARCH or a realization pattern only while wording still hides that selection.
4. **Add only receiver-needed apparatus.** Add a reusable `RelationSignature` and A.6.5 `SlotSpec` values, relation-occurrence identity, participant designations, designators, references, publication forms, or C.29 representation elements only when a named later use needs that additional object. Keep each apparatus item under its direct owner. Use an E.24 `onticSlotRelation` only after durable ontic settlement makes that exact relation current. If the same entity participates in several direct relations, is designated in several assertion or occurrence-description epistemes, or corresponds to several representation elements, keep those uses distinct under their separate governors; shared entity identity does not merge the relations, epistemes, designations, or representation correspondences.
5. **Write the shortest usable sentence.** State the governed object, direct relation or claim, admissible action-facing use, and blocked stronger reading so the working reader need not consult the applicability row. A type-correct but inert sentence is not a completed repair.

Perform a terminology-source audit only when source ontology can change the governed object, direct relation kind, participant meaning, actual participant kind, declaration-local `SlotSpec`, assertion-side participant designation, exact use, admissible use, or governing-pattern selection. Stable ordinary prose remains ordinary. A source tuple or argument place remains representation-side until an explicit correspondence to a declared `SlotSpec` is current.

#### E.10.ARCH:3.1 - Method, work, and P2W governing-pattern constellation in wording restoration

Use this branch when one source label, project handle, or project concern points to changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern` rather than to one typed FPF value.

Do not name a new recovery object. Recover each current value and claim separately: one exact context-local `U.Method`; a `U.MethodDescription` episteme that describes that one exact method; `MethodRelationStructure@BoundedContext`; a mechanism declaration or realization; a formal-substrate declaration; a mathematical-lens or other representation use; a `U.WorkPlan`; one dated Work occurrence admitted under `U.Work`; one actual transformation; a local production-work, entity-identity-inception, or production-completion claim; a direct changed-referent relation; a measurement-result or evaluation-result episteme; a `C.11` `ChoiceResult` or decision episteme; an evidence, source, gate, publication, or temporal relation; a delivery or acceptance relation or claim; a selected structure; an `ArchitectureOf@Context` relation; an architecture-description episteme; or another exact governed object named by its direct owner. The A.15 role-method-plan-Work alignment remains a set of separately governed direct relations; it does not merge those values into one object.

When the concern is a relation among methods or method families, recover `MethodRelationStructure@BoundedContext`: serial or parallel composition, guarded choice, iteration, refinement, substitution, decomposition, parameterization, method-family membership, selector relation, fallback relation, or another exact method-side relation. Govern it through `A.3.1`, `G.5`, or its exact direct owner. A graph, algebra, tuple, categorical notation, process calculus, effect calculus, matrix, embedding, distributed notation, or neural notation used to present it is a C.29 representation or mathematical-lens use, not itself a method. Do not name that representation `U.MethodAlgebra`. A description of the relation is a separately governed claim-bearing episteme; `U.MethodDescription` does not widen to a method family, relation structure, mechanism, plan, Work occurrence, transformation, result, architecture, or representation. Do not type one value as both `U.Method` and `U.Mechanism` unless their direct owners independently admit both claims.

The authoring note may record the affected entity, bounded context, change or maintained-condition claim, any current state or delta predicate, the exact objects and relations exposed by the wording, and their direct owners. It is not a project object. If the project needs a method, description episteme, mechanism, plan, Work occurrence, transformation claim, result episteme, evidence or source relation, gate decision, choice result, structure, architecture description, representation, publication relation, or temporal relation, apply that direct pattern and keep each independently governed identity.

Treat `input`, `raw material`, epistemic `source data` or `source material`, `output`, `result`, `outcome`, `deliverable`, `handoff`, and work-name wording as triggers only while their exact relation is hidden. Once clear, bypass E.10.ARCH: use `A.3.2` only for a description episteme about one exact method; `A.15.2` for an intended participant or use in planned work; `A.15.1` and the exact resource or participation owner for a dated Work occurrence; `A.3.4.P` and the direct transformation owner for an actual transformation participant; `A.15.PROD`, the measurement or evaluation owner, or the delivery or acceptance owner for the exact result claim; and `C.29` when the word names only an argument, tuple component, graph element, or other representation place. Use `C.2.P` first for an epistemic source expression and source-to-use relation. Keep physical material under its direct physical governor.

If the exact method/work-boundary relation is still hidden after generic relation recovery, apply `A.6.P.WMR`. Its result remains exactly one family: a positive or governed-negative direct subject-relation claim; an exact `A.6.1` operation-application binding; an exact local `A.15.PROD` or `A.6.RCD` claim; or reason-specific non-assertability as `factually unsupported`, `missing-information`, or `missing-governor`. A failed known predicate such as `EpistemeUsedByReviewWorkAsReference` is `factually unsupported`; an unavailable ETL receiving-use fact under a known governor is `missing-information`; and an absent relation kind and owner for the named `Patient_8472` / `HE-8472` health-effect receiving use is `missing-governor`. Only the last names an affected receiving use and future owner. Classification, a generic result label, a type-correct designation, planned use, or inferred opposite polarity does not close the branch.

Durable naming follows the governed value. `F.18` may name a performed Work occurrence only after its A.15.1 occurrence basis is established, and it names neighboring production, measurement, evaluation, delivery, and acceptance results separately. If a proposed `U.*` name merely repeats a declaration-local `SlotSpec` label or direct-pattern participant meaning, keep it local unless E.24 supplies durable identity, action-facing gain, and the exact governing relation. If repeated method, Work, or process material is proposed as durable ontology, its E.24 ontic decision and, for any public `U.*` kind, `E.24.UK` admission plus the governing head pattern must precede current citation.

