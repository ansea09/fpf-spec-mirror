# First Principles Framework (FPF) - Core Conceptual Specification

> A standards-style pattern language for turning difficult engineering, research, management, and mixed human/AI work into explicit, reviewable, improvable reasoning.

- **Author:** Anatoly Levenchuk, with AI-agent assistance
- **Version:** June 2026
- **Status:** Normative kernel, eternal alpha: already used in working projects and development programs, while still evolving.

This monolith is the AI-agent and tool-assisted working specification for FPF.

Use the Table of Content below to find pattern ids that match the project question. For any substantive answer, open the relevant pattern and apply its Problem frame, Solution, worked slices, and checklist to the project claim or object.

The public FPF readme section after the Table of Content gives human-facing first practical entries. The Preface explains cross-cutting ideas. Pattern bodies carry the normative text to apply. Pattern and headers templates are explained in pattern E.8.

# Table of Content

 **Preface (non-normative)**

| ID & Title                                                                                                                                   | Status    | Concise content reminder — “what belongs here”                                                                                                                                                                                        |
| :------------------------------------------------------------------------------------------------------------------------------------------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| What this specification is (and how to use it) | full text | A practical orientation to the Core Conceptual Specification: what FPF is, which FPF patterns, publications, records, and tools it defines, how Parts A-K fit together, and where to start for different entry situations. |
| Creativity in Open-Ended Evolution and Assurance*                                                                                            | full text | FPF integrates assurance (audits, evidence) and creativity (generating novel ideas) as complementary engines for responsible innovation, providing a structured choreography for creative work from abduction to operation.           |
| Navigating Uncertainty: Building Closed Worlds within an Open World                                                                          | full text | Explains how FPF reconciles Open-World and Closed-World assumptions, using Bounded Contexts to create reliable 'islands of closure' for engineering decisions within an inherently open world.                                        |
| FPF as an Evolutionary Architecture for Thought                                                                                              | full text | Positions FPF as an architecture for the reasoning process itself, designed to sustain key characteristics like auditability, evolvability, and falsifiability by applying architectural thinking to the dynamics of reasoning.       |
| Architectural Characteristic of Thought                                                                                                      | full text | Details the key characteristics of rigorous thought (e.g., Auditability, Evolvability, Composability) and the specific FPF mechanisms designed to preserve them.                                                                      |
| Beyond Cognitive Biases: FPF as a Generative Architecture for Thought                                                                        | full text | Contrasts FPF's generative, structural approach to avoiding cognitive errors with the traditional corrective, diagnostic approach of hunting for biases, framing FPF as a scaffold that makes errors harder to commit.                |
| Thinking Through Writing: The FPF Discipline of Conceptual Work                                                                              | full text | Describes how FPF uses a discipline of "thinking through writing" with conceptual forms (Cards, Tables, Records) to make thought tangible, shareable, and auditable, while remaining tool-agnostic.                                   |
| Descriptive Ontologies vs. A Thinking-Oriented Architecture                                                                                  | full text | Differentiates FPF's goal of orchestrating reasoning from classical ontologies' goal of cataloging existence, emphasizing FPF's focus on objectives, trust, and dynamics.                                                             |
| The "Bitter Lesson" trajectory — compute, data, and freedom over hand‑tuned rules (FPF stance)                                               | full text | How FPF operationalizes the contemporary trend: prefer general models + data + compute + minimal constraints; autonomy budgets; rule‑of‑constraints vs instruction‑of‑procedure; continuous adaptation.                               |
| From Flat Documents to High-Dimensional Truth: The Multi-View Architecture                                                                   | full text | Shows how FPF replaces flat documents with a multi-view architecture: epistemes as slot graphs, engineering views as projections, and MVPK as typed publication surfaces that keep dashboards admissibly tethered to work and evidence. |
| Boundary Statements: Where Language Becomes a System Boundary                                                                          | full text | Introduces the A.6 boundary cluster: why certain sentences carry boundary claims, permissions, commitments, gate pressure, or evidence cues, and how L/A/D/E claim classification keeps those roles evolvable and multi-view safe. |
| Raising Semantic Precision: From Triggers to Math‑Backed Ontics                                                                        | full text | Describes the precision-upgrade discipline behind A.6.P: detect broad load-bearing words, unpack the local ontology, choose a stable mathematical substrate, refactor the model, and mint precise lexemes + guardrails (Tech/Plain twins). |
| The “big storylines” unique to FPF (load‑bearing commitments)                                                                                | full text | Lists the nine core, load-bearing commitments that define FPF's unique architectural and philosophical stance, from its holonic kernel to its explicit treatment of creativity and assurance.                                         |
| Transdisciplinarity as a Meta‑Theory of Thinking                                                                                             | full text | Explains how FPF treats transdisciplinarity as a meta-theory for designing reasoning, using FPF patterns as generative scaffolds grounded in physical reality to bridge disciplinary silos.                                          |
| FPF as a Culinary Architecture for Collective Thought: Why We Formalize “Obvious” Ideas                                                      | full text | Uses the 'culinary architecture' analogy to explain FPF's role in synthesizing 'obvious' ideas into a robust framework for complex, generative problems.                                                                              |
| Intellect Stack (informative Overview)                                                                                                       | full text | Presents a five-part pedagogical map of cognitive skills (Structure → Knowledge → Action → Strategy → Governance) and links them to FPF patterns.                                                                               |
| Purpose, Scope, and Explicit Non‑Goals                                                                                                       | full text | Clarifies FPF's mission as a generative scaffold for thought, its scope as tool-agnostic normative patterns, and what it explicitly is not (e.g., a domain encyclopedia or a specific methodology).                                   |

**Part A - Kernel Architecture Cluster**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| A.0 | **Onboarding Glossary (NQD & E/E‑LOG)** | Stable | *Keywords:* novelty, quality-diversity (NQD), explore/exploit (E/E-LOG), declared set result, typed portfolio publication, SearchSpaceRef, OutcomeSpaceRef, DeclaredSubstrateInterpretiveView, TypedSetViews, ParetoOnly default, scale-probe, BLP. *Queries:* "What terms must I publish when generating, selecting, or shipping a set result?", "How do I explain search-side vs outcome-side spaces and interpretive views on first use?", "How does FPF avoid single-winner bias in creative search?" | **Builds on:** E.2, A.5, C.17-C.19. **Coordinates with:** E.7, E.8, E.10, F.17, A.19.SOURCE-SET-SPACE-SUBSTRATE, A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW, G.5, G.9-G.12. **Constrains:** any pattern/UTS row that describes a generator, selector, declared set result, typed portfolio publication, or set-return publication. |
| ***Cluster A.I - Foundational Ontology*** | | | | |
| A.1 | **Holonic Foundation: Entity → Holon** | Stable | *Keywords:* part-whole composition, system boundary, entity, holon, U.System, U.Episteme. *Queries:* "How does FPF model a system and its parts?", "What is a holon?", "Difference between entity and system." | **Builds on:** P-8 Cross-Scale Consistency. **Prerequisite for:** A.1.1, A.2, A.14, B.1. |
| A.1.1 | **`U.BoundedContext`: The Semantic Frame** | Stable | *Keywords:* local meaning, context, semantic boundary, domain, invariants, glossary, DDD. *Queries:* "How does FPF handle ambiguity?", "What is a Bounded Context in FPF?", "How to define rules for a specific project?" | **Builds on:** A.1. **Prerequisite for:** A.2.1, F.0.1. |
| A.2 | **Role Taxonomy** | Stable | *Keywords:* role, assignment, holder, context, function vs identity, responsibility, U.RoleAssignment. *Queries:* "How to model responsibilities?", "What is the difference between what a thing *is* and what it *does*?" | **Builds on:** A.1, A.1.1. **Prerequisite for:** A.2.1-A.2.6, A.13, A.15. |
| A.2.1 | **`U.RoleAssignment`: Contextual Role Assignment** | Stable | *Keywords:* Standard, holder, role, context, RoleEnactment, RCS/RSG. *Queries:* "How to formally assign a role in FPF?", "What is the Holder#Role:Context Standard?" | **Refines:** A.2. **Prerequisite for:** A.15. |
| A.2.2 | **`U.Capability`: System Ability (dispositional property)** | Stable | *Keywords:* ability, skill, performance, action, work scope, measures. *Queries:* "How to separate ability from permission?", "What is a capability in FPF?" | **Builds on:** A.2. **Informs:** A.15, A.2.3. |
| A.2.3 | **`U.PromiseContent`: Consumer‑facing Promise Clause** | Stable | *Keywords:* promise content, promise content, accessSpec, acceptanceSpec, SLO, SLA, claim scope (G), Work evidence, provider/consumer roles. *Queries:* "What is a promise content in FPF?", "Promise content vs Work vs MethodDescription", "How do access and acceptance differ?", "How is SLO/SLA adjudicated from Work evidence?" | **Builds on:** A.2.2. **Prerequisite for:** F.12. **Used by:** A.2.8, A.6.C, A.6.8. |
| A.2.4 | **`U.EvidenceRole`: The Evidential Stance** | Stable | *Keywords:* evidence, claim, support, justification, episteme. *Queries:* "How does an episteme serve as evidence?", "Modeling evidence roles." | **Builds on:** A.2. **Informs:** A.10, B.3. |
| A.2.5 | **`U.RoleStateGraph`: The Named State Space of a Role**| Stable | *Keywords:* state machine, RSG, role state, enactability, role-state evolution. *Queries:* "How to model the state of a role?", "What is a Role State Graph?" | **Builds on:** A.2.1. **Prerequisite for:** A.15. |
| A.2.6 | **Unified Scope Mechanism (USM): Context Slices & Scopes**| Stable | *Keywords:* scope, applicability, ClaimScope (G), WorkScope, set-valued. *Queries:* "How to define the scope of a claim or capability?", "What is G in F-G-R?" | **Builds on:** A.1.1. **Constrains:** A.2.2, A.2.3, B.3. |
| A.2.7 | **`U.RoleAlgebra`: In-Context Role Relations (`≤`, `⊥`, `⊗`)** | Stable | *Keywords:* role algebra, specialization (`≤`), incompatibility (`⊥`), bundles (`⊗`), separation of duties (SoD), requiredRoles substitution. *Queries:* "What does `RoleS ≤ RoleG` mean in FPF?", "How do I encode Separation of Duties with `⊥`?", "How do role bundles (`⊗`) work?" | **Builds on:** A.2. **Prerequisite for:** A.15, A.2.5. |
| A.2.8 | **`U.Commitment`: Deontic Commitment Object** | Stable | *Keywords:* commitment, deontics, obligation, permission, prohibition, modality normalization, scope+validity window, adjudication hooks, evidenceRefs, BCP‑14 (RFC 2119/8174). *Queries:* "How to represent MUST/SHALL as a lintable object?", "How to keep deontics separate from admissibility gates?", "How to make commitments auditable via evidence hooks?" | **Refines:** A.2. **Builds on:** A.2.1, A.2.3, A.2.6, A.7, A.15.1. **Used by:** A.6.B (Quadrant D), A.6.C. |
| A.2.9 | **`U.SpeechAct`: Communicative Work Object** | Stable | *Keywords:* speech act, communicative work, approval/authorization/publication/revocation, provenance, act≠utterance≠carrier, judgement context, window/freshness, institutes.*. *Queries:* "How to model approvals/authorizations as Work?", "How to separate act vs utterance vs carrier?", "How to link commitments to instituting acts without commitment-by-publication?" | **Refines:** A.2. **Builds on:** A.2.1, A.2.6, A.7, A.10, A.15.1. **Used by:** A.2.8, A.6.C (utterance/instituting-act hook). |
| ***Cluster A.II - Transformation Engine*** | | | | |
| A.3 | **Transformer Constitution (Quartet)** | Stable | *Keywords:* action, causality, change, System-in-Role, MethodDescription, Method, Work. *Queries:* "How does FPF model an action or a change?", "What is the transformer quartet?" | **Builds on:** A.2. **Prerequisite for:** A.3.1, A.3.2, A.15. |
| A.3.1 | **`U.Method`: The Abstract Way of Doing** | Stable | *Keywords:* recipe, how-to, procedure, abstract process. *Queries:* "What is a Method in FPF?", "Difference between Method and Work." | **Refines:** A.3. **Prerequisite for:** A.15. |
| A.3.2 | **`U.MethodDescription`: The Recipe for Action** | Stable | *Keywords:* specification, recipe, SOP, code, model, `U.Episteme`. *Queries:* "How to document a method?", "What is a MethodDescription?" | **Refines:** A.3. **Informs:** A.15. |
| A.3.3 | **`U.Dynamics`: The Law of Change** | Stable | *Keywords:* state evolution, model, simulation, state space. *Queries:* "How to model state transitions or system dynamics?", "Difference between a Method and Dynamics." | **Builds on:** A.19. **Informs:** B.4. |
| ***Cluster A.III - Time & Evolution*** | | | | |
| A.4 | **Temporal Duality & Open-Ended Evolution Principle** | Stable | *Keywords:* design-time, run-time, evolution, versioning, open-ended state change, continuous improvement. *Queries:* "How does FPF handle plan vs. reality?", "How are systems updated?" | **Builds on:** P-10 Open-Ended Evolution. **Prerequisite for:** B.4. |
| ***Cluster A.IV - Kernel Modularity*** | | | | |
| A.5 | **Open-Ended Kernel & Extension Layering** | Transitional stub | *Keywords:* FPF architecture, specialization vs dependancy hierarhies, modularity, extensibility. *Queries:* "What is the architecture of FPF?", "How are new domains added?" | **Builds on:** P-4, P-5. |
| ***Cluster A.IV.A - Signature Stack & Boundary Discipline (A.6.*)*** | | | | |
| A.6 | **Signature Stack & Boundary Discipline** | Stable | *Keywords:* boundary, signature stack, boundary claim-classification fields, A.6.B L/A/D/E claims, authority-wording split, register-backed status boundary, promise/commitment/API/policy wording, probe/order/frame/export/state-reading claims. *Queries:* "How do I classify boundary statements?", "Where do probe, frame, export, and state-reading claims belong?", "When does authority-looking wording split into source, gate, work, assurance, or boundary claims?", "When is a pass, badge, tile, or status display only a publication of a register-backed source?" | **Builds on:** E.8, A.6.0, A.6.1, A.6.3, E.17.0, E.17, A.7, F.18, E.10.D2, E.10 publication face, form, unit, and carrier discipline. **Coordinates with:** A.6.B, A.6.P, C.26, C.26.1, F.9, A.10, A.15, B.3, E.17.EFP, A.20, A.21, E.19. |
| A.6.RSIG | **Recognition Signatures for Descriptions** | Stable | description-recognition signature; encountered carrier vs defining `U.Episteme`; API/access description not promise; method applicability note; false neighboring description | `A.6`, `A.6.P`, `F.18`, `E.10` |
| A.6.B | **Boundary Norm Square (Laws / Admissibility / Deontics / Work-Effects)** | Stable | *Keywords:* boundary norm square, atomic claims, L/A/D/E claim classification, laws vs gates vs commitments vs evidence, admissible use, non-admissible use, claim IDs, triangle decomposition. *Queries:* "What is the Boundary Norm Square in FPF?", "How do I decompose probe-coupled or mixed boundary statements?", "Where do RFC keywords and use conditions belong in FPF patterns?" | **Builds on:** E.8, A.6.0, A.6.1, A.6.3, E.17.0, E.17, A.7, F.18, E.10.D2, E.10 publication face, form, unit, and carrier discipline. **Coordinates with:** A.6, A.6.P, C.26.1, A.10, B.3. |
| A.6.C | **Contract Unpacking for Boundaries** | Stable | *Keywords:* contract bundle unpacking, SLA/guarantee claim classification, promise content (promise content) ≠ work, promise-act/utterance/commitment separation, Boundary Norm Square (L/A/D/E), MVPK faces “no new semantics”. *Queries:* "How to unpack contract language into promise content / utterance / commitment / work+evidence?", "How to prevent interface-as-agent / contract soup mistakes?", "How to stop MVPK faces becoming ‘second contracts’?", "When contract talk includes service-cluster tokens, what gets unpacked first?" | **Builds on:** A.6, A.6.B, A.6.8, A.7, A.2.3, A.2.8, A.2.9, E.10, E.17. **Coordinates with:** F.12, F.18. |
| A.6.0| **U.Signature — Universal, law‑governed declaration** | Stable | *Keywords:* signature, vocabulary, laws, applicability, bounded context. *Queries:* "What is the universal signature block?", "Where do laws vs. implementations live?" | **Placement:** Kernel; **Coordinates:** A.6.1. |
| A.6.1 | **U.Mechanism - Law‑governed application to a SubjectKind over a BaseType** | Stable | Keywords: Mechanism, OperationAlgebra, LawSet, AdmissibilityConditions, Transport, Bridge‑only. Queries: "How to define a mechanism like USM/UNM?", "Where do operational guards live?", "How to handle cross‑context transport?" | **Builds on:** A.6.0, E.10.D1. **Instances:** USM (A.2.6), UNM (A.19). |
| A.6.2 | **U.EffectFreeEpistemicMorphing - Effect-Free Morphisms of Epistemes** | Stable | Effect-free, law-constrained episteme-to-episteme morphisms over ClaimGraph, EntityOfConcern, grounding holon, viewpoint, reference scheme, representation scheme, and metadata; preserve or retarget EntityOfConcern only through declared change mode. | **Builds on:** A.1, A.6.0, A.6.1, A.6.5, C.2.1, E.10.D2, C.3.*. **Used by:** A.6.3, A.6.4, E.17.0, E.17, E.18, KD-CAL mapping rules. |
| A.6.3 | **U.EpistemicViewing - EntityOfConcern-Preserving Morphism** | Stable | EntityOfConcern-preserving effect-free projection between epistemes: content, representation, viewpoint, or reference scheme may change, but `entityOfConcernRef` stays fixed unless A.6.4 retargeting is explicitly opened. | **Builds on:** A.6.0, A.6.2, A.6.5, A.7, E.10.D2, C.2.1, C.2. **Used by:** E.17.0, E.17, E.17.1, E.17.2, E.18, B.5.3, KD-CAL view operators. |
| A.6.3.CSC | **Controlled Semantic Coarsening** | Stable | *Keywords:* controlled semantic coarsening, source-bearing episteme or source publication, coarsened rendering, narrower admissible use, non-admissible downstream use, reopen trigger, redaction, dashboard tile, lookup handle, state-representation shortcut. *Queries:* "When may a summary or redaction stand in only for narrow use?", "What is Controlled Semantic Coarsening in FPF?", "When must a coarsened rendering reopen the source-bearing episteme or source publication?" | **Builds on:** A.6.3, A.6.3.CR, A.6.3.RT, E.17.EFP, A.6.P, E.8, E.10, E.19, F.18. **Coordinates with:** C.26, C.26.1, E.17.ID.CR, F.9, F.9.1, A.15, A.6.4, A.20, A.21. |
| A.6.3.CR | **ConservativeRetextualization - entityOfConcernRef-preserving textual re-expression** | Stable | Textual re-expression, summary, report rewrite, translation, or filtering that preserves `entityOfConcernRef`, keeps source tether and omission/loss visible, and exits to explanation, representation change, retargeting, bridge, work, evidence, gate, or assurance patterns when those claims are being made.
 | **Builds on:** A.6.3, A.6.2, A.7, E.10.D2, E.17.0, E.17, F.9, F.18, E.10. **Coordinates with:** A.6.3.CSC, A.6.3.RT, E.17.EFP, E.17.ID.CR, A.6.4, B.5.2, A.15. |
