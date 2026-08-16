---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human‑Centric Working‑Model"
section_id: "E.14:8"
section_title: "Conformance Checklist (normative; author‑facing duties for thought and prose)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__011_conformance-checklist-normative-author-facing-duties-for-thought-and-prose.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "E.14 — Human‑Centric Working‑Model"
  - "E.14:8 — Conformance Checklist (normative; author‑facing duties for thought and prose)"
line_start: 78949
line_end: 79007
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

### E.14:8 - Conformance Checklist *(normative; author‑facing duties for thought and prose)*

| ID                                         | Requirement                                                                                                                                                                      | Purpose                                                       |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **CC‑E14‑1 (Working‑Model primacy).**      | Authors **SHALL** publish claims in **Working‑Model** form (human‑oriented **ut:\*Of** relations or equivalent domain statements) as the canonical publication face for readers.          | Preserve human‑first canon and didactic clarity.              |
|**CC-E14-2 (Downward grounding).** | When assurance is attached, grounding **SHALL** flow **downwards** from the Working-Model to the appropriate assurance shoulder (**Mapping, Logical, Constructive, or Empirical**) and **SHALL NOT** impose vocabulary back onto the Working-Model. | Maintain relation-family separation and cognitive economy. |
| **CC‑E14‑3 (Stance declaration).**         | For any claim where assurance matters, the author **SHALL** declare `validationMode` (*postulate / inferential / axiomatic*).                                                    | Make assurance intent explicit and readable.                  |
| **CC-E14-4 (No order/time in structure).** | Authors **SHALL NOT** encode execution order, parallelism, or temporal coverage as part-whole; keep them adjacent in their own relation families.                                           | Prevent layer leakage and category errors.                    |
| **CC‑E14‑5 (Collection differs from composition).** | Authors **SHALL** keep exact membership occurrences and collection identity distinct from component relations and integrated assembly. A gathering description or `set` trace creates neither membership nor component status. | Preserve the direct relation and identity boundaries. |
| **CC‑E14‑6 (Notational independence).**    | Core meaning **MUST NOT** hinge on a specific diagram or syntax; any rendering present **SHALL** be marked informative.                                                          | Ensure longevity and cross‑discipline portability.            |
| **CC‑E14‑7 (Layer direction).**            | Authors **SHALL** avoid back-defining Working-Model terms by their assurance publications or records; dependence is one‑way (Working‑Model → Assurance).                                       | Preserve unidirectional dependence of layers.                 |
| **CC‑E14‑8 (Template compliance).**        | Sections **SHALL** follow the canonical pattern order; *Archetypal Grounding* is mandatory for architectural patterns.                                                                            | Keep patterns comparable and auditable by reading.            |
| **CC‑E14‑9 (Progressive formality).**      | Authors **SHOULD** escalate assurance deliberately (from working claim to reasoned to constructive), and use **Empirical Validation** where observation is the right currency.    | Support staged formality without overloading early drafts.  |
| **CC-E14-10 (Structural grounding handshake).** | A published structural assertion **SHALL** declare the author's `validationMode=axiomatic` posture and link through `tv:groundedBy` to exactly one current C.2.1 construction-trace episteme in a C.13 `sum`, `set`, or `slice` form. The direct relation pattern and the candidate's identity or reidentification rule decide occurrence and continuity; the trace and mode create neither and guarantee no timelessness. | Makes the assertion's construction basis inspectable while keeping ontology, identity, assurance, and currentness separate. |
| **CC‑E14‑11 (Empirical bindings).** | When `validationMode=postulate` or real-world confirmation is current, authors **SHALL** name the target claim, scope, qualification window, dated evaluation or measurement Work, every performer System, and the selected Method; F.6 **SHALL** identify the assignment under which each performer acted. Any current MethodDescription or local system-role-kind classification, direct participants or A.6.1 bindings, domain-local result and result episteme, A.10 evidence-provenance path, and B.3 assurance claim remain separate. Expose only identities the bounded assurance use consumes. | Keeps performer, assignment, Method, Work, result, evidence, provenance, assurance, and subject truth distinct and replayable. |
| **CC-E14-12 (F-declaration).**             | Normative Working-Model publications **SHALL** declare `U.Formality = Fk` per **C.2.3** (**recommended F ≥ F3** for readable publications). Assurance publications or records **MAY** carry higher F; **min-F** applies to composites. | Aligns E.14 with the unified Formality characteristic; avoids obsolete “tiers/modes”. |
| **CC‑E14‑13 (Light records, not thin prose).** | Authors **SHALL NOT** use the Working‑Model-first stance as a reason to strip problem framing, rationale, or worked slices out of the pattern text. Ordinary use may stay light, but readers **MUST** still be able to understand the pattern without nearby project notes. | Keeps human-facing economy from collapsing into under-explained prose. |
| **CC‑E14‑14 (Recognition text before assurance text).** | When a pattern claims a Working‑Model or other human-facing benefit, authors **SHALL** keep recognition-first working text distinct from the heavier assurance text. The assurance text **MAY** refine and justify the working text, but it **SHALL NOT** silently change the recognition-text claim. If the pattern claims broad or transdisciplinary reach, the working text **SHOULD** show heterogeneous situations early, preferably through an `F.16`-style example matrix or an equally explicit alternative. | Keeps Working‑Model-first drafting from collapsing into either thin prose or late-only universality. |

