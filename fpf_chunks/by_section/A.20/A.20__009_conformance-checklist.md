---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "U.Flow.ConstraintValidity — Eulerian"
section_id: "A.20:7"
section_title: "Conformance Checklist  ✱"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__009_conformance-checklist.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "A.20 — U.Flow.ConstraintValidity — Eulerian"
  - "A.20:7 — Conformance Checklist  ✱"
line_start: 27900
line_end: 27932
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "E.TGA"
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
  - "TransductionFlow"
  - "flow"
---

### A.20:7 - Conformance Checklist  ✱

**Conformance use.** This checklist is evidence for the internal-step CV guidance already stated in the Solution. It is not the first entry text for ordinary use and not a full audit regime by default; an item is applied only when its corresponding CV class, witness, publication face, or neighboring relation is live. Before applying any item, name the Solution move it tests; if no such reader move is live, treat the item as orientation-only or not applicable rather than expanding the applied assurance or conformance material.

**Conformance groups.** Ordinary CV use starts with step, applicable CV class, `CV.Status`, and witness or refusal. Crossing/launch items apply only when a CV-checked step is adjacent to a live gate, crossing, or launch boundary. Publication/assurance items apply only when the CV result is carried on MVPK faces or consumed by downstream replay/audit. Extension/change items apply only when species binding, valuation/refresh, or neighboring selector/comparator loci are being changed or consumed.

**Static lint (graph and faces)**

* CC‑TGA‑01: only `U.Transfer` edges; crossings appear only on gates.
* CC‑TGA‑05: `⟨L,P,E⃗,D⟩` unchanged across raw transfers.
* CC‑TGA‑09: MVPK faces present; edition & Γ pins where expected; no new numeric claims on faces (E.17).

**CV discipline**

 * CV classes present exactly as {UnitsCoherence, LawSetInvariants, Admissibility, LipschitzBounds, TypeDomainRange}; **plus** `ReinterpretationEquivalence` when the node kind is `StructuralReinterpretation`. None declare/translate planes/comparators.
 * **Open‑world species.** Any node **species** binds to one of the minimal kinds; adding a new **kind** is out of scope for A.20 and belongs in an E.TGA update.
* Aggregated **CV.Status** computed; errors/timeouts imply `CV.Status != pass`.
* Any wider use beyond the local step names the receiving relation. `CV.Status` is not gate passage, release confidence, assurance, safety acceptance, work occurrence, or work authorization.

**Gate coupling**

* CC‑TGA‑07: when **`CV.Status != pass`**, all GateFit checks report **abstain**.
* CC‑TGA‑23: SquareLaw witnesses present on crossings adjacent to CV‑checked steps.
* Any edition citation on faces includes `Bridge+UTS` through `F.9`, `F.17`, `E.17`, and `E.18`; comparator or set-return implications use `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, or `G.11` when live.

**UNM declaration locus**

* CC‑TGA‑24: `CG‑Spec`, `ComparatorSet`, and `TransportRegistryΦ` declarations are governed by UNM; CV is ref‑only.

**Valuation & refresh**

* CC‑TGA‑18/19: Flow publishes valuation with `PublicationScopeId`/`PathSliceId`; Γ pinned at compare and launch faces; sentinel triggers slice‑local refresh.

