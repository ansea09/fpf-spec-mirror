---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human‑Centric Working‑Model"
section_id: "E.14:5"
section_title: "Layer Standard & Downward Flow (Working‑Model → Assurance)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__008_layer-standard-downward-flow-working-model-assurance.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "E.14 — Human‑Centric Working‑Model"
  - "E.14:5 — Layer Standard & Downward Flow (Working‑Model → Assurance)"
line_start: 76115
line_end: 76182
dependencies:
  - "B.3.5"
  - "C.13"
  - "C.2.3"
  - "E.10"
  - "E.7"
  - "E.8"
keywords:
  - "assurance layers"
  - "grounding"
  - "human-centric"
  - "publication surface"
  - "working model"
---

### E.14:5 - Layer Standard & Downward Flow (Working‑Model → Assurance)

This section defines **what each layer is for**, **what it guarantees when selected**, and **how purpose-selected support is carried down** from a direct Working-Model statement.

#### E.14:5.1 - Working‑Model (what humans see)

**Purpose.** A small, curated graph of kinds and relations that a mixed team can read at a glance.

**Elements.**

* **Kinds** — one **chosen concept** per node (no slash‑labels).
* **Relations** — a short list intelligible to non‑specialists (e.g., *Component‑of*, *Member‑of*, *Aspect‑of*, plus a small number of cross‑disciplinary ties such as *Interface‑of* or *Constituent‑of*).
* **Language register badges** — labels shown in the Working-Model are L-1 or L-2; L-3 and L-4 remain in Mapping as synonyms or symbols.

**Obligations.**

* A Working-Model edge or node whose use elects an assurance profile keeps that profile's required support recoverable downward. A direct claim outside such a profile can stand on its direct meaning and truth conditions; E.14 adds no assurance field or separate support account.
* The Working‑Model **does not display** constructor jargon, proof terminology, or evidence identifiers; those live in Assurance and are **available on demand**.

#### E.14:5.2 - Assurance-1: Mapping (from words to chosen model values)

**Purpose.** Consolidate human labels from varied sources and **bind them to the chosen model values** used in the Working-Model, including admitted U-kinds where kindhood is live.

**Guarantee.** When Mapping assurance is selected, the Working-Model label has a **stable alignment** to one chosen model value in the current scope; synonyms, abbreviations, locales, and registers are recorded here, **not** in the displayed Working-Model. Mapping primarily raises **Concept-Bridge Assurance (CBA)** by consolidating synonyms and registers and binding tokens and labels to the chosen value; calculus-level metrics live outside Part E.

**Deliverable.** When the current use needs source-word alignment, provide a compact alignment table for that scope. It makes obvious which **one label** the Working-Model shows and which background labels remain source wording.

*(Rationale: Working teams speak many dialects; the Working‑Model speaks one. Mapping is the interpreter.)*

#### E.14:5.3 - Assurance‑2: Logical (from Working‑Model relations to label semantics)

**Purpose.** Give each Working-Model relation **one precise intended meaning** and **its admissible use cases**, keeping the Working-Model vocabulary small.

**Guarantee.** When Logical assurance is selected, a Working-Model edge such as *Component-of* or *Aspect-of* carries one stated reading, including the scope and relation properties needed for the current use, so an auditor can assess whether that use is legitimate.

**Deliverable.** When the current use needs an explicit label-meaning account, give a short rule such as: “When an edge is labeled *Component-of* in the Working-Model text, it intends the direct structural reading whose participants, relation occurrence, construction rule, and identity conditions must be recovered before the assertion is accepted.” The Logical shoulder ties the human label to that accepted meaning; it does not make the relation obtain. Calculus-level symbols are not used in E-patterns.

*(Rationale: logical label alignment protects the small Working-Model text from relation proliferation while keeping meanings crisp.)*

#### E.14:5.4 - Assurance-3: Constructive (from a structural claim to its inspectable construction account)

**Purpose.** Make the construction basis of a published structural claim inspectable without turning the assurance account into the relation or the whole.

**Guarantee.** When Constructive assurance is selected, one truthful construction trace names the exact whole, collection, or aspect; its participants; the direct relation occurrences that obtain; the applicable assembly, collection, or facet rule; and the direct identity or reidentification conditions. The same inputs under another assembly may form another whole, while a permitted constituent replacement may preserve the same whole. The trace decides neither case.

