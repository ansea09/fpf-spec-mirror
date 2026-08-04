---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human‑Centric Working‑Model"
section_id: "E.14:5"
section_title: "Layer Standard & Downward Flow (Working‑Model → Assurance)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__008_layer-standard-downward-flow-working-model-assurance.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "E.14 — Human‑Centric Working‑Model"
  - "E.14:5 — Layer Standard & Downward Flow (Working‑Model → Assurance)"
line_start: 78317
line_end: 78384
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

This section defines **what each layer is for**, **what it guarantees**, and **how a single Working‑Model statement is carried down**.

#### E.14:5.1 - Working‑Model (what humans see)

**Purpose.** A small, curated graph of kinds and relations that a mixed team can read at a glance.

**Elements.**

* **Kinds** — one **chosen concept** per node (no slash‑labels).
* **Relations** — a short list intelligible to non‑specialists (e.g., *Component‑of*, *Member‑of*, *Aspect‑of*, plus a small number of cross‑disciplinary ties such as *Interface‑of* or *Constituent‑of*).
* **Language register badges** — labels shown in the Working-Model are L‑1 or L‑2; L‑3/L‑4 remain in Mapping as synonyms or symbols.

**Obligations.**

* Every Working‑Model edge and node is **grounded downward** (see below).
* The Working‑Model **does not display** constructor jargon, proof terminology, or evidence identifiers; those live in Assurance and are **available on demand**.

#### E.14:5.2 - Assurance-1: Mapping (from words to chosen governed values)

**Purpose.** Consolidate human labels from varied sources and **bind them to the chosen governed values** used on the Working-Model, including admitted U-kinds where kindhood is live.

**Guarantee.** For any Working-Model label, there exists a **stable alignment** to exactly one chosen governed value in the current scope; synonyms, abbreviations, locales, and registers are recorded here, **not** in the displayed Working-Model. Mapping primarily raises **Concept-Bridge Assurance (CBA)** by consolidating synonyms/registers and binding tokens/labels to the chosen governed value; calculus-level metrics live outside Part E.

**Deliverable.** A compact alignment table per scope that makes it obvious which **one label** the Working‑Model will show and which background source labels are recognized only as source wording.

*(Rationale: Working teams speak many dialects; the Working‑Model speaks one. Mapping is the interpreter.)*

#### E.14:5.3 - Assurance‑2: Logical (from Working‑Model relations to label semantics)

**Purpose.** Give each Working-Model relation **one precise intended meaning** and **its admissible use cases**, keeping the Working-Model vocabulary small.

**Guarantee.** A Working‑Model edge such as *Component‑of* or *Aspect‑of* **carries one intended reading** (transitivity/antisymmetry expectations, scope notes), sufficient for auditors to assess whether the **use is legitimate** in a given context.

**Deliverable.** A short set of label-meaning rules: “When an edge is labeled *Component-of* in the Working-Model text, it intends the direct structural reading whose exact participants, relation occurrence, construction rule, and identity conditions must be recovered before the assertion is accepted.” The Logical layer ties human labels to accepted meanings; it does not make the relation obtain. Calculus-level symbols are not used in E-patterns.

*(Rationale: logical label alignment protects the small Working-Model text from relation proliferation while keeping meanings crisp.)*

#### E.14:5.4 - Assurance-3: Constructive (from a structural claim to its inspectable construction account)

**Purpose.** Make the construction basis of a published structural claim inspectable without turning the assurance account into the relation or the whole.

**Guarantee.** One truthful construction trace names the exact whole, collection, or aspect; its participants; the direct relation occurrences that obtain; the applicable assembly, collection, or facet rule; and the direct identity or reidentification conditions. The same inputs under another assembly may form another whole, while a permitted constituent replacement may preserve the same whole. The trace decides neither case.

**Deliverable.** For a published structural assertion, link through `tv:groundedBy` to one current C.2.1 construction-trace episteme in the C.13 `sum`, `set`, or `slice` form and declare the author's `validationMode=axiomatic` posture. Creating, revising, publishing, or losing that trace changes the account or its availability, not the relation occurrence or whole identity. The trace edition, its warrants and evidence, and the temporal status of the described direct facts retain their own currentness.

*(Rationale: constructive assurance makes the facts and identity tests behind ordinary part-whole talk inspectable; it does not substitute an author narrative for those facts.)*

#### E.14:5.5 - Assurance-4: Empirical Validation (from claims to observed world)

**Purpose.** Make the empirical basis and bounded admissible use of one Working-Model claim inspectable without turning evidence, provenance, or an assurance record into the subject result.

**Guarantee.** Every empirical assurance use names the exact target claim, `U.ClaimScope`, qualification window, and direct result owner. When the claim depends on evaluation or measurement, it also names the exact dated Work, performer `U.System`, obtaining `U.RoleAssignment`, selected `U.Method`, any separately relied-on `U.MethodDescription`, actual direct participants or A.6.1 bindings, and the domain-local result plus its C.2.1 result episteme. A.10 supplies the exact evidence-provenance path and bounded reliance disposition; B.3 supplies any assurance claim. Those objects can support or qualify the Working-Model claim but create neither the subject fact nor one another.

**Deliverable.** Keep the ordinary Working-Model sentence first. Beneath it, expose only the exact result, work, provenance, currentness, and assurance relations that the current use consumes. Intended evaluation remains in `U.WorkPlan` until dated Work occurs. If a claim that evaluation Work first constituted the result episteme is separately current, A.15.PROD alone recovers that local entity-identity inception claim; no universal work-result, evidence-result, or production relation is implied. Expiry, evidence ageing, or changed source, method, calibration, result, qualification window, provenance, or assurance basis ends only the reliance that consumes that support and requires its direct owner to be re-evaluated. In B.3 terms Empirical Validation contributes on the LA shoulder; B.3 alone computes any effect on reliability R or claim scope G, and G cannot extend beyond the exact supported scope and qualification window.

#### E.14:5.6 - The downward grounding for a single Working-Model statement

Consider a Working‑Model arrow **A –Component‑of→ B**:

1. **Mapping** shows that the words *A* and *B* are the chosen labels for their kinds; it records background source labels without making them displayed Working-Model names.
2. **Logical** confirms that **Component‑of** in the Working-Model text means the **structural reading** with its ordinary mereological expectations; if the Working-Model text used *Member‑of* instead, Logical would similarly certify the intended reading and its boundaries.
3. **Constructive** links the published assertion to one current C.2.1 trace episteme that reports the exact participants, direct relation occurrences, applicable construction rule, and identity or reidentification conditions in a `sum`, `set`, or `slice` form. The author declares `validationMode=axiomatic` as the assurance posture. The direct relation and identity tests remain decisive; the trace and mode create neither.
4. **Empirical Validation** names the exact empirical claim and scope, the domain-local result and result episteme when current, the dated evaluation or measurement Work and actual bindings required by that result's direct owner, its qualification window, the A.10 evidence-provenance path, and any separately current B.3 assurance claim. Those objects support this bounded use; they do not create the result or make the structural relation obtain.

Together, these assurance shoulders and empirical evidence-use relation **ground the human arrow without leaking their machinery upward**. The Working‑Model remains simple; the Assurance stack carries the proof.

