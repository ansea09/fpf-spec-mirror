---
chunk_kind: "child"
pattern_id: "C.2.7"
pattern_title: "LanguageStateRepresentationFactorBundle — How Is the Representation Organized?"
section_id: "C.2.7:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.7/C.2.7__005_solution.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.2.7 — LanguageStateRepresentationFactorBundle — How Is the Representation Organized?"
  - "C.2.7:4 — Solution"
line_start: 53917
line_end: 53959
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
`LanguageStateRepresentationFactorBundle` is a factor bundle, not one scalar characteristic. The core starter set for the comparison questions below is:

- `LocalityDistribution`
- `Sparsity`
- `Symbolicity`

A local alias such as `EncodingBasis` shall identify the factors and readings it summarizes.

#### C.2.7:4.0a - Factors and their readings

`LanguageStateRepresentationFactorBundle` groups readings of distinct representation Characteristics. Each factor needs its own meaning and Scale, and the declared chart binds these under A.18/A.19. The bundle describes the representation identified in the position claim; a factor reading is distinct from that representation or its publication form.

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

##### C.2.7:4.1.1 - Why begin with these factors?

The starter set separates three questions that often change how a representation can be read or transferred. **LocalityDistribution** concerns whether one selected unit distinguishes a represented value or whether a combination is needed. **Sparsity** concerns how much of the declared unit set is active or used; its reading depends on what is counted and on the local comparison criterion. **Symbolicity** concerns the explicit tokens and structures available to the receiving interpretation, including the applicable decoding or composition rules. These questions can matter separately: locating a report, estimating the units used to express it and recovering its interpretation require different information.

The pair code in :4.1 explains why a count of active units cannot settle locality and why a compact inscription needs its decoder. The starter bundle keeps these distinctions available without requiring a complete model of the representation. Select only the factors that affect the receiving question, as :16.1 permits. Preserve the representation and unit basis for each reading; factors of a source model and factors of its explanation concern different representations.

An assessment aimed at reconstruction error, robustness or the effect of a causal intervention may need other Characteristics directly. Use those Characteristics when they answer the question; retain a starter factor only when its reading contributes. The gain from the shared triple is a reusable starting vocabulary for code organization, use of units and explicit symbolic structure. It is not an exhaustive representation-quality model, and it supplies no universal thresholds or empirical claim that the factors are statistically independent. Add a needed factor under :4.3 while keeping the meanings of the factors already used.

#### C.2.7:4.2 - Non-collapse rules

Representation organization, articulation and closure are assessed under their own Characteristics; source and use claims retain their direct predicates. A distributed code can be computed from an identified trace; a symbolic note can leave its meaning unclear; a sparse representation can express a claim that remains open. Assess each relevant facet on its own grounds. The representation factors alone establish neither evidence for the claim nor permission to act on it.

#### C.2.7:4.3 - Extension rule
Authors may add extra local representation factors only if the extension is published as a factor addition rather than as a new master factor that erases the core factor bundle.

