---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:10"
section_title: "Micro-examples (illustrative, one-liners)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__012_micro-examples-illustrative-one-liners.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:10 — Micro-examples (illustrative, one-liners)"
line_start: 74843
line_end: 74859
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "B.3"
  - "C.16.Q"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:10 - Micro-examples (illustrative, one-liners)

1. **Participant vs Agent (process model vs provenance)**
   *Cells:* `BPMN:Participant` - `PROV:Agent` - *senseFamily:* Role - *Kind:* `Partial-overlap` - *CL:* 2 - *Loss:* participation vs attribution scopes differ - *Use:* **Naming-only** ("actor").

2. **Process (design) vs Activity (run)**
   *Cells:* `BPMN:Process` -> `PROV:Activity` - *senseFamily:* Method / Execution - *Kind:* **Design-spec -> Run-trace** - *CL:* 2 - *Loss:* graph vs event; concurrency vs temporalization - *Use:* **Explanation-only**.

3. **Observation vs SLO check**
   *Cells:* `SOSA:Observation` -> `ITIL:SLO-fulfilment` - *senseFamily:* Measurement / Status - *Kind:* `Measure-of` - *CL:* 2 - *Loss:* sampling window; target definition - *Use:* **Explanation-only**.

4. **Subtype across OWL and curated taxonomy**
   *Cells:* `OWL:SubClassOf` - `TaxonomyX:is-a` - *senseFamily:* Type-structure - *Kind:* `Equivalence` - *CL:* 3 *(only if TaxonomyX is acyclic and anti-symmetric)* - *Loss:* profile differences - *Use:* **Type-structure** rows supported.

5. **Accuracy (metrology vs data-quality)**
   *Cells:* `ISO80000:accuracy` - `ISO25024:accuracy` - *senseFamily:* Measurement - *Kind:* `Partial-overlap` - *CL:* 2 - *Loss:* instrument vs dataset perspective - *Use:* **Naming-only** row -accuracy-; methods stay context-local.

