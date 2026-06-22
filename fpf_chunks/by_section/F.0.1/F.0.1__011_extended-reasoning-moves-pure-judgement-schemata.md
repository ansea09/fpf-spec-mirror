---
chunk_kind: "child"
pattern_id: "F.0.1"
pattern_title: "Contextual Lexicon Principles"
section_id: "F.0.1:10"
section_title: "Extended reasoning moves (pure judgement schemata)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.0.1/F.0.1__011_extended-reasoning-moves-pure-judgement-schemata.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "F.0.1 — Contextual Lexicon Principles"
  - "F.0.1:10 — Extended reasoning moves (pure judgement schemata)"
line_start: 75645
line_end: 75696
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.4"
  - "A.7"
  - "A.8"
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "U.BoundedContext"
  - "bridge"
  - "congruence"
  - "context"
  - "lexicon"
  - "local meaning"
  - "semantic boundary"
---

### F.0.1:10 - Extended reasoning moves (pure judgement schemata)

> *Judgements are conceptual entailments over Contexts, SenseCells, and Bridges. They carry no storage, workflow, or governance semantics.*

#### F.0.1:10.1 - Context‑qualified use

`Context(C) ∧ mentions(C, s) ⊢ uses(s@C)`
*If s is used under Context C, we treat it as the local term s\@C.*

#### F.0.1:10.2 - Sense formation (local)

`uses(t@C) ∧ gloss_C(t) ⊢ SenseCell⟨t@C⟩`
*A Context‑true gloss yields a SenseCell inside C.*

#### F.0.1:10.3 - Admissible Bridge (creation predicate)

`SenseCell⟨x@A⟩ ∧ SenseCell⟨y@B⟩ ∧ A≠B ∧ rel∈R ∧ cl∈{0,1,2} ⊢ Bridge(x@A,y@B,rel,cl)`
*Only explicit relation `rel` with Congruence Level `cl` constitutes a Bridge.*

**Canonical relation set `R` (didactic catalogue):**
`equivalent‑under‑assumptions` - `near‑equivalent` - `overlaps` - `broader‑than` - `narrower‑than` - `design‑spec‑of` - `run‑trace‑of` - `representation‑of` - `member‑of‑set‑in` - `provides‑value‑for`.

#### F.0.1:10.4 - Bridge composition (minimum CL and relation loss)

`Bridge(a,b,rel₁,cl₁) ∧ Bridge(b,c,rel₂,cl₂) ⊢ Bridge*(a,c,rel*,cl*)`

* `cl* := min(cl₁, cl₂)` (do **not** inflate confidence)
* `rel* := conservativeRel(rel₁, rel₂)` (e.g., near‑equiv composed with overlaps yields overlaps)

*Reading:* Chained passages inherit the minimum `CL` and the relation that remains admissible after composition.

#### F.0.1:10.5 - Non‑identity by stance

`SenseCell⟨x@A(design)⟩ ∧ SenseCell⟨y@B(run)⟩ ∧ ¬declared(Bridge(x,y,near‑equiv,_)) ⊢ ¬same‑row(x,y)`
*Different time stances forbid same‑row unless an explicit near‑equiv Bridge exists.*

#### F.0.1:10.6 - Row viability (Concept‑Set candidacy)

`Cells = {c₁…cₙ} ⊢ row‑viable(Cells) ⇔ connected(Cells, Bridges_{rel∈{equiv,near‑equiv}, cl≥k}) ∧ ¬contradiction(Cells)`

*Reading:* A row is viable if its cells form a connected subgraph via Bridges with sufficient CL and contain no mutually exclusive links.

#### F.0.1:10.7 - Contradiction sieve

`Bridge(a,b,broader) ∧ Bridge(a,b,narrower) ⊢ contradiction(a,b)`
*Incompatible relations across the same pair flag a contradiction for review (conceptually).*

#### F.0.1:10.8 - Non‑bridge implication ban

`name(x) = name(y) ∧ A≠B ⊢ ¬Bridge(x@A, y@B, _, _)`
*String equality across Contexts never implies a Bridge.*

