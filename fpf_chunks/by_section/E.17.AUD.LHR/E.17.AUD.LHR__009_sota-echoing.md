---
chunk_kind: "child"
pattern_id: "E.17.AUD.LHR"
pattern_title: "PublicationUnit Stability Discipline and Local Head Restoration - repair the overloaded local lexical head before the publication unit inherits it"
section_id: "E.17.AUD.LHR:8"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD.LHR/E.17.AUD.LHR__009_sota-echoing.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "E.17.AUD.LHR — PublicationUnit Stability Discipline and Local Head Restoration - repair the overloaded local lexical head before the publication unit inherits it"
  - "E.17.AUD.LHR:8 — SoTA-Echoing"
line_start: 59162
line_end: 59176
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "E.10"
  - "E.10.SEMIO"
  - "E.14"
  - "E.17.AUD"
  - "E.17.AUD.OOTD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "F.18"
keywords:
---

### E.17.AUD.LHR:8 - SoTA-Echoing

**Assurance-recovery note.** Use these rows only after the ordinary five-row card, the local-repair threshold, and the nearest worked slices already tell you which repair disposition is primary. Each row must recover back into the same local question, repair disposition, or safeguard; if a citation starts carrying the case by itself, recover the ordinary card first.

| Claim this pattern needs | Relevant practice | Primary source | Practitioner implication here | Popular shortcut rejected | Nearest recovery section | Adoption status |
| --- | --- | --- | --- | --- | --- | --- |
| One overloaded word should not silently switch concerns, viewpoints, or object readings inside one publication unit. | Architecture-description practice treats explicit concerns and consistency across descriptions as first-class obligations. | Joint ISO, IEC, and IEEE 42010:2022 | In `E.17.AUD.LHR:5.2` and `E.17.AUD.LHR:5.5`, repair the local lexical head by making explicit whether the sentence names a publication unit, a governed object, or outside work before later sentences inherit the wrong local reading. | Reject the shortcut that a familiar word can carry several concerns merely because the surrounding document feels coherent. | `E.17.AUD.LHR:3.2 Rows 2-4`; `E.17.AUD.LHR:5.2`; `E.17.AUD.LHR:5.5` | **Adopt and adapt.** Adopt viewpoint accountability; adapt it to one overloaded local lexical head inside one publication unit. |
| One local lexical head should not be repaired by synonym taste alone. | Terminology work separates designation, concept, definition, and term-formation practice. | ISO 704:2022 and ISO 1087:2019 | In `E.17.AUD.LHR:5.1` and `E.17.AUD.LHR:5.3`, repair the local head by naming the FPF kind or locally declared head it designates here, without importing an ISO concept system as FPF ontology. | Reject synonym substitution, dictionary taste, and global vocabulary rows as local head restoration. | `E.17.AUD.LHR:3.2 Rows 1-3`; `E.17.AUD.LHR:5.1`; `E.17.AUD.LHR:5.3` | **Adapt lightly.** Use designation discipline, not a new global vocabulary. |
| The common sense of a word is not enough when the local context points to a rarer or narrower reading. | Word-sense disambiguation practice treats sense recovery as context-sensitive; long-tail WSD work shows why common-sense defaulting fails. | Blevins and Zettlemoyer (2020); Blevins et al. (2021); source maturity = analogy-only support | In `E.17.AUD.LHR:5.2` and `E.17.AUD.LHR:5.4`, do not assume that `review`, `interpretation`, `text`, or `document` has its common local reading when the FPF context selects a narrower kind or neighboring pattern. | Reject common-usage defaulting as proof that the local FPF sense has been recovered. | `E.17.AUD.LHR:3.2 Row 2`; `E.17.AUD.LHR:5.2`; `E.17.AUD.LHR:5.4` | **Adapt as analogy.** Do not import machine-learning benchmarks as authoring rules. |
| Human-readable local heads should improve comprehension rather than merely sound tidy. | Identifier and label clarity practice treats names as comprehension aids whose bad choices can mislead readers. | Hofmeister et al. (2017), identifier-name comprehension study; source maturity = empirical analogy only | In `E.17.AUD.LHR:5.1` and `E.17.AUD.LHR:5.6`, choose the lightest local head that lets the reader recover kind, active local reading, governed object, move, and outside work. | Reject a nicer label when it changes kind, scope, authority, or downstream use. | `E.17.AUD.LHR:3.2`; `E.17.AUD.LHR:5.1`; `E.17.AUD.LHR:5.6` | **Adapt lightly.** Use clarity to aid local repair, not to justify renaming stable FPF heads. |
| A working pattern should make the first useful move teachable and critique-ready, not merely correct in hindsight. | Pattern-writing practice emphasizes clear template usage, concrete consequences, and critique-ready worked guidance. | Iba (2021), “How to Write Patterns …” (PLoP 2021) | The ordinary card and worked slices are here so a practitioner can repair one overloaded local lexical head in `E.17.AUD.LHR:5.1` or `E.17.AUD.LHR:5.4` without opening publication-unit discipline too early. | Reject a skeleton-only pattern that leaves the actual local repair move to reviewer intuition. | `E.17.AUD.LHR:3.2`; `E.17.AUD.LHR:5.1`; `E.17.AUD.LHR:5.4` | **Adopt.** Keep the move teachable through one small card plus concrete slices. |
| Review quality improves when criteria are explicit instead of left to taste. | Pattern-validation practice pushes toward explicit criteria and documented review checks. | Riehle et al. (2020), “Pattern Discovery and Validation Using Scientific Research Methods”. | The local-repair threshold and the three repair dispositions keep review from collapsing into style debate: see `E.17.AUD.LHR:5.2` for stay-local, `E.17.AUD.LHR:5.4` for return-to, and `E.17.AUD.LHR:5.5` for apply the governing pattern. | Reject style-debate closure when the repair disposition is still not named. | local-repair threshold; `E.17.AUD.LHR:3.2 Row 5`; `E.17.AUD.LHR:5.2`; `E.17.AUD.LHR:5.4`; `E.17.AUD.LHR:5.5`; `E.17.AUD.LHR:5.6` | **Adopt.** Keep the criteria lightweight but explicit. |

Read `E.17.AUD.LHR:6 - Boundary dispositions` through this table only after the repair disposition is already visible by value. The citations do not choose the repair disposition for you; they discipline why the already-recovered repair disposition is reviewable and teachable.

