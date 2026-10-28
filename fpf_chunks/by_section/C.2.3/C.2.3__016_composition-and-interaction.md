---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Formality of an Episteme"
section_id: "C.2.3:15"
section_title: "Composition and interaction"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__016_composition-and-interaction.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.2.3 — Formality of an Episteme"
  - "C.2.3:15 — Composition and interaction"
line_start: 52623
line_end: 52644
dependencies:
  - "A.16"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.19.2"
  - "C.2"
  - "C.2.2"
  - "C.2.4"
  - "C.2.7"
  - "C.2.LS"
  - "C.39"
  - "F.9"
keywords:
  - "Formality assessment"
  - "expression properties"
  - "language-state separation"
  - "local ordinal scale"
  - "partial order"
  - "proof"
  - "specification"
---

### C.2.3:15 - Composition and interaction

#### C.2.3:15.1 - Essential-content and connection rule

Identify the assessed episteme's expressed claim or argument and its compositional support relation. A property of the whole requires the relevant properties of its essential content and of the inferences that connect it. A machine-checked annex does not make an informal connecting inference machine-checked. Listing common constituent properties is also insufficient when the composition can fail to preserve them.

External evidence has a different role. A typed claim supported by an informal observation can retain its explicit predicate and interpretation while its empirical warrant remains weak or unresolved under B.3. If the assessed subject is instead the whole argument, include its essential observation-to-conclusion inference in that assessment. Do not take a minimum over every external source in an evidence chain.

A minimum can abbreviate an upper bound on a local ordered scale only when all assessed parts use that scale and the composition rule establishes the bound, including the connection. A minimum alone does not prove that the whole meets that level; additional joining obligations may remain. Without that basis, inspect the needed properties directly.

#### C.2.3:15.2 - Relation to G

Formality concerns expression; G concerns applicability or claim scope. Making an assumption explicit can reveal that the claim applies less widely than expected. Record that scope correction separately from the improvement in expression. A precise claim can still have broad scope.

#### C.2.3:15.3 - Relation to R

An explicit expression can make a claim easier to test or its derivation easier to check. It does not create empirical support. A checked formal argument establishes its conclusion under the admitted premises and calculus; applying that conclusion to the world additionally needs the relevant interpretation and evidence. Assess freshness, corroboration and mapping limitations under their actual assurance models.

#### C.2.3:15.4 - Relation to CL and Bridges

A Bridge may expose loss or mismatch across contexts. Preserve that limitation for the receiving use. Reuse a formality assessment only if the properties and interpretation on which it relies survive the transfer. A receiving rewrite that changes claim content, EntityOfConcern or the effective reference scheme identifies a new episteme under C.2.1; assess the expression of that episteme. A changed carrier alone does not require a new assessment.

