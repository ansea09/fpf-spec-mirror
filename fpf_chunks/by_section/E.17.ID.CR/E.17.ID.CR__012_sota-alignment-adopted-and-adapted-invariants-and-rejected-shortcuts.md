---
chunk_kind: "child"
pattern_id: "E.17.ID.CR"
pattern_title: "ComparativeReading — bounded comparative reading over comparative review units"
section_id: "E.17.ID.CR:11"
section_title: "SoTA Alignment: Adopted And Adapted Invariants And Rejected Shortcuts"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.ID.CR/E.17.ID.CR__012_sota-alignment-adopted-and-adapted-invariants-and-rejected-shortcuts.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "E.17.ID.CR — ComparativeReading — bounded comparative reading over comparative review units"
  - "E.17.ID.CR:11 — SoTA Alignment: Adopted And Adapted Invariants And Rejected Shortcuts"
line_start: 64648
line_end: 64672
dependencies:
  - "A.15"
  - "A.15.4"
  - "A.16.0"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.9"
  - "A.6.P"
  - "B.5.2"
  - "B.5.2.0"
  - "C.11"
  - "C.2.2a"
  - "E.14"
  - "E.17.AUD.LHR"
  - "E.17.AUD.OOTD"
  - "E.17.EFP"
  - "F.9"
  - "F.9.1"
keywords:
---

### E.17.ID.CR:11 - SoTA Alignment: Adopted And Adapted Invariants And Rejected Shortcuts

**SoTA alignment rule.** Read each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and Relations of this pattern.
**Assurance recovery note.** Read each row here as a heavier confirmation of one already-declared ComparativeReading governing rule. If a row cannot be recovered through the ordinary card, the interpretant-side block, the quick boundary corridor, or the nearest worked slices, do not let the citation carry the pattern by itself.

**Traditions covered.** This pattern binds itself to architecture-description governance, explainable-AI review discipline, interactive explanation-system practice, and design-space anti-scalarization practice. These rows are selected because they discipline recurrent review work in the problem-owning domains named in the case bank; they are not a decorative literature collage added after the governing pattern was chosen.

| Claim need | Source idea and current source | Current source section or reference | Local FPF invariant and practical local test | Nearest recovery reference | Adopted, adapted, or rejected shortcut |
| --- | --- | --- | --- | --- | --- |
| Comparative review units should stay tied to explicit source, view, and review structure rather than shifting through helpful prose alone. | Architecture-description practice treats views, viewpoints, and comparison units as explicit review targets rather than letting reader-help prose replace structural review. | Joint ISO, IEC, and IEEE 42010:2022; source maturity = mature standard | This pattern adopts explicit source references, declared comparison basis, and explicit boundary rules instead of letting comparative fluency define the case. | `E.17.ID.CR:4.3.b.a` rows **Reviewed source**, **Source references**, and **Bounded lift**; `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.a` | **Adopt.** |
| Interpretation and explanation use are use-sensitive and bounded by intended reader and knowledge limits rather than audience-neutral by default. | Explainable-AI guidance distinguishes explanation, meaningfulness for intended users, explanation accuracy, and knowledge limits instead of treating all helpful prose as equally safe. | Phillips et al. (2021), NIST IR 8312, *Four Principles of Explainable Artificial Intelligence*; source maturity = current government guidance | This pattern adapts that stance into `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `allowedUse`, and `misuseRisk`, while still keeping explanation-face use discipline with `E.17.EFP`. | `E.17.ID.CR:4.3.d` interpretant-side block, kept subordinate to the ordinary card; `E.17.ID.CR:5.4.4`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.b` | **Adopt and adapt.** |
| Static comparative notes and interactive comparative aids must not carry the same relation load. | Static review notes need source references, comparison basis, bounded lift, unsupported downstream claim or effect, and boundary trigger; interactive explanation-system practice becomes relevant only when the aid is actually interactive, stateful, adaptive, or user-model-bearing. | Labarta et al. (2026), *X-SYS: A Reference Architecture for Interactive Explanation Systems*, arXiv:2602.12748v3; source maturity = emerging preprint, not settled standard. | This pattern keeps the ordinary seven-row card sufficient for static notes and adds `targetUserModel`, `interactionMode`, state and history, `misuseRisk`, and admissible-use boundary only for actual interactive comparative aids. | `E.17.ID.CR:4.3.b.a` ordinary card; `E.17.ID.CR:4.3.f` static and interactive split; `E.17.ID.CR:5.4.4`, `E.17.ID.CR:5.4.7` | **Adapt conditionally.** Reject importing XAI architecture into ordinary static notes. |
| Faithful source relation is not the same as merely plausible or persuasive prose. | Current interpretation research distinguishes faithful source relation from attractive but low-source-relation narrative, especially in explanation-like publication. | Jacovi and Goldberg (2020), *Towards Faithfully Interpretable NLP Systems*; source maturity = research paper as source for evaluation use | This pattern adopts explicit source references, `E.17:5.1b` source-relation class when live, unsupported downstream claim or effect, and bridge-claim visibility so that bounded comparative reading is not over-read as source relation or governing-pattern authority it does not carry. | `E.17.ID.CR:4.3.b.a` rows **Unsupported downstream claim or effect** and **World-contact limit**; `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.9`, `E.17.ID.CR:5.4.10`, `E.17.ID.CR:5.4.11` | **Adopt.** |
| Comparative review units must not become hidden ranking, aggregate recommendation, or false equivalence when a comparison sheet sorts or scores alternatives. | Quality-diversity practice and multi-objective optimization practice preserve diverse candidate sets and non-scalar trade-offs when one scalar score would hide relevant differences. | Mouret and Clune (2015), MAP-Elites; Deb et al. (2002), NSGA-II; source maturity = adapted design-space analogy, not naming or review standard | This pattern adapts only the anti-scalarization invariant: one comparison sheet may expose row-level comparison bases, trade-offs, and visible ordering bases, but it must not add equivalence, substitution, recommendation, method choice, gate passage, or decision authority unless `C.11`, `F.9`, `A.20`, `A.21`, another exact FPF pattern, or an exact project record supplies that exact source relation or project record. | `E.17.ID.CR:4.3.b.a` rows **Bounded lift**, **Unsupported downstream claim or effect**, and **Boundary trigger**; `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6.e`, `E.17.ID.CR:5.4.6.f` | **Adapt conditionally.** Reject treating optimization vocabulary, Pareto wording, benchmark tables, or sorted display order as proof of a governing FPF relation. |

