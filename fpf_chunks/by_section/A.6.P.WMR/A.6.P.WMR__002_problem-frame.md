---
chunk_kind: "child"
pattern_id: "A.6.P.WMR"
pattern_title: "Exact Relation Recovery for Method and Work Claims"
section_id: "A.6.P.WMR:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.P.WMR/A.6.P.WMR__002_problem-frame.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.6.P.WMR — Exact Relation Recovery for Method and Work Claims"
  - "A.6.P.WMR:1 — Problem Frame"
line_start: 15635
line_end: 15660
dependencies:
  - "A.15.1"
  - "A.15.1-A.15.3"
  - "A.15.2"
  - "A.15.3"
  - "A.15.PROD"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "A.6.P"
  - "A.6.RCD"
  - "C.2.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.18.1"
  - "F.18"
keywords:
---

### A.6.P.WMR:1 - Problem Frame

**Use this when.** Practitioners **SHOULD** use this pattern after `A.6.P` generic relation recovery has isolated one current method/work-boundary claim and the exact entity is already in view, but words such as `input`, `raw material`, `source data`, `source material`, `output`, `result`, `outcome`, `deliverable`, or `handoff` still do not reveal the direct relation that makes the sentence true. They **SHOULD** also use it when method, intended-work, actual-work, production, evaluation, delivery, acceptance, transfer, or receiving-use wording leaves that claim's participant meaning or orthogonal claim dimensions unclear.

The primary EntityOfConcern is one relation-bearing claim in an episteme. The trigger word helps a practitioner notice the problem; it is not the governed object, a participant kind, a relation kind, or a universal family of inputs and results.

**Primary working reader, concern, and viewpoint.** The primary reader is a practitioner or engineer whose current task is to make one boundary-word claim safe for a named receiving use. Their concern is which exact relation and claim dimensions can be stated safely for that use now; the viewpoint is the receiving use, while the direct subject-pattern owner supplies or rejects any missing governor.

**First useful result.** The first useful result is the shortest ordinary sentence that names:

1. the exact entity under its admitted kind;
2. the exact object relative to which it is being named;
3. the direct relation claim under its selected modality and polarity, or the exact proposed claim still not assertable;
4. the orthogonal claim dimensions; and
5. the direct governor: for a direct relation, the exact `RelationKind` token and its resolving direct pattern or relation-specification edition; for an operation binding or local claim, the exact declaration-local or admitted predicate and owner.

A positive result is available only after two independent premises are present. First, suppose published project relation-specification edition `MFG-WORK-REL-2026` already admits `RelationKind` token `MachiningWorkConsumesResource`, with participant meanings `consumingWork = exact Work individual admitted under U.Work` and `consumedResourceQuantity = exact physical quantity`, required qualifier `Γ_time`, an obtaining predicate requiring actual consumption by that work, applicability to Plant-7 machining work, and accountable owner `MachiningWorkRelations@Plant-7`. Second, separately stipulate the didactic world-side fact that exact quantity `CF-17` was actually consumed by exact work `W-204` during `I-204` and therefore satisfies that obtaining predicate. Neither the specification, the work identity, nor assertion episteme `MFG-RU-CF17-W204` supplies that fact. The useful result can then be as short as: `Cutting-fluid quantity CF-17 was consumed as a resource by machining work W-204 during interval I-204 under RelationKind MachiningWorkConsumesResource from MFG-WORK-REL-2026.` If the governor is known but the separately required fact fails, return `factually unsupported`; if that fact is unavailable, return `missing-information`. If the conforming settlement itself is absent, return instead: `Whether CF-17 participated in W-204 as a consumed resource is unresolved because the direct resource-use governor for that work and material is absent; the machining-work owner is the named future owner for supply, rejection, or reframing of that relation.`

**What changes in practice.** The engineer stops asking which broad word is correct and asks which exact entity, related object, relation, claim subject, modality and temporal extent, polarity, recovery/support state, and governor the receiving work needs. Planning, actual participation, production, evaluation, delivery, acceptance, and transfer no longer inherit one another through vocabulary.

**Adoption test.** Given one compressed sentence, the reader can replace it with either the shortest direct sentence under its exact governor or an exact factually-unsupported, missing-information, or missing-governor result, without turning a plan, description, binding, record, or label into actuality.

**What goes wrong if missed.** A plan is read as actual participation; a method description is treated as a work occurrence; an operation result binding is mistaken for a produced entity; a changed continuing entity becomes a new output; a delivery or handoff package is treated as the transfer; or a convenient missing relation is replaced by a new universal kind.

**Ordinary non-use boundary.** Practitioners **SHOULD NOT** use this pattern when the exact direct relation and all claim dimensions needed by the receiving use are already readable; they **SHOULD** apply that direct pattern and stop. They **SHOULD** use `C.2.P` first when the unresolved question is which source expression, episteme, publication, or source-to-use relation is current; `A.15.PROD` directly when the only current question is production-work participation, entity-identity inception, or production completion and its participants are already exact; and the direct measurement, evaluation, commitment, delivery, acceptance, transfer, resource, premise, transformation, method, planning, or work pattern when that relation is already selected.

