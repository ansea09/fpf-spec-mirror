---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human-Centric Working-Model: Readable Claims and Recoverable Assurance"
section_id: "E.14:8"
section_title: "Conformance Checklist (normative; author‑facing duties for thought and prose)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__011_conformance-checklist-normative-author-facing-duties-for-thought-and-prose.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "E.14 — Human-Centric Working-Model: Readable Claims and Recoverable Assurance"
  - "E.14:8 — Conformance Checklist (normative; author‑facing duties for thought and prose)"
line_start: 90300
line_end: 90358
dependencies:
  - "B.3.5"
  - "C.13"
  - "C.2.3"
  - "E.10"
  - "E.7"
  - "E.8"
keywords:
---

### E.14:8 - Conformance Checklist *(normative; author‑facing duties for thought and prose)*

| ID                                         | Requirement                                                                                                                                                                      | Purpose                                                       |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **CC‑E14‑1 (Working‑Model primacy).**      | Authors **SHALL** publish claims in **Working‑Model** form (human‑oriented **ut:\*Of** relations or equivalent domain statements) as the canonical publication face for readers.          | Preserve human‑first canon and didactic clarity.              |
| **CC-E14-2 (Grounding and correction).** | When assurance is attached, authors **SHALL** keep its basis recoverable beneath the readable Working-Model claim and **SHALL NOT** let its notation or record structure dictate the public vocabulary. If the support defeats or narrows the claim, revise the recognition text under its direct governing pattern and expose the change. | Preserve readable presentation and prevent divergence between the public claim and its warranted support. |
| **CC-E14-3 (Assurance posture).** | For a claim covered by an elected `B.3.5` profile or another named current assurance requirement, the author **SHALL** declare the posture required there. Under `B.3.5`, covered claims declare `validationMode`; a direct claim outside such a profile needs no E.14 mode. | Make selected assurance intent explicit without taxing ordinary direct use. |
| **CC-E14-4 (No order or time in structure).** | Authors **SHALL NOT** encode execution order, parallelism, or temporal coverage as part-whole; keep them adjacent in their own relation families. | Prevent layer leakage and category errors. |
| **CC‑E14‑5 (Collection differs from composition).** | Authors **SHALL** keep a collection's identity rule and its own belongs-to occurrences distinct from component relations and integrated assembly. A gathering description or `set` trace creates neither belonging nor component status. | Preserve the direct relation and identity boundaries. |
| **CC‑E14‑6 (Notational independence).**    | Core meaning **MUST** remain recoverable independently of one specific notation. Illustrative expressions **SHALL** be marked informative. An expression carrying a reasoning or construction step **SHALL** explain its operation and prerequisites or cite their subject guidance; comparisons and substitutions retain the E.5.2 semantic-mapping duty.                                                          | Ensure longevity and cross‑discipline portability.            |
| **CC‑E14‑7 (Layer direction).**            | Authors **SHALL** avoid back-defining Working-Model terms by their assurance publications or records; dependence is one‑way (Working‑Model → Assurance).                                       | Preserve unidirectional dependence of layers.                 |
| **CC‑E14‑8 (Template compliance).**        | Sections **SHALL** follow the canonical pattern order; *Archetypal Grounding* is mandatory for architectural patterns.                                                                            | Keep patterns comparable and auditable by reading.            |
| **CC-E14-9 (Purpose-selected assurance).** | Authors **SHOULD** select the support needed by the current claim and use. The `postulate`, `inferential`, and `axiomatic` modes are permitted justification postures under their applicable profile, not an ordered ladder of confidence or rigor. Use **Empirical Validation** when observation addresses the actual assurance question. | Preserve branch-specific obligations without demanding promotion through mode labels. |
| **CC-E14-10 (Structural grounding handshake).** | When a publication elects `B.3.5` for a structural parthood or collection-belonging assertion, the author **SHALL** keep the readable claim first, declare `validationMode=axiomatic`, and link through `tv:groundedBy` to exactly one current C.2.1 construction-trace episteme in the applicable C.13 form: `sum` or `slice` for structural parthood, or `set` for collection belonging. Another named current assurance requirement governs its own obligations. Outside those conditions, a direct structural claim has no E.14 mode, link, or trace obligation. In every case, the direct relation pattern and the candidate's identity or reidentification rule decide occurrence and continuity; a trace and mode create neither. | Makes selected construction assurance inspectable while keeping ordinary use, ontology, identity, and currentness separate. |
| **CC‑E14‑11 (Postulate and empirical-result bindings).** | For `validationMode=postulate`, authors **SHALL** state the target claim and scope and **SHOULD** supply brief empirical cues that would ease later validation. That posture alone requires no dated Work, result, performer basis, provenance path, or assurance claim. When evaluation or measurement actually occurred and the current assurance use relies on its result, authors **SHALL** name the target claim, scope, qualification window, dated Work, every performer System, and at least one Method the Work enacted; each performer has an A.13 core and the Work is independently admitted under A.15.1. They **SHALL** use F.6 only when the assurance use also consumes exact Work-assignment attribution; the assignment species and occurrence remain separate A.2.1 claims. Any current MethodDescription or local system-role-kind classification, direct participants or A.6.1 bindings, domain-local result and result episteme, A.10 evidence-provenance path, and B.3 assurance claim remain separate. Expose only identities the bounded assurance use consumes; another named current assurance requirement keeps its own obligations. | Keeps a scoped working claim distinct from completed empirical Work while preserving replayable support when a result is actually used. |
| **CC-E14-12 (F-declaration).**             | Normative Working-Model epistemes **SHALL** declare U.Formality = Fk per C.2.3; F ≥ F3 is recommended for controlled expression. Readability remains a separate Working-Model duty. Any composite-F cap applies to the assessed expression and its essential content or inference under C.2.3, not automatically to external evidence. An assurance use consumes F only when its own argument needs it. | Aligns E.14 with the unified Formality characteristic; avoids obsolete “tiers/modes”. |
| **CC‑E14‑13 (Light records, not thin prose).** | Authors **SHALL NOT** use the Working‑Model-first stance as a reason to strip problem framing, rationale, or worked slices out of the pattern text. Ordinary use may stay light, but readers **MUST** still be able to understand the pattern without nearby project notes. | Keeps human-facing economy from collapsing into under-explained prose. |
| **CC‑E14‑14 (Recognition text before assurance text).** | When a pattern claims a Working‑Model or other human-facing benefit, authors **SHALL** keep recognition-first working text distinct from the heavier assurance text. The assurance text **MAY** refine and justify the working text, but it **SHALL NOT** silently change the recognition-text claim. If the pattern claims broad or transdisciplinary reach, the working text **SHOULD** show heterogeneous situations early, preferably through an `F.16`-style example matrix or an equally explicit alternative. | Keeps Working‑Model-first drafting from collapsing into either thin prose or late-only universality. |