| A.6.3.RT | **RepresentationTransduction - entityOfConcernRef-preserving representation-scheme transition** | Stable | Representation-scheme or reasoning-medium transition that preserves `entityOfConcernRef`, makes recoverability and loss visible, and blocks geometry, notation, carrier work, decode work, or TGA-flow language from becoming hidden ontology or action force. | **Builds on:** A.6.3, A.6.2, A.7, E.10.D2, C.2.7, E.17.0, E.17, F.9, F.18. **Coordinates with:** A.6.3.CSC, C.26, A.6.3.CR, E.17.EFP, E.17.ID.CR, A.6.4, A.15, A.20, A.21. |
| A.6.4 | **U.EpistemicRetargeting - EntityOfConcern-Retargeting Morphism** | Stable | Effect-free episteme-to-episteme morphism that intentionally changes `entityOfConcernRef` under a declared KindBridge, invariant, loss boundary, and admissible use while preserving only the commitments that the bridge makes reviewable. | **Builds on:** A.6.2, A.6.3, A.6.5, A.7, C.2.1, C.2, C.3, F.9, E.10.D2, E.18. **Used by:** E.18 StructuralReinterpretation, KD-CAL/LOG-CAL retargeting rules, Fourier-style and data-model retargetings. |
| A.6.P | **Relational Precision Restoration (RPR) — Kind-Explicit Qualified Relation Discipline** | Stable | *Keywords:* relation precision restoration, under-specified relational language, support/support-headed wording, selected support reading, RelationKind, QualifiedRelationRecord, coupling, probe, measurement, export, endpoint referential compression, lexical guardrails, language-state seam. *Queries:* "How do I repair an overloaded relation word without lexicon-only cleanup?", "How do I unpack support without minting a generic SupportRelation?", "How do I keep coupling/probe/measurement/export wording kind-explicit?", "When should quality/action/sameness/wholeness/QL wording apply another governing pattern?" | **Builds on:** A.6, A.6.B, A.6.S, A.6.0, A.6.5, E.8, E.10, F.18. **Coordinates with:** A.2.4, A.2.6, A.7, A.10, C.2.1, C.2.2a, C.3.3, C.16.Q, C.26, E.17, F.9, F.17. **Specialised by:** A.6.A, A.6.5, A.6.6, A.6.8, A.6.9, A.6.H. |
| A.6.A | **U.ActionInvitationPrecisionRestoration — Affordance / Action-Invitation Precision Restoration (ACT-INV)** | Stable | *Keywords:* affordance, action invitation, action-first language, post-threshold classification, A.15 docking, language-state seam. *Queries:* "How do I repair overloaded affordance language in FPF?", "When does action-guiding language become an action invitation?", "How does A.6.A differ from early cue routing?" | **Builds on:** A.6.P, A.15, C.2.2a, A.16, B.4.1, F.9. **Coordinates with:** C.16.Q, B.5.2.0. |
| A.6.F | **Function and Functional Precision Restoration (RPR-FUNCTION)** | Stable | *Keywords:* function wording, functional architecture, FunctionalStructure, function-use repair, capability/effect, work/method boundary, module allocation, mathematical function. *Queries:* "When is functional architecture a structure kind rather than a separate ontology?", "How do I repair function-like wording?", "When is a function a capability, method, work, role, quality, module allocation, or mathematical mapping?" | **Builds on:** A.6.P, A.6.5, A.7, C.30, C.30.ASV, C.29. **Coordinates with:** A.6.M, A.15, C.16.Q, A.6.0, A.6.5, A.6.B, A.6.C, A.6.8, E.18, C.30.TGA-FLOW-REL. |
| A.6.M | **Module Relation Repair** | Stable | *Keywords:* module relation, component, interface, port, platform, layer, stack, open architecture, substitutability, interface specification. *Queries:* "When is a module relation being claimed?"
, "How do I keep functional links, signatures, ports, and implemented interfaces distinct?", "When does open architecture require module-interface repair?" | **Builds on:** A.6.P, A.6.5, A.6.B, C.30, C.30.ASV, A.6.F. **Coordinates with:** C.31, C.31.RSA, E.18, C.30.TGA-FLOW-REL, A.10, B.3, A.20, A.21, C.28, E.20, G.5, C.11. |
| A.6.5 | **U.RelationSlotDiscipline - SlotKind / ValueKind / RefKind discipline for n‑ary relations (with slot‑operation lexicon)** | Stable | *Keywords:* slot, argument position, value, reference, signature, substitution, pass-by-value, pass-by-reference. *Queries:* “How do I declare positions and references in relations?”, “How do we stop mixing roles, values and ids in signatures?”, “How does SlotKind/ValueKind/RefKind interact with EntityOfConcern / Description / specification-use and Epistemes?” | **Builds on:** A.6.0 (U.Signature), A.1 (Holon), A.7 (Strict Distinction), E.8 (pattern authoring discipline), E.10 (LEX-BUNDLE; Tech/Plain registers). **Used by:** C.2.1 (U.EpistemeSlotGraph), A.6.2–A.6.4 (episteme morphisms), B.5.* (RoleEnactment), C.3.* (Kinds & KindSignature), E.17.0 (U.MultiViewDescribing), discipline-packs for methods/services. |
| A.6.6 | **U.BaseDeclarationDiscipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)** | Stable | *Keywords:* base declaration, basedness, baseRelation, SWBD, witnesses, scope, Γ_time, anchoring, support-as-basedness, rebase, retime, rescope. *Queries:* "What is U.BaseDeclarationDiscipline?", "How to model base-dependence without anchoring?", "When is support really base-dependence?", "What is a ScopedWitnessedBaseDeclaration (SWBD)?" | **Builds on:** A.6.0, A.6.5, A.2.6, A.2.4, A.7, E.8, E.10. **Coordinates with:** A.10, A.14, C.2.1, A.6.3-A.6.4, C.3.3, E.18, F.9, F.15, F.18. **Used by:** base-relative admissibility/calibration/attribution patterns; anchor* and support-as-basedness rewrites into explicit `baseRelation(dependent, base)`. |
| A.6.7 | **`MechSuiteDescription` — Description of a set of distinct mechanisms** | Stable | *Keywords:* mechanism suite, distinct mechanisms, suite obligations, spec pins, CN-Spec, CG-Spec, P2W, planned baseline, crossing visibility. *Queries:* "What is a MechSuiteDescription?", "How to describe a bundle of distinct mechanisms without using MechFamilyDescription?", "How do suite obligations differ from gate decisions?" | **Builds on:** E.8, A.6.1, A.6.5, E.10, E.19. **Coordinates with:** E.18, A.21. **Used by:** Part G universalization; CHR mechanism stacks. |
| A.6.8 | **Service Polysemy Unpacking (RPR-SERV)** | Stable | *Keywords:* service polysemy, service situation, interface semantics, promise content, provider principal, service/cell analogy, boundary exchange, viability envelope, API read/export. *Queries:* "How do I unpack service talk in FPF?", "When is an API read interface semantics rather than state evidence?", "When does service viability apply C.26.3?" | **Builds on:** A.6.P, A.6.B, A.6.5, A.2.3, A.2.8, A.2.9, A.15, E.10, F.17, F.18. **Coordinates with:** A.6.C, A.7, C.26.1, C.26.3, F.8, E.15. |
| A.6.9 | **`U.CrossContextSamenessDisambiguation` — Repairing cross-context “same / equivalent / align” via explicit Bridges (RPR-XCTX)** | Stable | *Keywords:* cross-context sameness, bridge, alignment, mapping, direction, substitution licence, loss notes, CL, SenseCells, weakest-link. *Queries:* "How to disambiguate 'same' across contexts?", "How to avoid silent inversion in mappings?", "Naming-only vs substitution bridge". | **Builds on:** A.6.P, F.9, E.10.D1, A.7. **Coordinates with:** E.17, C.3.3, A.6.6, F.7/F.8. |
| A.6.S | **U.SignatureEngineeringPair — Constructive signature engineering (ConstructorSignature + TargetSignature)** | Stable | *Keywords:* signature engineering, TargetSignature, ConstructorSignature, two-signature arrangement, EFEM, editioning, retargeting, slot/base change lexicon, MVPK views (no new semantics), claim register, no epistemic agency. *Queries:* "What is U.SignatureEngineeringPair in FPF?", "How do I model TargetSignature vs ConstructorSignature (and keep Work out of edits)?", "How do slot/base change verbs compose into a reproducible signature evolution account?" | **Builds on:** A.6.0, A.6.2, A.6.3, A.6.4, A.6.5, A.6.6, A.6.B, A.3, A.7, A.12, C.2.1, E.17, E.10. **Coordinates with:** E.18, E.19. |
| A.6.H | **Wholeness Language Unpacking (RPR-WHOLE)** | Stable | *Keywords:* wholeness, integrity, part-of, boundary, environment, mereology, completeness, order/time, publication-carrier and EntityOfConcern/Description distinction, role-method-work. *Queries:* "How to unpack 'whole/part/integrity' in FPF?", "RPR-WHOLE trigger words", "ComponentOf vs ConstituentOf vs PortionOf vs MemberOf vs PhaseOf", "How to separate order/time from mereology?" | **Builds on:** A.6.P, A.6.5, A.7. **Coordinates with:** A.14, B.1.1, B.1.4, A.15. |
| ***Cluster A.V - Constitutional Principles of the Kernel*** | | | | |
| A.7 | **Strict Distinction (Clarity Lattice)** | Stable | *Keywords:* category error, EntityOfConcern ≠ Description episteme, Role ≠ Work, ontology. *Queries:* "How to avoid common modeling mistakes?", "What are FPF's core distinctions?" | **Builds on:** A.1, A.2, A.3. **Constrains:** all patterns. |
| A.8 | **Universal Core (C-1)** | Stable | *Keywords:* universality, transdisciplinary, domain-agnostic, generalization. *Queries:* "How does FPF ensure its concepts are universal?" | **Builds on:** P-8. **Constrains:** Kernel-level `U.Type`s. |
| A.9 | **Cross-Scale Consistency (C-3)** | Stable | *Keywords:* composition, aggregation, holarchy, invariants, roll-up. *Queries:* "How do rules compose across different scales?", "How to aggregate metrics safely?" | **Builds on:** A.1, A.8. **Prerequisite for:** B.1. |
| A.10 | **Evidence Graph Referring (C-4)** | Stable | *Keywords:* evidence, traceability, provenance, evidence carrier, claim support, authority-reliance evidence path, status register, register excerpt, generated-explanation source support, exact authority reference, probe/distributed/export/causal evidence, SCR/RSCR. *Queries:* "How are claims supported by evidence?", "When does a generated explanation become source-backed evidence rather than approval or authorization?", "How do I keep evidence carriers separate from the state they report?", "When is a credential, pass, badge, or status display only an excerpt of a governing register entry or source `U.EpistemePublication`?" | **Builds on:** A.1. **Coordinates with:** A.6, A.15, B.3, E.17.EFP, A.20, A.21, C.16, F.9, C.26.1, C.26.2, C.26.3, C.28. |
| A.11 | **Ontological Parsimony (C-5)** | Stable | *Keywords:* minimalism, simplicity, Occam's razor, essential concepts. *Queries:* "How does FPF avoid becoming too complex?", "Rule for adding new concepts." | **Builds on:** P-1 Cognitive Elegance. **Constrains:** all new `U.Type` proposals. |
| A.12 | **External Transformer & Reflexive Split (C-2)** | Stable | *Keywords:* causality, agency, self-modification, external agent, control loop. *Queries:* "How to model a self-healing or self-calibrating system?", "What is the external transformer principle?" | **Builds on:** A.3. **Prerequisite for:** B.2.5. |
| A.13 | **The Agential Role & Agency Spectrum** | Stable | *Keywords:* agency as role, agency spectrum, contextual role assignment, autonomy grading, substrate-neutral autonomy. *Queries:* "How does FPF model agency without minting a `U.Agent` type?", "How do I grade autonomy on an evidence-backed spectrum?" | **Builds on:** A.2, A.2.1, A.12. **Informs:** C.9 Agency-CHR, E.16. |
| A.14 | **Advanced Mereology: Components, Portions, Aspects & Phases**| Stable | *Keywords:* mereology, part-of, ComponentOf, PortionOf, PhaseOf, composition. *Queries:* "How to model different kinds of 'part-of' relationships?" | **Refines:** A.1. **Prerequisite for:** B.1.1. |
| A.15 | **Role-Method-Work Alignment (Contextual Enactment)** | Stable | *Keywords:* role-method-work distinction, `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, actual `U.Work`, contextual enactment, coordinated-work evidence, work admission display, source-restoration boundary. *Queries:* "How do role, method, plan, and work stay distinct in FPF?", "When can coordinated work evidence a state that no one report carries?", "When is authorization-looking material a source-restoration problem rather than work enactment?", "When does something that looks like permission or prohibition to start work need the governing FPF pattern and project-side record behind it first?" | **Integrates:** A.2, A.4, A.12. **Builds on / coordinates with:** A.6, A.10, B.3, E.17, E.17.EFP, A.20, A.21, and C.26.2. **Prerequisite for:** A.15.1-A.15.4, C.24, E.16. |
| A.15.1 | **`U.Work`: The Record of Occurrence** | Stable | *Keywords:* execution, event, run, actuals, log, occurrence. *Queries:* "What is a Work record?", "Where are actual resource costs stored?" | **Refines:** A.15. **Used by:** B.1.6, all Part D. |
| A.15.2 | **`U.WorkPlan`: The Schedule of Intent** | Stable | *Keywords:* plan, schedule, intent, forecast. *Queries:* "How to model a plan or schedule?", "Difference between a WorkPlan and a MethodDescription." | **Refines:** A.15. **Informs:** `U.Work`. |
| A.15.3 | **`SlotFillingsPlanItem` — Planned Slot-Fillings Baseline (WorkPlanning PlanItem)** | Stable | *Keywords:* planned baseline, slot-bearing description, planned filler, edition pins, `Γ_time` selector, guard pins, WorkPlanning, P2W seam, variance trail. *Queries:* "What is SlotFillingsPlanItem in FPF?", "How to keep planned slot filling separate from FinalizeLaunchValues?", "How to pin editions and time in WorkPlanning baselines?" | **Builds on:** A.15.2, A.6.5, E.10.D1, E.17, E.18, E.19. **Used by:** A.6.7 (suite spec pins), Part G universalization, suite-specific and kit-specific planned baselines. |
| A.15.4 | **Work-Relevant Source Restoration** | Stable | *Keywords:* work-relevant source restoration, dashboard display, credential view, generated explanation, copied statement, provenance mark, required project-side FPF kind and reference, admissible next project move, blocked overread, P2W load and position, approval-looking display. *Queries:* "Which project-side FPF kind and reference is needed before a dashboard or explanation can guide work?", "When is a visible item only source-finding before work support or reliance support?", "How do I keep publication, display, or cue separate from work, evidence, gate passage, or engineering justification?" | **Builds on:** A.15, E.17, C.2.1. **Coordinates with:** A.10, B.3, A.6, A.2.1, A.2.8, A.2.9, A.20, A.21, and E.17.EFP. |
| A.16 | **Language-State Transduction Coordination** | Stable | *Keywords:* language-state, transduction, admissible moves, reopen, sketch-backoff, respecify, retire, handoff. *Queries:* "How do governed epistemes move across the language-state chart?", "What are the admissible move kinds in FPF?" | **Builds on:** C.2.2a, C.2.LS, A.19. **Coordinates with:** A.16.0-A.16.2, B.4.1, E.18. |
| A.16.0 | **`U.LanguageStateTransductionTrajectory` — Optional trajectory-account normal form** | Stable | *Keywords:* trajectory account, lineage, fork, merge, supersedes, handoff, heavy history. *Queries:* "When do I publish a language-state trajectory account?", "How does FPF record lineage and branch history?" | **Builds on:** A.16, C.2.2a, E.17, E.18. **Used by:** A.16.1, A.16.2, B.4.1, B.5.2.0. |
| A.16.1 | **`U.PreArticulationCuePack`** | Stable | *Keywords:* cue pack, pre-articulation, early publication, cue nucleus, primary witness, candidate route cues. *Queries:* "What is a PreArticulationCuePack?", "How do I preserve early cues before `RoutedCueSet` publication?" | **Builds on:** A.16, C.2.2a, C.2.LS. **Coordinates with:** B.4.1, A.16.2. |
| A.16.2 | **Reopen / SketchBackoff / Respecify** | Stable | *Keywords:* reopen, backoff, respecify, retire, retreat, branch withdrawal, authority withdrawal. *Queries:* "How do I admissibly reopen or back off a language-state publication?", "How do I retire a branch without silent deletion?" | **Builds on:** A.16, A.16.0, C.2.2a. **Coordinates with:** A.6.P, B.4.1. |
| A.17 | **A.CHR-NORM — Canonical “Characteristic” & rename (Dimension/Axis → Characteristic)** | Stable | *Keywords:* characteristic, measurement, property, attribute, dimension, axis. *Queries:* "What is the correct term for a measurable property?", "How to define a metric?" | **Prerequisite for:** A.18, A.19, C.16. |
| A.18 | **A.CSLC-KERNEL — Minimal CSLC in Kernel (Characteristic/Scale/Level/Coordinate)** | Stable | *Keywords:* CSLC, Characteristic, Scale, Level, Coordinate, polarity, ordinal vs cardinal scale, one-characteristic-one-scale rule, lawful comparability, no illegal averaging, measurement interpretability. *Queries:* "What must be declared before a value is interpretable?", "When can two measurements be compared?", "Why can ordinal labels not be averaged?" | **Builds on:** A.17. **Coordinates with:** C.16, A.19, A.19.CN, G.0, B.3. **Prerequisite for:** measurement, scoring, comparison, aggregation, and CHR mechanism patterns. |
| A.19 | **CharacteristicSpace & Dynamics Hook (A.CHR-SPACE)** | Stable | *Keywords:* CharacteristicSpace, U.Dynamics.stateSpace, state trajectories, declared Characteristics and Scales, subspace, embedding, product, structural overlays, coordinatewise comparability, role-specific space refs stay outside A.19. *Queries:* "How do I declare the state space a dynamics model moves through?", "How do Characteristics become a multi-coordinate state space?", "What stays inside A.19 and what belongs in source-set/space substrate or interpretive-view patterns?" | **Builds on:** A.17, A.18, A.2.5. **Coordinates with:** C.16, A.19.CN, A.19.SOURCE-SET-SPACE-SUBSTRATE, A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW, A.19.CHR, G.0, E.18, A.3.3. **Prerequisite for:** CHR mechanisms and dynamics models that quantify over trajectories. |
| A.19.ECS | **Evaluation CharacteristicSpace Construction** | Stable | Constructs or repairs the evaluation `CharacteristicSpace` for one evaluated object kind and use: characteristics, scales, value meanings, evidence rules, missingness, protected trade-offs, status meanings, stop or reopen conditions, and declarative governing-neighbour relations without route/reference apparatus. | **Builds on:** A.17-A.19, C.16, F.18. **Coordinates with:** E.22, E.23, C.25, E.21, E.9.DA, E.2.DA, E.8.ECSPF, F.19. |
| A.19.SPR | **State-Family Precision Restoration** | Stable | Repairs state, status, posture, readiness, stance, currentness, and close state-family wording by recovering bearer, state frame or governing pattern, value set, admissible use, blocked overread, and reopen condition. | **Builds on:** E.10, E.10.ARCH, A.19, A.3.3, C.2.2a, A.16.*, A.10, B.3, A.20, A.21, C.27, C.29, E.17, E.9.DA, E.21, F.18. **Coordinates with:** A.17, A.18, C.16, C.16.P, C.16.Q, A.6.P, C.2.P, C.30.P, E.8, E.19, E.11. |
| A.19.SOURCE-SET-SPACE-SUBSTRATE | **Source-Set and Search/Outcome-Space Substrate** | Stable | *Keywords:* source set, search-side space ref, outcome-side space ref, source-set/space substrate, SpaceRefRelationKind, SourceToOutcomeRelation, DistortionPosture, SourceSetRef, sameDeclaredSpaceAs, distinctDeclaredSpaceFrom. *Queries:* "How do I declare one source set plus search-side and outcome-side refs?", "How do I keep source-to-outcome relation and distortion posture explicit?", "When do search and outcome refs resolve to the same declared CharacteristicSpace?" | **Builds on:** A.19, A.17, A.18. **Coordinates with:** C.18, C.19, G.5, G.10, A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW, A.6.P, A.0. **Specialized by:** A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW and later interpretive-view or atlas specializations. |
| A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW | **Declared-Substrate Interpretive View** | Stable | *Keywords:* declared-substrate interpretive view, thin interpretation, atlas-form interpretation, DeclaredSubstrateInterpretiveView, DeclaredSubstrateAtlasView, TraditionAtlasView, TypedSetViews, interpretive qualifiers, interpretive-only reading. *Queries:* "When do I use an interpretive view over an already-declared substrate?", "When is thin interpretation enough and when do I need atlas form?", "How does TraditionAtlasView stay a local specialization instead of the generic head?" | **Builds on:** A.19.SOURCE-SET-SPACE-SUBSTRATE, A.19, A.6.3, E.17.0, E.17. **Coordinates with:** G.2, G.5, G.10, C.19, C.24, A.6.P, A.0. **Specialized locally by:** DeclaredSubstrateAtlasView and `TraditionAtlasView` under G.2. |
| A.19.CN| **CN-frame (comparability & normalization)** | Stable | *Keywords:* CN-frame, CN-Spec, chart, comparability modes, normalization refs, indicator policy refs, Γ-fold governance, registry, bridges, CL/loss notes, WLNK discipline, conformance checklist, SCR/RSCR harness, RSG admission hooks. *Queries:* "What is a CN-frame in FPF?", "How does CN-Spec govern comparability and normalization by reference?", "How do CN-frames use bridges and CL for cross-context reuse?", "What are the conformance and regression checks for CN-frames?" | **Builds on:** A.19. **Coordinates with:** A.6.1 (mechanism intension cards), C.16 (evidence/backing), F.9 (Bridges & CL), G.0 (CG-Spec legality gate). |
| A.19.CHR | **`CHRMechanismSuite` — CHR mechanism-suite anchor (suite obligations + P2W planned baseline)** | Stable | *Keywords:* CHR suite, characterization core, CN-Spec, CG-Spec, legality gate, suite obligations, set-return selection, tri-state guard decision, crossing visibility, Bridge-only transport, penalties→R_eff, planned baseline, `SlotFillingsPlanItem`, P2W seam, no hidden scalarization, no hidden thresholds. *Queries:* "What is CHRMechanismSuite in FPF?", "How do CHR mechanisms cite CN-Spec/CG-Spec?", "How to enforce planned slot filling in WorkPlanning only?", "How to keep UNM/UINDM/ULSAM explicit (no hidden tails)?" | **Builds on:** A.6.7, A.15.3, A.6.1, A.6.5, A.19, G.0, E.18, E.10, E.19. **Coordinates with:** A.21, G.5, G.10, C.23. **Used by:** Part G universalization; CHR mechanism stacks. |
| A.19.UNM | **Unified Normalization Mechanism (UNM)** | Stable | *Keywords:* normalization, `CV→NCV`, `≡_UNM`, `NormalizationMethodId`, `NormalizationMethodInstanceId`, `NormalizationInvariant[*]`, `NormalizationFixSpec`, validity window (no implicit “latest”), fail-closed tri-state guard (`pass|degrade|abstain`), `CN-Spec.normalization`, `CN-Spec.comparability.mode`, Bridge-only transport + ReferencePlane/CL pins, penalties→`R`/`R_eff` only. *Queries:* "What is UNM in FPF?", "How does FPF normalize coordinate values (CV→NCV)?", "What is ≡_UNM and why quotients/fix matter?", "How does CN-Spec.comparability.mode route normalization-based comparability?" | **Builds on:** A.19.CN, A.6.1, A.6.5, A.19.CHR, A.17–A.18, C.16, G.0, E.18, E.20, F.18. **Used by:** A.19.CHR, A.19.USCM, A.19.CPM, A.19.SelectorMechanism. **Coordinates with:** G.2, B.3. |
| A.19.UINDM | **Unified Indicatorization Mechanism (UINDM)** | Stable | *Keywords:* indicatorization, indicator set, `IndicatorChoicePolicy`, `CN-Spec.indicator_policy`, CHR suite stage `indicatorize`, tri-state admissibility (`pass|degrade|abstain`), evidence-gated indicator choice, Bridge+CL transport visibility, “no NCV⇒indicator”. *Queries:* "What is UINDM in FPF?", "How does FPF choose indicators?", "Difference between measurable characteristic and indicator", "How to make indicator choice auditable?" | **Builds on:** A.19.CN, A.6.1, A.6.5, A.19.CHR. **Used by:** A.19.CHR. **Coordinates with:** G.0, G.2, E.20, F.18. |
| A.19.USCM | **Unified Scoring Mechanism (USCM)** | Stable | *Keywords:* scoring, score profile, `ScoringMethodDescription`, ScaleComplianceProfile (SCP), CSLC-lawful transforms, `CG-Spec.MinimalEvidence`, tri-state admissibility (`pass|degrade|abstain`), “no implicit UNM”, vector scores by default, CHR suite stage `score`. *Queries:* "What is USCM in FPF?", "How does FPF do lawful scoring (SCP-first)?", "How are scoring methods pinned and audited in CHR?", "How does USCM handle unknowns and evidence?" | **Builds on:** A.19.CN, A.6.1, A.6.5, A.19.CHR, G.0, A.18, C.16. **Used by:** A.19.CHR. **Coordinates with:** UNM, ULSAM, CPM, SelectorMechanism, G.2, E.20, F.18. |
| A.19.ULSAM | **Unified Lawful Scale Aggregation Mechanism (ULSAM)** | Stable | *Keywords:* lawful aggregation, scale-lawful fold, `fold_Γ?`, `ΓFoldRef`, `CG-Spec.Γ_fold`, `CG-Spec.SCP`, `MinimalEvidence`, tri-state guard (`pass|degrade|abstain`), contributor set, no hidden aggregation, penalties→`R_eff` only. *Queries:* "What is ULSAM in FPF?", "How does FPF do lawful aggregation / Γ-fold?", "Why is fold_Γ a separate CHR stage?", "How to avoid ordinal averaging in FPF?" | **Builds on:** A.19.CN, G.0, A.18, A.6.1, A.6.5, A.19.CHR, B.3. **Used by:** A.19.CHR. **Coordinates with:** G.2, E.20, F.18. |
| A.19.CPM | **Unified Comparison Mechanism (CPM)** | Stable | *Keywords:* comparison, comparator, `ComparatorSpecRef`, `ComparatorSet`, set-valued comparison outcome, partial order, tri-state admissibility (`pass|degrade|abstain`), `MinimalEvidence`, “no hidden scalarization/totalization”, Bridge+CL transport, penalties→`R_eff` only. *Queries:* "What is CPM in FPF?", "How does FPF compare two profiles admissibly?", "Why comparison outputs are set-valued?", "How does CPM handle unknown evidence?" | **Builds on:** A.19.CN, A.6.1, A.6.5, A.19.CHR, G.0, A.18. **Used by:** A.19.CHR. **Coordinates with:** UNM, USCM, ULSAM, SelectorMechanism, G.2, G.5, G.9, E.20, F.18. |
| A.19.SelectorMechanism | **Unified Selection Kernel (SelectorMechanism)** | Stable | *Keywords:* selection kernel, set-returning selection, selected set, `SelectEligibility`, tri-state guard (`pass|degrade|abstain`), no hidden thresholds, no hidden scalarization, `CriteriaSlot`, `ComparisonResultSlot`, `TaskSignatureSlot`, evidence gating, `CG-Spec.MinimalEvidence`, CHR suite stage `select`, Bridge+CL/ReferencePlane transport, penalties→`R_eff` only. *Queries:* "What is SelectorMechanism in FPF?", "Why does selection return a selected set by default?", "How does SelectEligibility handle unknown or insufficient evidence?", "How does FPF prevent hidden thresholds and scalarization in selection?" | **Builds on:** A.6.1, A.6.5, A.19.CHR, A.19.CN, G.0, G.5, C.22. **Used by:** A.19.CHR, G.5, E.18 (E.TGA). **Coordinates with:** A.19.USCM, A.19.ULSAM, CPM (comparison stage). |
| A.20 | **U.Flow.ConstraintValidity — Eulerian** | Stable | *Keywords:* flow, ConstraintValidity, Eulerian, TransductionFlow, GateFit, MVPK, SquareLaw, Sentinel, PathSlice. *Queries:* "What is ConstraintValidity in FPF?", "What is the Eulerian stance in FPF flows?", "How does E.TGA relate to flows?" | **Builds on:** E.18 (E.TGA). **Coordinates with:** A.21, E.17, F.9, F.17, A.19.SelectorMechanism, C.18, C.19, G.5, G.6, G.11. |
| A.21 | **GateProfilization: `OperationalGate(profile)` (GateFit core)** | Stable | *Keywords:* OperationalGate, GateFit, GateProfile, GateChecks, join-semilattice, `GateDecision`, `DecisionLog`, EquivalenceWitness, LaunchGate, CV⇒GF. *Queries:* "What is GateProfilization in FPF?", "How does OperationalGate aggregate GateChecks?", "What is the CV⇒GF activation predicate?" | **Builds on:** E.18 (E.TGA), E.17 (MVPK), A.7. **Coordinates with:** A.20, A.2.6, F.9, F.17, G.6, G.11, A.19, G.0, G.5, C.18, C.19, G.9. |
| A.22 | **Structure and Structural Views (STRUCT-CAL)** | Stable | *Keywords:* structure, structural view, selected structure, preserved and lost structure, source return, architecture-description boundary, structural description. *Queries:* "What is structure in FPF?", "How do I separate structure from a description, view, graph, decision, or mathematical lens?", "When does an extracted view need source return?" | **Builds on:** A.1, A.6.3, A.7, C.2.1, E.10.D2, E.17. **Coordinates with:** C.30, C.30.AD, C.30.ASV, C.29, E.18, A.10, B.3, A.20, A.21. |

**Part B — Trans-disciplinary Reasoning Cluster**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| **B.1** | **Universal Algebra of Aggregation (Γ)** | Stable | *Keywords:* aggregation, composition, holon, invariants, IDEM, COMM, LOC, WLNK, MONO, gamma operator. *Queries:* "How does FPF combine parts into a whole?", "What are the rules for aggregation?", "What is the Gamma (Γ) operator?" | **Builds on:** A.1, A.9. **Prerequisite for:** All B.1.x, B.2. |
| B.1.1 | **Dependency Graph & Proofs** | Stable | *Keywords:* dependency graph, proofs, structural aggregators, sum, set, slice. *Queries:* "What is the input for the Gamma operator?", "How are aggregation invariants proven in FPF?" | **Builds on:** B.1. |
| B.1.2 | **System-specific Aggregation Γ_sys** | Stable | *Keywords:* system aggregation, physical systems, mass, energy, boundary rules, Sys-CAL. *Queries:* "How to aggregate physical systems?", "Conservation laws in FPF aggregation?" | **Builds on:** B.1, A.1, C.1. |
| B.1.3 | **Γ_epist — Knowledge-Specific Aggregation**| Stable | *Keywords:* knowledge aggregation, epistemic, provenance, trust, KD-CAL. *Queries:* "How to combine epistemes?", "How does trust propagate in FPF?" | **Builds on:** B.1, A.1, C.2. |
| B.1.4 | **Contextual & Temporal Aggregation (Γ_ctx & Γ_time)** | Stable | *Keywords:* temporal aggregation, time-series, order-sensitive, composition. *Queries:* "How does FPF handle time-series data?", "How to model processes where order matters?" | **Builds on:** B.1. |
| B.1.5 | **Γ_method — Order-Sensitive Method Composition & Work Enactment**| Stable | *Keywords:* method composition, workflow, sequential, concurrent, plan vs run. *Queries:* "How to combine methods or workflows?", "How does FPF model complex procedures?" | **Builds on:** B.1, B.1.4, A.3.1. |
| B.1.6 | **Γ_work — Work as Spent Resource**| Stable | *Keywords:* work, resource aggregation, cost, energy consumption, Resrc-CAL. *Queries:* "How to calculate the total cost of a process?", "How are resources aggregated in FPF?" | **Builds on:** B.1, A.15.1, C.5. |
| **B.2** | **Meta-Holon Transition (MHT): Recognizing Emergence and Re-identifying Wholes**| Stable | *Keywords:* emergence, MHT, meta-system, new whole, synergy, system of systems. *Queries:* "How does FPF model emergence?", "What is a Meta-Holon Transition?", "When does a collection become more than the sum of its parts?" | **Builds on:** B.1, A.1. **Prerequisite for:** All B.2.x. |
| B.2.1 | **BOSC Triggers** | Draft | *Keywords:* BOSC, triggers for emergence, boundary, objective, supervisor, complexity. *Queries:* "What triggers an MHT?", "What are the BOSC criteria for emergence?" | **Builds on:** B.2. |
| B.2.2 | **MST (Sys) — Meta-System Transition** | Stable | *Keywords:* system emergence, super-system, physical emergence. *Queries:* "How do new systems emerge from parts?", "What is a Meta-System Transition?" | **Builds on:** B.2, B.2.1, A.1. |
| B.2.3 | **MET (KD) — Meta-Epistemic Transition**| Stable | *Keywords:* knowledge emergence, meta-theory, paradigm shift, scientific revolution. *Queries:* "How do new theories emerge?", "What is a Meta-Epistemic Transition?" | **Builds on:** B.2, B.2.1, A.1. |
| B.2.4 | **MFT (Meta-Functional Transition)**| Stable | *Keywords:* functional emergence, capability emergence, adaptive workflow, new process. *Queries:* "How do new capabilities or workflows emerge?", "What is a Meta-Functional Transition?" | **Builds on:** B.2, B.2.1, A.3.1. |
| B.2.5 | **Supervisor–Subholon Feedback Loop** | Stable | *Keywords:* control architecture, feedback loop, supervisor, stability, layered control. *Queries:* "How does FPF model control systems?", "What is the supervisor-subholon pattern?" | **Builds on:** B.2, A.1. |
| B.3 | **Trust & Assurance Calculus (F–G–R with Congruence)** | Stable | *Keywords:* trust, assurance, reliability, F-G-R, formality, scope, congruence, evidence, claim-support posture, authority-looking labels, dashboard tiles, probe/distributed/export/causal assurance. *Queries:* "How is trust calculated in FPF?", "When does an authority-looking label or dashboard tile fail to raise assurance?", "How does FPF handle evidence and confidence?" | **Builds on:** A.10. **Coordinates with:** A.6, A.15, E.17.EFP, A.20, A.21, C.26, C.26.1, C.26.2, C.26.3, C.16, C.28, F.9. **Prerequisite for:** All B.3.x, D.4. |
| B.3.1 | **Components & Epistemic Spaces** | Draft | *Keywords:* F-G-R components, measurement templates, epistemic space. *Queries:* "How are F, G, and R measured?", "What are epistemic spaces?" | **Builds on:** B.3. |
| B.3.2 | **Evidence & Validation Logic (LOG-use)** | Draft | *Keywords:* verification, validation, confidence, logic, proof. *Queries:* "What is the logic for validating claims in FPF?", "Difference between verification and validation." | **Builds on:** B.3, C.6. |
| B.3.3 | **Assurance Subtypes & Levels** | Stable | *Keywords:* assurance levels, L0-L2, TA, VA, LA, typing, verification, validation. *Queries:* "What are the assurance levels in FPF?", "How does an assurance record mature in FPF?" | **Builds on:** B.3. |
| B.3.4 | **Evidence Decay & Epistemic Debt** | Stable | *Keywords:* evidence aging, decay, freshness, epistemic debt, stale data. *Queries:* "How does FPF handle outdated evidence?", "What is epistemic debt?" | **Builds on:** B.3. |
| B.3.5 | **CT2R-LOG — Working-Model Relations & Grounding**| Stable | *Keywords:* grounding, constructive trace, working model, assurance layer, CT2R, Compose-CAL. *Queries:* "How are FPF models grounded in evidence?", "What is the CT2R-LOG?" | **Builds on:** B.3, E.14, C.13. |
| **B.4** | **Canonical Evolution Loop** | Stable | *Keywords:* evolution loop, DesignRunTag feedback, observe-notice-stabilize-route, drift repair, open-ended evolution. *Queries:* "How does FPF evolve a system or episteme without design-reality drift?", "Where does pre-abductive routing sit in the canonical loop?" | **Builds on:** A.4, A.12. **Prerequisite for:** B.4.1-B.4.3. |
| B.4.1 | **Observe -> Notice -> Stabilize -> Route** | Draft | *Keywords:* routed cue set, route plurality, route selection, pre-abductive seam, task-family specialization route. *Queries:* "How do under-articulated cues become routed before endpoint claim publication?", "When should a cue become a routed cue set instead of an abductive prompt?" | **Builds on:** A.16, A.16.1, C.2.2a. **Coordinates with:** B.5.2.0, C.16.Q, A.6.A, C.22.1. |
| B.4.2 | **Knowledge Instantiation** | Stub | *Keywords:* theory refinement, knowledge evolution, scientific method. *Queries:* "How are scientific theories refined in FPF?" | **Builds on:** B.4, A.1. |
| B.4.3 | **Method Instantiation** | Stub | *Keywords:* adaptive workflow, process improvement, operational evolution. *Queries:* "How do workflows or methods evolve in FPF?" | **Builds on:** B.4, A.3.1. |
| **B.5** | **Canonical Reasoning Cycle** | Stable | *Keywords:* reasoning, problem-solving, Abduction-Deduction-Induction, scientific method. *Queries:* "How does FPF model problem-solving?", "What is the canonical reasoning cycle?" | **Builds on:** A.10. **Prerequisite for:** All B.5.x. |
| B.5.1 | **Explore → Shape → Evidence → Operate** | Stable | *Keywords:* development state cycle, open-ended progression, state machine, Explore, Shape, Evidence, Operate. *Queries:* "What states can project work and its records pass through in FPF?" | **Builds on:** B.5. |
| B.5.2 | **Abductive Loop** | Stable | *Keywords:* abduction, explanatory prompt, candidate hypotheses, plausibility filters, origin trace, route-to-hypothesis. *Queries:* "How does FPF model abductive hypothesis generation?", "What is the abductive loop?" | **Builds on:** B.5, B.5.2.0, A.10, B.3.3. **Coordinates with:** B.4.1, A.16, A.6.P. |
| B.5.2.0 | **`U.AbductivePrompt`** | Draft | *Keywords:* abductive prompt, prompt species, rival-set discipline, threshold crossing, explanation-ready cue. *Queries:* "When is a routed cue ready to enter abduction?", "What prompt species does FPF distinguish before hypothesis work begins?" | **Builds on:** B.4.1, A.16, C.2.2a. **Coordinates with:** A.6.P, A.6.A, C.16.Q. **Used by:** B.5.2. |
| B.5.2.1 | **Creative Abduction with NQD** | Stable | *Keywords:* creative abduction, NQD binding, Γ_nqd.generate, Creativity-CHR, Q-front, declared Q components, retained exploration/archive evidence, Novelty@context, ΔDiversity_P, E/E-LOG, DecisionSubject note. *Queries:* "How do I make abductive idea generation instrumented instead of ad-hoc?", "How does B.5.2 delegate generation to C.18 and pool policy to C.19?", "Why does creative abduction return a front/evidence set rather than one bundled winner?" | **Builds on:** B.5.2, A.17, A.18, C.17, C.18, C.19. **Coordinates with:** B.4, C.11, G.5. |
| B.5.3 | **Role-Projection Bridge** | Stable | *Keywords:* domain-specific vocabulary, concept bridge, mapping, terminology. *Queries:* "How does FPF integrate domain-specific language?", "What is a Role-Projection Bridge?" | **Builds on:** A.2, C.3. |
| **B.6** | **Characterisation Families (CHR-use)** | Draft | *Keywords:* characterization, templates, CHR patterns, measurement. *Queries:* "How to use CHR patterns?" | **Builds on:** Part C (CHR). |
| **B.7** | **Common Logic Suite (LOG-use)** | Draft | *Keywords:* logic, inference, trust propagation, LOG-CAL. *Queries:* "How to apply formal logic in FPF?" | **Builds on:** Part C (LOG-CAL). |

**Part C — Kernel Extension Specifications**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| **Cluster C.I – Core CALs / LOGs / CHRs** | | | | |
| C.1 | **Sys‑CAL** | Draft | *Keywords:* physical system, composition, conservation laws, energy, mass, resources, U.System. *Queries:* "How to model physical systems in FPF?", "What are conservation laws in FPF?", "Modeling a pump or engine." | **Builds on:** A.1 Holonic Foundation, A.14. **Coordinates with:** Resrc-CAL. **Prerequisite for:** M-Sys-CAL. |
| C.2 | **KD‑CAL** | Stable | *Keywords:* knowledge, epistemic, evidence, trust, assurance, F-G-R, Formality, ClaimScope, Reliability, provenance. *Queries:* "What is F-G-R?", "How does FPF handle evidence and trust?", "How to model a scientific theory?". | **Builds on:** A.1, A.10, B.3. **Prerequisite for:** All patterns using F-G-R, M-KD-CAL. |
| C.2.1 | **U.Episteme - Epistemes and their slot graph** | Stable | `U.EpistemeSlotGraph` organizes EntityOfConcern, GroundingHolon, ClaimGraph, Viewpoint, View, ReferenceScheme, RepresentationScheme, and related slots for claim-bearing epistemes across symbolic, diagrammatic, latent, and tool-mediated representations. | **Builds on:** C.2, A.1, A.6.5, A.7, E.10.D2. **Used by:** A.6.2-A.6.4, E.17.0-E.17.2, E.17, E.18, B.1.3, KD-CAL/LOG-CAL discipline packs. |
| C.2.P | **Epistemic Precision Restoration** | Stable | Restores precision for source expression, claim-bearing episteme, publication, view, face, carrier, PublicationUnit, EntityOfConcern, grounding relation, pattern-application wording, and FPF-governed use dispositions without turning files or names into claim objects. | **Builds on:** E.10, C.2.1, A.7, E.17.0, E.17, A.6.P, F.18. **Coordinates with:** E.8, E.12, E.17.AUD, E.17.EFP, E.17.ID.CR, A.10, A.15, A.20, A.21, B.3, C.11. |
| C.2.2 | **Reliability R in the F–G–R triad** | Stable | *Keywords:* Reliability (R), warrant, evidence-bound, F–G–R, ClaimScope (G), Bridge-only reuse, Congruence Level (CL / CL^k / CL^plane), weakest-link, pathwise justification (PathId), TA/VA/LA lanes, no implicit averaging. *Queries:* "What is R in F–G–R?", "How does FPF propagate reliability?", "How do CL penalties route under transport?", "Bridge-only reuse of claims in FPF". | **Builds on:** C.2, A.2.6, C.2.3, B.3, B.1.3, C.3, F.9. **Coordinates with:** G.6, G.7, E.14, E.18. **Constrains:** any cross-context claim reuse and any publication of `R_eff`. |
| C.2.2a | **`U.LanguageStateSpace` — Language-state chart over `U.CharacteristicSpace`** | Stable | *Keywords:* language-state chart, characteristic space, position claim, partial coordinates, thresholds, governed episteme publication. *Queries:* "What is the language-state space in FPF?", "How do I publish a position claim before endpoint claim publication?" | **Builds on:** A.19, E.10, F.18. **Used by:** C.2.LS, A.16, B.4.1, C.16.Q, A.6.A. |
| C.2.3 | **Unified Formality Characteristic F** | Stable | *Keywords:* Formality, F-scale, F0-F9, rigor, proof, specification, language-state separation. *Queries:* "What is Formality F in FPF?", "How does F differ from articulation, closure, or anchoring?" | **Builds on:** C.2. **Constrains:** all patterns referencing F-G-R or language-state facets. |
| C.2.LS | **`U.LanguageStateFacetProfile` — Compact profile for language-state facets** | Stable | *Keywords:* facet profile, articulation, closure, anchoring, representation factors, threshold package. *Queries:* "How are language-state facets named together in FPF?", "What is a LanguageStateFacetProfile?" | **Builds on:** C.2.2a, C.2.4-C.2.7. **Coordinates with:** A.16. |
| C.2.4 | **`U.ArticulationExplicitness`** | Draft | *Keywords:* articulation explicitness, semantic shape, under-articulated cue, explicitness, early repair readiness. *Queries:* "How explicit is a governed episteme already?", "What is ArticulationExplicitness in FPF?" | **Builds on:** C.2.2a. **Coordinates with:** C.2.LS, A.16. |
| C.2.5 | **`U.LanguageStateClosureDegree`** | Draft | *Keywords:* closure degree, candidate-space closure, reopen, rival routes, settledness. *Queries:* "How closed is the current candidate space?", "What is LanguageStateClosureDegree in FPF?" | **Builds on:** C.2.2a. **Coordinates with:** C.2.LS, A.16. |
| C.2.6 | **`U.LanguageStateAnchoringMode`** | Draft | *Keywords:* anchoring mode, embodiment, trace, model state, document, operator loop. *Queries:* "How is a language-state claim anchored in FPF?", "What is LanguageStateAnchoringMode?" | **Builds on:** C.2.2a. **Coordinates with:** C.2.LS, F.9.1. |
| C.2.7 | **`U.LanguageStateRepresentationFactorBundle`** | Draft | *Keywords:* representation factors, locality, sparsity, symbolicity, factor bundle, representation organization. *Queries:* "How does FPF describe representation factors in language-state work?", "What is the representation-factor bundle?" | **Builds on:** C.2.2a. **Coordinates with:** C.2.LS, C.2.6. |
| C.3 | **Kind‑CAL — Kinds, Intent/Extent, and Typed Reasoning** | Stable | *Keywords:* kind, type, intension, extension, subkind, typed reasoning, classification, vocabulary. *Queries:* "How does FPF handle types?", "What is a 'Kind'?", "Difference between 'scope' and 'type'?". | **Builds on:** A.1, A.2.6 (USM). **Prerequisite for:** LOG-CAL, ADR-Kind-CAL, and any pattern needing typed guards. |
| C.3.1 | **`U.Kind` & `U.SubkindOf` (Core)** | Stable | *Keywords:* kind, subkind, partial order, type hierarchy. *Queries:* "What is U.Kind in FPF?", "How to model 'is-a' relationships?". | **Builds on:** A.1, A.2.6 (USM). **Prerequisite for:** C.3.2, C.3.3. |
| C.3.2 | **`KindSignature` (+F) & `Extension`/`MemberOf`** | Stable | *Keywords:* KindSignature, intension, extension, MemberOf, Formality F, determinism. *Queries:* "How to define the meaning of a Kind?", "What is the difference between intent and extent in FPF?". | **Builds on:** C.3.1. **Prerequisite for:** C.3.3, C.3.4. |
| C.3.3 | **`KindBridge` & `CL^k` — Cross‑context Mapping of Kinds** | Stable | *Keywords:* KindBridge, type-congruence, CL^k, cross-context mapping, R penalty. *Queries:* "How to map types between domains?", "What is a KindBridge?". | **Builds on:** C.3.1, C.3.2, A.2.6, C.2.2. |
| C.3.4 | **`RoleMask` — Contextual Adaptation of Kinds (without cloning)** | Stable | *Keywords:* RoleMask, context-local adaptation, constraints, subkind promotion. *Queries:* "How to adapt a Kind for a local context?", "What is a RoleMask in FPF?". | **Builds on:** C.3.1, C.3.2. |
| C.3.5 | **`KindAT` — Intentional Abstraction Facet for Kinds (K0…K3)** | Stable | *Keywords:* KindAT, abstraction tier, K0-K3, informative facet, planning. *Queries:* "What are the abstraction tiers for Kinds?", "How to plan formalization effort?". | **Builds on:** C.3.1. |
| C.3.A | **Typed Guard Macros for Kinds + USM (Annex)** | Stable | *Keywords:* Typed guard, ESG, Method-Work, USM, Kind-CAL, regulatory profile. *Queries:* "How to write a typed guard?", "How do Kinds and USM interact in gates?". | **Builds on:** All C.3.x, A.2.6. |
| C.4 | **Method‑CAL** | Draft | *Keywords:* method, recipe, procedure, workflow, SOP, MethodDescription, operator. *Queries:* "How to model a process or workflow?", "What is a MethodDescription in FPF?". | **Builds on:** A.3, A.15. **Coordinates with:** Γ_method (B.1.5). |
| C.5 | **Resrc‑CAL** | Draft | *Keywords:* resource, energy, material, information, cost, budget, consumption, Γ_work. *Queries:* "How does FPF model resource usage?", "How to track costs of a process?". | **Builds on:** A.15.1 (Work). **Coordinates with:** Sys-CAL. |
| C.6 | **LOG‑CAL – Core Logic Calculus** | Draft | *Keywords:* logic, inference, proof, modal logic, trust operators, reasoning. *Queries:* "What is the base logic of FPF?", "How does FPF handle formal proofs?". | **Builds on:** Kind-CAL. **Is used by:** B.7. |
| C.7 | **CHR‑CAL – Characterisation Kit** | Draft | *Keywords:* characteristic, property, measurement, metric, quality. *Queries:* "How to define a new measurable property in FPF?", "What is a CHR pattern?". | **Builds on:** A.17, A.18. **Prerequisite for:** Agency-CHR, Creativity-CHR. |
| **Cluster C.II – Domain‑Specific Patterns** | | | | |
| C.9 | **Agency‑CHR** | Draft | *Keywords:* agency, agent, autonomy, decision-making, active inference. *Queries:* "How to measure autonomy?", "What defines an agent in FPF?". | **Builds on:** CHR-CAL, A.13. |
| C.10 | **Norm‑CAL** | Draft | *Keywords:* norm, constraint, ethics, obligation, permission, deontics. *Queries:* "How to model rules and constraints?", "Where are ethical principles defined in FPF?". | **Builds on:** A.10. **Is used by:** Part D. |
| C.11 | **Decision Theory (Decsn-CAL)** | Stable | *Keywords:* decision theory, DecisionSubject, OptionSet, comparison basis, ChoiceRule, ChoiceResult, question order, probe-worthiness, non-shared comparison frame, ValueOfInformation, ValueOfComputation, choose now, reject current set, probe again, reroute. *Queries:* "When should one choose now versus probe again?", "What must be explicit before a choice among already-available options is lawful?", "When do question order or incompatible frames require C.26 rather than ordinary choice?" | **Builds on:** A.6.P, A.6.5, A.13, C.9, A.18, A.19. **Coordinates with:** C.26, C.18, C.19, C.24, G.5. |
| **Cluster C.III – Meta‑Infrastructure CALs** | | | | |
| C.12 | **ADR‑Kind-CAL** | Draft | *Keywords:* versioning, rationale, DRR, architecture decision record. *Queries:* "How are changes to kinds managed?". | **Builds on:** Kind-CAL, E.9. |
| C.13 | **Compose‑CAL — Constructional Mereology** | Stable | *Keywords:* mereology, part-whole, composition, sum, set, slice, extensional identity. *Queries:* "How does FPF formally construct parts and wholes?", "What is Compose-CAL?". | **Builds on:** A.14. **Is used by:** B.3.5 (CT2R-LOG). |
| **Cluster C.IV – Composite & Macro‑Scale** | | | | |
| C.14 | **M‑Sys‑CAL** | Draft | *Keywords:* system-of-systems, infrastructure, large-scale systems, orchestration. *Queries:* "How to model a complex infrastructure like a power grid?". | **Builds on:** Sys-CAL, B.2.2. |
| C.15 | **M‑KD‑CAL** | Draft | *Keywords:* paradigm, scientific discipline, meta-analysis, knowledge ecosystem. *Queries:* "How to model an entire field of science?". | **Builds on:** KD-CAL, B.2.3. |
| C.16 | **MM-CHR — Measurement & Metrics Characterization** | Stable | *Keywords:* measurement, measurement template, `U.DHCMethod(Ref)`, `U.Measure`, `U.Unit`, `U.EvidenceStub`, polarity, direct comparability, scoring method disclosure, probe-changing-state, shared-frame check, CSLC. *Queries:* "How do I define a measurement template in FPF?", "When is a metric a passive read and when does it change the state?", "How do EvidenceStubs support measurement claims?" | **Builds on:** A.17, A.18. **Coordinates with:** A.10, B.3, C.26, C.26.1. **Is a prerequisite for:** All CHR patterns and any pattern that issues typed measures/scores. |
| C.16.P | **Characteristic and Scale Precision Restoration** | Stable | Repairs overloaded characteristic, scale, coordinate, metric, score, indicator, threshold, comparison, and scalar-quality wording before C.16/A.17-A.19/C.25/C.29/E.21 or another governing pattern is applied. | **Builds on:** E.10, E.10.ARCH, A.17, A.18, C.16, A.19, C.25, C.29, E.21, F.18, A.6.P. **Coordinates with:** C.16.Q, A.19.ECS, evidence, assurance, gate, decision, causal-use, benchmark, and publication patterns governing those claims. |
| C.16.Q | **Quality-Term Precision Restoration** | Stable | Repairs overloaded quality and evaluative-characterization wording by selecting an endpoint-governed evaluative form or a bounded transitional quality-term repair form with declared bearer, evaluation frame, sense family, admissible normal form, and governing pattern. | **Builds on:** E.10, E.10.ARCH, C.16.P, C.16, C.25, E.21, A.17, A.18, A.19, A.7, C.2.1, E.8, F.9, F.18. **Coordinates with:** A.6.P, A.6.A, A.16, B.4.1, B.5.2.0, A.10, B.3, F.9.1. |
| C.17 | **Creativity‑CHR — Characterising Generative Novelty & Value** | Stable | *Keywords:* Creativity-CHR, Novelty@context, Use-Value and ValueGain, Surprise, ConstraintFit, Diversity_P, Originality, ResourceEfficiency, MM-CHR measurement templates, ReferenceBase, evidence, portfolio composition. *Queries:* "How do I make a creativity claim measurable and evidence-bound?", "Which characteristics distinguish novelty, value, surprise, constraint fit, diversity, originality, and resource efficiency?", "How do creative outputs compose from individuals to portfolios?" | **Builds on:** C.16, A.17, A.18, A.19. **Coordinates with:** B.5.2.1, C.18, C.19, C.9, B.3, B.4, F.5/F.18. |
| C.18 | **NQD‑CAL — Open‑Ended Search Calculus** | Stable | *Keywords:* NQD-CAL, Γ_nqd.generate, Γ_nqd.updateArchive, Γ_nqd.illuminate, Γ_nqd.selectFront, DescriptorMapRef, DistanceDefRef, NQDArchive, CandidateSet, Front vs ExplorationArchive, IlluminationSummary report-only telemetry, EmitterPolicyRef, InsertionPolicyRef, provenance editions. *Queries:* "How does FPF run open-ended search without illegal scalarization?", "What is the difference between a front and an exploration archive?", "What provenance must an NQD generation call publish?" | **Builds on:** C.16, C.2, A.17-A.19. **Coordinates with:** B.5.2.1, C.17, C.19, G.5, G.6, G.11. |
| C.18.1 | **SLL — Scaling‑Law Lens (binding)** | Stable | *Keywords:* scaling law, scale variables (S), compute‑elasticity, data‑elasticity, resolution‑elasticity, exponent class, knee, diminishing returns. *Queries:* "How to make search scale‑savvy?", "Where to declare scale variables and expected elasticities?" | **Builds on:** C.16, C.17, C.18. **Coordinates with:** C.19, G.5, G.9, G.10. |
| C.19 | **Explore–Exploit Governor (E/E‑LOG)** | Stable | *Keywords:* explore-exploit, live candidate pool, pool-policy result, widen, keep frontier, narrow to subset, sunset line, reroute, EmitterPolicy, InsertionPolicy, lens id, dominance default routing, DecisionSubject clarification. *Queries:* "How should one govern a still-live candidate pool?", "When do I widen, keep frontier, narrow, sunset, or reroute?", "How does pool policy stay separate from C.11 choice, C.24 planning, and G.5 publication?" | **Builds on:** C.18, C.17, C.11, B.3, Compose-CAL. **Coordinates with:** C.24, G.5, G.9. |
| C.19.1 | **Bitter‑Lesson Preference (BLP)** | Stable | BLP comparison and waiver discipline for scalable general methods versus bounded specialization, including `E.23` method-family choice and cost/risk posture. | **Builds on:** C.19, C.24, B.3. **Coordinates with:** E.23, G.5, G.8, G.9, G.11, A.0. |
| C.20 | **Discipline‑CAL — Composition of `U.Discipline`** | Stable| *Keywords:* discipline, **U.AppliedDiscipline**, **U.Transdiscipline**, episteme corpus, standards, institutions, **Γ_disc**. *Queries:* "How to compose and assess a discipline in FPF?" | **Builds on:** C.2 KD‑CAL, G.0, Part F (Bridges/UTS). **Coordinates with:** C.21, C.23. |
| C.21 | **Discipline‑CHR - Field Health & Structure** | Stable | *Keywords:* discipline, field health, reproducibility, standardisation, alignment, disruption. *Queries:* "How to measure the health of a scientific field?", "What is reproducibility rate?". | **Builds on:** C.16, C.2, A.2.6, B.3. **Coordinates with:** C.20, G.2. |
| C.22 | **Problem Typing & TaskSignature Assignment (Problem‑CHR)** | Stable | *Keywords:* Problem‑CHR, TaskSignature, TaskKind, ScopeSlice(G), unknown handling, specialization anchor. *Queries:* "How does FPF bind a typed `TaskSignature` for lawful selection?", "How does TaskSignature stay separate from method choice and specialization claims?" | **Builds on:** C.16, G.0, G.5. **Coordinates with:** G.4, C.22.1, C.23. |
| C.22.1 | **Task-family adaptation signature** | Stable | Durable task-family specialization fields: threshold target, time-to-threshold, budget-to-threshold, prior exposure, transfer, retention, downside, and corridor entry. | **Builds on:** C.22, C.19.1, A.15, C.24, E.16. **Coordinates with:** E.23, G.5, G.9, G.11. |
| C.22.2 | **ProblemCard@Context** | Stable | *Keywords:* problem card, problem-side record, P2W-ready, Thin problem card, `setContextRef`, problem signal, support posture, validation boundary, first-principles cue, `safe-probe-needed`, freshness and unknown disposition. *Queries:* "How do I turn a messy signal into a reviewable problem before P2W?", "When is a problem card P2W-ready?", "How do problem cards keep evidence, gates, autonomy, archives, and method selection in neighboring patterns?" | **Builds on:** E.2, E.9, E.10, C.2.P, A.6.P, C.16.Q, C.16, A.19, C.22, C.25, C.29, G.5, G.9, A.6.3.RT, A.6.4. **Coordinates with:** C.11, C.18, C.19, C.22.1, C.24, C.27, C.28, A.15, A.21, E.16, G.6, G.11, A.10, B.3, E.17, E.17.ID.CR, A.6.3, F.9, E.18. |
| C.23 | **Method‑SoS‑LOG — MethodFamily Evidence & Maturity** | Stable | *Keywords:* MethodFamily, evidence, maturity, SoS-LOG, admit, degrade, abstain, selector. *Queries:* "How is method family maturity assessed?", "What is the SoS-LOG for selection?". | **Builds on:** G.5, G.4, C.22, B.3. |
| C.24 | **Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)** | Stable | Call-route and call-plan discipline for tool-using agents: plan/work separation, checkpoint return, tool-call budget, stop or replan condition, and overread boundaries. | **Builds on:** A.15, B.3, C.5, C.18, C.19. **Coordinates with:** E.23, C.11, C.28, G.5, G.6, G.9. |
| C.25 | **Q-Bundle: Authoring "-ilities" as Structured Quality Bundles** | Stable | *Keywords:* quality bundle, -ility, quality family, characteristic plus scope, mechanism/status slots, endpoint classification, viability envelope, proxy metric, admissible quality-family use, failure mode. *Queries:* "What is a Q-Bundle in FPF?", "When is an -ility one characteristic and when is it a bundle?", "When does a viability claim need C.26.3 rather than one metric?" | **Builds on:** A.2.6, A.6.1, C.16, B.3. **Coordinates with:** C.16.Q, A.15, C.26.3. |
| C.26 | **Quantum-Like Modeling Lens** | Stable | *Keywords:* quantum-like, QL-lite, QL-NQ, probe frame, order effect, incompatible probes, instrument update, state export, source-loss coarsening, minimal admissible output. *Queries:* "When is quantum-like useful as a mathematical lens in FPF?", "What representational mistake does QL-lite prevent?", "How do I use QL without making a physical quantum claim?" | **Builds on:** C.11, C.16, A.6, A.10, B.3, F.9, A.6.3.CSC, A.6.3.RT. **Constrains:** C.26.1-C.26.3. **Coordinates with:** A.15, C.25, C.18, C.19. |
| C.26.1 | **Probe-Coupled Boundary Interaction** | Stable | *Keywords:* probe-coupled boundary, passive read, dashboard as instrument, workshop as state-changing interaction, API read, survey, bridge result, export loss, evidence window. *Queries:* "When does a dashboard, workshop, metric, or API read change what it reports?", "How do I stop treating a boundary interaction as a passive read?", "When should a probe-coupled case apply evidence or assurance patterns?" | **Builds on:** C.26, A.6, A.6.B, A.10, B.3, C.16, F.9, A.15. **Coordinates with:** C.26.2, C.26.3, A.6.8. |
| C.26.2 | **Enacted Distributed State Evidence** | Stable | *Keywords:* distributed-state evidence, coordinated work, enacted state, minimal state reading, evidence carrier, window, rival explanation, no group mind, report/export loss. *Queries:* "When does coordinated work evidence a state no participant report carries?", "How do I bound a distributed-state reading?", "When is a survey or dashboard thinner than the enacted state?" | **Builds on:** C.26, A.15, A.10, B.3, F.9, C.16. **Coordinates with:** C.26.1, C.26.3. |
| C.26.3 | **Viability-Envelope Boundary Regulation** | Stable | *Keywords:* viability envelope, homeostasis, allostasis, boundary regulation, sensor/probe/actuator split, metric-induced distortion, service viability, quality bundle, failure mode. *Queries:* "When is viability more than one green metric?", "How do boundary probes or metrics change a viability envelope?", "When does a service split or support load need envelope regulation?" | **Builds on:** C.26, C.25, U.Dynamics, A.6, A.15, C.16, A.10, B.3, A.3, A.19, C.18, C.19. **Coordinates with:** C.26.1, C.26.2. |
| C.27 | **Temporal Claim Adequacy: State Readings, Temporal Trends, and Intervention-Sensitive Temporal Change** | Stable | *Keywords:* temporal claim adequacy, temporal claim, state reading, rate reading, temporal trend, rate-change, intervention-sensitive temporal change, effort window, resistance/inertia, rhythm/cadence, throughput, recovery, braking, coasting, stabilization, dynamic benchmark. *Queries:* "When does a speed, rhythm, throughput, or recovery claim need temporal adequacy?", "How do I separate state, rate, and intervention-sensitive rate-change?", "When is faster improvement not enough for benchmark, quality, viability, or QL claims?" | **Builds on:** C.16, A.3.3, B.1.4, B.1.6. **Coordinates with:** C.18.1, C.19, C.22.1, C.24, C.25, C.26, C.26.3, G.9. |
| C.28 | **CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability** | Stable | *Keywords:* causal-use question, causality ladder, association, intervention, counterfactual, Pearl Causal Hierarchy, Structural Causal Model, causal diagram, causal estimand, identification, counterfactual sampling realizability, causal evidence support basis, target trial, causal fairness, off-policy causal evaluation, causal-RL evaluation. *Queries:* "Can I say this caused that?", "Is this intervention claim supported?", "What evidence supports a counterfactual claim?", "When does a fairness metric need causal support?", "Is simulation enough for a counterfactual claim?", "Which pattern handles causal benchmark parity?", "When should causal language be downgraded to association, measurement, temporal, QL, or local prose?" | **Builds on:** A.10, B.3, C.11, C.19, C.24, C.26, C.27, D.5, G.5, G.9. **Coordinates with:** A.2.4, A.3.2, A.6, A.15, C.16, G.11. |
| C.29 | **Mathematical Lens Use** | Stable | *Keywords:* mathematical lens, structure-preserving representation, lens mapping mode, preserved structure, lost structure, invariants, stop condition, scale window, coarse-graining, rival lens, `LensUseAdmissibilityValue`, validation boundary, learned lens, ontology smuggling. *Queries:* "When does a mathematical analogy become an admissible FPF lens?", "What structure is preserved by this lens?", "Where must this math transfer stop?", "How do I use mathematical structure without importing ontology?" | **Builds on:** A.1.1, A.6.P, A.3.3, A.19, A.10, A.15, B.3, C.16, E.17.EFP, E.17.ID.CR, A.6.3.RT, A.6.3.CSC, F.9. **Constrained by:** E.8, E.10, C.2.P, E.19. **Decision basis:** E.9 and C.29:13a. **Coordinates with:** C.11, A.15.1, A.15.4, C.18.1, C.19.1, C.26, C.27, C.28, G.5, G.9, G.2, G.10. |
| C.30 | **Grounded Architecture and Selected-Structure Adequacy** | Stable | *Keywords:* grounded architecture, ArchitectureOf@Context, selected structure, architecture claim, architecture question card, architecture-description boundary, artifact-as-architecture guard. *Queries:* "How do I recover a grounded architecture claim?", "Which selected structure changes the architecture move?", "When is an architecture description only a conditional description use?" | **Builds on:** A.22, C.2.1, A.6.3, A.7, E.17.0, E.17, E.10.D2, F.18. **Coordinates with:** C.30.AD, C.30.ASV, A.6.F, C.30.TGA-FLOW-REL, C.30.LCA, C.30.ILC, C.29, C.16, C.25, C.28, A.10, B.3, A.20, A.21, A.15, C.11. |
| C.30.AD | **Architecture Description Adequacy** | Stable | *Keywords:* architecture description, ArchitectureDescription@Context, architecture description use card, architecture structural view, viewpoint, correspondence, source return, specification-use boundary. *Queries:* "When is an architecture description the EntityOfConcern under repair?", "How do I keep views, viewpoints, selected structures, and publication boundaries distinct?", "When does an architecture description need C.30.AD rather than C.30?" | **Builds on:** C.30, C.30.ASV, A.22, A.7, A.6.3, E.17.0, E.17.1, E.17.2, E.17, C.2.P, E.10, E.10.ARCH. **Coordinates with:** C.30.P, C.30.TGA-FLOW-REL, C.30.LCA, C.30.ILC, A.6.F, A.6.M, C.29, C.16, C.16.P, A.10, B.3, A.20, A.21, A.15, C.11, C.28, E.8, F.18. |
| C.30.P | **Architecture and Structure Precision Restoration** | Stable | Repairs architecture or structure wording whose EntityOfConcern or claim kind is hidden before A.22, C.30, C.30.AD, C.30.ASV, a selected C.30.* pattern
, or another governing pattern is applied. | **Builds on:** E.10, E.10.ARCH, A.22, C.30, C.30.AD, C.30.ASV, C.2.P, A.6.P, A.6.F, C.29, C.16.P, C.16, C.25, E.17, E.8. **Coordinates with:** C.30.TGA-FLOW-REL, C.30.LCA, C.30.ILC, A.10, B.3, A.20, A.21, C.11, C.28, A.15, E.11. |
| C.30.STRAT | **Stratification Wording Precision Restoration** | Stable | Repairs source-label uses such as layer, level, tier, stack, ladder, rung, block, expert, cache, router, and gate by recovering selected ontological neighborhood, primary EntityOfConcern kind, governing pattern, admissible use, and remaining reader move before FPF-governed use. | **Builds on:** E.10, E.10.ARCH, E.8, F.18, C.30.P, A.22, C.30. **Coordinates with:** C.30.ASV, C.30.LCA, C.30.TGA-FLOW-REL, C.30.ILC, A.6.M, A.6.F, E.18, C.16.P, C.16, A.19.SPR, C.2.P, E.17, C.29, C.28, A.10, G.6, B.3, A.20, A.21, A.15, A.2, G.5, C.11, E.11, I.2. |
| C.30.ASV | **Architecture Structural View Adequacy (ASV)** | Stable | *Keywords:* architecture structural view, ArchitectureStructureKindRef, VF.ARCH.STRUCTURE, viewpoint bundle, structure kind, hidden/lost structure, correspondence, source return. *Queries:* "Which structure kind does this architecture view describe?", "How do viewpoint and structure kind stay distinct?", "When does a view hide or lose structure?" | **Builds on:** C.30, A.22, A.6.3, E.17.0, E.17.1, E.17.2, E.17, E.10.D2. **Coordinates with:** A.6.F, C.30.TGA-FLOW-REL, C.30.LCA, C.30.ILC, E.18, C.29. |
| C.30.TGA-FLOW-REL | **Architecture-TGA Flow-Structure Relation** | Stable | *Keywords:* TGA graph relation, architecture flow relation, FlowTransductionStructure, graph/path/crossing, ArchitectureFlowStructureRelation@TGA. *Queries:* "When can a TGA graph inform grounded architecture or an architecture structural view?", "How do flow, graph, and architecture structure stay distinct?", "When is a TGA path not work, evidence, gate, or decision?" | **Builds on:** C.30, C.30.ASV, E.18, A.22. **Coordinates with:** A.6.F, C.29, C.16, C.28, A.10, B.3, A.20, A.21, A.15. |
| C.30.LCA | **Control Structure View Adequacy (LCA)** | Stable | *Keywords:* control-structure view, layered control architecture, supervisor loop, controller/plant, rate band, control layer, proof overread. *Queries:* "When is LCA a control-structure view rather than proof?", "How do layer, level, stack, and rate labels recover fields named by value?", "Where do stability, safety, evidence, and gate claims go?" | **Builds on:** C.30, C.30.ASV, B.2.5, A.22. **Coordinates with:** A.3.3, C.27, C.28, A.10, G.6, B.3, A.20, A.21, C.29. |
| C.30.ILC | **Cross-Scope Architecture Residual Triage** | Stable | *Keywords:* cross-scope residual, interlevel conflict, frustration, declared scope, structure kind, local repair, source return. *Queries:* "What is the first architecture move when a local fix creates a residual elsewhere?", "How do level, layer, scope, scale, and frustration wording recover exact carriers?", "When should the case exit to measurement, scale, evidence, decision, or synthesis patterns?" | **Builds on:** C.30, C.30.ASV, A.22. **Coordinates with:** C.16, C.29, G.5, C.11, C.28, A.10, B.3, G.6, D.3, D.4. |
| C.31 | **Modularity and Reusable Structure Characteristics** | Stable | *Keywords:* modularity characteristics, reusable-structure characteristics, coupling, cohesion, substitutability, interface variation, evidence reuse, bespoke residue, ModularityVectorLite. *Queries:* "Which modularity characteristic is under evaluation?"
, "When is a modularity score report-only?", "How do I keep module, interface, reuse, and evidence-reuse claims distinct?" | **Builds on:** C.16, A.17, A.18, A.19, C.25, C.30, C.30.ASV. **Coordinates with:** A.6.M, C.31.RSA, C.31.ASAP, C.29, A.10, B.3, G.5, C.11. |
| C.31.RSA | **Reusable Structure Accounting** | Stable | *Keywords:* reusable-structure accounting, reusable share, bespoke residue, accounting basis, report-only share, source return, refactoring opportunity. *Queries:* "Where is reusable structure located?"
, "When is a reusable share only report-only?", "What gets worse when we increase reuse?" | **Builds on:** C.31, C.30, C.30.ASV, C.16, A.19. **Coordinates with:** A.6.M, C.31.ASAP, C.29, A.10, B.3, G.6, C.27, C.28, G.5, C.11. |
| C.31.ASAP | **Architecture Scale-Amenability Preference** | Stable | *Keywords:* architecture scale preference, scale amenability, ScaleClaimTriage, scale variable, scale window, architecture alternatives, source-return condition, coarse-graining, RG, platform scale claim, waiver reason. *Queries:* "When does modularity or platform wording carry an architecture scale-preference claim?", "How do I compare architectures under a scale window?", "When is coarse-graining or RG-like language only a mathematical lens?" | **Builds on:** C.31, C.31.RSA, C.16, A.17, A.18, A.19, C.18.1, C.19.1, C.29. **Coordinates with:** A.6.M, C.30, C.30.ASV, C.30.LCA, C.30.ILC, A.10, B.3, G.6, G.5, G.9, C.11. |

**Part D – Multi-scale Ethics & Conflict-Optimisation**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| **D.1** | **Axiological Neutrality Principle** | Stub | *Keywords:* axiology, values, ethics, neutrality, morals, preference lattice, objective function. *Queries:* "Does FPF have built-in ethics?", "How to model different value systems in FPF?", "What is axiological neutrality?" | **Builds on:** E.2 (Pillars). **Enables:** D.2, D.4. |
| **D.2** | **Multi-Scale Ethics Framework** | Stub | *Keywords:* ethics, scale, levels, scope, responsibility, agent, team, ecosystem, planet. *Queries:* "How to apply ethics at different scales?", "FPF model for team ethics vs. individual ethics." | **Builds on:** D.1, A.9 (Cross-Scale Consistency). **Constrains:** D.2.1-D.2.4. |
| D.2.1 | Local-Agent Ethics | Stub | *Keywords:* individual ethics, duties, permissions, agent, system. *Queries:* "Modeling duties for a single agent." | **Builds on:** D.2. |
| D.2.2 | Group-Ethics Standards | Stub | *Keywords:* collective norms, team ethics, veto, subsidiarity. *Queries:* "How to define rules for a team in FPF?" | **Builds on:** D.2. |
| D.2.3 | Ecosystem Stewardship | Stub | *Keywords:* externalities, tragedy of the commons. *Queries:* "Modeling ethical impact on an ecosystem." | **Builds on:** D.2. |
| D.2.4 | Planetary-Scale Precaution | Stub | *Keywords:* catastrophic risk, long-termism, precautionary principle. *Queries:* "How does FPF handle long-term ethical risks?" | **Builds on:** D.2. |
| **D.3** | **Holonic Conflict Topology** | Stub | *Keywords:* conflict, clash, disagreement, resolution, resource conflict, goal conflict, epistemic conflict. *Queries:* "How to model conflicts between systems in FPF?", "Types of conflicts in FPF." | **Builds on:** A.1 (Holon), B.1 (Aggregation). **Enables:** D.3.1, D.4. |
| D.3.1 | Conflict Detection Logic (LOG-use) | Stub | *Keywords:* conflict detection, logic, predicates, `conflictsWith`. *Queries:* "Formal logic for detecting conflicts." | **Builds on:** D.3. |
| D.3.2 | Conflict Routing Protocol | Stub | *Keywords:* routing, mediation, negotiation, DRR, appeals. *Queries:* "How does FPF route unresolved conflicts?" | **Builds on:** D.3. |
| **D.4** | **Trust-Aware Mediation Calculus** | Stub | *Keywords:* mediation, negotiation, conflict resolution, trust score, assurance, algorithm. *Queries:* "How does FPF resolve conflicts using trust?", "What is the algorithm for mediation?", "Using B.3 scores for decision making." | **Builds on:** D.3, B.3 (Trust & Assurance Calculus). **Uses:** C.5 (Resrc-CAL). |
| D.4.1 | Fair-Share Negotiation Operator | Stub | *Keywords:* fair division, negotiation, Nash bargaining, bias correction. *Queries:* "Modeling fair negotiation between agents." | **Builds on:** D.4. |
| D.4.2 | Assurance-Driven Override | Stub | *Keywords:* safety override, assurance, utility, risk management. *Queries:* "When does safety override performance in FPF?" | **Builds on:** D.4. |
| **D.5** | **Bias-Audit & Ethical Assurance** | Stable | *Keywords:* bias, audit, ethics, assurance, fairness, review cycle, taxonomy, AI ethics, responsible AI. *Queries:* "How does FPF handle bias?", "What is the Bias-Audit Cycle?", "How to ensure a model is fair?", "Ethical review process in FPF." | **Builds on:** E.5.4 (Cross-Disciplinary Bias Audit). **Complements:** B.3.3 (Assurance Levels). |
| D.5.1 | Taxonomy-Guided Audit Templates | Stub | *Keywords:* bias taxonomy, audit checklist, template. *Queries:* "Templates for conducting a bias audit." | **Builds on:** D.5. |
| D.5.2 | Assurance Metrics Roll-up | Stub | *Keywords:* ethical risk index, metrics, evidence, roll-up. *Queries:* "How to calculate an overall ethical risk score in FPF?" | **Builds on:** D.5, B.3. |

**Part E – The FPF Constitution and Authoring Guides**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| **Cluster E.I — The FPF Constitution** | | | | |
| E.1 | **Vision & Mission** | Stable | *Keywords:* vision, mission, operating system for thought, purpose, scope, goals, non-goals. *Queries:* "What is FPF?", "What is the purpose of the First Principles Framework?", "What problem does FPF solve?". | **Prerequisite for:** All other patterns, especially E.2. |
| E.2 | **The Eleven Pillars** | Stable | *Keywords:* principles, constitution, pillars, invariants, core values, rules, P-1 to P-11. *Queries:* "What are the core principles of FPF?", "What are the eleven pillars?". | **Builds on:** E.1. **Prerequisite for:** E.3 and all normative patterns. |
| E.2.DA | **FPF Pillar-Adequacy Evaluation CharacteristicSpace** | Stable | FPF-level object-under-improvement evaluation derived from the `E.2` Pillars for FPF as a whole, a corpus slice, release candidate, pattern family, projection set, or host set, including content-loss and excess-apparatus regressions. | **Builds on:** E.2, A.19.ECS. **Coordinates with:** E.21, E.9.DA, E.22, E.23, E.11, E.10, F.18, F.19. |
| E.3 | **Principle Taxonomy & Precedence Model** | Stable | *Keywords:* taxonomy, precedence, conflict resolution, hierarchy, principles, classification, Gov, Arch, Epist, Prag, Did. *Queries:* "How does FPF resolve conflicting principles?", "What is the hierarchy of FPF rules?". | **Builds on:** E.2. **Constrains:** All patterns and DRRs. |
| E.4 | **FPF Ecosystem Family Architecture** | Stable | *Keywords:* ecosystem families, Conceptual Core, Tooling Reference, Pedagogical Companion, canon, tutorial, linter. *Queries:* "How are FPF publications, tools, and learning companions structured?", "What is the difference between the core spec and tooling?". | **Builds on:** E.1. **Constrained by:** E.5.3. |
| E.5 | **Four Guard-Rails of FPF** | Stable | *Keywords:* guardrails, constraints, architecture, rules, safety, GR-1 to GR-4. *Queries:* "What are the main architectural constraints in FPF?". | **Builds on:** E.2, E.3. **Prerequisite for:** E.5.1, E.5.2, E.5.3, E.5.4. |
| E.5.1 | **DevOps Lexical Firewall** | Stable | *Keywords:* lexical firewall, jargon, tool-agnostic, conceptual purity, DevOps, CI/CD, yaml. *Queries:* "Can I use terms like 'CI/CD' in FPF core patterns?". | **Refines:** E.5. **Constrains:** All Core patterns. |
| E.5.2 | **Notational Independence** | Stable | *Keywords:* notation, syntax, semantics, tool-agnostic, diagram, UML, BPMN. *Queries:* "Does FPF require a specific diagram style?", "How is meaning defined in FPF?". | **Refines:** E.5. **Constrains:** All Core patterns. |
| E.5.3 | **Unidirectional Dependency** | Stable | *Keywords:* dependency, layers, architecture, modularity, acyclic, Core, Tooling, Pedagogy. *Queries:* "What are the dependency rules between FPF ecosystem families?". | **Refines:** E.5. **Constrains:** E.4. |
| E.5.4 | **Cross-Disciplinary Bias Audit** | Stable | *Keywords:* bias, audit, ethics, fairness, trans-disciplinary, neutrality, review. *Queries:* "How does FPF handle bias?", "Is there an ethics review process in FPF?". | **Refines:** E.5. **Constrains:** All Core patterns. **Links to:** Part D. |
| **Cluster E.II — The Author’s Handbook** | | | | |
| E.6 | **Didactic Architecture of the Spec** | Stable | *Keywords:* didactic, pedagogy, structure, narrative flow, on-ramp, learning. *Queries:* "How is the FPF specification structured for learning?", "What is the 'On-Ramp first' principle?". | **Builds on:** E.2 (P-2 Didactic Primacy). |
| E.7 | **Archetypal Grounding Principle** | Stable | *Keywords:* grounding, examples, archetypes, U.System, U.Episteme, Tell-Show-Show. *Queries:* "How are FPF patterns explained?", "What are the standard examples in FPF?". | **Builds on:** E.6. **Constrains:** All architectural patterns. |
| E.8 | **FPF Authoring Conventions and Style Guide** | Stable | Pattern body as user-facing pattern body; recognition text and assurance text; working-reader boundary; positive subject/action spine; precision-restoration profile and phrase-apparatus cleanup; evaluation-characteristic-space pattern publication form is delegated to `E.8.ECSPF`. | `E.6`, `E.7`, `E.8.ECSPF`, `E.9`, `E.10`, `E.19`, `E.21`, `F.18`, `F.19` |
| E.8.ECSPF | **Evaluation CharacteristicSpace FPF Pattern Publication Form** | Stable | Authoring form for publishing an accepted evaluation `CharacteristicSpace` as an FPF pattern while preserving working-reader recognition, value meanings, non-use boundaries, neighbour relations, governing-pattern references, and phrase-apparatus discipline. | **Builds on:** E.8, A.19.ECS. **Coordinates with:** E.21, E.9.DA, E.2.DA, E.22, E.23, F.18, F.19, C.25. |
| E.9 | **Design-Rationale Record (DRR) Method** | Stable | `DRR` as one bounded decision and rationale record: exact basis, selected answer, source and decision carry-through, positive content distribution to patterns and selected non-pattern FPF kind-reference pairs, kind-or-boilerplate diagnostic for draft wording, and decision-adequacy evaluations through `E.9.DA`. | `E.2`, `E.8`, `E.9.DA`, `E.10`, `E.19`, `E.22`, `F.19` |
| E.9.DA | **DRR Decision-Adequacy Evaluation CharacteristicSpace** | Stable | Evaluates whether one `DRR` is decisive enough for its declared FPF authoring use: selected answer, source carry-through, selected-locus distribution, rejected alternatives, first drafting move, and phrase-apparatus or boilerplate debt before pattern drafting. | **Builds on:** E.9, A.19.ECS. **Coordinates with:** E.8, E.10, E.19, E.21, E.22, E.23, F.19. |
| E.10 | **LEX-BUNDLE: Unified Lexical Rules for FPF** | Stable | Word/head/use precision, register discipline, term formation, ontology guards, precision-restoration check registry, and closure rule: local wording accepted, rewritten to kind named by value/relation, or sent to the selected restoration or governing pattern. | `A.7`, `E.5`, `F.5`, `F.18`; coordinates with `A.6.P`, `C.2.P`, `A.19.ECS`, `E.22`, `E.23`, `F.19` |
| E.10.ARCH | **Wording-Use Ontological Precision Restoration Architecture** | Stable | Distributes wording-use precision restoration: E.10 catches overloaded wording, E.10.ARCH selects the applicability row, selected restoration or governing patterns recover ontology, F.19 handles phrase-level apparatus after kind recovery, and subject patterns keep thin local cues plus declarative relations. | **Builds on:** E.10, A.6.P, A.6.F, C.2.P, A.6.3.CSC, F.18, F.19, E.8, E.19, E.2. **Coordinates with:** C.30.P, C.16.P, C.16.Q, A.22, C.30, C.30.ASV, C.16, A.19, C.25, C.27, C.29, E.21, E.11, I.2. |
| E.10.P | **Conceptual Prefixes (policy & registry)** | Stable | *Keywords:* prefixes, U., Γ_, ut:, tv:, namespace, registry. *Queries:* "What do the prefixes like 'U.' mean in FPF?". | **Depends on:** E.9. **Constrains:** E.5.1, E.5.2. |
| E.10.D1 | **Lexical Discipline for “Context” (D.CTX)** | Stable | *Keywords:* context, U.BoundedContext, anchor, domain, frame. *Queries:* "What is the formal meaning of 'Context' in FPF?". | **Builds on:** A.7, A.4. **Coordinates with:** F.1, F.2, F.3, F.7, F.9. |
| E.10.D2 | **EntityOfConcern, Description Episteme, and Specification-Use Discipline** | Stable | *Keywords:* EntityOfConcern, Description episteme, specification use, DescriptionContext, testable, verifiable. *Queries:* "Difference between a description and a specification in FPF?". | **Builds on:** A.7, E.10.D1, C.2.1, C.2.3. **Constrains:** F.4, F.5, F.8, F.9, F.15. |
| E.11 | **First-Practical Entry and Pattern-Use Discoverability Discipline** | Stable | Public `readme` first-entry scenarios, Preface plain-engineering explanation of FPF ideas, ToC/retrieval cues, local Problem-frame recognition, expanded entry-disambiguation cases, and projection-boundary discipline. | **Builds on:** E.8, E.19, E.21, F.18. **Coordinates with:** I.2, E.10, E.10.ARCH, F.19. |
| E.12 | **Didactic Primacy & Cognitive Ergonomics** | Stable | *Keywords:* didactic, cognitive load, ergonomics, usability, Rationale Mandate, HF-Loop. *Queries:* "How does FPF ensure it's understandable?", "What is the 'So What?' test in FPF?". | **Builds on:** E.2 (P-2). **Complements:** E.13. |
| E.13 | **Pragmatic Utility & Value Alignment** | Stable | *Keywords:* pragmatic, utility, value, Goodhart's Law, Proxy-Audit Loop, MVE. *Queries:* "How does FPF ensure solutions are useful, not just correct?", "What is a Minimally Viable Example (MVE)?". | **Builds on:** E.2 (P-7). **Complements:** E.12. |
| E.14 | **Human-Centric Working-Model** | Stable | *Keywords:* working model, human-centric, publication surface, grounding, assurance layers. *Queries:* "What is the main interface for FPF users?", "How does FPF separate human-readable models from formal assurance?". | **Builds on:** E.7, E.8, C.2.3. **Coordinates with:** B.3.5, C.13, E.10. |
| E.15 | **Lexical Authoring & Evolution Protocol (LEX-AUTH)** | stable | *Keywords:* lexical authoring, evolution protocol, LAT, delta-classes. *Queries:* "How are FPF patterns authored and evolved?", "What is a Lexical Authoring Trace (LAT)?". | **Builds on:** E.9, E.10, B.4, C.18, C.19, A.10, B.3, F.15. |
| E.16 | **RoC‑Autonomy Budget & Enforcement** | Stable | *Keywords:* autonomy budget, guarded enactment, autonomy ledger, override speech act, scout/probe/commit checkpoint. *Queries:* "How does FPF make autonomy enforceable and auditable?", "How do bounded specialization budgets stay separate from committed rollout?" | **Builds on:** A.13, A.15, A.21, B.3. **Coordinates with:** C.24, G.4, G.5, G.9. |
| E.17.0 | **U.MultiViewDescribing - Viewpoints, Views & Correspondences** | Stable | Multi-view describing for families of Description epistemes and specification-use Description epistemes indexed by EntityOfConcernClass, EntityOfConcernRef, bounded context, and viewpoint; keeps viewpoint, episteme-lane view, publication face/form, and carrier distinct. | **Builds on:** C.2.1, A.6.2, A.6.3, A.6.4, A.7, E.10.D1, E.10.D2. **Used by:** E.17, E.17.1, E.17.2, E.18, domain-specific description schemes. |
| E.17.1 | **`U.ViewpointBundleLibrary` — Reusable Viewpoint Bundles** | Stable | *Keywords:* viewpoint bundle, reusable viewpoint family, import discipline, alias discipline, governance, engineering/management/research bundles. *Queries:* "How do I define reusable viewpoint bundles in FPF?", "What is a ViewpointBundleLibrary?" | **Builds on:** E.17.0, A.6.2-A.6.4, A.7, E.7, E.10. **Used by:** E.17.2, E.18, domain-specific viewpoint-bundle libraries. |
| E.17.2 | **TEVB - Typical Engineering Viewpoints Bundle** | Stable | Archetypal engineering viewpoint bundle for holons, with Functional, Procedural, Role-Enactor or Device-Structure, and Module-Interface viewpoints over an `EntityOfConcernClass = U.Holon`; architecture-specific viewpoint bundles import TEVB rather than mutating it. | **Builds on:** E.17.0, E.17.1, C.2.1, A.1, A.6.2-A.6.4, A.7, E.10.D2. **Used by:** E.18, E.17, engineering Description-episteme and specification-use patterns, ISO-aligned architecture-description bundles. |
| E.17 | **Multi-View Publication Kit** | Stable | Publication discipline for generic publication faces and governed MVPK faces; `U.View`, publication form, carrier and front-end, source pins, admissible publication use, and no face becoming evidence, gate, decision, or work by presentation. | `E.17.0`, `E.17.1`, `E.17.2`, `A.7`, `E.10`, `C.2.P`; coordinates with `E.17.EFP`, `E.17.ID.CR`, `E.17.AUD` |
| E.17.EFP | **ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces** | Stable | Explanation-facing rendering classes; source-pinned rendering, source-linked reconstruction, didactic retelling, speculative retelling; admissible explanation use and boundary to evidence, gate, work, and source return. | `E.17`, `A.7`, `A.6.B`, `F.9`, `F.18`; coordinates with `A.10`, `A.15`, `A.15.4`, `A.6.3.CSC`, `E.17.ID.CR` |
| E.17.ID.CR | **ComparativeReading — bounded comparative reading over comparative review units** | Stable | Comparative review unit, source anchors, comparison basis, bounded lift, unsupported downstream claim or effect, and boundary to decision, equivalence, bridge, coarsening, explanation, prompt, ontology, or gate work. | `C.2.2a`, `A.16.0`, `F.9`, `E.14`; coordinates with `E.17.EFP`, `E.17.AUD.LHR`, `E.17.AUD.OOTD`, `A.6.3.*`, `A.15`, `A.20`, `A.21` |
| E.17.AUD | **PublicationUnit Stability Discipline** | Stable | One bounded publication unit as a readable unit; primary EntityOfConcern or subject named by value, carried publication move, and outside boundary to work, decision, gate, or reliance claim; choose local head restoration, whole-unit stabilization, bounded comparison, or neighboring pattern. | `C.2.2a`, `A.16.0`, `A.7`, `E.10`, `F.18`, `E.14`, `E.19`; coordinates with `E.17.AUD.LHR`, `E.17.AUD.OOTD`, `E.17.ID.CR`, `E.17.EFP` |
| E.17.AUD.LHR | **PublicationUnit Stability Discipline and Local Head Restoration** | Stable | Repair one overloaded local lexical head inside one publication unit before the whole publication unit inherits ambiguity; recover local head kind, active local reading, local head kind, carried move or question under repair, and outside-work boundary. | `A.6.P`, `A.7`, `E.10`, `C.2.P`, `F.18`, `E.14`; coordinates with `E.17.AUD`, `E.17.AUD.OOTD`, `E.17.ID.CR`, `E.17.EFP` |
| E.17.AUD.OOTD | **PublicationUnit Stability Discipline and PublicationUnit Primary EntityOfConcern Discipline** | Stable | Keep one publication unit explicit about one primary EntityOfConcern or subject named by value, one carried move over that entity, and one outside-work boundary; stop quiet shifts into another primary EntityOfConcern, concern, or wider process. | `A.6.P`, `A.7`, `E.10`, `F.18`, `E.14`, `E.19`, `C.2.2a`, `A.16.0`; coordinates with `E.17.AUD.LHR`, `E.17.ID.CR`, `E.17.EFP` |
| E.18 | **Transduction Graph Architecture (E.TGA)** | Stable | *Keywords:* transduction graph, **nodes=morphisms**, **edge=U.Transfer** (single-edge kind), **OperationalGate(profile)**, **CV⇒GF** (ConstraintValidity → GateFit), **MVPK** faces, **SquareLaw**, **UNM declaration locus**, **CSLC normalize-then-compare**, **Set-return selection**, **PathSlice/Sentinel refresh**, **DesignRunTag**. *Queries:* “What is E.TGA?”, “How do gates/bridges publish crossings?”, “How to model flows of morphisms?” | **Builds on:** E.17 (MVPK), E.8, E.10, A.7. **Coordinates with:** A.20, A.21, A.2.6, F.9, F.17, G.5, G.9, G.11, and current Part G bridge/crossing wiring when those relations are being used.
 |
| E.18.1 | **Principles-to-Work Transduction Path** | Stable | *Keywords:* P2W, principles-to-work, accepted `ProblemCard@Context`, carried distinction, carry-through record, first-principles cue, result carry-through, source-currentness, selected application, stop condition, return trigger. *Queries:* "How do accepted problem-side distinctions become a next admissible FPF use?", "How do first principles carry into work without selecting a method too early?", "How do I keep P2W separate from evidence, gates, decisions, work, and publication claims?" | **Builds on:** E.18, C.22.2, E.10, E.19. **Coordinates with:** C.29, A.6.0, A.6.1, A.15, A.15.1, A.15.2, A.15.3, A.15.4, A.10, B.3, A.20, A.21, E.17. |
| E.19 | **Pattern Quality Gates: Review and Refresh Profiles** | Stable | Pattern-quality review and refresh profiles; PCP-TERM, PCP-ENTRY, SoTA binding, terminology restoration, reader-role discipline, support-role parity, phrase-apparatus cleanup, semantic trust, profile-depth decisions, and quality-evaluation routing to `E.21`, `E.9.DA`, `E.2.DA`, or `E.22` when those evaluations are being made.
 | `E.8`, `E.9`, `E.10`, `E.21`, `E.22`, `E.23`, `C.2.P`, `F.18`, `F.19`, `A.6.P` |
| E.20 | **Mechanism Introduction Protocol (MIP)** | Draft | *Keywords:* mechanism introduction, authoring protocol, governing-definition assignment, MIP-run manifest, canonical card-first, no dangling `…IntensionRef`, suite boundary hygiene, P2W seam, SlotKind lexicon discipline, alias docking, typed RSCR triggers, regression envelope, PQG profiles. *Queries:* "How to introduce a new mechanism in FPF?", "How to avoid dangling IntensionRefs in suites?", "How to assign mechanism changes to their governing definitions?", "How to evolve mechanism suites without drift?" | **Builds on:** E.8, E.9, E.10, E.15, E.19. **Coordinates with:** A.6.1, A.6.7, A.15.3, F.18, E.18, G.Core, G.2, `G.x:Ext.*`. **Constrains:** Any change-set that introduces or revises mechanisms, suites, planned baselines, wiring modules, or citeable tokens. |
| E.21 | **FPF Pattern-Quality Evaluation CharacteristicSpace** | Stable | Evaluates one FPF pattern version for a declared reader, use, and scope with one required coordinate set, ordinal values with short rationales, protected trade-offs, precision-restoration profile, status, and stop or reopen conditions. | **Builds on:** E.8, E.19, C.25, C.16, A.17-A.19, F.18, A.19.ECS. **Coordinates with:** E.22, E.23, E.9.DA, E.2.DA, E.10, F.19, A.6.P, C.2.P, E.11, I.2. |
| E.22 | **Improvement-Oriented Quality Evaluation Question Framing** | Stable | Frames one improvement-oriented quality evaluation over an object version named by value under a declared object-under-improvement evaluation, including evaluation purpose, floor or improvement aim, protected trade-offs, evidence basis, mandatory result form, precision-restoration profile expectations, and next-admissible-move hypothesis. | **Builds on:** A.19.ECS, E.21, E.9.DA, E.2.DA. **Coordinates with:** E.23, E.19, E.10, F.19, C.25, C.17-C.19, G.5, G.9, G.11. |
| E.23 | **Quality Improvement Loop Method** | Stable | Repeated quality-improvement method parameterized by an object version named by value under improvement and object-under-improvement evaluation; governs change, re-evaluation, absorption, stop, continue, switch-method, open-new-frame, hold decisions, and kind-restoration checks for repairs. | **Builds on:** E.22, A.19.ECS. **Coordinates with:** E.21, E.9.DA, E.2.DA, F.19, C.19.1, C.22.1, C.24, C.17-C.19, G.5, G.9, G.11. |

**Part F — The Unification Suite (U‑Suite): Concept‑Sets, SenseCells & Contextual Role Assignment**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| F.0.1 | **Contextual Lexicon Principles** | Stable | *Keywords:* local meaning, context, semantic boundary, bridge, congruence, lexicon, U.BoundedContext. *Queries:* "How does FPF handle ambiguity?", "What is the principle of local meaning?", "How do different contexts communicate?". | **Builds on:** A.1.1. **Prerequisite for:** All patterns in Part F. |
| **Cluster F.I — Context of Meaning and Lexical Inputs** | | | | |
| F.1 | **Domain‑Family Landscape Survey** | Stable | Keywords: domain‑family survey, context map, canon, scope notes, versioning, authoritative source. | **Builds on:** E.10.D1, F.0.1, A.7. **Prerequisite for:** F.2, F.3, F.4, F.9. |
| F.2 | **Term Harvesting & Normalisation** | Stable | *Keywords:* term harvesting, lexical unit, normalization, provenance, source-text terms. *Queries:* "How to extract terminology from a standard?", "What is a local lexical unit?", "How to handle synonyms within one domain?". | **Builds on:** F.1. **Prerequisite for:** F.3. |
| F.3 | **Intra‑Context Sense Clustering** | Stable | *Keywords:* sense clustering, disambiguation, Local-Sense, SenseCell, counter-examples. *Queries:* "How to group similar terms within a single domain?", "What is a SenseCell?", "How to handle words with multiple meanings in one context?". | **Builds on:** F.2. **Prerequisite for:** F.4, F.7, F.9. |
| **Cluster F.II — Concept-Sets & Role Assignment/Description (definition, naming, decision)** | | | | |
| F.4 | **Role Description (RCS + RoleStateGraph + Checklists)** | Stable | *Keywords:* role template, status template, invariants, RoleStateGraph (RSG), Role Characterisation Space (RCS). *Queries:* "How to define a role in FPF?", "What is a Role Description?", "How to specify the states of a role?". | **Builds on:** F.3, A.2.1. **Prerequisite for:** F.6, F.8. |
| F.5 | **Naming Discipline for U.Types & Roles** | Stable | *Keywords:* naming conventions, lexical rules, morphology, twin registers, U.Type naming. *Queries:* "What are the rules for naming roles in FPF?", "How to create clear and consistent names for concepts?". | **Builds on:** F.4, E.10. |
| F.6 | **Role Assignment & Enactment Cycle (Six-Step)** | Stable | *Keywords:* role assignment, enactment, conceptual moves, asserting status. *Queries:* "What is the process for assigning a role?", "How is a role enacted in FPF?", "What are the six steps of role assignment?". | **Builds on:** F.4, A.2.1, A.15. |
| F.7 | **Concept‑Set Table Construction** | Stable | *Keywords:* concept-set, table, row, columns, differences, comparisons. *Queries:* "How do I create a concept-set table?", "How do I compare concepts across contexts?". | **Builds on:** F.3, F.9. **Coordinates with:** A.6.9. **Prerequisite for:** F.8. |
| F.8 | **Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)** | Stable | *Keywords:* decision lattice, type explosion, reuse, minting new types, parsimony. *Queries:* "When should I create a new U.Type?", "How to avoid creating too many roles?", "Decision guide for new concepts.". | **Builds on:** F.4, F.7. |
| **Cluster F.III — Cross‑Context Alignment & Applied Bindings** | | | | |
| F.9 | **Alignment & Bridge across Contexts** | Stable | *Keywords:* bridge, cross-context alignment, CL, direction, loss notes, Bridge-supported use, bridge reading, weakest-link scope, state export. *Queries:* "How do I bridge concepts across contexts?", "How do I express alignment safely in FPF?", "When is an orientation note not enough for a bridge card?" | **Builds on:** E.10.D1, F.0.1, F.1, F.2/F.3, F.7, F.8. **Coordinates with:** C.26, C.26.1, A.6.3.CSC, A.6.9, E.17.ID.CR, F.9.1. **Prerequisite for:** F.7, F.10. |
| F.9.1 | **Bridge Stance Overlay** | Stable | *Keywords:* bridge stance, stance overlay, interpretive gloss, projection note, rename note, language-state comparisons, overlay annotation. *Queries:* "How do I add a stance gloss to a bridge card without changing bridge semantics?", "What is the Bridge Stance Overlay?", "When does a stance label still depend on the underlying F.9 bridge card?" | **Builds on:** F.9, C.2.2a, A.16.0. **Coordinates with:** A.6.3.CSC, E.17.ID.CR, E.17.1, C.16.Q, A.6.A. |
| F.10 | **Status Families Mapping (Evidence • Standard • Requirement)** | Stable | *Keywords:* status, evidence, standard, requirement, polarity, applicability windows. *Queries:* "How to map different types of status like 'evidence' and 'requirement'?", "How does FPF handle compliance?". | **Builds on:** F.9, B.3. |
| F.11 | **Method Quartet Harmonisation** | Stable | *Keywords:* Method, MethodDescription, Work, Actuation, Role–Method–Work alignment. *Queries:* "How to align the concepts of 'method' and 'work' across domains?", "What is the method quartet?". | **Builds on:** F.9, A.15. |
| F.12 | **Service Acceptance Binding** | Stable | *Keywords:* Service Level Objective (SLO), Service Level Agreement (SLA), acceptance criteria, binding, observation. *Queries:* "How to bind an SLO to actual work?", "How is service acceptance modeled in FPF?". | **Builds on:** F.9, A.2.3, KD-CAL. |
| **Cluster F.IV — Lexical Development Cycle, Growth Control, Tests & Examples** | | | | |
| F.13 | **Lexical Continuity & Deprecation** | Stable | *Keywords:* evolution, deprecation, renaming, splitting terms, merging terms. *Queries:* "How to manage changes to terminology over time?", "What is the process for renaming a concept?". | **Builds on:** F.5. |
| F.14 | **Anti‑Explosion Control (Roles & Statuses)** | Stable | *Keywords:* vocabulary growth, guard-rails, separation-of-duties, bundles, reuse. *Queries:* "How to prevent having too many roles and statuses?", "What are the strategies for controlling vocabulary size?". | **Builds on:** F.4, F.8. |
| F.15 | **SCR/RSCR Harness for Unification** | Stable | *Keywords:* static checks, regression tests, acceptance tests, validation, SenseCell testing. *Queries:* "How is the unification process validated?", "What are SCR/RSCR tests in FPF?". | **Builds on:** All of F.1-F.14. |
| F.16 | **Worked‑Example Template (Cross‑Domain)** | Stable | *Keywords:* didactic template, example, pedagogy, cross-domain illustration. *Queries:* "What is the standard format for a worked example in FPF?", "How to show a concept applied across different fields?". | **Builds on:** All of F.1-F.12. |
| F.17 | **Unified Term Sheet (UTS)** | Stable | *Keywords:* Unified Term Sheet, UTS, summary table, glossary, publication, human-readable output. *Queries:* "What is the final output of the FPF unification process?", "Where can I find a summary of all unified terms?". | **Builds on:** F.1-F.12. |
| F.18 | **Local-First Unification Naming Protocol** | Stable | Local-first naming; Name Cards; guarded heads; NQD-front label candidates; context-bound semantic read-through; interpretive-view wording; stewardship context examples; FPF kind named by value and reference naming instead of topic-like or entity-interest wording. | `F.0.1`, `F.1`-`F.17`, `E.10`, `C.2.P`; coordinates with `A.6.P`, `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW`, `G.2`, `G.6`, `G.10` |
| F.19 | **Ontology-First Plain Technical Rewriting** | Stable | Ontology-first plain rewriting; phrase apparatus; boilerplate apparatus; negative catalogue; pattern-application drift; kind-preserving plain technical prose. | **Builds on:** `E.8`, `E.10`, `E.10.ARCH`, `F.18`, `A.6.P`, `A.7`, `E.18`, `E.21`. **Coordinates with:** `E.19`, `E.22`, `E.23`, `A.19.SPR`, `C.2.P`, `C.16.P`, `C.30.P`, `E.11`, `I.2`. |


**Part G – Discipline SoTA Patterns Kit**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| G.Core | Part G Core Invariants | Stable | *Keywords:* Part‑G invariants, delegation-first core, RSCR trigger kinds, Default Governing Definition Index, ID continuity, core linkage. *Queries:* "How to universalize Part G without drift?", "How to make RSCR triggers id-based?" | **Builds on:** E.8/E.10/E.19, A.6.7, A.15.3, A.19, G.0, A.19.CHR. Used by: all `G.0…G.13`. |
| G.0 | **CG-Spec — Frame Standard & Comparability Governance** | Stable | *Keywords:* CG-Spec, CG-Frame, legality gate, ComparatorSet, ScaleComplianceProfile (SCP), MinimalEvidence, Γ-fold, Φ(CL), Φ_plane, CL-routing, ReferencePlane, edition pins, RSCRTriggerKindId. *Queries:* "What is CG-Spec in FPF?", "How does CG-Spec constrain lawful comparison and aggregation?", "What must be pinned for CG-Spec reproducibility?" | **Builds on:** G.Core, A.19 (CN-Spec), A.10, A.17–A.19 / C.16 (MM-CHR legality), A.18 (CSLC), B.3, Part F (Bridges/UTS), E.10, E.5.2. **Prerequisite for:** G.1–G.6. |
| G.1 | **CG-Frame-Ready Generator**| Stable | *Keywords:* generator chassis, generator, selector, and set-result scaffold, six-card kit (M1-M6), `CGKitId` manifest, `SoTA_SetId`, `VariantPoolId`, `ShortlistId`, `CGFrameLibraryId`, `RefreshReadinessCardId`, set-return selection, set-result outcome, UTS/Name Cards, RSCR linkage surfaces, edition pins, shipping and refresh boundaries. *Queries:* "How do I author a reusable CG-Frame generator kit?", "What belongs in the six-card chassis M1-M6?", "How do G.2 harvesting, G.5 set-return selection, G.10 shipping, and G.11 refresh connect without becoming one method spec?" | **Builds on:** G.Core, E.8, E.10, E.19. **Uses:** A.10, A.15.3, A.19 (CN-Spec), G.0 (CG-Spec), G.2, G.3, G.4, G.5, G.10, G.11; (via Extensions) C.17, C.18, C.19. **Produces:** `CGKitId` plus reusable CG-Frame kit or chassis, set-result scaffold, and linkage surfaces (UTS and RSCR ready). |
| G.2 | **SoTA Harvester & Synthesis** | Stable | *Keywords:* SoTA harvest, synthesis, SoTA Synthesis Pack@CG-Frame, SoTAPaletteDescription, Tradition, TraditionAtlasView, DeclaredSubstrateAtlasView, TypedSetViews, BridgeMatrix, GammaEpistSynthId, FlowRecord, palette-first. *Queries:* "How does FPF harvest and synthesize SoTA for a CG-Frame?", "When is TraditionAtlasView lawful and when is palette-first or thinner interpretation enough?", "How do competing Traditions stay plural while bridgeable and refreshable?" | **Builds on:** G.Core, E.8, E.10, E.19, A.10, B.3, F.9, F.17, G.0. **Used by:** G.1, G.3-G.5, G.10, G.11. **Coordinates with:** A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW, A.6.P, G.13. |
| G.3 | **CHR Authoring: Characteristics - Scales - Levels - Coordinates** | Stable | *Keywords:* CHR authoring, characteristics, scales, levels, coordinates, CSLC legality, typed measurement, CHR Pack@CG-Frame, ReferencePlane, Φ/CL policy pins, edition pins, RSCRTriggerKindId. *Queries:* "How do I author CHR packs (typed characteristics and scales) for a CG-Frame?", "How to keep measurement lawful (CSLC) and refreshable (RSCR)?" | **Builds on:** G.Core, G.2, G.0, A.17–A.19, A.18 (CSLC), C.16 (MM-CHR), A.19.CHR, A.15.3, G.6, F.17. **Prerequisite for:** G.4. **Used by:** G.4, G.5, G.10, G.11. |
| G.4 | **CAL Authoring: Calculi - Acceptance - Evidence** | Stable | *Keywords:* CAL authoring, operators, acceptance clauses, evidence profiles, tri-state admissibility, Γ-fold hooks, Φ/Ψ/Φ_plane policy pins, legality gates, edition pins, RSCRTriggerKindId. *Queries:* "How to author CAL operators and acceptance clauses for CG-Frames?", "How to keep acceptance/evidence wiring auditable and refreshable?" | **Builds on:** G.Core, G.3, G.0, B.3 (Trust), A.18 (CSLC), G.6. **Prerequisite for:** G.5. **Used by:** G.5, G.8–G.10, G.11. |
| G.5 | **Multi‑Method Dispatcher & MethodFamily Registry** | Stable | *Keywords:* method-family registry, generator-family registry, dispatcher, SelectorOutcomeKind, selected-set publication, set-result outcome, `Shortlist`, `RankedShortlist`, `ShortlistId`, `SpecialistHandoff`, abstain/escalation result, basis pins, no hidden scalar winner. *Queries:* "How does FPF dispatch among rival method families without hidden scalarization?", "How do I publish a Shortlist or RankedShortlist honestly?", "When does G.5 begin after C.11 choice, C.19 pool policy, or C.24 planning?" | **Builds on:** G.Core, G.0, G.2-G.4, G.6. **Coordinates with:** C.11, C.19, C.24, G.9-G.11. |
| G.6 | **Evidence Graph & Provenance Ledger** | Stable | *Keywords:* EvidenceGraph, provenance, PathId, PathSliceId, lane tags (TA/VA/LA), SCR/RSCR, GateCrossing, CrossingBundle, UTS PathCard, TriggerAliasMap, Γ-fold pinning. *Queries:* "How does FPF trace claims to evidence?", "What is an EvidenceGraph?", "How do PathId/PathSliceId support audit and refresh?" | **Builds on:** G.Core, A.10, B.3, G.4, F.9, F.15, F.17, E.18, A.21, E.10, E.5.2. **Used by:** G.5, G.8, G.9, G.10, G.11. |
| G.7 | **Cross-Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)** | Stable | *Keywords:* bridge calibration, BridgeCard, BridgeCalibrationTable (BCT), RegressionSet, SentinelSet, BridgeSentinel, Congruence Level (CL/CL^k/CL^plane), loss notes, waivers, ReferencePlane, Φ(CL)/Ψ(CL^k)/Φ_plane policy pins, PathSliceId, GateCrossing, UTS, RSCRTriggerKindId. *Queries:* "How to calibrate cross-Tradition bridges in Part G?", "What is BCT and how is it used?", "How do Bridge Sentinels trigger RSCR?" | **Builds on:** G.Core, G.2, F.9, F.3, F.7, B.3, G.6, E.18, A.21, E.10, C.21. **Prerequisite for:** G.5. **Used by:** G.9–G.11, G.10, G.12. |
| G.8 | **SoS-LOG Bundles & Maturity Ladders** | Stable | *Keywords:* SoS-LOG, rule ids, admissibility ledger, tri-state `{pass|degrade|abstain}`, maturity ladder (poset/ordinal), selector-facing bundle, evidence path pins (`PathId/PathSliceId`), Bridge/CL/Φ policy pins, set-result/archive telemetry, RSCRTriggerKindId. *Queries:* "How to package SoS-LOG rules for the selector?", "How to publish a maturity ladder as a citable card?", "How to keep thresholds out of LOG and pin evidence paths?" | **Builds on:** G.Core, C.23, G.4, G.6, G.5, C.22. **Coordinates with:** G.7, G.10, G.11, F.8, F.9, E.18, E.10, E.5.2. |
| G.9 | **Parity / Benchmark Harness** | Stable | *Keywords:* parity harness, benchmark plan, adaptation parity, freshness windows, comparator pins, selected-set outcomes. *Queries:* "How does FPF run reproducible parity with explicit pins and windows?", "How do adaptation-speed and specialization claims become lawful parity questions?" | **Builds on:** G.Core, G.5, G.6, G.4, F.15. **Uses:** G.0, A.19, C.22.1. **Coordinates with:** C.27 when parity compares rate-change, rhythm change, recovery speed, intervention effect, effort budget, or dynamic outcome. |
| G.10 | **SoTA Pack Shipping (pack-boundary governing definition; `SoTA-Pack(Core)`)** | Stable | *Keywords:* shipping, `SoTA-Pack(Core)`, pack-boundary governing definition, selector-ready publication surface, `AuditPins`, `MOOManifest`, `PortfolioRosterId`, UTS publication, `PathId`/`PathSliceId`, `CrossingBundle`, edition pins, telemetry pins, RSCR wiring, parity pins, notation-independent pack, no semantic respecification. *Queries:* "How does FPF ship a SoTA pack without smuggling semantics?", "What is SoTA-Pack(Core) as a pack rather than a kit or suite?", "How do AuditPins, MOOManifest, path citations, and crossing bundles support replay and refresh?" | **Builds on:** G.Core, F.17-F.18, E.5.2, E.18, A.10, A.15.3. **Consumes/cites:** G.2-G.9, optional G.12-G.13. **Used by:** selector-facing consumers via G.5 and refresh orchestration via G.11. |
| G.11 | **Telemetry-Driven Refresh & Decay Orchestrator** | Stable | *Keywords:* telemetry, refresh, decay, RSCR, PathSlice, Bridge Sentinels, edition-aware, epistemic debt, deprecation, edition bumps, re-shipping. *Queries:* "How does FPF keep SoTA packs up-to-date?", "What triggers refresh / RSCR reruns?", "How are deprecations and edition bumps governed?". | **Builds on:** G.Core, G.6, G.7, G.5, G.8, G.9, G.10, B.3.4, E.18. **Coordinates with:** G.12, C.18 and C.19, C.23, F.15. |
| G.12 | **DHC Dashboards — Discipline-Health Time-Series (admissible telemetry, generation-first)** | Stable | *Keywords:* dashboard, DHC, discipline health, time-series, admissible telemetry, view-only slices, PathId/PathSliceId, edition pins, UTS twins, RSCR/refresh wiring. *Queries:* "How to build DHC dashboards in FPF?", "How to publish admissible DHC time-series with evidence and edition pins?", "How to wire dashboard telemetry into RSCR refresh?" | **Builds on:** G.Core, C.21, G.6, G.11, A.19, G.0, F.17/F.18, E.5.2, E.10. **Coordinates with:** G.5 (selector set-result outputs), G.7 (crossings/CL/Φ_plane pins), G.8 (maturity ladder panel), G.10 (shipping inclusion), C.18 and C.19 (QD/OEE telemetry), G.2 (SoTA palette hooks). |
| G.13 | **External Interop Hooks for SoTA Discipline Packs (conceptual; normative when used)** | Stable | *Keywords:* interop, external index, claim mapper, mapping policy, plane map, embedding spec, `ExternalIndexCard@Context`, `ClaimMapperCard@Context`, `InteropSurface@Context`, CHR-typed SoS features, edition pins, UTS twins, RSCRTriggerKindId, telemetry pin. *Queries:* "How does FPF integrate external scholarly indexes into Part G?", "What is an ExternalIndexCard / ClaimMapperCard / InteropSurface in FPF?", "How to make interop refreshable with RSCR trigger kinds and edition pins?" | **Builds on:** G.Core, G.2–G.7, G.9–G.12, A.19, A.18, G.0, F.17, E.5.2, E.18. |

**Part H – Glossary & Definitional Pattern Index**

| § | ID & Title |  Status | Concise reminder |
| :--- | :--- | :--- | :--- |
| H.1 | **Alphabetic Glossary** | stub | Every `U.Type`, relation & operator with four‑register naming. |
| H.2 | **Definitional Pattern Catalogue** | stub | One‑page micro‑stubs of every definitional pattern for quick lookup. |
| H.3 | **Cross‑Reference Maps** | stub | Bidirectional links: Part A ↔ Part C ↔ Part B terms. |

**Part I – Annexes & Extended Tutorials**

| § | ID & Title | Status | Concise reminder |
| :--- | :--- | :--- | :--- |
| I.1 | **Deprecated Aliases** | stub | Deprecated names kept as alias labels for continuity; aliases do not carry current semantics. |
| I.2 | **Expanded Entry Disambiguation Cases** | Stable | Expanded entry-disambiguation cases for high-risk or compact-insufficient first-entry pattern comparison; compact-index-only is a complete admissible posture when enough. |
| I.3 | **Change‑Log (auto‑generated)** | stub | Version history keyed to DRR ids. |
| I.4 | **External Standards Mappings** | stub | Trace tables to ISO 15926, BORO, CCO, Constructor‑Theory terms. |

**Part J – Indexes & Navigation Aids**

| § | ID & Title | Status | Concise reminder |
| :--- | :--- | :--- | :--- |
| J.1 | **Concept‑to‑Pattern Index** | stub | Quick jump from idea (“boundary”) to pattern (§, id). |
| J.2 | **Pattern‑to‑Example Index** | stub | Table listing every archetypal grounding vignette. |
| J.3 | **Principle‑Trace Index** | Stub | Maps each Pillar / C‑rule / P‑rule to concrete clauses. |

**Part K - Lexical Debt**

| § | ID & Title | Status | Concise content reminder — “what belongs here” |
| :--- | :--- | :--- | :--- |
| K.1 | **Mandatory Replacement of Measurement Terms** | Stub | Retires "axis/dimension" in favor of "Characteristic" and aligns other measurement terms. |
| K.2 | **Migration Debt from A.2.6 (USM)** | Stub | Specifies the required edits across the FPF to align with the new Unified Scope Mechanism (USM). |
| K.3 | **Temporal Claim Lexical Debt from C.27** | Stable | Retires untyped velocity, acceleration, cadence, agility, rhythm, inertia, and dynamics language when it is used outside a named C.27, C.16, or A.3.3 reading. |

# First Principles Framework (FPF) Readme

> First Principles Framework (FPF) is a standards-style pattern language for turning difficult engineering, research, management, and mixed human/AI work into explicit, reviewable, improvable reasoning.

- **Author:** Anatoly Levenchuk, with AI-agent assistance
- **Version:** June 2026
- **Status:** Normative kernel, eternal alpha: already used in working projects and development programs, while still evolving.

FPF helps when a project has outgrown one clever conversation. It is useful when meanings, claims, options, evidence, architecture, work decisions, publication forms, and improvement criteria must stay coherent across people, teams, tools, time, or AI agents.

Use FPF as a reference model and pattern language, not as a linear textbook. Start from the working question you bring from your project. Bring in internal FPF terms only after they help you keep the work precise.

## Decide Whether FPF Fits

Use FPF when ordinary discussion is no longer enough to keep work coherent. Typical signs:

- several teams, experts, tools, or AI agents must reason about the same work;
- the real-world test is slow, expensive, noisy, risky, or politically hard to repeat;
- different readers need different reports, dashboards, explanations, or decisions about the same underlying work;
- names, roles, responsibilities, options, evidence, or quality criteria are starting to blur;
- the team needs a current view of possible approaches, not just one recommendation;
- a decision is small enough to make now but important enough to leave a durable reason.

FPF is probably too heavy when the task is small, feedback is fast and cheap, the vocabulary is already stable, the decision will not be reused or audited, and a quick answer is enough.

FPF is mainly useful for people who have to keep difficult work understandable across boundaries:

- engineers and systems engineers working with complex products or operations;
- researchers building claims that others must inspect or reuse;
- platform and AI teams coordinating humans, models, tools, and approvals;
- safety, assurance, compliance, and regulatory leads who need visible evidence and responsibility boundaries;
- managers and product leaders who must compare options, budgets, risks, and delivery promises without hiding trade-offs.

There are three common ways to use FPF:

1. Human-only: use it as a writing and review discipline for meetings, notes, decisions, and technical documents.
2. Mixed team: use it to keep specialists, managers, safety leads, and AI assistants aligned around the same work.
3. AI-assisted: attach or index the specification, ask for plain-language project help first, and use pattern names only when they make the answer easier to check.

Stronger AI does not remove the need for FPF. AI can generate fluent options quickly, but projects still need to decide what counts as evidence, which option is being compared, who may rely on an answer, when a claim is stale, what remains only a guess, and what work is actually authorized. FPF helps make those boundaries explicit before a confident answer becomes an expensive mistake.

Core ideas in plain language:

- local teams may use local meanings, but translation must be explicit when work crosses a boundary;
- the thing itself, its description, a dashboard about it, a decision about it, and the work done to change it are not the same;
- keep several options alive until the comparison is clear enough to choose;
- say what "better" means before optimizing or scoring;
- make trust depend on evidence, freshness, scope, and intended use;
- publish different views for different readers without changing the underlying claim;
- use mathematics or formal models when they clarify what structure is preserved, what is lost, and what can be checked.

## First Practical Entries

A first practical entry is the first useful way to enter FPF from a real working project. Choose it by the project question you are trying to settle, not by the order of patterns in the specification.

The entries below are not a required sequence. They are common places where FPF can start paying rent in a project.

### 1. Develop or review architecture

Use this when you need to design, explain, review, or improve the architecture of a product, organization, technical system, document system, AI-agent setup, research program, or other thing with important internal structure.

FPF helps you ask what is being architected, which structures matter, what property of the architecture is being changed or judged, and which description, diagram, view, promise, decision, evidence, or implementation task is a different matter. It gives you language for selected structures, structural views, architecture characteristics, modularity, interfaces, scale, interlevel tensions, and architecture-changing moves.

Typical first result: a short architecture question note that says what is being architected, which structures matter, which architecture characteristic is at stake, what description or view is needed, and what decision or implementation work is still not settled by the architecture statement.

First inspect: `C.30`, `A.22`, `C.30.ASV`, `C.30.AD`, `C.31`, `A.6.M`, and the relevant architecture precision-restoration patterns when wording hides the kind of structure being discussed.

### 2. Write rules, methods, and work-process documents

Use this when you need to write or review technical regulations, procedures, method descriptions, operating instructions, work-process descriptions, standards-like project documents, API documents, contracts, SLAs, protocols, permissions, or compliance wording.

FPF helps you keep the described method separate from the method itself, a plan separate from performed work, responsibility separate from permission, an interface contract separate from implementation, and a published document separate from actual execution. It can also describe chains of methods when the chain itself is the subject, while keeping actual work occurrences separate from the document that says how work should be done.

Typical first result: a cleaned method, regulation, or interface outline that names what is being governed, the method or interface being described, the roles and responsibilities involved, the expected work result, and any evidence, gate, permission, or compliance claim that the document does not yet justify.

First inspect: `A.6`, `A.6.B`, `A.6.C`, `A.15`, `A.15.1`, `A.15.2`, `A.15.3`, `A.15.4`, `E.18`, `E.18.1`, `E.8`, and `E.19`.

### 3. Compare alternatives and make a local choice

Use this when a team needs to compare technologies, vendors, designs, policies, research paths, implementation options, or architecture moves without jumping to one favorite too early.

FPF helps you state what is being compared, which characteristics matter, which candidates are still in play, what evidence is missing, when a local choice is justified, and how to publish a selected set without hiding the comparison logic.

Typical first result: a comparison note with declared characteristics, candidate set, evidence gaps, the present scope of the choice, and what a selected-set publication may and may not be used to decide.

First inspect: `A.19`, `A.19.ECS`, `C.11`, `C.18`, `C.19`, `G.0`, and `G.5`.

### 4. Turn a vague situation into a usable problem statement

Use this when a project has complaints, opportunities, risks, anomalies, or strategic pressure, but no clear problem yet.

FPF helps you preserve partly formed concerns without pretending they are already requirements, decisions, causes, evidence, or work items. It can turn a vague situation into a problem card or problem portfolio that later work can use without erasing uncertainty.

Typical first result: a problem card, problem portfolio, or problem note that records what has been accepted, what remains only a cue, which context is involved, and which first pattern family can use the problem statement.

First inspect: `C.22.2`, `C.2.2a`, `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, and `B.5.2.0`.

