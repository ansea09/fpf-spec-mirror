---
chunk_kind: "child"
pattern_id: "C.3.5"
pattern_title: "KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
section_id: "C.3.5:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.5/C.3.5__001_intro.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.3.5 — KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
  - "C.3.5:intro — Intro"
line_start: 46246
line_end: 46264
dependencies:
  - "A.2.6"
  - "C.2.2"
  - "C.2.3"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.4"
  - "C.3.A"
keywords:
  - "K0-K3"
  - "KindAT"
  - "assurance planning"
  - "declaration planning"
  - "editorial facet"
---

## C.3.5 - KindAT — Intentional Abstraction Facet for Kinds (K0…K3)

> **One-line summary.** `KindAT` is an informative editorial facet on one local `U.Kind`. Its anchors—K0 Instance, K1 Behavioral Pattern, K2 Formal Kind/Class, and K3 Up-to-Iso—help plan declaration rigor, assurance coverage, bridge expectations, catalog search, and refactoring. KindAT is not a Characteristic: it has no algebra or threshold and never appears in guards or composition. It changes neither the kind, a `KindSignature`, a classification judgment, an extension representation, nor F–G–R.

**Status.** Informative for anchors, heuristics, examples, and guidance; normative only for the usage rules that prohibit guard/composition use and constrain placement.

**Placement.** Part C (Kinds), identifier **C.3.5**. Audience: engineering managers, architects, editors, and assurance leads.

**Depends on.**

- **C.3/C.3.1:** the context-local `U.Kind`, obtaining `U.SubkindOf` relations, and kind continuity.
- **C.3.2:** the separate `KindSignature` declaration episteme, exact four-input classification judgment, and optional pinned-edition extension representation.
- **C.3.3:** the obtaining `KindBridge` relation and its separate bridge-assertion episteme carrying `CL^k`, loss, evidence, and admitted use.
- **C.3.4:** the `KindUseAdaptationDeclaration` episteme and exact `KindUseAdaptationJudgment`.
- **A.2.6, C.2.2, and C.2.3:** Claim/Work scope, F–G–R, and `U.Formality` on the episteme that owns it.
- **MM-CHR:** the Facet-versus-Characteristic distinction.

**Non-goals.** KindAT supplies no numerical scale, gating rule, composition operator, public-kind admission, classification result, or assurance score.

