---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern-Quality Evaluation CharacteristicSpace"
section_id: "E.21:7"
section_title: "Common anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__008_common-anti-patterns-and-repairs.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "E.21 — FPF Pattern-Quality Evaluation CharacteristicSpace"
  - "E.21:7 — Common anti-patterns and repairs"
line_start: 68552
line_end: 68568
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
  - "F.19"
  - "I.2"
keywords:
---

### E.21:7 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **Score illusion.** `Pattern quality = 87/100`. | Use ordinal coordinate values; no arithmetic aggregation. |
| **Two-column table.** Coordinate/value table has no rationale. | Add `ShortRationale` for every coordinate. |
| **Floor as omission.** A floor evaluation omits maturity, SoTA, formal, corpus, or evolution coordinates. | Keep floor low if needed; evaluate all coordinates. |
| **Scope laundering.** A landing-input, corpus-facing, `Stable`, release, or external-review request is reported under an easier use, local-only use, diagnostic pass, or evaluator-selected use. | Re-evaluate under the governing scope; if it fails, return `repairBeforeUse`, `holdForArchitectureDecision`, or `refreshNeeded` with the missed coordinates and repairs. |
| **Administrative proxy.** "4 because landed" or "3 because not externally reviewed". | Evaluate pattern content. |
| **Comparator-free or locus-free maturity.** `MaturePatternParity... = 4` by impression, comparator IDs only, or category list such as "frame, first move, checklist, SoTA, relations". | Name mature comparison patterns and use the maturity-discharge payload: comparator, selected ingredient, current locus, and missing/lowering item. Without that payload, cap at `3`. |
| **Omission account as maturity.** A note explaining absence raises the value. | Add content to body/neighboring pattern governing the claim, lower value, or mark the current request `repairBeforeUse`. |
| **Semio-biased maturity.** Non-semio pattern is judged by episteme/publication exemplars only. | Include non-epistemic mature comparators and score action on the primary `EntityOfConcern`. |
| **Quality-carrier leakage.** Corpus projection, retrieval evidence, README/ToC/E.11/I.2 alignment, monolith parity, `PatternQualityStatus`, developer/reviewer/executor correspondence, or other quality evidence is written anywhere in the pattern as method, problem, note, appendix, relation, rationale, or status content about the pattern. | Move the evidence to the `E.21` result, `E.19` run record, README/ToC/E.11/I.2, card/retrieval/projection carrier, or release/landing evidence carrier; keep only the user move or boundary that the evidence justifies. |
| **Apparatus overwrap.** A simple FPF claim is wrapped in extra role, carrier, locus, flow, state, status, text-state, package, or process words, such as `live pattern text`, `current object`, `active record`, `field when live`, or route-like pattern talk where no real state/use-position is named, so the reader sees a bureaucratic apparatus instead of the object, relation, action, or boundary. | Apply `F.19`; record the scalar effect in `PrecisionRestorationProfile`, then lower the affected coordinates or name the completed repair. |
| **Apparatus maximalism.** Every pattern gets evidence cards, telemetry, archives, and companions. | Keep evidence compact unless it changes value, status, stop, or candidate comparison. |
| **Quality veto theatre.** "Not ready" has no E.21 coordinate named by value, evidence, status effect, and repair. | Rewrite as an `E.21` finding or remove the veto. |

