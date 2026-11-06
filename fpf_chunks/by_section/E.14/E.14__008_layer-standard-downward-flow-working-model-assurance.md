---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human-Centric Working-Model: Readable Claims and Recoverable Assurance"
section_id: "E.14:5"
section_title: "Layer Standard & Downward Flow (Working‑Model → Assurance)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__008_layer-standard-downward-flow-working-model-assurance.md"
commit_sha: "d8dd955fddb923b5b946d2c5865d0665cff5a67e"
heading_path:
  - "E.14 — Human-Centric Working-Model: Readable Claims and Recoverable Assurance"
  - "E.14:5 — Layer Standard & Downward Flow (Working‑Model → Assurance)"
line_start: 105368
line_end: 105435
dependencies:
  - "B.3.5"
  - "C.13"
  - "C.2.3"
  - "E.10"
  - "E.7"
  - "E.8"
keywords:
---

### E.14:5 - Layer Standard & Downward Flow (Working‑Model → Assurance)

This section defines **what each layer is for**, **what it guarantees when selected**, and **how purpose-selected support is carried down** from a direct Working-Model statement.

#### E.14:5.1 - Working‑Model (what humans see)

**Purpose.** A small, curated graph of kinds and relations that a mixed team can read at a glance.

**Elements.**

* **Kinds** — one **chosen concept** per node (no slash‑labels).
* **Relations** — a short set of statements intelligible to non-specialists (for example, *Component-of*, a subject-specific sentence such as “this cartridge belongs to this bank under the bank's rule”, *Aspect-of*, and a small number of cross-disciplinary ties such as *Interface-of* or *Constituent-of*).
* **Language registers** — choose Plain or Tech wording under E.10 for what the intended reader must identify and use. Keep background synonyms, source labels, and unused symbols in Mapping; expose a technical term in the Working-Model when the current claim or reader use needs it.

**Obligations.**

* A Working-Model edge or node whose use elects an assurance profile keeps that profile's required support recoverable downward. A direct claim outside such a profile can stand on its direct meaning and truth conditions; E.14 adds no assurance field or separate support account.
* The Working-Model omits constructor jargon, proof terminology, and evidence identifiers that its intended reader does not need. Keep the support available on demand, and include a technical term or identifier in the working statement when it changes the claim or the reader's action.

#### E.14:5.2 - Assurance-1: Mapping (from words to chosen model values)

**Purpose.** Consolidate human labels from varied sources and **bind them to the chosen model values** used in the Working-Model, including admitted U-kinds where kindhood is live.

**What to check.** When Mapping assurance is selected, verify the Working-Model label's alignment to its chosen model value in the current scope. Recover the synonyms, abbreviations, locales, and registers needed for that comparison in the Mapping account. This can contribute to **Concept-Bridge Assurance (CBA)** under B.3.3 when it establishes a claim-relevant meaning correspondence; collecting labels alone does not raise assurance.

**Deliverable.** When the current use needs source-word alignment, provide a compact alignment account for that scope. It makes obvious which **one label** the Working-Model shows and which background labels remain source wording.

*(Rationale: Working teams speak many dialects; the Working‑Model speaks one. Mapping is the interpreter.)*

#### E.14:5.3 - Assurance‑2: Logical (from Working‑Model relations to label semantics)

**Purpose.** Give each Working-Model relation **one precise intended meaning** and **its admissible use cases**, keeping the Working-Model vocabulary small.

**Guarantee.** When Logical assurance is selected, a Working-Model edge such as *Component-of* or *Aspect-of* carries one stated reading, including the scope and relation properties needed for the current use, so an auditor can assess whether that use is legitimate.

**Deliverable.** When the current use needs an explicit label-meaning account, give a short rule such as: “When an edge is labeled *Component-of* in the Working-Model text, it intends the direct structural reading whose participants, relation occurrence, construction rule, and identity conditions must be recovered before the assertion is accepted.” The Logical shoulder ties the human label to that accepted meaning; it does not make the relation obtain. When a calculus or other expression carries a reasoning or construction step, explain its interpretation, operation and prerequisites or cite their subject guidance under E.5.2. Keep the readable claim recoverable from that expression.

*(Rationale: logical label alignment protects the small Working-Model text from relation proliferation while keeping meanings crisp.)*

#### E.14:5.4 - Assurance-3: Constructive (from a structural claim to its inspectable construction account)

**Purpose.** Make the construction basis of a published structural claim inspectable without turning the assurance account into the relation or the whole.

**Guarantee.** When Constructive assurance is selected, one truthful construction trace names the exact whole, collection, or aspect; its participants; the direct relation occurrences that obtain; the applicable assembly, collection, or facet rule; and the direct identity or reidentification conditions. The same inputs under another assembly may form another whole, while a permitted constituent replacement may preserve the same whole. The trace decides neither case.

**Deliverable.** For a structural parthood or collection-belonging assertion covered by an elected `B.3.5` profile, keep the readable claim first, link it through `tv:groundedBy` to one current C.2.1 construction-trace episteme in the applicable C.13 form — `sum` or `slice` for structural parthood, or `set` for collection belonging — and declare `validationMode=axiomatic`. If another named current assurance requirement calls for a construction account, follow that requirement and use C.13 for the trace content. Outside those conditions, the direct structural claim has no E.14 mode, link, or trace obligation. Creating, revising, publishing, or losing a trace changes the account or its availability, not the relation occurrence or whole identity. The trace edition, its warrants and evidence, and the temporal status of the described direct facts retain their own currentness.

*(Rationale: constructive assurance makes the facts and identity tests behind ordinary part-whole talk inspectable; it does not substitute an author narrative for those facts.)*

#### E.14:5.5 - Assurance-4: Empirical Validation (from claims to observed world)

**Purpose.** Make the empirical basis and bounded admissible use of one Working-Model claim inspectable without turning evidence, provenance, or an assurance record into the subject result.

**Guarantee.** Supply the empirical support required for the target claim and receiving use. A permitted `B.3.5` postulate states its scope, links an admissible evidence object and gives challenge cues; an ungrounded proposal does not satisfy that elected profile. For a relied-on domain result, recover its interpretation, applicability and source grounds under the pattern that defines or tests it. Keep any required scope selectors and temporal qualification; do not add a time window to a non-temporal claim merely for this account. Where the result or profile consumes a dated Work claim, establish its performer basis under A.13, independently admit the Work under A.15.1 and retain its enacted Method. F.6 supplies exact assignment-bound attribution when consumed; A.2.1 governs the assignment. Keep any relied-on MethodDescription edition, participant or A.6.1 binding, local classification and C.2.1 result-episteme identity under their own rules. Use A.10 for a source-to-use account that needs to be explicit or replayable, and B.3 for an assurance claim. Already sufficient grounds remain usable; an unresolved required premise remains open.

**Deliverable.** Keep the ordinary Working-Model sentence first and expose only the support required for its stated use. A `postulate` follows the elected profile, including B.3.5's evidence object and challenge cues when that profile applies; no new evaluation is required merely to declare the posture. A proposed evaluation remains prospective; use `U.WorkPlan` when coordination of future Work is needed. If the current question concerns the Work's productive treatment, an episteme's identity inception or a production-completion condition, use A.15.PROD for that question. Re-evaluate only reliance affected by a changed source, method, calibration, result, temporal qualification, provenance or assurance premise. Narrow or withdraw that reliance when its applicable condition fails; age alone does not defeat still-applicable evidence. Under B.3/B.3.3, Empirical Validation contributes what its result establishes for the target claim and receiving use. A reliability calculation needs its exact domain quantity and model; scope follows A.2.6 and its warrant.

#### E.14:5.6 - Purpose-selected support for a single Working-Model statement

Start with the direct Working-Model arrow **A –Component-of→ B**. If no assurance-bearing reliance question is current, the author may stop there. If a profile or named current requirement is active, add only the support it calls for:

1. **Mapping**, when source-word alignment matters, shows that *A* and *B* are the chosen labels for their model values and records background labels without making them Working-Model names.
2. **Logical**, when the relation reading needs assurance, states what **Component-of** means here and the boundaries of that use.
3. **Constructive**, when `B.3.5` is elected for this structural assertion, links the readable claim to one current C.2.1 trace episteme that reports the participants, direct relation occurrences, construction rule, and identity conditions in a C.13 `sum` form; the author declares `validationMode=axiomatic`. The direct relation and identity tests remain decisive.
4. **Empirical Validation**, when the current reliance needs observation, exposes the empirical claim, supported domain result and scope, together with the Work, result-episteme identity, bindings, temporal qualification and source-to-use account that the claim or elected profile consumes under §5.5. A separately current B.3 assurance claim retains its own grounds.

The selected support stays below the readable claim. It makes the needed basis inspectable without forcing unused assurance machinery into the Working-Model.

