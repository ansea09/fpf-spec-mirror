---
chunk_kind: "child"
pattern_id: "F.3"
pattern_title: "Source-Local Sense Clustering"
section_id: "F.3:6"
section_title: "Solution — how to think about clustering"
source_path: "FPF-Spec.md"
output_path: "by_section/F.3/F.3__007_solution-how-to-think-about-clustering.md"
commit_sha: "b223469ecafb9735c1d9bac220671e3336618339"
heading_path:
  - "F.3 — Source-Local Sense Clustering"
  - "F.3:6 — Solution — how to think about clustering"
line_start: 119313
line_end: 119344
dependencies:
  - "A.11"
  - "A.7"
  - "E.10.D1"
  - "F.1"
  - "F.17"
  - "F.2"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "LocalSenseClaim"
  - "alias consolidation"
  - "counterexample"
  - "effective ReferenceScheme"
  - "optional SchemeSenseCell"
  - "source expression"
---

### F.3:6 - Solution — how to think about clustering

#### F.3:6.1 - Consolidate source-blessed aliases

If spelling variants, abbreviations, or explicit synonyms are interchangeable in the relevant passages and do not change a conclusion, let one LocalSenseClaim cover them.

*Example:* ITIL’s *service-level objective* and *SLO* may support one local claim when the cited edition uses them interchangeably.

#### F.3:6.2 - Split incompatible argument patterns

Split when the same head takes materially different participants or occupies a different place in the source’s propositions.

*Example:* a BPMN *event* as a diagram node is not an outage occurrence merely because a tutorial uses the same word narratively.

#### F.3:6.3 - Split divergent entailments

If one use entails occurrence in time and another entails a design structure or capability, the uses support different claims.

*Example:* a PROV *activity* is a time-bounded occurrence; that claim does not describe a static algorithmic capability.

#### F.3:6.4 - Prefer the coarsest adequate partition

Merge candidates when the recovered source uses establish that they are interchangeable for the receiving question and preserve every relevant conclusion. A failed attempt to find a distinction is insufficient when the source basis is too weak to decide. Keep that uncertainty explicit. Split when a concrete counterexample would otherwise be admitted; do not split merely to fill a taxonomy.

#### F.3:6.5 - Keep labels honest

When the receiving use needs an additional label, keep the Tech designation in the source’s idiom. Add a Plain designation for a stated didactic use, explaining the same claim. Neither label is the value being described, and neither may widen the claim.

#### F.3:6.6 - Address only when needed

Ordinary prose may cite the source, expression, and claim directly. Create an F.17 cell when reuse, comparison or traceability needs a stable address for the local meaning.

