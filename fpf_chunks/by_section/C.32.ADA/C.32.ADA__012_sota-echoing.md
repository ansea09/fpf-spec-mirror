---
chunk_kind: "child"
pattern_id: "C.32.ADA"
pattern_title: "Architecture Decision Adequacy Scales"
section_id: "C.32.ADA:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADA/C.32.ADA__012_sota-echoing.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.32.ADA — Architecture Decision Adequacy Scales"
  - "C.32.ADA:11 — SoTA-Echoing"
line_start: 66592
line_end: 66606
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2.1"
  - "A.2.6"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.25"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.13"
  - "E.17"
  - "E.21"
  - "E.22"
  - "E.24.PUB"
keywords:
  - "ArchitectureDecisionAdequacyEvaluation@Project"
  - "E.21 labels"
  - "architecture decision adequacy"
  - "complete coordinate set"
  - "declared use"
  - "method docking"
  - "no average"
  - "publication projection"
  - "repair target"
---

### C.32.ADA:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.ADA. Keep a source citation only when it changes a coordinate, value meaning, stop condition, or repair exit.

| Source to inspect | Why this source is load-bearing here | Transfer into ADA | Concrete ADA mutation | Blocked overread |
|---|---|---|---|---|
| Current FPF `E.21` scale discipline | Existing FPF pattern for declared-use evaluation, exact `0 absent` through `5 exceptionallyExpressedForDeclaredUse` labels, complete coordinates, adjacent-value rationale, and no averaging. | Reuse the value domain and evaluation discipline for architecture decisions without copying pattern-quality coordinates. | ADA requires declared use, complete coordinate set, E.21 value labels with adjacent rationale, no average, and use-specific stop conditions. | E.21 pattern-quality status and coordinates are not architecture-decision adequacy. |
| `C.32.PAD` and `C.32.ADR` | PAD and ADR define the decision relation and publication projection being evaluated. | Make relation adequacy and projection adequacy separate coordinates. | ADA can say a PAD relation is usable while ADR projection needs repair, or the reverse. | A complete ADR does not make the decision relation adequate. |
| ISO/IEC/IEEE 42010:2022 official standard (`https://www.iso.org/standard/74393.html`; IEEE page `https://standards.ieee.org/ieee/42010/6846/`) with the 42010 companion site as secondary reading (`https://iso-architecture.org/42010/`) | Current official source for architecture descriptions, viewpoints, views, correspondence, and rationale; the companion site is used only as secondary reading. | Add coordinates for affected structure, architecture-description adequacy, and source-return. | ADA identifies `C.30.AD` and `C.30.ASV` as subject-pattern locators for weak description assertions. | Architecture-description adequacy does not decide or approve the architecture. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Current practitioner source for architecture feedback and incremental change under eval-like mechanisms. | Add evolution, reopen, guardrail, and confirmation coordinates. | ADA checks reopen and eval exits before a decision is used for long-running work. | Source-side fitness-function wording is not imported as ADA object naming. |
| Ford, Richards, Sadalage, and Dehghani, `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Current practitioner source for trade-off analysis under competing characteristics. | Add architecture-characteristic trade-off adequacy and accepted-loss repair. | ADA identifies ACS, ACE, C.16, C.25, C.31, or C.31.ASAP as subject-pattern locators for the exact weak trade-off assertion. | Trade-off discussion is not an assurance claim or governance approval. |
| 2026 ADR violation-detection research (`https://arxiv.org/abs/2602.07609`) | Recent research shows explicit, code-inferable decisions are easier to check than implicit deployment or organization decisions. | Add confirmation, source-return, method, deployment, and organization refs to adequacy checks when live. | ADA scores confirmation and method docking separately and blocks hidden organizational knowledge from passing as ready. | Automated violation detection is not proof, evidence, assurance, or gate passage. |

**Source-currentness boundary.** Recheck a source row when FPF evaluation discipline, architecture-decision practice, ADR violation checking, evolutionary-architecture eval practice, or project governance changes a coordinate, value meaning, or repair exit.

