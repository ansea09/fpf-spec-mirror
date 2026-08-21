---
chunk_kind: "child"
pattern_id: "F.1"
pattern_title: "Question-Relative Source Selection"
section_id: "F.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/F.1/F.1__006_archetypal-grounding.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "F.1 — Question-Relative Source Selection"
  - "F.1:5 — Archetypal Grounding"
line_start: 88002
line_end: 88078
dependencies:
  - "A.10"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "F.0.1"
  - "F.0.2"
  - "F.17"
  - "F.9"
keywords:
  - "SourceCutNote"
  - "answer-changing source role"
  - "exact source and edition"
  - "finite source cut"
  - "intended use"
  - "receiving question"
  - "reopen condition"
---

### F.1:5 - Archetypal Grounding

#### F.1:5.1 - Three heterogeneous source cuts

##### F.1:5.1.1 - Role assignment, performed work, sensing, and execution

Candidate sources include BPMN 2.0 (designed workflow structures), PROV-O (performed activities and provenance), ITIL 4 (service vocabulary), ODRL 2.2 (permissions, prohibitions, and duties), SOSA/SSN (observations and results), and IEC 61131-3 (control-program execution). Retain only those whose exact claims change the receiving question.

The cut keeps false friends visible: a BPMN participant is not an RBAC role; a PROV activity is not a BPMN process; an SOSA observation is an act, not a status; an ITIL incident is not automatically a plant fault. F.1 exposes these source roles but does not settle their relations.

##### F.1:5.1.2 - Methods, types, and measurement

SPEM 2.0 or ISO 24744 may change the reading of Method and MethodDescription; OWL 2 and formal concept analysis may change kind reasoning; SOSA/SSN and ISO 80000-1 may change measurement and quantity claims. The cut preserves the source-fixed differences rather than making *method*, *concept*, or *measurement* globally uniform.

##### F.1:5.1.3 - Control, actuation, and services

Control-theory sources, IEC 61131-3, ISA-95, ITIL 4, and SOSA/SSN can contribute different claims about controller design, program execution, integration, service commitments, and observations. A current question may need only a subset. *Actuation* is not a service promise, and *incident* is not a plant fault merely because the words occur near operational work.

#### F.1:5.2 - Minimal worked source cut

The project brief already identifies this receiving question: **Can one contribution use “process” for both a workflow description and a performed occurrence?** The exact question, not the note or source list, is the `SourceCutNote`'s EntityOfConcern. The project names its effective ReferenceScheme **Workflow and occurrence source cut, August 2026**; that scheme fixes the three editions below and the ordinary-English role statements. The intended use stays in the ClaimGraph.

```text
Receiving use: decide which subjects the later pattern must keep distinct.

Retain:
- OMG BPMN 2.0.2 (January 2014), §10.1: its workflow-structure claim changes the design-description side.
- W3C PROV-O Recommendation (30 April 2013), §3.1: its Activity claim supplies the performed-occurrence contrast.
- W3C SOSA/SSN Recommendation (19 October 2017), §4.3.2.2: Observation supplies an action-changing counterexample—an act that follows a Procedure and yields a Result, not a workflow graph.

Exclude for now:
- thermodynamic-process literature: no inspected claim changes this stated use.

Known limit: service commitments are outside this cut.
Reopen if: the use adds physical transformation or service commitments, a relied edition changes the relevant claim, or a known counterexample no longer fits.
Search policy: none needed for this bounded question.
```

The resulting `SourceCutNote` is identified by that ClaimGraph, the stated receiving question, and the named reading scheme. Because this cut turns on the difference between a designed workflow and a performed occurrence, the project recovers any disputed *process* reading through ordinary F.0.1 while inspecting source roles, before stabilizing the cut. It adds an F.17 cell afterward only if later reuse, a claim, a named receiver, or an actual relation needs one.

#### F.1:5.3 - Portable first-hour case — function-to-module allocation