**Row 1.** The ISO row matters because this pattern is governing reviewable comparative units, not free comparative commentary. The pattern adopts the explicit-structure lesson directly: comparison basis, source references, and boundary rules must stay visible enough that a reviewer is not forced to infer the real comparison question from tone alone. Ordinary recovery: read the **Reviewed source**, **Source references**, and **Bounded lift** rows together before leaning on the citation. Engineer-manager payoff: a comparison note can help a review meeting move faster without being mistaken for a free-form equivalence judgement. Case linkage: see `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6`, and `E.17.ID.CR:5.4.6.a`.

**Row 2.** The NIST row matters because this pattern is not really audience-neutral even when the review unit looks small. The pattern therefore adapts user-meaningfulness and knowledge-limit practice into explicit interpretant-side fields, while rejecting any move that would let those fields replace source or pattern discipline. Assurance recovery: keep those fields subordinate to the ordinary card and unsupported downstream claim or effect rather than letting them stand alone. Engineer-manager payoff: the note can be written for a real audience and task without pretending it is safe for every audience and every downstream use. Case linkage: see `E.17.ID.CR:5.4.4`, `E.17.ID.CR:5.4.6`, and `E.17.ID.CR:5.4.6.b`.

**Row 3.** The interactive-system row matters because bounded comparative aids can become more directive than static prose without crossing into a full new governing pattern of their own. The pattern adapts only the minimal architectural lesson it needs: if interaction mode is load-bearing, that fact must be explicit and must still stop before prompt, ontology, or authority escalation. Assurance recovery: read that pressure through the interaction fields plus the prompt and authority boundary rows rather than treating the source citation as a licence for action selection, coaching, prompt selection, approval, or other downstream guidance. Engineer-manager payoff: a guided comparative UI can stay useful for review without silently becoming coaching, prompt selection, action selection, or approval machinery. Case linkage: see `E.17.ID.CR:5.4.4` and `E.17.ID.CR:5.4.7`.

**Row 4.** The faithfulness row matters because a comparative review unit can sound careful while still smuggling bridge, prompt, or authority claims. The pattern adopts the demand for explicit grounding, but rejects any shortcut where plausible comparative prose is treated as if it were already a semantic or operational licence. Ordinary recovery: use the **Unsupported downstream claim or effect** and **World-contact limit** rows before letting polished prose win the argument by tone. Engineer-manager payoff: polished prose is no longer enough to overrule the underlying source episteme or source publication set or to sneak in a decision claim. Case linkage: see `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.9`, `E.17.ID.CR:5.4.10`, and `E.17.ID.CR:5.4.11`.

**Row 5.** The anti-scalarization row matters because a comparison sheet often becomes a ranking by layout, sort order, or score aggregation before anyone states a decision. The pattern adapts only the design-space lesson it can honestly use: keep non-scalar trade-offs, row-level comparison bases, and visible ordering bases inspectable. It rejects any move where a benchmark table, Pareto label, or sorted order becomes equivalence, recommendation, method choice, gate passage, or decision authority. Ordinary recovery: read **Bounded lift**, **Unsupported downstream claim or effect**, and **Boundary trigger** before accepting any ordering as more than a review aid. Engineer-manager payoff: the team can compare alternatives without a quiet scalar score deciding the work. Case linkage: see `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6.e`, and `E.17.ID.CR:5.4.6.f`.

