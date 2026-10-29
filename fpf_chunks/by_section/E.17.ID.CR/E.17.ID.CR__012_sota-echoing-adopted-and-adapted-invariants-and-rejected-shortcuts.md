---
chunk_kind: "child"
pattern_id: "E.17.ID.CR"
pattern_title: "Compare Sources Within a Shared Review Frame (ComparativeReviewUnit)"
section_id: "E.17.ID.CR:11"
section_title: "SoTA-Echoing: Adopted and Adapted Invariants and Rejected Shortcuts"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.ID.CR/E.17.ID.CR__012_sota-echoing-adopted-and-adapted-invariants-and-rejected-shortcuts.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "E.17.ID.CR — Compare Sources Within a Shared Review Frame (ComparativeReviewUnit)"
  - "E.17.ID.CR:11 — SoTA-Echoing: Adopted and Adapted Invariants and Rejected Shortcuts"
line_start: 108550
line_end: 108564
dependencies:
  - "A.15"
  - "A.15.2"
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

### E.17.ID.CR:11 - SoTA-Echoing: Adopted and Adapted Invariants and Rejected Shortcuts


| Claim need | Source idea and named source | Source scope or reference | Local FPF invariant and practical local test | Nearest recovery reference | Adopted, adapted, or rejected shortcut |
| --- | --- | --- | --- | --- | --- |
| Comparative review units normally stay tied to explicit source, view, and review structure rather than shifting through helpful prose alone. | The official abstract identifies architecture-description concepts and practices; it supplies lineage for keeping the described subject and its views explicit. | Joint ISO, IEC, and IEEE 42010:2022; official abstract only, not a complete standard-conformance basis | This pattern uses that limited lineage. Its source references, comparison criterion and bounded-comparison rules are local FPF design, not requirements established by the inspected abstract. | `E.17.ID.CR:4.3.b.a` rows **Reviewed source**, **Source references**, and **Bounded lift**; `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.a` | **Use limited lineage.** |
| Interpretation and explanation use are use-sensitive and bounded by intended reader and knowledge limits rather than audience-neutral by default. | Explainable-AI guidance distinguishes explanation, meaningfulness for intended users, explanation accuracy, and knowledge limits instead of treating all helpful prose as equally safe. | Phillips et al. (2021), NIST IR 8312, *Four Principles of Explainable Artificial Intelligence*; source status = government guidance on AI explanations (2021) | This pattern adapts that stance into `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `boundedComparativeUse`, and `overreadRisk`, while still keeping explanation-face use discipline with `E.17.EFP`. | `E.17.ID.CR:4.3.d` interpretant-side block, kept subordinate to the ordinary minimum; `E.17.ID.CR:5.4.4`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.b` | **Adopt and adapt.** |
| Static comparative notes and interactive comparative aids carry different relation loads. | Static review notes need source references, comparison criterion, bounded lift, blocked downstream claim or effect, and boundary trigger; interactive explanation-system practice becomes relevant only when the aid is actually interactive, stateful, adaptive, or user-model-bearing. | Labarta et al. (2026), *X-SYS: A Reference Architecture for Interactive Explanation Systems*, arXiv:2602.12748v3; source status = emerging preprint, not settled standard. | This pattern keeps the ordinary minimum sufficient for static notes and adds `targetUserModel`, `interactionMode`, state and history, `overreadRisk`, and bounded-use boundary only for actual interactive comparative aids. | `E.17.ID.CR:4.3.b.a` ordinary card; `E.17.ID.CR:4.3.f` static and interactive split; `E.17.ID.CR:5.4.4`, `E.17.ID.CR:5.4.7` | **Adapt conditionally.** Reject importing XAI architecture into ordinary static notes. |
| Reader plausibility, fidelity to a cited text, and faithfulness to a model decision process answer different questions. | NLP interpretation research distinguishes an explanation that convinces people from one that accurately reflects the model's prediction process; this does not establish fidelity to a cited engineering document. | Jacovi and Goldberg (2020), [*Towards Faithfully Interpretable NLP Systems*](https://aclanthology.org/2020.acl-main.386/), §§1–5; research source about NLP-model interpretation. | This pattern adapts the separation of evaluation questions by analogy. Its ordinary comparison of source claims uses its own explicit source references and comparison criterion, with the source-relation meanings in `E.17:5.1b`; it does not import a model-interpretation test. Further bridge, prompt or authority claims retain their own grounds. | `E.17.ID.CR:4.3.b.a` rows **Source references**, **Bounded lift row(s)**, **Blocked downstream claim or effect** and **World-contact limit**; `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.9`, `E.17.ID.CR:5.4.10`, `E.17.ID.CR:5.4.11` | **Adapt a limited analogy.** Keep the paper's model-process subject distinct from this pattern's source-text comparison. |
| Comparative review units do not become hidden ranking, aggregate recommendation, or false equivalence when a comparison sheet sorts or scores alternatives. | Quality-diversity practice and multi-objective optimization practice preserve diverse candidate sets and non-scalar trade-offs when one scalar score would hide relevant differences. | Mouret and Clune (2015), MAP-Elites; Deb et al. (2002), NSGA-II; source status = adapted design-space analogy, not naming or review standard | This pattern adapts only the anti-scalarization invariant: one comparison sheet can expose row-level comparison criteria, trade-offs, and visible ordering criteria, but it does not add equivalence, substitution, recommendation, method choice, gate passage, or decision authority unless `C.11`, `F.9`, `A.20`, `A.21`, another governing FPF pattern, or a project record named by value supplies that source relation or project record. | `E.17.ID.CR:4.3.b.a` rows **Bounded lift**, **Blocked downstream claim or effect**, and **Boundary trigger**; `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6.e`, `E.17.ID.CR:5.4.6.f` | **Adapt conditionally.** Reject treating optimization vocabulary, Pareto wording, benchmark tables, or sorted display order as proof of a governing FPF relation. |

**Row 1.** The inspected ISO abstract supplies architecture-description lineage, not a rule for comparative review units. This pattern itself requires visible source references and comparison criteria so the reviewer can inspect the contrast. The **Reviewed source**, **Source references** and **Bounded lift** rows carry that local requirement; applying them makes no claim of conformity to the complete standard.

**Row 4.** Jacovi and Goldberg examine whether an interpretation reflects the reasoning behind an NLP model's prediction, separately from whether people find it convincing. A comparative review unit here instead compares claims in available sources under an explicit criterion. Its source-text fidelity follows from comparing what the note says with those sources, keeping their qualifiers, omissions and added contrasts visible under `E.17:5.1b` and this pattern's ordinary working card. A note may reproduce a source accurately while the source's explanation misrepresents a model; a faithful model explanation may also be misquoted in a note. The evaluation question therefore selects what must be checked. Human review of source claims remains useful; this source analogy imposes no NLP-model intervention on an ordinary static comparison. The **Blocked downstream claim or effect** and **World-contact limit** rows keep further bridge, prompt and authority claims subject to their own grounds. This lets an engineer-manager inspect what the comparison actually warrants without giving polished prose authority over the source episteme or publication set. Case linkage: see `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.9`, `E.17.ID.CR:5.4.10`, and `E.17.ID.CR:5.4.11`.

