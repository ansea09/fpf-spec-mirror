---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:14"
section_title: "Rationale (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__016_rationale-informative.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:14 — Rationale (informative)"
line_start: 45505
line_end: 45524
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:14 - Rationale (informative)

**14.1 Why canonical‑first?**
CT2R-LOG treats the **human-readable, task-appropriate relation** (e.g., `ut:ComponentOf`) as the **canonical publication form** because that is what engineers and managers actually use to reason, decide, and communicate. The formal layers **ground** that form; they do not replace it. Authors state the relation readers need, then point to the support required by the selected assurance use.

**14.2 Why distinguish the two `tv:` links?**
`tv:AliasOf` connects designations so a reader can recover which relation an expression names. `tv:groundedBy` connects a covered assertion to the account supporting that assertion. An agreed glossary meaning can remain stable while a component is removed and the earlier construction account ceases to support the current claim. Conversely, a changed glossary can require a new interpretation while the physical assembly stays unchanged. Keeping these subjects distinct tells the author what to re-examine. Both links can be expressed in prose or another suitable notation.

**14.3 Why a triad of `validationMode`?**
The triad **{postulate, inferential, axiomatic}** distinguishes permitted justification postures, not stages of formality or increasing confidence. The direct relation kind and elected profile determine which posture and support are appropriate for the receiving claim and use. A sufficient calibration account in a branch permitting `postulate` needs no mode promotion; an elected structural-parthood or collection-belonging claim still requires its respective current construction trace. Where a load-bearing claim needs stronger proof or an empirical check, select that contribution for the assurance gap it can resolve, not to advance through the three labels. The mode declaration changes neither the canonical relation nor the strength of its support.

**14.4 Why recover parthood independently of order and time?**
Order and temporal coverage answer different questions from parthood. A chronology or diagram supplies no part relation by itself. A.15.1 can independently establish a Work temporal part, and A.14 a proper temporal phase of an unchanged non-Work carrier. Preserve those relations alongside the applicable Method and temporal claims; B.1.4 aggregates only the relations already recovered.

**14.5 Why point to `Γ_m.sum | set | slice` (Compose‑CAL) for constructive grounding?**
The three C.13 forms—**sum, set, slice**—are sufficient to report the recurring construction accounts for integrated assemblies, collections, aspects and measured portions without expanding the kernel. They are not identity functions. A truthful account carries exact participants, direct relation occurrences, the applicable rule, and identity or reidentification conditions: the same inputs under another assembly can form another whole, while a permitted replacement can preserve one whole.

**14.6 Why mental obligations rather than process mandates?**
These obligations govern how a relation claim is justified and published: declare a permitted mode for an elected profile, supply the branch's required support, and keep order and temporal claims distinct from parthood. A tool can help inspect that account; its successful execution does not replace the relation's grounds. The requirements concern the claim's justification, not attainment of an axiomatic strength level.