### 5. Define what "better" means and run improvement

Use this when you need to improve a product, process, architecture, document, pattern, regulation, research program, or organization, but the improvement criteria are vague or competing.

FPF helps you define characteristics for evaluation, evaluate what is being improved, generate a portfolio of improvement proposals, choose changes that really improve the situation, and repeat the cycle without reducing quality to one score.

Typical first result: a quality-and-improvement note with evaluation characteristics, one evaluation of the object under improvement, a portfolio of proposed changes, and a condition for stopping or reopening the cycle.

First inspect: `A.19.ECS`, `E.22`, `E.23`, `C.16`, `C.25`, `E.21`, `E.9.DA`, and `E.2.DA` when the object is an FPF artifact.

### 6. Prepare evidence, assurance, or gate decisions before commitment

Use this when a project cannot responsibly act yet because evidence, assurance, constraints, gate validity, or decision permission is unclear.

FPF helps you separate what is being claimed from the evidence path, assurance argument, internal constraint validity, gate decision, local choice, and performed work. That separation matters when the cost of acting too early is high.

Typical first result: a commitment-readiness note that lists the claim, the evidence or assurance still needed, the gate or decision condition, and the work that remains blocked until those checks exist.

First inspect: `A.10`, `B.3`, `A.20`, `A.21`, `C.11`, `C.28`, and the relevant work or architecture pattern if the claim is about planned or performed work.