**Deliverable.** For a structural assertion covered by an elected `B.3.5` profile, keep the readable claim first, link it through `tv:groundedBy` to one current C.2.1 construction-trace episteme in the C.13 `sum`, `set`, or `slice` form, and declare `validationMode=axiomatic`. If another named current assurance requirement calls for a construction account, follow that requirement and use C.13 for the trace content. Outside those conditions, the direct structural claim has no E.14 mode, link, or trace obligation. Creating, revising, publishing, or losing a trace changes the account or its availability, not the relation occurrence or whole identity. The trace edition, its warrants and evidence, and the temporal status of the described direct facts retain their own currentness.

*(Rationale: constructive assurance makes the facts and identity tests behind ordinary part-whole talk inspectable; it does not substitute an author narrative for those facts.)*

#### E.14:5.5 - Assurance-4: Empirical Validation (from claims to observed world)

**Purpose.** Make the empirical basis and bounded admissible use of one Working-Model claim inspectable without turning evidence, provenance, or an assurance record into the subject result.

**Guarantee.** A `postulate` remains a scoped working claim: state its target and scope and supply the brief empirical cues that B.3.5 calls for. It does not establish that evaluation or measurement Work occurred or that a result exists. When evaluation or measurement did occur and the current assurance use relies on its result, name the target claim, `U.ClaimScope`, qualification window, and the pattern that defines or tests the result, and keep the complete A.15.1/F.6 basis recoverable. The assurance account then names the dated Work, every performer `U.System`, and the Method the Work enacted; it uses F.6 to check each Work-assignment link and A.2.1 for the assignment itself. Cite a relied-on `U.MethodDescription` only when current, test any local system-role-kind classification separately, and name the participants or A.6.1 bindings, domain-local result, and C.2.1 result episteme that the claim uses. Use A.10 for the evidence-provenance path and reliance disposition, and B.3 for any assurance claim. These objects can support or qualify the Working-Model claim but create neither the subject fact nor one another. Another named current assurance requirement retains its own obligations.

**Deliverable.** Keep the ordinary Working-Model sentence first. For a postulate with no relied-on completed result, state the scope and brief empirical cues, then stop. When the current use relies on an actual evaluation or measurement result, expose only the exact result, Work, provenance, currentness, and assurance relations that use consumes. Intended evaluation remains in `U.WorkPlan` until dated Work occurs. If a claim that evaluation Work first constituted the result episteme is separately current, A.15.PROD alone recovers that local entity-identity inception claim; no universal work-result, evidence-result, or production relation is implied. Expiry, evidence ageing, or changed source, method, calibration, result, qualification window, provenance, or assurance basis ends only the reliance that consumes that support and requires the affected reliance claim to be re-evaluated under its applicable pattern. In B.3 terms Empirical Validation contributes on the LA shoulder; B.3 alone computes any effect on reliability R or claim scope G, and G cannot extend beyond the exact supported scope and qualification window.

#### E.14:5.6 - Purpose-selected support for a single Working-Model statement

Start with the direct Working-Model arrow **A –Component-of→ B**. If no assurance-bearing reliance question is current, the author may stop there. If a profile or named current requirement is active, add only the support it calls for:

1. **Mapping**, when source-word alignment matters, shows that *A* and *B* are the chosen labels for their model values and records background labels without making them Working-Model names.
2. **Logical**, when the relation reading needs assurance, states what **Component-of** means here and the boundaries of that use.
3. **Constructive**, when `B.3.5` is elected for this structural assertion, links the readable claim to one current C.2.1 trace episteme that reports the participants, direct relation occurrences, construction rule, and identity conditions in a `sum`, `set`, or `slice` form; the author declares `validationMode=axiomatic`. The direct relation and identity tests remain decisive.
4. **Empirical Validation**, when the current reliance needs observation, names the empirical claim and scope, domain result and result episteme, dated evaluation or measurement Work, actual bindings required by the measurement rule, qualification window, A.10 evidence-provenance path, and any separately current B.3 assurance claim. Those objects support this bounded use; they do not create the result or make the structural relation obtain.

The selected support stays below the readable claim. It makes the needed basis inspectable without forcing unused assurance machinery into the Working-Model.

