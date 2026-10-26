---
chunk_kind: "child"
pattern_id: "C.2.7"
pattern_title: "U.LanguageStateRepresentationFactorBundle — How Is the Representation Organized?"
section_id: "C.2.7:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.7/C.2.7__005_solution.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.2.7 — U.LanguageStateRepresentationFactorBundle — How Is the Representation Organized?"
  - "C.2.7:4 — Solution"
line_start: 53327
line_end: 53361
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.18"
  - "A.19"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.6"
  - "C.2.LS"
  - "F.9"
  - "F.9.1"
keywords:
  - "factor bundle"
  - "locality"
  - "representation factors"
  - "representation organization"
  - "sparsity"
  - "symbolicity"
---

### C.2.7:4 - Solution
`U.LanguageStateRepresentationFactorBundle` is a factor bundle, not one scalar characteristic. The minimal core starter set is:

- `U.LocalityDistribution`
- `U.Sparsity`
- `U.Symbolicity`

A local alias such as `EncodingBasis` shall identify the factors and readings it summarizes.

#### C.2.7:4.0a - Kind and factor-bundle boundary

`U.LanguageStateRepresentationFactorBundle` groups readings of distinct representation Characteristics. Each factor needs its own meaning and Scale, and the declared chart binds these under A.18/A.19. The bundle describes the representation identified in the position claim; a factor reading is distinct from that representation or its publication form.

#### C.2.7:4.1 - Minimal factor readings
| Factor | Question it answers | Typical values |
|---|---|---|
| `LocalityDistribution` | Is the representation concentrated in local units or distributed across many units? | local / mixed / distributed |
| `Sparsity` | How concentrated are activation, representation use, or descriptive marks? | sparse / mixed / dense |
| `Symbolicity` | How explicit are the symbolic structures and tokens? | symbolic / mixed / subsymbolic |

Before comparing factors, identify the representation and the units being described. A model-side code and its written summary need not have the same factors.

For example, one scheme represents four states by four distinct units, with one unit active at a time. Another represents 28 states by the unordered pairs of eight units, with two units active at a time. An individual unit identifies the state in the first scheme; a pair identifies it in the second. The active-unit fractions are equal, `1/4 = 2/8`, although locality differs. These fractions do not define a universal sparse/dense threshold.

In the second scheme, `[0,1,0,0,0,0,1,0]` and the list of active positions `{2,7}` express the same code: positions 2 and 7 are active and the other six are inactive. Suppose decoder D1 assigns that pair to state S. Both inscriptions then denote S. If decoder D2 assigns the same pair to state T, the interpretation has changed despite the unchanged list. The shorter inscription alone changes neither the underlying code nor its factors.

When the list travels separately, supply the unit order and decoding rule needed for its next use, directly or through an accessible return to the exact source content. Counting written marks instead of active units requires a different comparison basis.

#### C.2.7:4.2 - Non-collapse rules

Representation organization, anchoring, articulation and closure answer different questions. A distributed code can be trace-anchored; a symbolic note can leave its meaning unclear; a sparse representation can express a claim that remains open. Assess each relevant facet on its own grounds. The representation factors alone establish neither evidence for the claim nor permission to act on it.

#### C.2.7:4.3 - Extension rule
Authors may add extra local representation factors only if the extension is published as a factor addition rather than as a new master factor that erases the core factor bundle.