### 7. Check timing, freshness, rhythm, and action windows

Use this when a project depends on timing: freshness, latency, rate, cadence, action window, synchronization, inertia, aging, or rhythm.

FPF helps you separate timing information from evidence, permission, work completion, or vague urgency. It can say what timestamp, interval, cadence, freshness limit, action window, or rhythm claim is being used, and when that claim is no longer current enough for action.

Typical first result: a timing note that names what the timing is about, the relevant time relation or rhythm, the freshness or action-window limit, and the action that remains blocked when the timing claim is stale or underspecified.

First inspect: `C.27`, `A.10`, `A.20`, `A.21`, `C.11`, and the pattern that governs the thing whose timing matters.

### 8. Use causal explanations, interventions, responsibility, and model outputs safely

Use this when a project says that one thing causes another, a model output justifies an action, a change will produce an effect, or a role is responsible for an outcome.

FPF helps you separate causal use, counterfactual use, intervention claims, responsibility claims, model-output reliance, evidence, and decisions. It keeps a plausible explanation, prediction, or dashboard output from becoming permission to act.

Typical first result: a causal-use or model-output-use note that names the claim, the intervention or counterfactual being considered, the evidence or validation still needed, the responsibility limit, and the decision or work that remains blocked.

First inspect: `C.28`, `A.10`, `B.3`, `A.20`, `A.21`, `C.11`, and the domain pattern that governs the affected thing.

