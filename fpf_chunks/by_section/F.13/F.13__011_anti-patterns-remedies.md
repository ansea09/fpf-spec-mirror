---
chunk_kind: "child"
pattern_id: "F.13"
pattern_title: "Lexical Continuity & Deprecation"
section_id: "F.13:10"
section_title: "Anti‑patterns & remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/F.13/F.13__011_anti-patterns-remedies.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "F.13 — Lexical Continuity & Deprecation"
  - "F.13:10 — Anti‑patterns & remedies"
line_start: 130695
line_end: 130711
dependencies:
  - "F.1"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "deprecation"
  - "historical reading"
  - "lexical continuity"
  - "local aliases"
  - "renaming labels"
  - "retirement"
  - "splitting and merging labels"
---

### F.13:10 - Anti‑patterns & remedies

| #       | Anti‑pattern               | Symptom in texts                                                      | Why it harms thinking                                          | Remedy (conceptual move)                                                                                                         |
| ------- | -------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Cross‑context rename**      | “Let’s rename *process (BPMN)* to *activity (PROV)*.”                 | Erases Context boundaries; hides loss; violates locality.         | **Do not rename across semantic contexts.** Keep both labels; test any needed F.9 relation and its bounded-use claim with current reliance. CL remains optional.              |
| **A2**  | **Retroactive rewrite**    | Old passages silently updated to new names.                           | Breaks provenance; misleads readers about what was meant then. | **Non‑retroactivity.** Past texts stand; add **read‑paths** via `renames/aliases`; attach **epoch notes** when helpful.          |
| **A3** | **Alias flood** | Long lists of unused synonyms. | Obscures the preferred current designation. | Keep the main presentation economical and preserve the historical aliases needed to recover actual uses. |
| **A4**  | **Paint‑over rename**      | Rename used where the sense changed.                             | Confuses continuity with revision; hides splits.               | Recover the changed meaning under its subject rule, preserve the earlier claim, then settle the later name. Split or merge only when those relations hold.                |
| **A5**  | **Global alias**           | One catchy word reused as alias in several Contexts.                     | Creates a pseudo‑global dictionary; invites category errors.   | **Local aliases only.** Recover each local meaning and keep aliases within one exact naming use. Use F.9 only for a needed semantic correspondence.                  |
| **A6**  | **Euphemism treadmill**    | Frequent cosmetic renames (“modernising” labels) with no gain.        | Cognitive noise; readers lose confidence in names.             | Apply the **Same‑sense test**. If gain is marginal, **do nothing**; if clarity improves materially, one **`renames`** is enough. |
| **A7**  | **Grandfather everything** | Never deprecate confusing legacy labels.                              | Drags ambiguity forward; blocks sharper distinctions.          | When a label misleads and has no single successor, **`retires`** with a short **pointer note** to Contexts/rows.              |
| **A8**  | **Row drift via rename**   | Concept‑Set row is relabeled while its membership silently changes.   | Hides that the set changed; breaks Cross‑context alignment.       | Recover the changed F.7 comparison content and its earlier/later displays. Rename only when the displayed comparison and receiving use are unchanged; split or merge only when warranted.                             |
| **A9**  | **Bridge‑by‑alias**        | Using an alias to hint two Contexts are “the same.”                      | Asserts correspondence without testing the meanings or proposed use.                          | **No Cross‑context aliasing.** If similarity matters, test the proposed **Bridge** under F.9 and state the result. Keep the labels separate.                         |
| **A10** | **Acronym absolutism**     | Treating acronyms as preferred labels everywhere (“SLO” in any Context). | Obscures Context‑specific senses; hurts didactics.                | Choose the preferred designation for this naming use under F.5. Use the expansion when it helps readers recognize the meaning, and retain the acronym as a local alias when readers need it.            |
| **A11** | **Temporal fudge**         | Rename used to imply design↔run shift (“execution ≈ process”).        | Conflates time stances; erases important dualities.            | State the design/run meaning in labels or glosses. Use F.9 only for a needed semantic correspondence; direct design-to-run relations keep their subject patterns.                                       |
| **A12** | **Over‑canonicalisation**  | Forcing a single “perfect” label across all rows/Contexts.               | Centralises language; breaks heterogeneity guard.              | Let each Context/row keep its **own preferred label**; put unification pressure only into **rows** and **Bridges**.                 |