“First hour” means a compact entry slice, not a deadline or completeness claim.

**Receiving question.** Which current FPF sources must a Systems Engineering author use to prepare a first function-to-module allocation teaching slice without collapsing functions into modules? The project identifies this sentence as one exact question before treating the note as a C.2.1 episteme; that question is its EntityOfConcern.

**Receiving use.** Prepare a slice that helps a practitioner generate and compare candidate bearers, modules, allocations, interfaces, and trade-offs instead of copying functions into a component list or selecting familiar bearers first. This use stays in the note's ClaimGraph.

**Effective ReferenceScheme.** `FPFCoreReferenceScheme`, applied to the FPF August 2026 edition and the exact section locators below.

**Retained sources and answer-changing roles.** All five are exact passages in that edition.

1. **A.6.F §§4.2 and 4.5.** Separates the possible subjects hidden by function-like wording and requires function, bearer, flow, module allocation, and interface claims to remain distinct. This blocks the one-function-one-component shortcut.
2. **A.6.M §§4 and 4.3.** Treats module use as claim content over exact holons, allows many-to-many or still-unallocated functional claims, and requires an actual interface specification when compatibility or substitution is claimed. This changes what an allocation row must show.
3. **C.30.TFS-REL §4.2.** Relates functional structure to selected transformation-flow structure without identifying them. This exposes candidate flow topology, crossings, and correspondence limits that can change bearer placement.
4. **C.31 §4.5.** Makes function-module alignment, interface burden, and flow-boundary alignment separate characteristics rather than one modularity score. This changes the trade-offs the comparison must expose.
5. **C.32 §§4–5.** Starts candidate synthesis from functional demand and candidate bearers, keeps materially different configurations visible, and records expected gain, known loss, constraints, and source-return conditions. This prevents the source cut from pretending to choose the architecture.

**Deliberate limits.** The cut claims neither an exhaustive survey of allocation algorithms nor one module taxonomy or cross-sector optimum. It does not decide the final DPF pattern identity. The campaign-specific guide and research-source pilot remains in `FPF-DPF-CLAIM-PLACEMENT-CAMPAIGN/PILOT-SYSTEMS-ENGINEERING-FUNCTION-TO-MODULE-ALLOCATION.md`; it is not a hidden dependency of this portable example.

**First result.** One `SourceCutNote` whose ClaimGraph contains the five roles, use, limits, and reopen conditions; whose EntityOfConcern is the stated question; and whose effective scheme is `FPFCoreReferenceScheme` for FPF August 2026. The later comparison must expose unsupported capabilities, unallocated functions, unresolved interfaces, alternatives, trade-offs, and accepted losses.

**Reopen when.** A relied FPF passage changes, the question expands to external allocation algorithms or another domain, or the intended DPF use changes the required answer or boundary.

#### F.1:5.4 - Readable reasoning moves

- **Retain:** “This exact source stays because this inspected claim changes the answer in this way.”
- **Exclude:** “No inspected claim from this source changes the stated use; record the exclusion and what would reopen it.”
- **Return a gap:** “This unavailable or uninspectable source may be load-bearing; the cut remains limited here.”
- **Keep meanings local:** “Selection puts both sources in view; it does not say their terms are identical or related.”
- **Use search assistance:** “The ranking tells us what to inspect next; the source claim decides whether it enters the cut.”
- **Reopen:** “This question, use, relied claim, rival, counterexample, or transfer boundary changed, so select again.”

#### F.1:5.5 - Didactic distillation

> State and independently identify the question; keep the later use in the claims. Keep a source because an inspected claim can change the answer, expose a rival or counterexample, or mark a transfer limit. Return one finite `SourceCutNote` whose ClaimGraph carries those roles, exclusions, limits, and reopen conditions, whose EntityOfConcern is the exact question, and whose named effective scheme resolves the question and exact editions. Search scores may guide inspection; they do not admit or exclude a source. Stop when additional candidates do not change the answer.