### 9. Compare descriptions, dashboards, explanations, and views of the same thing

Use this when a project has several descriptions, dashboards, explanations, renderings, model slices, or views and needs to know whether they are about the same thing, serve the same concern, or can be relied on in the same way.

FPF helps you keep the thing being described separate from its description, publication form, rendering, viewpoint, and same-thing claim. It can keep a diagram, dashboard, generated explanation, or view from silently becoming the thing itself, evidence, assurance, or decision.

Typical first result: a description-use note that names what is being described, which description or view is being used, how it is published or rendered, whether the same thing is really being addressed, and what the publication may and may not be used to claim.

First inspect: `E.17`, `E.17.0`, `E.17.EFP`, `A.15.4`, `A.7`, `C.30.AD`, and the pattern that governs the described thing.

### 10. Give things better names

Use this when project terms are misleading, overloaded, politically convenient, too broad, too local, or hard to translate between teams.

FPF helps you name products, roles, work processes, architecture elements, standards, document types, claims, characteristics, and project objects without treating a catchy label as ontology.

Typical first result: a naming card or term sheet that says what is being named, which local contexts use the name, which candidate names were rejected, which plain and technical names are allowed, and which alternate names are risky.

First inspect: `F.17`, `F.18`, `F.19`, `E.10`, `E.10.ARCH`, and the subject pattern that governs the thing being named.