*All obligations above are **conceptual** and apply to thought and prose; they introduce no notational or data‑processing requirements.*

**E — Conceptual Examples (no notation, no data handling)**

1. **Exact skid assembly -> “Component Of”**
   For PumpSkid 7, recover the exact pump, frame, reservoir, valve set, and other constituents; the direct fastening, coupling, enclosure, terminal, flange, and seal occurrences that obtain; the applicable skid assembly rule; and the skid reidentification rule. The team may then publish each truthful **Component Of** claim and, when assurance is current, link it to one C.2.1 `sum` trace that reports that basis. The same parts unconnected or assembled differently do not thereby form PumpSkid 7. A permitted pump replacement may preserve PumpSkid 7. The direct relations and reidentification rule decide; the trace and `axiomatic` posture do not.

2. **Exact collection memberships -> “Member Of”**
   For a four-cartridge bank, identify the exact collection, its collection-identity rule, and each direct membership occurrence. A C.13 `set` trace can then report that construction for assurance. Parallel use, physical proximity, a list, or an author's gathering act does not license **Member Of**, does not imply **Component Of**, and does not make the bank an acting system.

3. **Exact bearer, facet, and aspect -> “Aspect Of”**
   For the thermal envelope of one reactor, identify the exact reactor bearer, the exact thermal-envelope aspect, the governed thermal facet, the direct **Aspect Of** occurrence, and the aspect's identity rule. A C.13 `slice` trace can report those facts. Selecting a view, naming a facet, carving a diagram, or choosing a time window creates no aspect occurrence and no independent system.

> **Notes across the examples**
> • Everyday labels (*Component Of, Member Of, Aspect Of*) remain the only labels engineers need to see; direct relation facts make them true or false, and the linked construction account makes their basis inspectable.
> • Structural assertions use Constructive assurance under this pattern; epistemic assertions such as “Representation Of” or “Usage Of” use the direct logical or evidence relation appropriate to the claim.

**F — Resulting Context (after you apply the pattern)**

**What improves**

* **One readable structural vocabulary.** Teams can ask which exact relation obtains—component, member, aspect, or another direct kind—without exposing assurance machinery in ordinary work. Assurance readers can still recover the participants, direct relation facts, construction rule, and identity conditions behind a published assertion.
* **Explicit identity tests.** Input lists and traces do not decide identity. Different assembly relations can make the same listed inputs another whole; an admitted replacement can preserve one whole. Collections use their own identity rule and exact memberships; aspects use the exact bearer, facet, direct relation, and aspect identity.
* **Layer harmony.** Engineer-facing labels live at the same level as other relation names, while their warrants and construction accounts live one step below, keeping human language clean and the claim basis auditable.

**What to watch**

* **Discipline for structural relation kinds.** A published structural assertion is unsafe when its direct relation basis or identity test is missing, even if a trace or `axiomatic` flag exists. Conversely, forcing epistemic links to pretend they are structural over-physicalises knowledge claims; for those, a direct logical or evidence relation is the right currency.
* **Author workload moves, not grows.** Day-to-day model authors stay with working labels; specification authors must recover the direct relation occurrence and identity test and keep one current construction account when this publication policy requires it. The account supports review; it does not repair missing world-side facts.

**Invariants you must preserve**

* **Parsimony of construction accounts.** Use `sum` to report integrated assembly, `set` to report a governed collection, and `slice` to report an exact aspect. Do not treat them as generative acts or add forms for parallelism or time-slicing; order and time remain with their direct conceptual services.
* **Relation-kind-specific justification.** Structural claims require independently grounded direct relations plus an inspectable construction account under this policy; epistemic claims require their direct logical or evidence relations. Neither assurance route changes the governed relation kind.

**Known consequences**

* **Stable queries, fewer surprises.** Working labels retain one direct meaning across disciplines, while each published structural assertion can be followed to the facts and identity conditions reported in its construction account.
* **Audit trail without jargon.** Reviewers can follow a structural claim to its exact participants, direct relation occurrences, construction rule, identity conditions, and current trace edition while everyday collaborators keep using familiar relation names.

