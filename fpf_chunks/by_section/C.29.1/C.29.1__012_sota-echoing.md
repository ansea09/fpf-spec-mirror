---
chunk_kind: "child"
pattern_id: "C.29.1"
pattern_title: "Mathematical Result Transfer"
section_id: "C.29.1:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.1/C.29.1__012_sota-echoing.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.29.1 — Mathematical Result Transfer"
  - "C.29.1:11 — SoTA-Echoing"
line_start: 60116
line_end: 60128
dependencies:
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5"
  - "B.5.MPC"
  - "C.29"
keywords:
---

### C.29.1:11 - SoTA-Echoing

The working problem is reuse of mathematical consequences across accounts at a cost justified by the receiving question. Two established lines supply complementary methods: preservation of operations, and coverage of possible results by a sound abstraction.

| Source and applicable contribution | Comparison at comparable effort | Adopt, adapt and limit |
|---|---|---|
| Brendan Fong and David I. Spivak, *Seven Sketches in Compositionality* (consulted 2018 version), §3.3.2 and §2.5.3. Functors preserve identities and composition; the route constructions distinguish composition from choice among alternatives. [Primary text](https://arxiv.org/pdf/1803.05316). | Comparing corresponding operations is stronger than analogy by shared shape. A categorical formulation repays its setup when many objects and composable maps recur; a short elementary derivation can be cheaper for one reservation update. | **Adopt** preservation of the relevant operations. **Adapt** it as the two-order construction and route comparison in C.29.1:4.3 and C.29.1:5.2. Use categorical machinery when the objects and laws warrant it; this pattern does not require every working account to be presented as a category. |
| Patrick Cousot, *Abstract Interpretation: From 0, 1, To ∞*, §2. Its abstract operations cover the possible concrete results represented by their inputs. [Author's text](https://pcousot.github.io/publications/CSV-2023-cousot.pdf). | Exact reconstruction retains more information; a sound abstraction can establish a property with less information but can leave a question undecided. Testing selected cases is cheaper in some settings but does not establish coverage of all permitted cases. | **Adopt** coverage as the reason a bounded abstract result supports a concrete conclusion. **Adapt** that reasoning to C.29.1:4.5's compatible cases and bounds. General abstract-domain construction and program-analysis algorithms remain in their mathematical and computational practice. |

The pattern's synthesis is the practitioner sequence connecting these obligations to the intended answer: construct the map, compare operations and availability, establish independence or coverage, and return the consequence. The reservation, permission-sensitive route and thermal constructions derive their own claims from their stated premises. The cited sources supply reusable mathematical lines, not evidence that a particular physical or organizational application satisfies those premises.

A direct proof in the original account remains a serious alternative. Prefer it when it is simpler than establishing and maintaining a transfer. Reconsider a chosen summary when a new query needs a distinction it omits, when composition introduces a new condition, or when a tighter justified bound changes the decision. Reopen the mathematical work affected by that change.

