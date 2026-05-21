---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping (Evidence • Standard • Requirement)"
section_id: "F.10:10"
section_title: "Anti‑patterns & remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__011_anti-patterns-remedies.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "F.10 — Status Families Mapping (Evidence • Standard • Requirement)"
  - "F.10:10 — Anti‑patterns & remedies"
line_start: 64109
line_end: 64125
dependencies:
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:10 - Anti‑patterns & remedies

| #         | Anti‑pattern                                 | Symptom                                                                        | Why it harms reasoning                                                               | Remedy (conceptual move)                                                                                                                                                                                                                       |
| --------- | -------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AP‑1**  | **“Validated ⇒ Approved ⇒ Compliant” chain** | A single word *validated* is treated as proving approval and compliance.       | Collapses **statusModalities** (epistemic → deontic); ignores Targets & Windows.               | Keep **EvidenceStatus** about **claims**, **StandardStatus** about **artefacts/methods**, **RequirementStatus** about **clauses**. Use **two Bridges** (evidence→requirement via interpretation + standard→requirement via policy), never one. |
| **AP‑2**  | **Run‑time proves design‑time**              | A month of logs is cited as “therefore the method is approved.”                | Directional fallacy; design‑time approval is curatorial, not measured.               | Separate **design vs run**. Evidence may justify a **proposal** Bridge to *Approved* only in Contexts where such promotion exists; otherwise keep **explanation‑only**.                                                                           |
| **AP‑3**  | **“Approved model” ⇒ “SLO satisfied”**       | Governance stamp is cast as automatic service compliance.                      | **StandardStatus** does not entail **RequirementStatus**; the latter needs evidence. | Require **EvidenceStatus** on the clause’s **Window**, then apply the **evaluation rule** (Service pattern).                                                                                                                                   |
| **AP‑4**  | **Synonym drift of status labels**           | *Verified/validated/approved* used interchangeably across Contexts.               | Homonymy across Contexts; undercuts claim support.                                               | Treat each status word as a **StatusCell** tied to its Context; relate only via **Bridge(kind, CL, Loss)**.                                                                                                                                       |
| **AP‑5**  | **No Window**                                | Status claimed without time/condition (“Compliant.”).                          | Unfalsifiable; blocks conflict detection.                                            | Every positive/negative status **names a Window**; contradictions checked per Window.                                                                                                                                                          |
| **AP‑6**  | **Double truth**                             | *Satisfied* and *Violated* asserted for same clause silently.                  | Violates mutual exclusivity; hides differing Windows.                                | Force **Window discipline**; if Windows coincide, at least one assertion must retract.                                                                                                                                                         |
| **AP‑7**  | **Substitute by name**                       | “SOSA Observation = ITIL SLO check”.                                           | Cross‑context equality without Loss accounting.                                         | Prefer **explanation Bridges**; allow **substitution** only when **same statusModality**, **kind ∈ {≈,⊑,⊒}**, **CL≥project threshold**, **Windows aligned**.                                                                                            |
| **AP‑8**  | **Evidence escalation without diversity**    | One lab repeats itself and calls it “replicated”.                              | Confuses **repetition** with **independent replication**.                            | In EvidenceStatus, **Replicated** demands **independent** settings/sources; else keep at **Corroborated**.                                                                                                                                     |
| **AP‑9**  | **Clause‑less compliance**                   | “Compliant” with no clause named.                                              | Target missing; cannot evaluate.                                                     | Every RequirementStatus **points to a clause** (Target).                                                                                                                                                                                       |
| **AP‑10** | **Negative erased by summary**               | A later summary lists *Satisfied* but omits earlier *Violated* in same Window. | Cherry‑picks; breaks auditability.                                                   | Apply **Weakest‑link**: within a Window, **negative outranks** prior positives for the same clause.                                                                                                                                            |
| **AP‑11** | **Bridge‑free roll‑up**                      | Cross‑context dashboards aggregate statuses as if native.                         | Hidden Cross‑context semantics; CL unknown.                                             | Each Cross‑context line **must cite Bridges**; roll‑up shows the **effective CL (min)**.                                                                                                                                                          |
| **AP‑12** | **Status explosion**                         | New bespoke statuses minted to match every tool state.                         | Pollutes lexicon; blurs statusModalities.                                                      | Map tool states to the **nearest ladder level** in the local context; keep tool terms as **Naming‑only** where needed.                                                                                                                            |