### 11. Repair wording in technical documents before it changes action

Use this when standards, specifications, contracts, policies, dashboards, model cards, explanations, or working documents use words that may quietly change what can be claimed or done.

FPF helps you repair wording by first recovering the ontology: what thing, relation, value, evidence path, publication use, gate, decision, work, or architecture claim is actually being made. The repair is not word-policing; it succeeds only when the repaired text still tells someone what can now be used, checked, or named, or which related pattern to apply.

Typical first result: a repaired paragraph, claim register, term sheet row, or non-use decision that says what the text may now be used for and what claim or action remains blocked.

First inspect: `E.10`, `E.10.ARCH`, `F.18`, `F.19`, `A.6.P`, `C.2.P`, `C.16.P`, `C.16.Q`, `C.30.P`, `A.6.F`, and `A.6.M`.

### 12. Decide whether mathematics or formal modeling would help

Use this when intuition is not enough and a mathematical model, formal declaration, invariant, or explicit structure could make the work easier to review, compare, or improve.

FPF helps with two opposite mistakes: missing useful mathematics, and using mathematics without saying what structure it preserves and what it loses. It keeps mathematical-lens use, formal declarations of the assumed substrate, mechanism import or realization, and first-principles-to-work carry-through as different claims that may need different patterns.

Typical first result: a short modeling note that names what is being modeled, the candidate mathematical lens, any formal declaration that is needed, preserved and lost structure, payoff, validation limit, and next project action.

