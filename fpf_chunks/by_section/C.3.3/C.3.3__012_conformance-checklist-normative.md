---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge & CL^k — Cross‑context Mapping of Kinds"
section_id: "C.3.3:11"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__012_conformance-checklist-normative.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "C.3.3 — KindBridge & CL^k — Cross‑context Mapping of Kinds"
  - "C.3.3:11 — Conformance Checklist (normative)"
line_start: 45322
line_end: 45345
dependencies:
  - "A.2.6"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
  - "F.9"
keywords:
  - "CL^k"
  - "KindBridge direct relation"
  - "R penalty"
  - "bridge assertion episteme"
  - "loss"
  - "target judgment"
---

### C.3.3:11 - Conformance Checklist (normative)

| ID | Requirement |
| --- | --- |
| **KB-01** | One obtaining KindBridge relation has exact source-kind and target-kind participants; signatures, assertions, evidence, CL, loss notes, and slices are not participants. |
| **KB-02** | A KindBridge does not map Scope; USM owns scope translation and its separate bridge occurrence. |
| **KB-03** | Participants, direction, source/target scheme editions, obtaining predicate, definedness, and participant-plus-scheme occurrence identity are recoverable; signature, mapping-rule, assertion, card, row, and publication editions remain separate epistemic objects and trigger reevaluation rather than automatic relation reidentification. |
| **KB-04** | Target classification is the exact four-input C.3.2 judgment under fixed inputs; a source result is not target truth and `unknown` remains distinct from guard refusal. |
| **KB-05** | A preservation assertion names the exact source order fact, both mapped target kinds and their obtaining KindBridge relations, and the target `SubkindOfObtains` fact; an `R_sub` designator appears only for an occurrence-consuming use. |
| **KB-06** | A bridge assertion does not claim preservation when target order inverts the source relation; inversion is non-preservation with loss, while unsettled target order remains `unknown`. |
| **KB-07** | Collapses designate the affected source order relations and lost properties without rewriting either local order. |
| **KB-08** | `CL^k` is an assessment in the bridge assertion, labeled kind-congruence; neither it nor the relation alters KindAT. |
| **KB-09** | Reliance on the bridge and target judgment applies `Ψ(CL^k)` to R only; F, G, and judgment truth are unchanged. |
| **KB-10** | Chained reliance uses the weakest `CL^k` assessment while keeping each bridge occurrence and assertion distinct. |
| **KB-11** | Loss notes state non-preserved signature invariants and subkind relations and do not change the kinds. |
| **KB-12** | Bridge definedness is explicit; outside it the guard declines that bridge use while the independent target judgment keeps its own value. |

**Integration requirements with Part B (bridges):**

* **B-P1.** Part B (Bridges) SHALL distinguish the kind channel—reliance on an obtaining C.3.3 `KindBridge` direct relation plus its separate bridge assertion—from USM scope and F.9 sense-Bridge channels. A Bridge Card or bridge-class row does not become the `KindBridge` occurrence.
* **B‑P2.** Part B **SHALL** state that **`CL^k` penalties route to R** via a monotone **Ψ**, never to **F/G**.
* **B‑P3.** Part B **SHALL** define **chaining = min** for both **CL** and **`CL^k`** (weakest‑link).
* **Templates.** ESG/Method templates should expose references to the exact relied-on Scope-Bridge and `KindBridge` relation/assertion pairs. `CL`, `CL^k`, loss notes, and definedness remain assertion or assessment content; template fields neither create nor identify the world-side relation by record identity.

