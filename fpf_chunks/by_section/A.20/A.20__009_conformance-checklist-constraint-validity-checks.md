---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Flow Constraint Validity — Eulerian"
section_id: "A.20:7"
section_title: "Conformance Checklist - Constraint-validity checks"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__009_conformance-checklist-constraint-validity-checks.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "A.20 — Flow Constraint Validity — Eulerian"
  - "A.20:7 — Conformance Checklist - Constraint-validity checks"
line_start: 33804
line_end: 33836
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
  - "ConstraintValidity"
  - "Eulerian"
  - "GateFit"
  - "MVPK"
  - "PathSlice"
  - "Sentinel"
  - "SquareLaw"
  - "TransformationFlowStructure"
  - "flow"
---

### A.20:7 - Conformance Checklist - Constraint-validity checks

**Conformance use.** This checklist is evidence for the internal-step CV guidance already stated in the Solution. It is not the first entry text for ordinary use and not a full audit regime by default; a checklist row is applied only when its corresponding CV class, witness, publication face, or neighboring relation is present. Before applying any row, name the Solution guidance it tests; if no such Solution guidance is present, treat the row as orientation-only or not applicable rather than expanding the applied assurance or conformance material.

**Conformance groups.** Ordinary CV use starts with step, applicable CV class, `CV.Status`, and witness or refusal. Crossing and launch rows apply only when a CV-checked step is adjacent to a present gate, crossing, or launch boundary. Publication and assurance rows apply only when the CV result is carried on MVPK faces or consumed by replay or audit. Extension and change rows apply only when species binding, valuation, refresh, or neighboring selector and comparator loci are being changed or consumed.

**Static lint (graph and faces)**

* CC-TFS‑01: only `U.Transfer` edges; crossings appear only on gates.
* CC-TFS‑05: `⟨L,P,E⃗,D⟩` unchanged across raw transfers.
* CC-TFS‑09: MVPK faces present; edition & Γ pins where expected; no new numeric claims on faces (E.17).

**CV discipline**

* Required CV classes here: {UnitsCoherence, LawSetInvariants, Admissibility, LipschitzBounds, TypeDomainRange}; **plus** `ReinterpretationEquivalence` when the locus kind is `StructuralReinterpretation`. None declare or translate planes or comparators.
* **Open‑world species.** Any locus **species** binds to one of the minimal kinds; adding a new **locus kind** is out of scope for A.20 and belongs in an `E.18` locus-baseline update.
* Aggregated **CV.Status** computed; errors or timeouts imply `CV.Status != pass`.
* Any wider use beyond the local step names the governing neighboring relation. `CV.Status` is not gate passage, release confidence, assurance, safety acceptance, work occurrence, or work authorization.

**Gate coupling**

* CC-TFS‑07: when **`CV.Status != pass`**, all GateFit checks report **abstain**.
* CC-TFS‑23: SquareLaw witnesses present on crossings adjacent to CV‑checked steps.
* Any edition citation on faces includes `Bridge+UTS` through `F.9`, `F.17`, `E.17`, and `E.18`; comparator or set-return implications use `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, or `G.11` when those claims are present.

**UNM declaration locus**

* CC-TFS‑24: `CG‑Spec`, `ComparatorSet`, and `TransportRegistryΦ` declarations are governed by UNM; CV is ref‑only.

**Valuation & refresh**

* CC-TFS‑18 and CC-TFS‑19: Flow publishes valuation with `PublicationScopeId` and `PathSliceId`; Γ pinned at compare and launch faces; sentinel triggers slice‑local refresh.