First inspect: `C.29`, `A.6.0`, `A.6.1`, `E.18.1`, `C.16`, `C.27`, `C.30.LCA`, `C.30.ILC`, and the domain pattern that governs the modeled claim.

### 13. Build a state-of-the-art or option portfolio

Use this when the project needs the current field of possible solutions, schools of thought, research lines, technologies, or design options, rather than one recommendation.

FPF helps you harvest alternatives, keep novelty and diversity visible, define comparison characteristics, avoid early collapse to one winner, and refresh the portfolio as the field changes.

Typical first result: a SoTA pack, option portfolio, candidate set, archive, or selector-ready publication with declared scope, comparison characteristics, and refresh condition.

First inspect: `G.0`, `G.1`, `G.2`, `G.5`, `G.10`, `G.11`, `C.18`, `C.19`, `A.19`, and `A.19.ECS`.

## One-Minute Example

A platform team asks:

> Should we buy, fine-tune, or build an agent stack for our product?

Without FPF, the conversation often mixes architecture, vendor comparison, safety, evidence, budget responsibility, user value, and implementation planning. The loudest option can win before the team knows what is being compared.

With FPF, the first pass can become a small set of explicit project objects:

- architecture question: what stack architecture is being changed or chosen;
- comparison frame: which alternatives are in the candidate set;
- evaluation characteristics: cost, latency, controllability, safety, maintainability, time to first use, and other project-specific characteristics;
- evidence gaps: what must be tested before commitment;
- current choice state: whether the team is choosing now, keeping a selected set, or doing more discovery;
- reader reliance: what engineering, management, and assurance readers may responsibly rely on.

That same shape can be used for a factory modernization, laboratory protocol, construction design change, supply-chain decision, safety case, or research program. The point is not the AI topic; the point is one body of reasoning that can be reviewed, improved, and published without changing meaning on the way.

## What FPF Is

FPF is a pattern language for disciplined thinking in projects where ordinary prose, local expert judgment, or one-off AI output is not enough.

It helps teams:

- keep meanings stable when work crosses teams, tools, documents, and time;
- separate the thing being discussed from diagrams, dashboards, explanations, promises, decisions, and actual work;
- state what a claim can responsibly be used for before people rely on it;
- compare options without collapsing too early to one favorite;
- define quality criteria before improvement starts;
- keep evidence, assurance, decisions, and implementation work visible as different questions;
- repair confusing wording by first asking what the wording is doing in the project, not by swapping synonyms;
- leave each pass with one useful next result: a clearer question, a better name, a comparison note, an evidence gap, a safer document, or a reason to inspect a specific pattern.

## What FPF Is Not

FPF is not:

- a shrink-wrapped project methodology;
- a checklist bureaucracy;
- a quick-answer cheat sheet;
- a replacement for domain expertise;
- a demand to study the whole specification before useful work begins;
- a promise that every project needs every pattern.

FPF is most useful when the cost of semantic drift, premature convergence, hidden evidence gaps, weak architecture, vague quality, or unreviewable work is higher than the cost of using a disciplined pattern language.

## How to Use This Repository

Start with the first practical entry that matches your project question. Then inspect the named pattern family and apply its Problem frame, Solution, examples, and checklist.

Use the `Preface` for the cross-cutting ideas behind the pattern language. Use the Table of Content when you already know the pattern family or need a search-oriented overview. Use extended cases only when the compact first entry is not enough.

If you use an AI assistant, attach or index `FPF-Spec.md` and ask for plain-language project help first. Let internal pattern names enter the conversation only when they make the reasoning more precise.

A good first prompt is:

```text
You have the FPF specification as a file.
Help me structure this project:
[short project description]

Use plain language for engineer-managers.
Propose the first useful FPF entry:
architecture, rules and methods, API or interface wording, permission or compliance wording, comparison and choice,
problem shaping, quality improvement, evidence and assurance,
temporal claims, causal or model-output use, publication or view use,
naming, technical-text precision, mathematical modeling,
or current options and state of the art.
For the selected entry, give:
1. the main project thing or claim at stake,
2. the first useful written result,
3. the first FPF patterns to inspect,
4. what still cannot be decided, trusted, or used responsibly.
```

## Citation

If you use FPF, please cite:

```text
Levenchuk, Anatoly. First Principles Framework (FPF).
GitHub repository: https://github.com/ailev/FPF
```

# **Preface** (non-normative)

## What This Specification Is And How To Use It

This document is the Core Conceptual Specification of the First Principles Framework (FPF). It defines a standards-style pattern language for explicit, reviewable, improvable conceptual work in engineering, research, management, governance, and mixed human and AI projects.

The reader should not need FPF vocabulary before this Preface becomes useful. Here an FPF term should first name an ordinary engineering distinction, then point to the pattern that gives the stricter form.

FPF is not a domain encyclopedia and not a project-management method. It is a framework for making hard project reasoning coherent when many kinds of things are easy to mix: systems, bodies of knowledge and models, architecture, descriptions, publications, concern-specific views, roles, methods, plans, performed work, evidence, decisions, options, commitments, and improvement criteria.

FPF starts from holons: project entities that can be treated as wholes and as parts. A holon can be a physical system, software system, organization, method, publication system, body of knowledge or model, research program, AI-agent arrangement, or another entity selected by a pattern. This is why FPF can be used across domains without flattening every domain into one vocabulary.

FPF is written as a pattern language. A pattern is not a tutorial, blog post, checklist bureaucracy, or local process script. It is a reusable action-guidance form. A mature FPF pattern lets a working practitioner recover:

- the working situation where the pattern is useful;
- the project thing under concern, which FPF calls the EntityOfConcern, and the relation, claim, or work object being handled;
- what goes wrong when the distinction is missed;
- the forces that make the problem hard;
- the solution and first useful result;
- the consequences and related patterns;
- the checks that keep the result reviewable.

The standard pattern form is governed by `E.8`. Review and refresh discipline is governed by `E.19`. Pattern-quality evaluation is governed by `E.21`. Decision-rationale records, or DRRs, are short records explaining why one bounded FPF content decision changed; they are governed by `E.9` and its specializations. Those patterns matter because the FPF corpus itself evolves by the same discipline it asks other projects to use: explicit decisions, visible losses, recoverable meanings, and repeated improvement.

The FPF `readme` section at the beginning of the specification is the public first-practical-entry section. It starts from recognizable project questions: architecture review, method writing, problem shaping, comparison, evidence, naming, mathematical modeling, quality improvement, and portfolios of current best-known options. This Preface has a different job. It explains why those entries fit into one framework and how FPF can answer them without becoming a pile of disconnected tools.

Use the `readme` when deciding where FPF may first help a project. Use this Preface when you need the whole-FPF picture. Use the Table of Content when you already know the pattern family or need a search-oriented overview. Use the pattern bodies after a project issue has proved important enough to need exact treatment.

The large areas of the specification can be read as one conceptual architecture. You do not need every name in this list yet; it is a map for later lookup:

- Part A gives the kernel: holons, contexts, roles, capabilities, methods, work, time, scope, signatures, architecture, characteristics, measurement, comparison, and foundations for choosing from candidate sets.
- Part B gives transdisciplinary reasoning, emergence, evidence, assurance, trust, canonical reasoning, creativity, problem-side material, and bridge discipline.
- Part C gives major extension patterns: characterization, measurement, mathematical modeling, architecture, temporality, causality, option portfolios, quality, problem shaping, and precision restoration in specialized domains.
- Part D keeps ethics, conflict, and multi-scale value questions visible where they are live.
- Part E gives the FPF constitution: pillars, guard rails, pattern form, lexical discipline, description and publication discipline, transduction graphs for carrying results through work, admission, review, and design-rationale discipline.
- Part F gives unification and naming: local meaning units, concept sets, bridges, term sheets, local-first naming, and technical prose repair.
- Part G gives state-of-the-art work, option portfolios, option selection, benchmarks, shipping, evidence, bridges, dashboards, and refresh disciplines for reusable domain work.
- Later material carries glossaries, expanded cases, annexes, or other supporting publication units when the compact pattern body is not enough.

That orientation list is only for lookup. The exact rules remain in the pattern bodies.

## FPF As A Project, Not Only A Pattern List

FPF is a project for improving how difficult reasoning is written, checked, taught, used by humans, and used by AI agents. The Core Specification is the normative center of that project, but it is not the whole project.

The Core Specification gives the pattern language: the named concepts, distinctions, pattern bodies, conformance checks, and relations that make FPF usable across domains. It says what the reasoning objects are and how claims should be governed. When a project needs to know whether a diagram is architecture, whether a dashboard is evidence, whether a model output may be used for a decision, or whether a term is hiding several kinds, the Core patterns carry the authoritative answer.

Other publication families may sit around the Core:

- companion explanations that teach the ideas more slowly;
- worked cases that show FPF on real engineering, research, management, AI, or safety problems;
- tooling guides that explain how to implement FPF written forms, including publication forms, in files, databases, editors, assistants, or review systems;
- project-local adaptations that apply FPF to one organization, product line, discipline, or regulatory environment;
- research notes that discuss adjacent ideas without governing FPF use.

Those materials can be valuable, but they have different jobs. They may teach, demonstrate, implement, translate, or specialize. They do not replace the Core pattern that governs the claim. If a companion says something more clearly than the Core, the useful explanation can be brought back into a pattern. If a tool makes an FPF form easier to use, the tool still implements the conceptual form; it does not become the conceptual form.

This separation protects both sides. The Core can stay tool-agnostic and pattern-centered. Companions and tools can be vivid, practical, and domain-rich without turning every example into a new norm. The Preface therefore speaks about FPF as a whole project while keeping the boundary clear: patterns govern, companions teach, tools implement, project-local material applies, and examples show.

## Why FPF Exists

Many projects do not fail because nobody had an idea. They fail because the idea changes kind as it travels.

A sketch becomes a promise. A dashboard becomes evidence. A model output becomes permission. A selected set becomes one winner. A method description becomes performed work. A diagram becomes the architecture. A safety case becomes safety. A clever metaphor becomes an ontology. The sentence still sounds familiar, but the project has changed what it is allowed to claim or do.

FPF exists to prevent that kind of drift while preserving useful movement. It does not ask every team to speak in formal notation. It lets rough, early, useful language remain rough while it is still only recognition text. When the same language begins to influence work, commitment, evidence, assurance, architecture, or choice, FPF gives a way to recover the kind of claim being made and the pattern that can govern it.

The practical ambition is simple: keep difficult reasoning alive long enough to improve it. A project should be able to generate alternatives, preserve uncertainty, compare options, choose locally, publish decisions, reopen stale claims, and repair language without losing the thing the reasoning was about. FPF calls that thing the EntityOfConcern.

For humans, FPF gives a shared working memory for complex reasoning. For AI agents, FPF gives typed constraints, named distinctions, and checkable written forms so generated text can be tested against the kind of work it claims to perform. For organizations, FPF gives a way to make reasoning transfer across teams without pretending that all teams use the same local meanings.

## Creativity And Assurance Mature Together

Many frameworks choose a side. Some optimize for assurance: audit trails, evidence, safety gates, confidence, compliance, and sign-off. Others celebrate creativity: exploration, novelty, pivots, abduction, and open-ended search. FPF is built to keep both rails alive at once.

Creativity without assurance drifts. Assurance without creativity calcifies. A project that only imagines produces attractive but untested possibilities. A project that only checks can become excellent at rejecting new options before it has generated any worth checking.

FPF treats creative work as governed search. It gives names to the early move where a team asks "what could be true?", to the generation of multiple candidate explanations or designs, to the preservation of novelty and diversity, to the comparison of alternatives, and to the point where exploration should narrow into refinement. The relevant families include abduction, problem shaping, novelty-diversity and open-ended exploration, set-returning selection, publications of current best-known options, and option portfolios.

FPF also treats assurance as more than a final audit. Evidence, assurance, freshness, source relation, gate validity, and decision permission are different claims. They can mature while creativity is still active. An early idea can be preserved as a cue without pretending it is evidence. A candidate can be kept in a portfolio without pretending it has been selected. A promising mathematical way of looking at the problem can be recorded without pretending it validates the world.

The useful order is not a required sequence. The practical stance is:

- generate enough candidate explanations or designs before converging;
- keep novelty, use value, constraint fit, and comparison characteristics visible;
- turn promising candidates into forms that evidence and assurance can inspect;
- publish selected options, Pareto-like fronts, or portfolios without hiding remaining uncertainty;
- reopen the work when evidence, source currentness, context, or state of the art changes.

In a laboratory, an anomaly is not merely noise. It may be a prompt for candidate explanations, followed by evidence and model comparison. In a product team, a concept sketch is not a meeting souvenir. It can become a reviewable knowledge object, which FPF calls an episteme, with scope, candidate value, and evidence needs. In operations, an emergency workaround may be a useful abductive move, but it must later be brought back into evidence, assurance, and work records.

This is one of FPF's central payoffs: a team can be inventive without losing its audit trail, and conservative without closing down imagination too early.

## Local Closure Inside An Open World

FPF assumes an open world. New evidence can arrive. A better mathematical model may appear. A source may become stale. A competitor may change the state of the art. A user need may shift. A new concern may reveal that the same system should be described differently.

Engineering and management still need local closure. A bridge cannot wait for all possible facts. A gate decision cannot cite the entire universe. A release, experiment, procurement, safety case, or architecture review must decide what is enough for the next action.

The old open-world versus closed-world distinction is a useful didactic picture. In an open world, absence of proof is not proof of absence. If a name is missing from a party guest list, the list may be incomplete. In a locally closed operational world, absence from the accepted manifest matters. If a name is missing from the aircraft manifest, the airline acts as if that passenger is not on the flight.

FPF does not transform the open world into a closed one. It lets a project build small closed worlds for declared purposes:

- a bounded context states which meanings and invariants are current;
- an EntityOfConcern states what project thing the reasoning is about;
- a description states what can be relied on and under what relation;
- evidence and assurance state what claim is credible enough for the local use;
- a gate or decision states what boundary is crossed;
- a reopen condition states when local closure is no longer enough.