*All obligations above are **conceptual** and apply to thought and prose; they introduce no notational or data‑processing requirements.*

**E — Conceptual Examples (no notation, no data handling)**

1. **Exact skid assembly -> “Component Of”**
   For PumpSkid 7, recover the pump, frame, reservoir, valve set, and other constituents; the direct fastening, coupling, enclosure, terminal, flange, and seal occurrences that obtain; the applicable skid assembly rule; and the skid reidentification rule. The team may publish each truthful **Component Of** claim and stop there. If the publication elects `B.3.5`, keep that readable claim first, link it to one current C.2.1 `sum` trace that reports the basis, and declare `validationMode=axiomatic`. The same parts unconnected or assembled differently do not thereby form PumpSkid 7. A permitted pump replacement may preserve PumpSkid 7. The direct relations and reidentification rule decide; the trace and posture do not.

2. **Cartridges that belong to a bank under its collection rule**
   For a four-cartridge bank, identify the bank and its collection-identity rule, then state which cartridge belongs to it and what makes that belonging begin and end. A C.13 `set` trace can report the collection for assurance. Parallel use, physical proximity, a list, or an author's gathering act does not establish that a cartridge belongs to the bank, does not imply **Component Of**, and does not make the bank an acting system.

3. **Bearer, facet rule, and aspect -> “Aspect Of”**
   For the thermal envelope of one reactor, identify the reactor bearer, the thermal-envelope aspect, the thermal-facet rule, the **Aspect Of** occurrence, and the aspect's identity rule. A C.13 `slice` trace can report those facts. Selecting a view, naming a facet, carving a diagram, or choosing a time window creates no aspect occurrence and no independent system.

> **Notes across the examples**
> • Keep the ordinary working statement first: **Component Of** or **Aspect Of** where that direct relation is admitted, and a subject-specific sentence such as “this cartridge belongs to this bank under the bank's rule” for collection belonging. When an assurance profile calls for a construction account, the linked trace makes that basis inspectable.
> • Structural assertions covered by an elected `B.3.5` profile use Constructive assurance. Direct structural claims outside the profile can stand without E.14 assurance fields; epistemic assertions such as “Representation Of” or “Usage Of” use the direct logical or evidence relation appropriate to the claim.

**F — Resulting Context (after you apply the pattern)**

**What improves**

* **One readable structural vocabulary.** Teams can ask which claim obtains—component parthood, belonging under the collection's own rule, aspect, or another direct relation—without exposing assurance machinery in ordinary work. When a profile calls for support, assurance readers can also recover the participants, direct relation facts, construction rule, and identity conditions behind the published assertion.
* **Explicit identity tests.** Input lists and traces do not decide identity. Different assembly relations can make the same listed inputs another whole; an admitted replacement can preserve one whole. Collections use their own identity rule and belongs-to occurrences; aspects use the bearer, facet, direct relation, and aspect identity.
* **Layer harmony.** Engineer-facing labels live at the same level as other relation names, while their warrants and construction accounts live one step below, keeping human language clean and the claim basis auditable.

**What to watch**

* **Discipline for structural relation kinds.** A published structural assertion is unsafe when its direct relation basis or identity test is missing, even if a trace or `axiomatic` flag exists. Conversely, forcing epistemic links to pretend they are structural over-physicalises knowledge claims; for those, a direct logical or evidence relation is the right currency.
* **Author workload follows the required support.** Day-to-day model authors use working labels; specification authors recover the direct relation occurrence and identity test and keep a current construction account when the publication policy requires it. That account adds authoring and maintenance work where needed. It supports review but does not repair missing world-side facts.

**Invariants you must preserve**

* **Parsimony of construction accounts.** Use `sum` to report integrated assembly, `set` to report a collection, and `slice` to report an aspect. Do not treat them as generative acts or add forms for parallelism or time-slicing; order and time remain with their own patterns.
* **Relation-kind-specific justification.** A direct structural claim needs grounded relation occurrences and its applicable identity test. It needs an inspectable construction account only when an elected profile or named current requirement calls for one. Epistemic claims use the logical or evidence relations they actually need. No assurance route changes the relation kind being claimed.

**Known consequences**

* **Stable queries, fewer surprises.** Working labels retain one direct meaning across disciplines. When a structural assertion is covered by an assurance profile, readers can also follow it to the facts and identity conditions reported in its construction account.
* **Audit trail without jargon.** When construction assurance is current, reviewers can follow a structural claim to its participants, direct relation occurrences, construction rule, identity conditions, and trace edition while everyday collaborators keep using familiar relation names.