This is why FPF patterns often look strict. The strictness is local. It lets a project act while keeping the wider world open. A local closure is not a claim that nothing else exists. It is a declared scope for responsible action.

## FPF As An Evolutionary Architecture For Thought

A method of thinking is itself a system. It can be brittle, ad hoc, and dependent on the memory of a few people. Or it can be architected so that reasoning can grow, change, and remain reviewable.

FPF is an evolutionary architecture for thought. It is not a static inventory of concepts. It is an architecture of patterns, relations, checks, publication units, and improvement loops that can evolve as new problems, domains, AI tools, and state-of-the-art lines appear.

The analogy with evolutionary architecture in engineering is deliberate. A good architecture does not freeze a system forever. It provides structures that make guided change possible. It names the characteristics that matter, the constraints that must survive change, the comparison basis for alternatives, and the records that explain why a change was accepted.

FPF applies the same idea to reasoning:

- patterns provide stable forms for recurring reasoning problems;
- DRRs record why normative FPF content changes;
- evidence and assurance patterns keep trust from becoming a feeling;
- characteristic spaces define what "better" means for the object under improvement;
- precision-restoration patterns repair language when it begins to carry work;
- state-of-the-art and option-portfolio patterns keep the frontier moving;
- review and refresh patterns let FPF itself improve.

The result is not one final answer. It is a way to keep producing, comparing, selecting, publishing, and improving answers without losing traceability or semantic integrity.

## Architectural Characteristics Of Thought

If FPF is an architecture for thought, then thought has architecture characteristics. Some of them are familiar quality words, but FPF treats them as characteristics of reasoning arrangements that can be improved, damaged, compared, or inspected.

| Characteristic of reasoning | What it protects | FPF mechanisms that help preserve it |
| --- | --- | --- |
| Auditability | A practitioner can ask why a claim is accepted and recover the evidence, rationale, or pattern that bears on it. | Evidence patterns, assurance patterns, DRRs, source-use discipline, and conformance checklists. |
| Evolvability | A model, pattern, or project claim can change without losing what it is about. | DRR discipline, refresh patterns, improvement loops, source currentness, and explicit reopen conditions. |
| Creativity | A project can generate novel and useful alternatives instead of converging on the first plausible answer. | Abduction, problem-side material, novelty-diversity search, option portfolios, set results, and current-option publications. |
| Composability | Complex reasoning can be built from smaller distinctions without hidden collapse. | Holons, roles, methods, signatures, interfaces, bridges, selected structures, and relation precision. |
| Falsifiability | A claim can fail in a declared way. | Pattern conformance checks, evidence boundaries, measurement construction, and explicit non-use results. |
| Cross-scale coherence | Reasoning can move across parts, wholes, systems of systems, and bodies of knowledge without free aggregation. | Holonic structure, bridge discipline, aggregation patterns, scale and temporal patterns, and mathematical modeling that states preserved and lost structure. |
| Design-run integrity | Plans, method descriptions, design choices, performed work, and runtime evidence do not collapse into one object. | Design and run separation, work patterns, method patterns, planning patterns, and P2W carry-through. |
| Lexical and representation discipline | Names, diagrams, dashboards, and encodings do not quietly become the entity or claim they describe. | EntityOfConcern and description distinction, `E.10`, `E.10.ARCH`, `F.18`, `F.19`, and publication-use patterns. |
| Measurement and comparability | "Better", "safer", "faster", or "ready" is tied to declared characteristics and scales. | Characteristic spaces, measurement patterns, comparison patterns, option-evaluation patterns such as NQD and OEE for comparing candidates under declared characteristics, and discipline for choosing options from candidate sets. |
| Trust calibration | Reliance changes with evidence, source freshness, scope, and cross-context movement. | Evidence graph discipline, assurance, decay, gate, bridge, and source-return patterns. |
| Scope safety | A claim remains inside its context and does not silently widen. | Bounded contexts, EntityOfConcern, concern-specific descriptions, source relation, scope, and bridge-loss discipline. |
| Reproducibility | A result can be replayed or rechecked under the same declared inputs, edition, time, and source state. | Design-run separation, evidence source references, versioned records, time patterns, and publication currentness. |
| Change-impact visibility | A reader or evaluator can see what a change affects and what it leaves untouched. | DRRs, relations, source-return conditions, architecture characteristics, and improvement records. |
| Exploration health | A project can see whether it has explored enough of the option space before selecting. | Novelty-diversity, option portfolios, current-option publications, Pareto-like fronts, archives, and publications ready for option selection. |
| Didactic clarity | The working reader can see why a distinction matters and what changes in practice. | `E.2` pillars, `E.8` pattern form, `E.11` discoverability, `E.12`, `E.19`, and plain explanation paired with technical fields. |
| Epiplexity control | The structural entanglement that makes a holon hard to understand, change, reuse, or improve is not hidden by a simple diagram. | Architecture patterns, structural views, module and interface patterns, scale patterns, and architectural-characteristic evaluation. |

The table is not a checklist for every project. It shows the kind of quality FPF is trying to preserve in reasoning itself. A project may enter through architecture, naming, evidence, mathematics, or comparison, but the deeper benefit is that the reasoning becomes more auditable, evolvable, and usable.

## Beyond Bias Hunting

Critical-thinking practice often focuses on cognitive biases: confirmation bias, availability bias, planning fallacy, fixation, groupthink, and many others. That work is useful. It gives names to predictable failures in human judgment.

But bias hunting is mostly corrective. It starts after a bad pattern of reasoning has appeared. It asks the thinker to remember a growing list of mistakes and avoid them by vigilance.

FPF takes a more constructive stance. It does not only say "do not confuse the plan with reality." It gives separate objects for method description, plan, performed work, evidence, and result. It does not only say "do not trust the dashboard too much." It distinguishes evidence, published dashboard rendering, assurance, gate, and decision. It does not only say "do not jump to a favorite option." It gives candidate sets, comparison characteristics, selected options, and portfolio refresh.

That is why FPF's discipline around wording and descriptions should not make FPF look like a commission for checking speech. The repair matters, but it is not the center. The center is constructive: build reasoning arrangements in which whole classes of mistakes become harder because the thing under concern, claim kind, evidence path, publication use, decision, and work object are not allowed to collapse unnoticed.

This changes the tone of FPF. It is not a list of warnings. It is a design language for better reasoning. The user should come away not only knowing what not to say, but knowing what to build next: an architecture question note, problem card, comparison frame, characteristic space, evidence-readiness note, naming card, repaired paragraph, modeling note, option portfolio, or improvement loop.

## Thinking Through Writing

FPF relies on written forms because serious reasoning needs objects that can be inspected. In everyday work, much reasoning stays inside conversation, memory, chat logs, sketches, or tool outputs. That is often enough for one short exchange. It is not enough when reasoning must survive delegation, review, reuse, publication, AI assistance, or time.

FPF's cards, records, tables, views, term sheets, characteristic spaces, pattern bodies, conformance checks, and DRRs are thinking instruments. They are not documentation after the fact. Writing the record is often the work of thinking:

- a problem card separates a complaint from a problem that later work can use;
- a comparison frame forces the team to say what is being compared and by which characteristics;
- a characteristic space makes "better" visible before improvement starts;
- a term sheet keeps local meanings from being flattened across teams;
- a DRR exposes what decision changed the specification and why;
- a pattern body makes a recurring working problem reusable without hiding its boundaries.

The medium is not prescribed. A team may use paper, markdown, a wiki, a spreadsheet, a model repository, or a specialized tool. FPF is tool-agnostic. What matters is the conceptual structure of the durable publication unit and the relations it makes recoverable.

This is especially important for AI use. An AI assistant can generate fluent prose faster than a team can inspect it. FPF forms give the generated material places to land: candidate set, evidence gap, description-use note, architecture question, term sheet row, source-return condition, or blocked-use result. Without such forms, the output often remains persuasive text rather than project reasoning.

Thinking through writing is not paperwork. It is how thought becomes durable enough to challenge, improve, and responsibly act on.

## Thinking-Oriented Architecture, Not A Descriptive Upper Ontology

FPF shares one ambition with upper ontologies: it tries to make reasoning travel across domains. But its primary task is different.

A descriptive upper ontology tries to give a consistent inventory of what exists. It asks "what kind of entity is this?" and gives a taxonomy, axioms, and relations. That work is valuable. FPF uses ontological discipline constantly. But FPF is not only an inventory of entities.

FPF is a thinking-oriented architecture. It asks:

- what project thing is under concern in this project moment;
- what claim, relation, decision, evidence path, work object, or publication use is being made;
- what distinction must remain visible for action to be responsible;
- what pattern can govern the next move;
- what would make the result reviewable and reopenable.

This is the difference between a catalogue and an instrument. A catalogue can tell you that a method description and performed work are different kinds of things. FPF also asks what happens in the project when those two are confused, what written form should separate them, what evidence or decision remains blocked, and what pattern should be used next.

The ontology therefore serves action guidance. FPF does not replace domain ontologies, mathematics, standards, or evidence. It gives them a place in project reasoning so they can be used without collapsing local meanings or publication forms.

## The Bitter Lesson Stance

FPF also carries a Bitter-Lesson-compatible stance. In AI, software, and open-ended engineering, systems that can use more search, more data, more compute, and more general learning often outperform brittle hand-coded procedure scripts when the domain changes or scale grows.

FPF does not turn that observation into blind automation. It translates it into an architectural preference:

- state goals, constraints, budgets, and checks more clearly;
- give agents and teams freedom to search within those declared bounds;
- keep safety, evidence, assurance, and gate conditions explicit;
- measure outcomes and refresh policies when the environment or model changes;
- avoid hiding brittle procedure scripts inside prose that looks like general guidance.

The important separation is between design-time constraints and run-time action. A designer may declare prohibited actions, risk budgets, cost ceilings, allowed tools, escalation conditions, evidence minima, or acceptance criteria. That is different from prescribing every step the acting system must take.

There are cases where procedure is required: safety, regulation, legal compliance, reproducibility, and training may need specified method descriptions. FPF does not forbid that. It requires the kind of claim to be explicit. A procedure script is a method description or work instruction; a constraint set is not the same thing; a monitor is not the same thing as evidence of success; a gate is not the work itself.

This stance helps with human and AI work alike. A team can use general agents, search, simulation, model refresh, or state-of-the-art harvesting without surrendering safety. The freedom lives inside constraints, budgets, evidence, and typed checks.

## From Flat Documents To Multi-View Truth

Traditional document practice often treats one file as "the truth". Contemporary projects rarely fit that shape. A product, organization, architecture, safety case, research program, model, or AI-agent arrangement may need many descriptions for different concerns.

FPF separates the pieces:

- the EntityOfConcern is the project thing under concern;
- a description is a reviewable knowledge object, or episteme, that describes it;
- a view is a selected presentation of description material for a concern;
- a viewpoint states the concern and selection discipline behind a view;
- a publication form makes a description, view, card, record, table, or dashboard available for use;
- a carrier is the physical or digital rendering or storage that makes the publication form available;
- a reliance boundary says what the publication may responsibly be used for.

This is why a diagram is not the architecture, a dashboard is not evidence by itself, a model card is not model safety, and a generated explanation is not the system it explains. They can all be valuable, but each has a kind and a relation.

Multi-view publication is therefore a strength, not a defect. A safety case, architecture description, dashboard, model card, evidence graph, and management summary may all concern the same project thing under different viewpoints. FPF's job is to keep them connected without letting one view silently replace another.

This is also how FPF can work with distributed and AI-generated representations. A vector representation, solver model, graph, natural-language summary, and human-readable pattern can all be treated as descriptions or views when their relation to the project thing, source, viewpoint, and reliance boundary is declared. The question is not whether one carrier is more "real" than another. The question is what claim the publication can responsibly carry.

## Architecture As Structure Of Holons

FPF treats architecture as structure of a holon in a context, not as a diagram, document, approval, promise, or implementation plan.

This makes architecture broad. There can be architecture of a physical system, software system, organization, work system, body of knowledge, publication system, research program, AI-agent arrangement, or FPF itself. Wherever holons have structure, architecture can be discussed.

Architecture descriptions, structural views, viewpoints, diagrams, models, and publication forms are descriptions or publications about architecture. They are valuable, but they do not replace the architecture itself.

The architecture patterns make this distinction usable. `C.30` governs architecture as an EntityOfConcern. `A.22` governs architectural characteristics. `C.30.ASV` governs architecture structural views. `C.30.AD` governs architecture descriptions. `A.6.M` governs module-interface relation repair. `C.31` and related architecture patterns govern modularity, reusable structure, scale, selected structures, interlevel tension, and architecture-changing moves.

This matters because architecture work is not only "draw the diagram". It is also "which structure matters", "what characteristic changes", "what tradeoff is visible", "what description is needed", "what interface claim is being made", "what evidence would make this architecture decision responsible", and "which move changes the architecture rather than merely changing a document about it".

Epiplexity is one important architecture characteristic. It names the structural entanglement that makes a holon hard to understand, change, control, reuse, or improve. A low-epiplexity design is not merely simpler in ordinary speech. It is structurally easier to reason about under declared characteristics and concerns.

## Boundary Statements

Most of the time, teams can use fast compressed speech. "The service guarantees it." "The model is synced." "The dashboard proves it." "The interface is stable." "The process is compliant." In ordinary conversation, people often infer enough to continue.

That changes when the sentence crosses into an API, contract, safety case, evaluation protocol, dashboard used for commitment, SLO, SLA, compliance text, model card, dataset sheet, reproducibility checklist, or operational gate. At that point language is not merely communication. It can become system-relevant.

The danger is that one sentence may try to do several jobs at once:

- define a term or condition;
- say what a mechanism admits;
- assign a commitment or permission;
- claim evidence or work effect;
- publish a view or decision;
- move responsibility across a boundary.

If those jobs remain bundled, the sentence becomes hard to check. Later disagreement is then resolved by authority or politics rather than by the pattern that governs the claim.

FPF's boundary discipline, especially around the `A.6` family, repairs such cases by separating claim kinds. A contract line, interface statement, API schema, compliance note, or safety-case sentence can be unpacked into definition, admissibility, commitment, evidence, work effect, publication, and decision components as needed. The point is not to force every document into a heavy form. The point is to keep boundary language from changing system behavior without an inspectable claim.

## Raising Semantic Precision

FPF does not expect people to start with perfect terminology. Early thinking is often compressed, metaphorical, and useful. That is not a failure. It becomes a problem only when the compressed phrase begins to govern action, evidence, architecture, publication, decision, work, assurance, or mathematical modeling.

FPF therefore provides a semantic precision upgrade path:

1. Notice the wording that is doing too much. Broad heads, pronouns, metaphors, status words, level words, support words, function words, architecture words, and evidence words often signal a hidden claim.
2. Recover the project thing under concern, relation, claim, or project-side source relation being made.
3. Recover the ontology before changing the word. Name the kinds, slots, context, viewpoint, time, evidence, and use that matter.
4. Use mathematical modeling or a formal signature only when it helps. FPF calls these a math lens or formal substrate when a graph, order, signature, state space, topology, probability model, or variational principle makes the structure reviewable. Mathematics is not decoration.
5. Rewrite the wording as a plain reader line and, when needed, technical fields so the practical point remains readable and the claim remains checkable.
6. State what can now be done, what remains blocked, and which pattern governs a different claim.

This is why `E.10` is a trigger scan rather than a synonym list. `E.10.ARCH` distributes repair to the pattern that can recover the ontology. `A.6.P`, `C.2.P`, `C.16.P`, `C.16.Q`, `C.30.P`, `A.19.SPR`, `A.6.F`, `F.18`, and `F.19` carry major repair families. `C.29` helps when a mathematical lens is needed. `A.6.0` governs formal-substrate declarations when a formal signature is the right object.

The success condition is not "the text now sounds precise". The success condition is that after removing overread, the working reader still has a useful move: use the claim within its declared limit, repair it further, apply the related pattern that governs the remaining claim, or block the claim until needed material is supplied.

## Big FPF Storylines

Several commitments make FPF more than a collection of patterns.

1. Holons give one root for systems, bodies of knowledge, organizations, publications, methods, and other entities that can be treated as wholes and parts.
2. The project thing under concern and its description are kept distinct so descriptions, views, diagrams, publications, and carriers do not replace what they describe.
3. Context keeps meaning local, while bridges and term sheets let meanings travel without collapse.
4. Role, method, plan, performed work, evidence, decision, and gate are different kinds of project objects.
5. Architecture is structure of holons, and architecture descriptions are descriptions of that structure.
6. Evidence and assurance are first-class, so trust is not reduced to confidence prose.
7. Comparison and improvement require declared characteristics, scales, candidate sets, and current comparator fields.
8. Creativity is governed search over candidate possibilities, not an uninspectable burst of inspiration.
9. State of the art is a refreshable publication object, not a frozen leaderboard.
10. Semantic precision starts from ontology and, when useful, from mathematical modeling that preserves declared structure, not from synonym replacement.
11. Pattern publication is itself part of the thinking architecture: patterns, DRRs, checks, and improvement loops keep FPF evolvable.
12. Didactic primacy keeps the whole structure usable by working readers rather than only by authors of the specification.

These storylines are connected. Architecture needs characteristics. Characteristics need comparison. Comparison needs evidence. Evidence needs publication and source-use discipline. Language repair needs ontology. Ontology often benefits from a mathematical lens. Improvement needs state-of-the-art comparison. FPF's value comes from the composition.

## Transdisciplinarity As A Meta-Theory Of Thinking

Modern complexity lives at the junction of traditions. A manufacturing engineer, software architect, safety engineer, finance analyst, ML researcher, and operations manager may use the same words for different things and different words for the same thing. They may also use different forms of proof, different measures of quality, and different standards for acting.

FPF treats transdisciplinarity as a meta-theory of thinking. It is not a new specialist dialect that replaces local traditions. It is a way to design reasoning across traditions while preserving local meanings.

The key move is local-first meaning. A term belongs to a context before it travels. A term sheet can align senses, but it does not erase their local differences. A bridge can say how meanings correspond, where they lose structure, and what cannot be transferred. A comparison can compare candidates, but only under declared characteristics and evidence minima. A mathematical lens can reveal shared structure, but it must say what it preserves and what it loses.

This is how a single framework can help in architecture, biology, manufacturing, AI-agent systems, safety assurance, management, education, and research without pretending those domains are the same. FPF does not flatten domains. It gives them governed interfaces for reasoning together.

## The Culinary Architecture Of Collective Thought

Many FPF ideas sound familiar. Evolution, exploration and exploitation, evidence, roles, boundaries, architecture, comparison, naming, and improvement are not new ingredients. A thoughtful reader may ask why FPF formalizes so many "obvious" ideas.

The answer is that FPF is not trying to invent the ingredients. It is trying to build the kitchen.

A domain methodology is like a cookbook. It gives excellent recipes for a class of dishes: software delivery, scientific experiment, safety case, product discovery, architecture review, or policy design. A skilled practitioner can often cook one dish beautifully from experience alone.

FPF is closer to the architecture of a professional kitchen. It gives places, instruments, roles, interfaces, checks, and repeatable forms so many dishes can be prepared, compared, improved, and served without chaos. The value is not that flour or heat are new. The value is that ingredients, techniques, stations, timing, quality checks, and presentation can work together at scale.

In FPF terms:

- roles separate who can act, review, evidence, decide, or publish;
- methods and method descriptions separate how action can be performed from the document describing it;
- work patterns keep actual change distinct from plans;
- evidence and assurance keep proof and reliance inspectable;
- characteristic spaces define what quality means for the object at hand;
- architecture patterns keep structure distinct from diagrams;
- naming and term sheets let people talk across contexts without semantic collapse;
- state-of-the-art and option portfolios keep search open before selection;
- improvement loops let the whole arrangement get better over time.

For a small well-known problem solved by one expert, FPF may feel heavier than intuition. Its advantage appears when reasoning must be collective, long-lived, high-stakes, cross-domain, AI-assisted, or open-ended. That is where tacit expertise alone becomes hard to audit, transfer, or refresh.

FPF does not replace expert judgment. It gives expert judgment a shared architecture so it can compound rather than evaporate.

## The Intellect Stack As A Pedagogical Map

The phrase "Intellect Stack" names a learning map of capabilities. In this specification it is pedagogy, not a required sequence or a new ontology.

The point is simple: complex reasoning usually needs several capability families, and teams often underinvest in one of them.

| Capability area | Question it helps a learner ask | FPF families that often appear |
| --- | --- | --- |
| Structure and reality | What exists, how is it bounded, and what structure matters? | Holons, contexts, architecture, selected structures, signatures, and discipline about the project thing under concern. |
| Knowledge and reasoning | Why should this claim be trusted, and what would change that trust? | Evidence, assurance, source-use, publication, views, explanations, and refresh. |
| Action and work | How does intent become change, and what work actually happened? | Roles, methods, method descriptions, plans, performed work, design-run linking records, and P2W. |
| Strategy and choice | Which option is better under uncertainty and for whom? | Characteristics, comparison, local decision, selected options, portfolios, and current-option publications. |
| Purpose and governance | Why act, what must not happen, and what is allowed to count as success? | Objectives, constraints, gates, ethics, assurance, budgets, and improvement loops. |

This stack is not a sequence that every project must follow. It is a way to notice missing capability. A team may enter through architecture and discover that it lacks evidence. It may enter through naming and discover that it has not named the project thing under concern. It may enter through mathematical modeling and discover that it lacks declared characteristics for comparison.

The learning value is that FPF can be taught as a set of capabilities, not only as a list of pattern ids.

## Purpose, Scope, And Non-Goals

FPF's purpose is to help people and AI agents produce reasoning that survives use: reasoning that can be aligned, reviewed, improved, published, delegated, refreshed, and reopened without losing the thing it was about.

The Core Specification defines conceptual patterns, distinctions, publication forms, and checks. It is tool-agnostic. It does not prescribe a software stack, file format, repository layout, meeting style, workflow engine, or organizational method. Those may be useful in a project, but they are not the conceptual core.

FPF also does not replace domain expertise, evidence, mathematics, standards, or local judgment. It gives them a disciplined place in reasoning. A domain expert still knows the pump, reactor, contract, model, laboratory, organization, or market. FPF helps the expert's reasoning become inspectable, comparable, and evolvable across contexts.

FPF's non-goals are short:

- it is not a domain encyclopedia;
- it is not a universal procedure sequence;
- it is not a prompt collection;
- it is not one mathematical doctrine;
- it is not a license to turn every project into paperwork;
- it is not a substitute for evidence or accountability.

Its positive scope is broader than those refusals. FPF is a compact language for keeping hard work honest enough to act on and alive enough to improve.

## How To Continue After The readme

Start with the `readme` when you are deciding whether FPF can help a working project. Read this Preface when you want the ideas that make the first practical entries fit together. Use the Table of Content when you need to locate a pattern family. Then use the pattern body that governs the claim, relation, publication use, architecture, evidence, decision, work, name, mathematical lens, option portfolio, or improvement object you actually have.

Do not read the specification linearly unless that is your study goal. In project use, the first useful FPF pattern family is selected by the working question.

The main practical habit is this: when a project sentence starts to matter, ask what kind of thing it is talking about, what claim it is making, what can responsibly be done with that claim, and which pattern can keep the next move honest. That habit is small. The architecture behind it is the rest of FPF.

# Part A – Kernel Architecture Cluster

