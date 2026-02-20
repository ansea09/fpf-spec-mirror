# First Principles Framework (FPF) — Core Conceptual Specification
by Anatoly Levenchuk and assortment of LLMs.
February 2026

Pattern and headers templates are explained in pattern E.8.

# Table of Content

 **Preface (non-normative)**

| ID & Title                                                                                                                                   | Status    | Concise content reminder — “what belongs here”                                                                                                                                                                                        |
| :------------------------------------------------------------------------------------------------------------------------------------------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| FPF is a first principle based architecture decisions for transdiciplinary SoTA methods of evolving holons: systems, epistemes, communities. | full text | FPF serves the Engineer, Researcher, and Manager by providing a generative pattern language for constructing and evolving thought, designed as an "operating system for thought".                                                     |
| Creativity in Open-Ended Evolution and Assurance*                                                                                            | full text | FPF integrates assurance (audits, evidence) and creativity (generating novel ideas) as complementary engines for responsible innovation, providing a structured choreography for creative work from abduction to operation.           |
| Navigating Uncertainty: Building Closed Worlds within an Open World                                                                          | full text | Explains how FPF reconciles Open-World and Closed-World assumptions, using Bounded Contexts to create reliable 'islands of closure' for engineering decisions within an inherently open world.                                        |
| FPF as an Evolutionary Architecture for Thought                                                                                              | full text | Positions FPF as an architecture for the reasoning process itself, designed to sustain key characteristics like auditability, evolvability, and falsifiability by applying architectural thinking to the dynamics of reasoning.       |
| Architectural Characteristic of Thought                                                                                                      | full text | Details the key characteristics of rigorous thought (e.g., Auditability, Evolvability, Composability) and the specific FPF mechanisms designed to preserve them.                                                                      |
| Beyond Cognitive Biases: FPF as a Generative Architecture for Thought                                                                        | full text | Contrasts FPF's generative, structural approach to avoiding cognitive errors with the traditional corrective, diagnostic approach of hunting for biases, framing FPF as a scaffold that makes errors harder to commit.                |
| Thinking Through Writing: The FPF Discipline of Conceptual Work                                                                              | full text | Describes how FPF uses a discipline of "thinking through writing" with conceptual forms (Cards, Tables, Records) to make thought tangible, shareable, and auditable, while remaining tool-agnostic.                                   |
| Descriptive Ontologies vs. A Thinking-Oriented Architecture                                                                                  | full text | Differentiates FPF's goal of orchestrating reasoning from classical ontologies' goal of cataloging existence, emphasizing FPF's focus on objectives, trust, and dynamics.                                                             |
| The "Bitter Lesson" trajectory — compute, data, and freedom over hand‑tuned rules (FPF stance)                                               | full text | How FPF operationalizes the contemporary trend: prefer general models + data + compute + minimal constraints; autonomy budgets; rule‑of‑constraints vs instruction‑of‑procedure; continuous adaptation.                               |
| From Flat Documents to High-Dimensional Truth: The Multi-View Architecture                                                                   | full text | Shows how FPF replaces flat documents with a multi-view architecture: epistemes as slot graphs, engineering views as projections, and MVPK as typed publication surfaces that keep dashboards lawfully tethered to work and evidence. |
| Boundary Statements: Where Language Becomes a System Boundary                                                                          | full text | Introduces the A.6 boundary cluster: why certain sentences behave like contracts, and how routing (laws vs gates vs duties vs evidence) keeps them evolvable and multi-view safe. |
| Raising Semantic Precision: From Triggers to Math‑Backed Ontics                                                                        | full text | Describes the precision-upgrade workflow behind A.6.P: detect umbrella words, unpack the local ontology, choose a stable mathematical substrate, refactor the model, and mint precise lexemes + guardrails (Tech/Plain twins). |
| The “big storylines” unique to FPF (load‑bearing commitments)                                                                                | full text | Lists the nine core, load-bearing commitments that define FPF's unique architectural and philosophical stance, from its holonic kernel to its explicit treatment of creativity and assurance.                                         |
| Transdisciplinarity as a Meta‑Theory of Thinking                                                                                             | full text | Explains how FPF treats transdisciplinarity as a meta-theory for designing reasoning, using FPF patterns as generative scaffolds grounded in physical reality to bridge disciplinary silos.                                          |
| FPF as a Culinary Architecture for Collective Thought: Why We Formalize “Obvious” Ideas                                                      | full text | Uses the 'culinary architecture' analogy to explain FPF's role in synthesizing 'obvious' ideas into a robust framework for complex, generative problems.                                                                              |
| Intellect Stack (informative Overview)                                                                                                       | full text | Presents a five-layer pedagogical map of cognitive skills (Structure → Knowledge → Action → Strategy → Governance) and links them to FPF patterns.                                                                               |
| Purpose, Scope, and Explicit Non‑Goals                                                                                                       | full text | Clarifies FPF's mission as a generative scaffold for thought, its scope as tool-agnostic normative patterns, and what it explicitly is not (e.g., a domain encyclopedia or a specific methodology).                                   |

**Part A - Kernel Architecture Cluster**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| A.0 | **Onboarding Glossary (NQD & E/E‑LOG)** | Stable | *Keywords:* novelty, quality‑diversity (NQD), explore/exploit (E/E‑LOG), portfolio (set), illumination map (report‑only telemetry), parity run, comparability, ReferencePlane, CL^plane, ParetoOnly default. *Queries:* "What is NQD in FPF?", "How does FPF handle creative generation?", "What is an explore-exploit policy in FPF?" | **Builds on:** E.2, A.5, C.17–C.19. **Coordinates with:** E.7, E.8, E.10; F.17; G.5, G.9–G.12. **Constrains:** Any pattern/UTS row that describes a generator, selector, or portfolio. |
| ***Cluster A.I - Foundational Ontology*** | | | | |
| A.1 | **Holonic Foundation: Entity → Holon** | Stable | *Keywords:* part-whole composition, system boundary, entity, holon, U.System, U.Episteme. *Queries:* "How does FPF model a system and its parts?", "What is a holon?", "Difference between entity and system." | **Builds on:** P-8 Cross-Scale Consistency. **Prerequisite for:** A.1.1, A.2, A.14, B.1. |
| A.1.1 | **`U.BoundedContext`: The Semantic Frame** | Stable | *Keywords:* local meaning, context, semantic boundary, domain, invariants, glossary, DDD. *Queries:* "How does FPF handle ambiguity?", "What is a Bounded Context in FPF?", "How to define rules for a specific project?" | **Builds on:** A.1. **Prerequisite for:** A.2.1, F.0.1. |
| A.2 | **Role Taxonomy** | Stable | *Keywords:* role, assignment, holder, context, function vs identity, responsibility, U.RoleAssignment. *Queries:* "How to model responsibilities?", "What is the difference between what a thing *is* and what it *does*?" | **Builds on:** A.1, A.1.1. **Prerequisite for:** A.2.1-A.2.6, A.13, A.15. |
| A.2.1 | **`U.RoleAssignment`: Contextual Role Assignment** | Stable | *Keywords:* Standard, holder, role, context, RoleEnactment, RCS/RSG. *Queries:* "How to formally assign a role in FPF?", "What is the Holder#Role:Context Standard?" | **Refines:** A.2. **Prerequisite for:** A.15. |
| A.2.2 | **`U.Capability`: System Ability (dispositional property)** | Stable | *Keywords:* ability, skill, performance, action, work scope, measures. *Queries:* "How to separate ability from permission?", "What is a capability in FPF?" | **Builds on:** A.2. **Informs:** A.15, A.2.3. |
| A.2.3 | **`U.PromiseContent`: Consumer‑facing Promise Clause** | Stable | *Keywords:* promise content, promise content, accessSpec, acceptanceSpec, SLO, SLA, claim scope (G), Work evidence, provider/consumer roles. *Queries:* "What is a promise content in FPF?", "Promise content vs Work vs MethodDescription", "How do access and acceptance differ?", "How is SLO/SLA adjudicated from Work evidence?" | **Builds on:** A.2.2. **Prerequisite for:** F.12. **Used by:** A.2.8, A.6.C, A.6.8. |
| A.2.4 | **`U.EvidenceRole`: The Evidential Stance** | Stable | *Keywords:* evidence, claim, support, justification, episteme. *Queries:* "How does an episteme serve as evidence?", "Modeling evidence roles." | **Builds on:** A.2. **Informs:** A.10, B.3. |
| A.2.5 | **`U.RoleStateGraph`: The Named State Space of a Role**| Stable | *Keywords:* state machine, RSG, role state, enactability, lifecycle. *Queries:* "How to model the state of a role?", "What is a Role State Graph?" | **Builds on:** A.2.1. **Prerequisite for:** A.15. |
| A.2.6 | **Unified Scope Mechanism (USM): Context Slices & Scopes**| Stable | *Keywords:* scope, applicability, ClaimScope (G), WorkScope, set-valued. *Queries:* "How to define the scope of a claim or capability?", "What is G in F-G-R?" | **Builds on:** A.1.1. **Constrains:** A.2.2, A.2.3, B.3. |
| A.2.7 | **`U.RoleAlgebra`: In-Context Role Relations (`≤`, `⊥`, `⊗`)** | New | *Keywords:* role algebra, specialization (`≤`), incompatibility (`⊥`), bundles (`⊗`), separation of duties (SoD), requiredRoles substitution. *Queries:* "What does `RoleS ≤ RoleG` mean in FPF?", "How do I encode Separation of Duties with `⊥`?", "How do role bundles (`⊗`) work?" | **Builds on:** A.2. **Prerequisite for:** A.15, A.2.5. |
| A.2.8 | **`U.Commitment`: Deontic Commitment Object** | Stable | *Keywords:* commitment, deontics, obligation/permission/prohibition, modality normalization, scope+validity window, adjudication hooks, evidenceRefs, BCP‑14 (RFC 2119/8174). *Queries:* "How to represent MUST/SHALL as a lintable object?", "How to keep deontics separate from admissibility gates?", "How to make commitments auditable via evidence hooks?" | **Refines:** A.2. **Builds on:** A.2.1, A.2.3, A.2.6, A.7, A.15.1. **Used by:** A.6.B (Quadrant D), A.6.C. |
| A.2.9 | **`U.SpeechAct`: Communicative Work Object** | Stable | *Keywords:* speech act, communicative work, approval/authorization/publication/revocation, provenance, act≠utterance≠carrier, judgement context, window/freshness, institutes.*. *Queries:* "How to model approvals/authorizations as Work?", "How to separate act vs utterance vs carrier?", "How to link commitments to instituting acts without commitment-by-publication?" | **Refines:** A.2. **Builds on:** A.2.1, A.2.6, A.7, A.10, A.15.1. **Used by:** A.2.8, A.6.C (utterance/instituting-act hook). |
| ***Cluster A.II - Transformation Engine*** | | | | |
| A.3 | **Transformer Constitution (Quartet)** | Stable | *Keywords:* action, causality, change, System-in-Role, MethodDescription, Method, Work. *Queries:* "How does FPF model an action or a change?", "What is the transformer quartet?" | **Builds on:** A.2. **Prerequisite for:** A.3.1, A.3.2, A.15. |
| A.3.1 | **`U.Method`: The Abstract Way of Doing** | Stable | *Keywords:* recipe, how-to, procedure, abstract process. *Queries:* "What is a Method in FPF?", "Difference between Method and Work." | **Refines:** A.3. **Prerequisite for:** A.15. |
| A.3.2 | **`U.MethodDescription`: The Recipe for Action** | Stable | *Keywords:* specification, recipe, SOP, code, model, epistemic artifact. *Queries:* "How to document a procedure?", "What is a MethodDescription?" | **Refines:** A.3. **Informs:** A.15. |
| A.3.3 | **`U.Dynamics`: The Law of Change** | Stable | *Keywords:* state evolution, model, simulation, state space. *Queries:* "How to model state transitions or system dynamics?", "Difference between a Method and Dynamics." | **Builds on:** A.19. **Informs:** B.4. |
| ***Cluster A.III - Time & Evolution*** | | | | |
| A.4 | **Temporal Duality & Open-Ended Evolution Principle** | Stable | *Keywords:* design-time, run-time, evolution, versioning, lifecycle, continuous improvement. *Queries:* "How does FPF handle plan vs. reality?", "How are systems updated?" | **Builds on:** P-10 Open-Ended Evolution. **Prerequisite for:** B.4. |
| ***Cluster A.IV - Kernel Modularity*** | | | | |
| A.5 | **Open-Ended Kernel & Extension Layering** | Transitional stub | *Keywords:* FPF architecture, specialization vs dependancy hierarhies, modularity, extensibility. *Queries:* "What is the architecture of FPF?", "How are new domains added?" | **Builds on:** P-4, P-5. |
| ***Cluster A.IV.A - Signature Stack & Boundary Discipline (A.6.*)*** | | | | |
| A.6 | **Signature Stack & Boundary Discipline** | Stable | *Keywords:* boundary, signature stack, routing, laws, admissibility, deontics, evidence, claim register, MVPK, view/viewpoint, surface. *Queries:* "What is the Signature Stack in FPF?", "How do I route boundary statements (laws vs gates vs duties vs evidence)?", "How to avoid contract-soup drift in boundary descriptions?" | **Builds on:** E.8, A.6.0, A.6.1, A.6.3, E.17.0, E.17, A.7, F.18, E.10.D2, E.10/L-SURF. **Coordinates with:** A.6.5, A.6.6, A.6.7, E.19. |
| A.6.B | **Boundary Norm Square (Laws / Admissibility / Deontics / Work-Effects)** | Stable | *Keywords:* boundary norm square, atomic claims, L/A/D/E routing, laws vs gates, commitments, evidence carriers, no upward dependencies, claim IDs, triangle decomposition. *Queries:* "What is the Boundary Norm Square in FPF?", "How to decompose a mixed sentence into gate/duty/evidence claims?", "Where do RFC keywords belong in FPF patterns?" | **Builds on:** E.8, A.6.0, A.6.1, A.6.3, E.17.0, E.17, A.7, F.18, E.10.D2, E.10/L-SURF. **Used by:** A.6 (cluster overview). |
| A.6.C | **Contract Unpacking for Boundaries** | Stable | *Keywords:* contract bundle unpacking, SLA/guarantee routing, promise content (promise content) ≠ work, promise-act/utterance/commitment separation, Boundary Norm Square (L/A/D/E), MVPK faces “no new semantics”. *Queries:* "How to unpack contract language into promise content / utterance / commitment / work+evidence?", "How to prevent interface-as-agent / contract soup mistakes?", "How to stop MVPK faces becoming ‘second contracts’?", "When contract talk includes service-cluster tokens, what gets unpacked first?" | **Builds on:** A.6, A.6.B, A.6.8, A.7, A.2.3, A.2.8, A.2.9, E.10, E.17. **Coordinates with:** F.12, F.18.
| A.6.0| **U.Signature — Universal, law‑governed declaration** | Stable | *Keywords:* signature, vocabulary, laws, applicability, bounded context. *Queries:* "What is the universal signature block?", "Where do laws vs. implementations live?" | **Placement:** Kernel; **Coordinates:** A.6.1. |
| A.6.1 | **U.Mechanism - Law‑governed application to a SubjectKind over a BaseType** | Stable | Keywords: Mechanism, OperationAlgebra, LawSet, AdmissibilityConditions, Transport, Bridge‑only. Queries: "How to define a mechanism like USM/UNM?", "Where do operational guards live?", "How to handle cross‑context transport?" | **Builds on:** A.6.0, E.10.D1. **Instances:** USM (A.2.6), UNM (A.19). |
| A.6.2 | **U.EffectFreeEpistemicMorphing — Effect-Free Morphisms of Epistemes** | Stable | *Keywords:* episteme, effect-free, morphism, functoriality, describedEntity, lenses, reproducibility. *Queries:* "How to transform descriptions/specs without mechanisms?", "What are conservative episteme-to-episteme transforms in FPF?", "How do Describe_ID / Specify_DS fit into a general morphism class?" | **Builds on:** A.1 (Holon), A.7 (Strict Distinction, Object≠Description≠Carrier), A.6.0 (U.Signature), A.6.5 (U.RelationSlotDiscipline), E.10.D2 (I/D/S discipline), C.2.1 (U.EpistemeSlotGraph). **Used by:** A.6.3 (U.EpistemicViewing), A.6.4 (U.EpistemicRetargeting), E.17.0 (U.MultiViewDescribing), E.17 (MVPK), E.18 (E.TGA StructuralReinterpretation), KD-CAL mapping rules. |
| A.6.3 | **U.EpistemicViewing — describedEntity-Preserving Morphism** | Stable | *Keywords:* episteme, view, EpistemicViewing, describedEntity preservation, ClaimGraph, Viewpoint, RepresentationScheme, CorrespondenceModel, Direct vs Correspondence Viewing, optics, displayed fibration. *Queries:* "How to define a view of an artefact without adding new claims?", "What is an EpistemicViewing in FPF terms?", "How do ISO 42010 views and SysML v2 views-as-queries sit in FPF?" | **Builds on:** A.6.0 (U.Signature), A.6.2 (U.EffectFreeEpistemicMorphing), A.6.5 (U.RelationSlotDiscipline), A.7 (Strict Distinction; I/D/S vs Surface), E.10.D2 (I/D/S discipline), C.2.1 (U.EpistemeSlotGraph), C.2 (KD-CAL: describedEntity & ReferencePlane). **Used by:** E.17.0 (U.MultiViewDescribing), E.17 (MVPK), E.17.1/E.17.2 (ViewpointBundleLibrary & TEVB), E.18 (E.TGA viewpoint families), B.5.3 (Role-Projection Bridge), KD-CAL view operators. |
| A.6.4 | **U.EpistemicRetargeting — describedEntity-Retargeting Morphism** | Stable | *Keywords:* retargeting, subject retargeting, describedEntity shift, KindBridge, SquareLaw-retargeting, StructuralReinterpretation. *Queries:* "How to change the object-of-talk without losing truth?", "What is StructuralReinterpretation in FPF terms?", "When is a Fourier-like transform a retargeting rather than a new Γ-construction?" | **Builds on:** A.6.2 (effect-free episteme morphisms), A.1 (Holon: System/Episteme split), F.9 (Bridges & CL, including CL^plane and KindBridge), C.2.1 (U.EpistemeSlotGraph; DescribedEntity/GroundingHolon), C.2 (KD-CAL: ReferencePlane & CL propagation), E.18:5.9/E.18:5.12 (E.TGA crossings & StructuralReinterpretation rules). **Used by:** E.18 (StructuralReinterpretation node in E.TGA as species of U.EpistemicRetargeting), KD-CAL/LOG-CAL retargeting rules, Fourier-style transforms and data↔model re-targetings in discipline packs. |
| A.6.P | **U.RelationalPrecisionRestorationSuite — Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline** | Stable | *Keywords:* relation precision restoration, under‑specified relations, umbrella verbs, RelationKind, QualifiedRelationRecord, hidden arity, polarity, change‑class lexicon, lexical guardrails. *Queries:* "What is A.6.P in FPF?", "How do I rewrite under‑specified relational prose?", "How do the RPR specialisations (A.6.5/A.6.6/A.6.8/A.6.9/A.6.H) relate?" | **Builds on:** A.6, A.6.B, A.6.S, A.6.0, A.6.5, E.8, E.10, F.18. **Coordinates with:** A.2.6, A.10, C.3.3, E.17, F.9. **Specialised by:** A.6.5, A.6.6, A.6.8, A.6.9, A.6.H (and future A.6.x). |
| A.6.5 | **U.RelationSlotDiscipline - SlotKind / ValueKind / RefKind discipline for n‑ary relations (with slot‑operation lexicon)** | Stable | *Keywords:* slot, argument position, value, reference, signature, substitution, pass-by-value, pass-by-reference. *Queries:* “How do I declare positions and references in relations?”, “How do we stop mixing roles, values and ids in signatures?”, “How does SlotKind/ValueKind/RefKind interact with I/D/S and Epistemes?” | **Builds on:** A.6.0 (U.Signature), A.1 (Holon), A.7 (Strict Distinction), E.8 (pattern authoring discipline), E.10 (LEX-BUNDLE; Tech/Plain registers). **Used by:** C.2.1 (U.EpistemeSlotGraph), A.6.2–A.6.4 (episteme morphisms), B.5.* (RoleEnactment), C.3.* (Kinds & KindSignature), E.17.0 (U.MultiViewDescribing), discipline-packs for methods/services. |
| A.6.6 | **U.BaseDeclarationDiscipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)** | Stable | *Keywords:* base declaration, basedness, baseRelation, SWBD, witnesses, scope, Γ_time, anchoring, rebase, retime, rescope. *Queries:* "What is U.BaseDeclarationDiscipline?", "How to model base-dependence without anchoring?", "What is a ScopedWitnessedBaseDeclaration (SWBD)?" | **Builds on:** A.6.0, A.6.5, A.2.6, A.2.4, A.7, E.8, E.10. **Coordinates with:** A.10, A.14, C.2.1, A.6.3–A.6.4, C.3.3, E.18, F.9, F.15, F.18. **Used by:** base-relative admissibility/calibration/attribution patterns; anchor* rewrites into explicit `baseRelation(dependent, base)`. |
| A.6.7 | **`MechSuiteDescription` — Description of a set of distinct mechanisms** | Stable | *Keywords:* mechanism suite, distinct mechanisms, suite obligations, contract pins, CN-Spec, CG-Spec, P2W, planned baseline, crossing visibility. *Queries:* "What is a MechSuiteDescription?", "How to describe a bundle of distinct mechanisms without using MechFamilyDescription?", "How do suite obligations differ from gate decisions?" | **Builds on:** E.8, A.6.1, A.6.5, E.10, E.19. **Coordinates with:** E.18, A.21. **Used by:** Part G universalization; CHR mechanism stacks. |
| A.6.8 | **Service Polysemy Unpacking (RPR-SERV)** | Stable | *Keywords:* service polysemy, facet unpacking, serviceSituation QRR, promise content vs access point, provider principal, SLA/SLO, server/service provider rewrite. *Queries:* "How to unpack service talk in FPF?", "serviceSituation lens", "promise content vs service access point", "RPR-SERV rules". | **Builds on:** A.6.P, A.6.B, A.6.5, A.2.3, A.2.8, A.2.9, A.15, E.10, F.17, F.18. **Coordinates with:** A.6.C, A.7, F.8, E.15. |
| A.6.9 | **`U.CrossContextSamenessDisambiguation` — Repairing cross-context “same / equivalent / align” via explicit Bridges (RPR-XCTX)** | Stable | *Keywords:* cross-context sameness, bridge, alignment, mapping, direction, substitution licence, loss notes, CL, SenseCells, weakest-link. *Queries:* "How to disambiguate 'same' across contexts?", "How to avoid silent inversion in mappings?", "Naming-only vs substitution bridge". | **Builds on:** A.6.P, F.9, E.10.D1, A.7. **Coordinates with:** E.17, C.3.3, A.6.6, F.7/F.8. |
| A.6.S | **U.SignatureEngineeringPair — Constructive signature engineering (ConstructorSignature + TargetSignature)** | Stable | *Keywords:* signature engineering, TargetSignature, ConstructorSignature, two-signature arrangement, EFEM, editioning, retargeting, slot/base change lexicon, MVPK views (no new semantics), claim register, no epistemic agency. *Queries:* "What is U.SignatureEngineeringPair in FPF?", "How do I model TargetSignature vs ConstructorSignature (and keep Work out of edits)?", "How do slot/base change verbs compose into a reproducible signature evolution workflow?" | **Builds on:** A.6.0, A.6.2, A.6.3, A.6.4, A.6.5, A.6.6, A.6.B, A.3, A.7, A.12, C.2.1, E.17, E.10. **Coordinates with:** E.18, E.19. |
| A.6.H | **Wholeness Language Unpacking (RPR-WHOLE)** | Stable | *Keywords:* wholeness, integrity, part-of, boundary, environment, mereology, completeness, order/time, artefact–referent level, role–method–work. *Queries:* "How to unpack 'whole/part/integrity' in FPF?", "RPR-WHOLE trigger words", "ComponentOf vs ConstituentOf vs PortionOf vs MemberOf vs PhaseOf", "How to route order/time vs mereology?" | **Builds on:** A.6.P, A.6.5, A.7. **Coordinates with:** A.14, B.1.1, B.1.4, A.15. |
| ***Cluster A.V - Constitutional Principles of the Kernel*** | | | | |
| A.7 | **Strict Distinction (Clarity Lattice)** | Stable | *Keywords:* category error, Object ≠ Description, Role ≠ Work, ontology. *Queries:* "How to avoid common modeling mistakes?", "What are FPF's core distinctions?" | **Builds on:** A.1, A.2, A.3. **Constrains:** all patterns. |
| A.8 | **Universal Core (C-1)** | Stable | *Keywords:* universality, transdisciplinary, domain-agnostic, generalization. *Queries:* "How does FPF ensure its concepts are universal?" | **Builds on:** P-8. **Constrains:** Kernel-level `U.Type`s. |
| A.9 | **Cross-Scale Consistency (C-3)** | Stable | *Keywords:* composition, aggregation, holarchy, invariants, roll-up. *Queries:* "How do rules compose across different scales?", "How to aggregate metrics safely?" | **Builds on:** A.1, A.8. **Prerequisite for:** B.1. |
| A.10 | **Evidence Graph Referring (C-4)** | Stable | *Keywords:* evidence, traceability, audit, provenance, SCR/RSCR. *Queries:* "How are claims supported by evidence?", "How to ensure auditability?" | **Builds on:** A.1. **Prerequisite for:** B.3. |
| A.11 | **Ontological Parsimony (C-5)** | Stable | *Keywords:* minimalism, simplicity, Occam's razor, essential concepts. *Queries:* "How does FPF avoid becoming too complex?", "Rule for adding new concepts." | **Builds on:** P-1 Cognitive Elegance. **Constrains:** all new `U.Type` proposals. |
| A.12 | **External Transformer & Reflexive Split (C-2)** | Stable | *Keywords:* causality, agency, self-modification, external agent, control loop. *Queries:* "How to model a self-healing or self-calibrating system?", "What is the external transformer principle?" | **Builds on:** A.3. **Prerequisite for:** B.2.5. |
| A.13 | **The Agential Role & Agency Spectrum** | Stable | *Keywords:* agency, autonomy, AgentialRole, Agency-CHR, decision-making. *Queries:* "How is agency modeled in FPF?", "What is the agency spectrum?" | **Builds on:** A.2. **Refined by:** C.9 Agency-CHR. |
| A.14 | **Advanced Mereology: Components, Portions, Aspects & Phases**| Stable | *Keywords:* mereology, part-of, ComponentOf, PortionOf, PhaseOf, composition. *Queries:* "How to model different kinds of 'part-of' relationships?" | **Refines:** A.1. **Prerequisite for:** B.1.1. |
| A.15 | **Role–Method–Work Alignment (Contextual Enactment)** | Stable | *Keywords:* enactment, alignment, plan vs reality, design vs run, MIC, WorkPlan. *Queries:* "How do roles, methods, and work connect?", "How does an intention become an action in FPF?" | **Integrates:** A.2, A.3, A.4. **Prerequisite for:** all operational models. |
| A.15.1 | **`U.Work`: The Record of Occurrence** | Stable | *Keywords:* execution, event, run, actuals, log, occurrence. *Queries:* "What is a Work record?", "Where are actual resource costs stored?" | **Refines:** A.15. **Used by:** B.1.6, all Part D. |
| A.15.2 | **`U.WorkPlan`: The Schedule of Intent** | Stable | *Keywords:* plan, schedule, intent, forecast. *Queries:* "How to model a plan or schedule?", "Difference between a WorkPlan and a MethodDescription." | **Refines:** A.15. **Informs:** `U.Work`. |
| A.15.3 | **`SlotFillingsPlanItem` — Planned Slot-Fillings Baseline (WorkPlanning PlanItem)** | Stable | *Keywords:* planned baseline, slot owner, planned filler, edition pins, `Γ_time` selector, guard pins, WorkPlanning, P2W seam, variance trail. *Queries:* "What is SlotFillingsPlanItem in FPF?", "How to keep planned slot filling separate from FinalizeLaunchValues?", "How to pin editions and time in WorkPlanning baselines?" | **Builds on:** A.15.2, A.6.5, E.10.D1, E.17, E.18, E.19. **Used by:** A.6.7 (suite contract pins), Part G universalization, suite/kit specialised baselines. |
| A.16 | **Formality–Openness Ladder (FOL): Building Closed Worlds Inside an Open World** | Stub | *Keywords:* formality levels, rigor, proof, specification, sketch, F0-F9. *Queries:* "How to measure the formality of a document?", "What are the F0-F9 levels?" | **Builds on:** A.1. **Informs:** B.3. |
| A.17 | **A.CHR-NORM — Canonical “Characteristic” & rename (Dimension/Axis → Characteristic)** | Stable | *Keywords:* characteristic, measurement, property, attribute, dimension, axis. *Queries:* "What is the correct term for a measurable property?", "How to define a metric?" | **Prerequisite for:** A.18, A.19, C.16. |
| A.18 | **A.CSLC-KERNEL — Minimal CSLC in Kernel (Characteristic/Scale/Level/Coordinate)** | Stable | *Keywords:* CSLC, scale, level, coordinate, measurement Standard. *Queries:* "What is the CSLC Standard?", "How to ensure measurements are comparable?" | **Builds on:** A.17. **Prerequisite for:** all metric-based patterns. |
| A.19 | **A.CHR-SPACE — CharacteristicSpace & Dynamics hook** | Stable | *Keywords:* state space, CharacteristicSpace, dynamics, state model, RSG. *Queries:* "How to define a system's state space?", "How does FPF model change over time?" | **Builds on:** A.17, A.18, A.2.5. **Prerequisite for:** A.3.3. |
| A.19.CN| **CN-frame (comparability & normalization)** | Stable | *Keywords:* CN-frame, CN-Spec, chart, comparability modes, normalization refs, indicator policy refs, Γ-fold governance, registry, bridges, CL/loss notes, WLNK discipline, conformance checklist, SCR/RSCR harness, RSG admission hooks. *Queries:* "What is a CN-frame in FPF?", "How does CN-Spec govern comparability and normalization by reference?", "How do CN-frames use bridges and CL for cross-context reuse?", "What are the conformance and regression checks for CN-frames?" | **Builds on:** A.19. **Coordinates with:** A.6.1 (mechanism intension cards), C.16 (evidence/backing), F.9 (Bridges & CL), G.0 (CG-Spec legality gate). |
| A.19.CHR | **`CHRMechanismSuite` — CHR mechanism-suite anchor (suite obligations + P2W planned baseline)** | Stable | *Keywords:* CHR suite, characterization core, CN-Spec, CG-Spec, legality gate, suite obligations, set-return selection, tri-state guard decision, crossing visibility, Bridge-only transport, penalties→R_eff, planned baseline, `SlotFillingsPlanItem`, P2W seam, no hidden scalarization, no hidden thresholds. *Queries:* "What is CHRMechanismSuite in FPF?", "How do CHR mechanisms cite CN-Spec/CG-Spec?", "How to enforce planned slot filling in WorkPlanning only?", "How to keep UNM/UINDM/ULSAM explicit (no hidden tails)?" | **Builds on:** A.6.7, A.15.3, A.6.1, A.6.5, A.19, G.0, E.18, E.10, E.19. **Coordinates with:** A.21, G.5, G.10, C.23. **Used by:** Part G universalization; CHR mechanism stacks. |
| A.19.UNM | **Unified Normalization Mechanism (UNM)** | Stable | *Keywords:* normalization, `CV→NCV`, `≡_UNM`, `NormalizationMethodId`, `NormalizationMethodInstanceId`, `NormalizationInvariant[*]`, `NormalizationFixSpec`, validity window (no implicit “latest”), fail-closed tri-state guard (`pass|degrade|abstain`), `CN-Spec.normalization`, `CN-Spec.comparability.mode`, Bridge-only transport + ReferencePlane/CL pins, penalties→`R`/`R_eff` only. *Queries:* "What is UNM in FPF?", "How does FPF normalize coordinate values (CV→NCV)?", "What is ≡_UNM and why quotients/fix matter?", "How does CN-Spec.comparability.mode route normalization-based comparability?" | **Builds on:** A.19.CN, A.6.1, A.6.5, A.19.CHR, A.17–A.18, C.16, G.0, E.18, E.20, F.18. **Used by:** A.19.CHR, A.19.USCM, A.19.CPM, A.19.SelectorMechanism. **Coordinates with:** G.2, B.3. |
| A.19.UINDM | **Unified Indicatorization Mechanism (UINDM)** | Stable | *Keywords:* indicatorization, indicator set, `IndicatorChoicePolicy`, `CN-Spec.indicator_policy`, CHR suite stage `indicatorize`, tri-state admissibility (`pass|degrade|abstain`), evidence-gated indicator choice, Bridge+CL transport visibility, “no NCV⇒indicator”. *Queries:* "What is UINDM in FPF?", "How does FPF choose indicators?", "Difference between measurable characteristic and indicator", "How to make indicator choice auditable?" | **Builds on:** A.19.CN, A.6.1, A.6.5, A.19.CHR. **Used by:** A.19.CHR. **Coordinates with:** G.0, G.2, E.20, F.18. |
| A.19.USCM | **Unified Scoring Mechanism (USCM)** | Stable | *Keywords:* scoring, score profile, `ScoringMethodDescription`, ScaleComplianceProfile (SCP), CSLC-lawful transforms, `CG-Spec.MinimalEvidence`, tri-state admissibility (`pass|degrade|abstain`), “no implicit UNM”, vector scores by default, CHR suite stage `score`. *Queries:* "What is USCM in FPF?", "How does FPF do lawful scoring (SCP-first)?", "How are scoring methods pinned and audited in CHR?", "How does USCM handle unknowns and evidence?" | **Builds on:** A.19.CN, A.6.1, A.6.5, A.19.CHR, G.0, A.18, C.16. **Used by:** A.19.CHR. **Coordinates with:** UNM, ULSAM, CPM, SelectorMechanism, G.2, E.20, F.18. |
| A.19.ULSAM | **Unified Lawful Scale Aggregation Mechanism (ULSAM)** | Stable | *Keywords:* lawful aggregation, scale-lawful fold, `fold_Γ?`, `ΓFoldRef`, `CG-Spec.Γ_fold`, `CG-Spec.SCP`, `MinimalEvidence`, tri-state guard (`pass|degrade|abstain`), contributor set, no hidden aggregation, penalties→`R_eff` only. *Queries:* "What is ULSAM in FPF?", "How does FPF do lawful aggregation / Γ-fold?", "Why is fold_Γ a separate CHR stage?", "How to avoid ordinal averaging in FPF?" | **Builds on:** A.19.CN, G.0, A.18, A.6.1, A.6.5, A.19.CHR, B.3. **Used by:** A.19.CHR. **Coordinates with:** G.2, E.20, F.18. |
| A.19.CPM | **Unified Comparison Mechanism (CPM)** | Stable | *Keywords:* comparison, comparator, `ComparatorSpecRef`, `ComparatorSet`, set-valued comparison outcome, partial order, tri-state admissibility (`pass|degrade|abstain`), `MinimalEvidence`, “no hidden scalarization/totalization”, Bridge+CL transport, penalties→`R_eff` only. *Queries:* "What is CPM in FPF?", "How does FPF compare two profiles lawfully?", "Why comparison outputs are set-valued?", "How does CPM handle unknown evidence?" | **Builds on:** A.19.CN, A.6.1, A.6.5, A.19.CHR, G.0, A.18. **Used by:** A.19.CHR. **Coordinates with:** UNM, USCM, ULSAM, SelectorMechanism, G.2, G.5, G.9, E.20, F.18. |
| A.19.SelectorMechanism | **Unified Selection Kernel (SelectorMechanism)** | Stable | *Keywords:* selection kernel, set-returning selection, portfolio set, `SelectEligibility`, tri-state guard (`pass|degrade|abstain`), no hidden thresholds, no hidden scalarization, `CriteriaSlot`, `ComparisonResultSlot`, `TaskSignatureSlot`, evidence gating, `CG-Spec.MinimalEvidence`, CHR suite stage `select`, Bridge+CL/ReferencePlane transport, penalties→`R_eff` only. *Queries:* "What is SelectorMechanism in FPF?", "Why does selection return a portfolio set by default?", "How does SelectEligibility handle unknown or insufficient evidence?", "How does FPF prevent hidden thresholds and scalarization in selection?" | **Builds on:** A.6.1, A.6.5, A.19.CHR, A.19.CN, G.0, G.5, C.22. **Used by:** A.19.CHR, G.5, E.18 (E.TGA). **Coordinates with:** A.19.USCM, A.19.ULSAM, CPM (comparison stage). |
| A.20 | **U.Flow.ConstraintValidity — Eulerian** | Stable | *Keywords:* flow, ConstraintValidity, Eulerian, TransductionFlow, GateFit, MVPK, SquareLaw, Sentinel, PathSlice. *Queries:* "What is ConstraintValidity in FPF?", "What is the Eulerian stance in FPF flows?", "How does E.TGA relate to flows?" | **Builds on:** E.18 (E.TGA). **Coordinates with:** A.21, A.22, A.25, A.27, A.28, A.31, A.45. |
| A.21 | **GateProfilization: `OperationalGate(profile)` (GateFit core)** | Stable | *Keywords:* OperationalGate, GateFit, GateProfile, GateChecks, join-semilattice, `GateDecision`, `DecisionLog`, EquivalenceWitness, LaunchGate, CV⇒GF. *Queries:* "What is GateProfilization in FPF?", "How does OperationalGate aggregate GateChecks?", "What is the CV⇒GF activation predicate?" | **Builds on:** E.18 (E.TGA), E.17 (MVPK), A.7. **Coordinates with:** A.20, A.23, A.24, A.25, A.26, A.27, A.41. |

**Part B — Trans-disciplinary Reasoning Cluster**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| **B.1** | **Universal Algebra of Aggregation (Γ)** | Stable | *Keywords:* aggregation, composition, holon, invariants, IDEM, COMM, LOC, WLNK, MONO, gamma operator. *Queries:* "How does FPF combine parts into a whole?", "What are the rules for aggregation?", "What is the Gamma (Γ) operator?" | **Builds on:** A.1, A.9. **Prerequisite for:** All B.1.x, B.2. |
| B.1.1 | **Dependency Graph & Proofs** | Stable | *Keywords:* dependency graph, proofs, structural aggregators, sum, set, slice. *Queries:* "What is the input for the Gamma operator?", "How are aggregation invariants proven in FPF?" | **Builds on:** B.1. |
| B.1.2 | **System-specific Aggregation Γ_sys** | Stable | *Keywords:* system aggregation, physical systems, mass, energy, boundary rules, Sys-CAL. *Queries:* "How to aggregate physical systems?", "Conservation laws in FPF aggregation?" | **Builds on:** B.1, A.1, C.1. |
| B.1.3 | **Γ_epist — Knowledge-Specific Aggregation**| Stable | *Keywords:* knowledge aggregation, epistemic, provenance, trust, KD-CAL. *Queries:* "How to combine knowledge artifacts?", "How does trust propagate in FPF?" | **Builds on:** B.1, A.1, C.2. |
| B.1.4 | **Contextual & Temporal Aggregation (Γ_ctx & Γ_time)** | Stable | *Keywords:* temporal aggregation, time-series, order-sensitive, composition. *Queries:* "How does FPF handle time-series data?", "How to model processes where order matters?" | **Builds on:** B.1. |
| B.1.5 | **Γ_method — Order-Sensitive Method Composition & Instantiation**| Stable | *Keywords:* method composition, workflow, sequential, concurrent, plan vs run. *Queries:* "How to combine methods or workflows?", "How does FPF model complex procedures?" | **Builds on:** B.1, B.1.4, A.3.1. |
| B.1.6 | **Γ_work — Work as Spent Resource**| Stable | *Keywords:* work, resource aggregation, cost, energy consumption, Resrc-CAL. *Queries:* "How to calculate the total cost of a process?", "How are resources aggregated in FPF?" | **Builds on:** B.1, A.15.1, C.5. |
| **B.2** | **Meta-Holon Transition (MHT): Recognizing Emergence and Re-identifying Wholes**| Stable | *Keywords:* emergence, MHT, meta-system, new whole, synergy, system of systems. *Queries:* "How does FPF model emergence?", "What is a Meta-Holon Transition?", "When does a collection become more than the sum of its parts?" | **Builds on:** B.1, A.1. **Prerequisite for:** All B.2.x. |
| B.2.1 | **BOSC Triggers** | Draft | *Keywords:* BOSC, triggers for emergence, boundary, objective, supervisor, complexity. *Queries:* "What triggers an MHT?", "What are the BOSC criteria for emergence?" | **Builds on:** B.2. |
| B.2.2 | **MST (Sys) — Meta-System Transition** | Stable | *Keywords:* system emergence, super-system, physical emergence. *Queries:* "How do new systems emerge from parts?", "What is a Meta-System Transition?" | **Builds on:** B.2, B.2.1, A.1. |
| B.2.3 | **MET (KD) — Meta-Epistemic Transition**| Stable | *Keywords:* knowledge emergence, meta-theory, paradigm shift, scientific revolution. *Queries:* "How do new theories emerge?", "What is a Meta-Epistemic Transition?" | **Builds on:** B.2, B.2.1, A.1. |
| B.2.4 | **MFT (Meta-Functional Transition)**| Stable | *Keywords:* functional emergence, capability emergence, adaptive workflow, new process. *Queries:* "How do new capabilities or workflows emerge?", "What is a Meta-Functional Transition?" | **Builds on:** B.2, B.2.1, A.3.1. |
| B.2.5 | **Supervisor–Subholon Feedback Loop** | Stable | *Keywords:* control architecture, feedback loop, supervisor, stability, layered control. *Queries:* "How does FPF model control systems?", "What is the supervisor-subholon pattern?" | **Builds on:** B.2, A.1. |
| **B.3** | **Trust & Assurance Calculus (F–G–R with Congruence)**| Stable | *Keywords:* trust, assurance, reliability, F-G-R, formality, scope, congruence, evidence. *Queries:* "How is trust calculated in FPF?", "What is the F-G-R model?", "How does FPF handle evidence and confidence?" | **Builds on:** A.10. **Prerequisite for:** All B.3.x, D.4. |
| B.3.1 | **Components & Epistemic Spaces** | Draft | *Keywords:* F-G-R components, measurement templates, epistemic space. *Queries:* "How are F, G, and R measured?", "What are epistemic spaces?" | **Builds on:** B.3. |
| B.3.2 | **Evidence & Validation Logic (LOG-use)** | Draft | *Keywords:* verification, validation, confidence, logic, proof. *Queries:* "What is the logic for validating claims in FPF?", "Difference between verification and validation." | **Builds on:** B.3, C.6. |
| B.3.3 | **Assurance Subtypes & Levels** | Stable | *Keywords:* assurance levels, L0-L2, TA, VA, LA, typing, verification, validation. *Queries:* "What are the assurance levels in FPF?", "How does an artifact mature in FPF?" | **Builds on:** B.3. |
| B.3.4 | **Evidence Decay & Epistemic Debt** | Stable | *Keywords:* evidence aging, decay, freshness, epistemic debt, stale data. *Queries:* "How does FPF handle outdated evidence?", "What is epistemic debt?" | **Builds on:** B.3. |
| B.3.5 | **CT2R-LOG — Working-Model Relations & Grounding**| Stable | *Keywords:* grounding, constructive trace, working model, assurance layer, CT2R, Compose-CAL. *Queries:* "How are FPF models grounded in evidence?", "What is the CT2R-LOG?" | **Builds on:** B.3, E.14, C.13. |
| **B.4** | **Canonical Evolution Loop** | Stable | *Keywords:* continuous improvement, evolution, Run-Observe-Refine-Deploy, PDCA, OODA. *Queries:* "How do systems evolve in FPF?", "What is the canonical evolution loop?" | **Builds on:** A.4, A.12. **Prerequisite for:** All B.4.x. |
| B.4.1 | **System Instantiation** | Stable | *Keywords:* field upgrade, physical system evolution, deployment. *Queries:* "How are physical systems updated in FPF?" | **Builds on:** B.4, A.1. |
| B.4.2 | **Knowledge Instantiation** | Stable | *Keywords:* theory refinement, knowledge evolution, scientific method. *Queries:* "How are scientific theories refined in FPF?" | **Builds on:** B.4, A.1. |
| B.4.3 | **Method Instantiation** | Stable | *Keywords:* adaptive workflow, process improvement, operational evolution. *Queries:* "How do workflows or methods evolve in FPF?" | **Builds on:** B.4, A.3.1. |
| **B.5** | **Canonical Reasoning Cycle** | Stable | *Keywords:* reasoning, problem-solving, Abduction-Deduction-Induction, scientific method. *Queries:* "How does FPF model problem-solving?", "What is the canonical reasoning cycle?" | **Builds on:** A.10. **Prerequisite for:** All B.5.x. |
| B.5.1 | **Explore → Shape → Evidence → Operate** | Stable | *Keywords:* development cycle, lifecycle, state machine, Explore, Shape, Evidence, Operate. *Queries:* "What are the development stages of an artifact in FPF?" | **Builds on:** B.5. |
| B.5.2 | **Abductive Loop** | Stable | *Keywords:* abduction, hypothesis generation, creativity, innovation. *Queries:* "How does FPF model creative thinking?", "What is the abductive loop?" | **Builds on:** B.5. |
| B.5.2.1 | **Creative Abduction with NQD** | Stable | *Keywords:* NQD, novelty, quality, diversity, open-ended search, Pareto front, E/E-LOG. *Queries:* "How to systematically generate creative ideas?", "What is NQD in FPF?" | **Builds on:** B.5.2, C.17, C.18, C.19. |
| B.5.3 | **Role-Projection Bridge** | Stable | *Keywords:* domain-specific vocabulary, concept bridge, mapping, terminology. *Queries:* "How does FPF integrate domain-specific language?", "What is a Role-Projection Bridge?" | **Builds on:** A.2, C.3. |
| **B.6** | **Characterisation Families (CHR-use)** | Draft | *Keywords:* characterization, templates, CHR patterns, measurement. *Queries:* "How to use CHR patterns?" | **Builds on:** Part C (CHR). |
| **B.7** | **Common Logic Suite (LOG-use)** | Draft | *Keywords:* logic, inference, trust propagation, LOG-CAL. *Queries:* "How to apply formal logic in FPF?" | **Builds on:** Part C (LOG-CAL). |

**Part C — Kernel Extention Specifications**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| **Cluster C.I – Core CALs / LOGs / CHRs** | | | | |
| C.1 | **Sys‑CAL** | Draft | *Keywords:* physical system, composition, conservation laws, energy, mass, resources, U.System. *Queries:* "How to model physical systems in FPF?", "What are conservation laws in FPF?", "Modeling a pump or engine." | **Builds on:** A.1 Holonic Foundation, A.14. **Coordinates with:** Resrc-CAL. **Prerequisite for:** M-Sys-CAL. |
| C.2 | **KD‑CAL** | Stable | *Keywords:* knowledge, epistemic, evidence, trust, assurance, F-G-R, Formality, ClaimScope, Reliability, provenance. *Queries:* "What is F-G-R?", "How does FPF handle evidence and trust?", "How to model a scientific theory?". | **Builds on:** A.1, A.10, B.3. **Prerequisite for:** All patterns using F-G-R, M-KD-CAL. |
| C.2.1 | **U.Episteme — Epistemes and their slot graph** | Stable | *Keywords:* episteme, EpistemeSlotGraph, DescribedEntitySlot, GroundingHolonSlot, ClaimGraphSlot, ViewpointSlot, ReferenceScheme, RepresentationScheme, View/Viewpoint. *Queries:* "What is an episteme in FPF?", "How are DescribedEntity, ClaimGraph, GroundingHolon and Viewpoint organised as slots?", "How do KD-CAL epistemes connect to views/viewpoints and multi-view descriptions?" | **Builds on:** C.2 (KD-CAL), A.1 (Holonic Foundation), A.6.5 (U.RelationSlotDiscipline), E.10.D2 (I/D/S discipline). **Used by:** A.6.2–A.6.4 (U.EffectFreeEpistemicMorphing / U.EpistemicViewing / U.EpistemicRetargeting), E.17.0–E.17.2 (U.MultiViewDescribing, Viewpoint bundles, TEVB), E.17 (MVPK), B.1.3 (Γ_epist), discipline-packs that define or consume epistemes. |
| C.2.2 | **Reliability R in the F–G–R triad** | Stable | *Keywords:* Reliability (R), warrant, evidence-bound, F–G–R, ClaimScope (G), Bridge-only reuse, Congruence Level (CL / CL^k / CL^plane), weakest-link, pathwise justification (PathId), TA/VA/LA lanes, no implicit averaging. *Queries:* "What is R in F–G–R?", "How does FPF propagate reliability?", "How do CL penalties route under transport?", "Bridge-only reuse of claims in FPF". | **Builds on:** C.2, A.2.6, C.2.3, B.3, B.1.3, C.3, F.9. **Coordinates with:** G.6, G.7, E.14, E.18. **Constrains:** any cross-context claim reuse and any publication of `R_eff`. |
| C.2.3 | **Unified Formality Characteristic F** | Stable | *Keywords:* Formality, F-scale, F0-F9, rigor, proof, specification, formal methods. *Queries:* "What are the FPF formality levels?", "How to measure the rigor of a specification?". | **Builds on:** C.2. **Constrains:** All patterns referencing F-G-R. |
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
| C.11 | **Decsn‑CAL** | Draft | *Keywords:* decision, choice, preference, utility, options. *Queries:* "How does FPF model decision-making?", "How to represent preferences and utility?". | **Builds on:** A.13. |
| **Cluster C.III – Meta‑Infrastructure CALs** | | | | |
| C.12 | **ADR‑Kind-CAL** | Draft | *Keywords:* versioning, rationale, DRR, architecture decision record. *Queries:* "How are changes to kinds managed?". | **Builds on:** Kind-CAL, E.9. |
| C.13 | **Compose‑CAL — Constructional Mereology** | Stable | *Keywords:* mereology, part-whole, composition, sum, set, slice, extensional identity. *Queries:* "How does FPF formally construct parts and wholes?", "What is Compose-CAL?". | **Builds on:** A.14. **Is used by:** B.3.5 (CT2R-LOG). |
| **Cluster C.IV – Composite & Macro‑Scale** | | | | |
| C.14 | **M‑Sys‑CAL** | Draft | *Keywords:* system-of-systems, infrastructure, large-scale systems, orchestration. *Queries:* "How to model a complex infrastructure like a power grid?". | **Builds on:** Sys-CAL, B.2.2. |
| C.15 | **M‑KD‑CAL** | Draft | *Keywords:* paradigm, scientific discipline, meta-analysis, knowledge ecosystem. *Queries:* "How to model an entire field of science?". | **Builds on:** KD-CAL, B.2.3. |
| C.16 | **MM-CHR — Measurement & Metrics Characterization** | Stable | *Keywords:* measurement, measurement template, `U.DHCMethod(Ref)`, `U.Measure`, `U.Unit`, `U.EvidenceStub`, polarity, direct comparability (same-template), scoring method (𝒢) disclosure, CSLC. *Queries:* "How do I define a measurement template in FPF?", "What is direct comparability in MM-CHR?", "How do EvidenceStubs support measurement claims?" | **Builds on:** A.17, A.18. **Is a prerequisite for:** All CHR patterns (and any pattern that issues typed measures/scores). |
| C.17 | **Creativity‑CHR — Characterising Generative Novelty & Value** | Stable | *Keywords:* creativity, novelty, value, surprise, innovation, ideation. *Queries:* "How does FPF measure creativity?", "What defines a novel idea?". | **Builds on:** CHR-CAL, MM-CHR. **Coordinates with:** NQD-CAL, E/E-LOG. |
| C.18 | **NQD‑CAL — Open‑Ended Search Calculus** | Stable | *Keywords:* search, exploration, hypothesis generation, novelty, quality, diversity (NQD). *Queries:* "How does FPF support structured brainstorming?", "What is NQD search?". | **Builds on:** KD-CAL. **Coordinates with:** B.5.2.1, Creativity-CHR, E/E-LOG. |
| C.18.1 | **SLL — Scaling‑Law Lens (binding)** | Stable | *Keywords:* scaling law, scale variables (S), compute‑elasticity, data‑elasticity, resolution‑elasticity, exponent class, knee, diminishing returns. *Queries:* "How to make search scale‑savvy?", "Where to declare scale variables and expected elasticities?" | **Builds on:** C.16, C.17, C.18. **Coordinates with:** C.19, G.5, G.9, G.10. |
| C.19 | **E/E‑LOG — Explore–Exploit Governor** | Stable | *Keywords:* explore-exploit, policy, strategy, decision lens, portfolio management. *Queries:* "How to balance exploration and exploitation?", "What is an EmitterPolicy?". | **Builds on:** Decsn-CAL. **Coordinates with:** NQD-CAL. |
| C.19.1 | **BLP — Bitter‑Lesson Preference (policy)** | Stable | *Keywords:* general‑method preference, iso‑scale parity, scale‑probe, deontic override. *Queries:* "What is the default policy when a domain‑specific trick competes with a scalable general method?" | **Builds on:** C.19, C.24. **Coordinates with:** G.5, G.8, G.9, A.0. |
| C.20 | **Discipline‑CAL — Composition of `U.Discipline`** | Stable| *Keywords:* discipline, **U.AppliedDiscipline**, **U.Transdiscipline**, episteme corpus, standards, institutions, **Γ_disc**. *Queries:* "How to compose and assess a discipline in FPF?" | **Builds on:** C.2 KD‑CAL, G.0, Part F (Bridges/UTS). **Coordinates with:** C.21, C.23. |
| C.21 | **Discipline‑CHR - Field Health & Structure** | Stable | *Keywords:* discipline, field health, reproducibility, standardisation, alignment, disruption. *Queries:* "How to measure the health of a scientific field?", "What is reproducibility rate?". | **Builds on:** C.16, C.2, A.2.6, B.3. **Coordinates with:** C.20, G.2. |
| C.22 | **Problem‑CHR - Problem Typing & TaskSignature Binding** | Stable | Keywords: problem typing, TaskSignature, selector, eligibility, acceptance, CHR‑typed traits. Queries: "How does FPF type problems for selection?", "What is a TaskSignature?". | **Builds on:** C.16, G.5, G.0. **Coordinates with:** G.4, C.23. |
| C.23 | **Method‑SoS‑LOG — MethodFamily Evidence & Maturity** | Stable | *Keywords:* MethodFamily, evidence, maturity, SoS-LOG, admit, degrade, abstain, selector. *Queries:* "How is method family maturity assessed?", "What is the SoS-LOG for selection?". | **Builds on:** G.5, G.4, C.22, B.3. |
| C.24 | **C.Agent-Tools-CAL — Agentic Tool-Use & Call-Planning** | Stable | Keywords: agentic tools, call-planning, budget, BLP, SLL, policy-aware sequencing. Queries: "How to sequence tool calls?", "What is Agent-Tools-CAL?" | **Builds on:** C.5, C.18, C.19, B.3. **Coordinates with:** G.5, G.9. |
| C.25 | **Q-Bundle — Structured Treatment of “-ilities” (Quality Families)** | Stable | Clarifies how to model common “-ilities” (availability, reliability, etc.) either as single measurable Characteristics or as composite bundles combining Measures [CHR] + Scope [USM] + Mechanism/Status slots. | **Builds on:** A.2.6 (USM), A.6.1 (Mechanism), C.16 (MM-CHR) |

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
| E.3 | **Principle Taxonomy & Precedence Model** | Stable | *Keywords:* taxonomy, precedence, conflict resolution, hierarchy, principles, classification, Gov, Arch, Epist, Prag, Did. *Queries:* "How does FPF resolve conflicting principles?", "What is the hierarchy of FPF rules?". | **Builds on:** E.2. **Constrains:** All patterns and DRRs. |
| E.4 | **FPF Artefact Architecture** | Stable | *Keywords:* artifact, families, architecture, conceptual core, tooling, pedagogy, canon, tutorial, linter. *Queries:* "How are FPF documents structured?", "What is the difference between the core spec and tooling?". | **Builds on:** E.1. **Constrained by:** E.5.3. |
| E.5 | **Four Guard-Rails of FPF** | Stable | *Keywords:* guardrails, constraints, architecture, rules, safety, GR-1 to GR-4. *Queries:* "What are the main architectural constraints in FPF?". | **Builds on:** E.2, E.3. **Prerequisite for:** E.5.1, E.5.2, E.5.3, E.5.4. |
| E.5.1 | **DevOps Lexical Firewall** | Stable | *Keywords:* lexical firewall, jargon, tool-agnostic, conceptual purity, DevOps, CI/CD, yaml. *Queries:* "Can I use terms like 'CI/CD' in FPF core patterns?". | **Refines:** E.5. **Constrains:** All Core patterns. |
| E.5.2 | **Notational Independence** | Stable | *Keywords:* notation, syntax, semantics, tool-agnostic, diagram, UML, BPMN. *Queries:* "Does FPF require a specific diagram style?", "How is meaning defined in FPF?". | **Refines:** E.5. **Constrains:** All Core patterns. |
| E.5.3 | **Unidirectional Dependency** | Stable | *Keywords:* dependency, layers, architecture, modularity, acyclic, Core, Tooling, Pedagogy. *Queries:* "What are the dependency rules between FPF artifact families?". | **Refines:** E.5. **Constrains:** E.4. |
| E.5.4 | **Cross-Disciplinary Bias Audit** | Stable | *Keywords:* bias, audit, ethics, fairness, trans-disciplinary, neutrality, review. *Queries:* "How does FPF handle bias?", "Is there an ethics review process in FPF?". | **Refines:** E.5. **Constrains:** All Core patterns. **Links to:** Part D. |
| **Cluster E.II — The Author’s Handbook** | | | | |
| E.6 | **Didactic Architecture of the Spec** | Stable | *Keywords:* didactic, pedagogy, structure, narrative flow, on-ramp, learning. *Queries:* "How is the FPF specification structured for learning?", "What is the 'On-Ramp first' principle?". | **Builds on:** E.2 (P-2 Didactic Primacy). |
| E.7 | **Archetypal Grounding Principle** | Stable | *Keywords:* grounding, examples, archetypes, U.System, U.Episteme, Tell-Show-Show. *Queries:* "How are FPF patterns explained?", "What are the standard examples in FPF?". | **Builds on:** E.6. **Constrains:** All architectural patterns. |
| E.8 | **FPF Authoring Conventions & Style Guide** | Stable | *Keywords:* authoring, style guide, conventions, template, S-rules, narrative flow. *Queries:* "How to write a new FPF pattern?", "What is the FPF style guide?". | **Builds on:** E.6, E.7. **Constrains:** All new patterns. |
| E.9 | **Design-Rationale Record (DRR) Method** | Stable | *Keywords:* DRR, design rationale, change management, decision record, context, consequences. *Queries:* "How are changes to FPF managed?", "What is a DRR?". | **Builds on:** E.2 (P-10 Open-Ended Evolution). **Constrains:** All normative changes. |
| E.10 | **LEX-BUNDLE: Unified Lexical Rules for FPF** | Stable | *Keywords:* lexical rules, naming, registers, rewrite rules, process, function, service. *Queries:* "What is the complete set of FPF naming rules?". | **Builds on:** A.7, E.5, F.5. **Coordinates with:** A.2, A.10, A.15, B.1, B.3, Part F. |
| E.10.P | **Conceptual Prefixes (policy & registry)** | Stable | *Keywords:* prefixes, U., Γ_, ut:, tv:, namespace, registry. *Queries:* "What do the prefixes like 'U.' mean in FPF?". | **Depends on:** E.9. **Constrains:** E.5.1, E.5.2. |
| E.10.D1 | **Lexical Discipline for “Context” (D.CTX)** | Stable | *Keywords:* context, U.BoundedContext, anchor, domain, frame. *Queries:* "What is the formal meaning of 'Context' in FPF?". | **Builds on:** A.7, A.4. **Coordinates with:** F.1, F.2, F.3, F.7, F.9. |
| E.10.D2 | **Intension–Description–Specification Discipline (I/D/S)** | Stable | *Keywords:* intension, description, specification, I/D/S, testable, verifiable. *Queries:* "Difference between a description and a specification in FPF?". | **Builds on:** A.7, E.10.D1, C.2.1, C.2.3. **Constrains:** F.4, F.5, F.8, F.9, F.15. |
| E.12 | **Didactic Primacy & Cognitive Ergonomics** | Stable | *Keywords:* didactic, cognitive load, ergonomics, usability, Rationale Mandate, HF-Loop. *Queries:* "How does FPF ensure it's understandable?", "What is the 'So What?' test in FPF?". | **Builds on:** E.2 (P-2). **Complements:** E.13. |
| E.13 | **Pragmatic Utility & Value Alignment** | Stable | *Keywords:* pragmatic, utility, value, Goodhart's Law, Proxy-Audit Loop, MVE. *Queries:* "How does FPF ensure solutions are useful, not just correct?", "What is a Minimally Viable Example (MVE)?". | **Builds on:** E.2 (P-7). **Complements:** E.12. |
| E.14 | **Human-Centric Working-Model** | Stable | *Keywords:* working model, human-centric, publication surface, grounding, assurance layers. *Queries:* "What is the main interface for FPF users?", "How does FPF separate human-readable models from formal assurance?". | **Builds on:** E.7, E.8, C.2.3. **Coordinates with:** B.3.5, C.13, E.10. |
| E.15 | **Lexical Authoring & Evolution Protocol (LEX-AUTH)** | stable | *Keywords:* lexical authoring, evolution protocol, LAT, delta-classes. *Queries:* "How are FPF patterns authored and evolved?", "What is a Lexical Authoring Trace (LAT)?". | **Builds on:** E.9, E.10, B.4, C.18, C.19, A.10, B.3, F.15. |
| E.16 | **RoC-Autonomy: Budget & Enforcement** | Stable | *Keywords:* autonomy, budget, guarded enactment, ledger, SoD, override, UTS | *Queries:* "How is autonomy bounded and tested?", "How are overrides enforced under SoD?" | **Builds on:** E.8, E.10, **C.16 (MM‑CHR)**, **F.8 (Mint/Reuse)**, **E.18 (OperationalGate/GateCrossing)**, **A.21 (OperationalGate(profile); GateFit)**; ties F.4/F.6/F.15/F.17; G.4/G.5/G.9. |
| E.17.0 | **U.MultiViewDescribing — Viewpoints, Views & Correspondences** | New | Keywords: multi-view describing, viewpoint, view, entity-of-interest, description families, correspondence model, ISO 42010 alignment, view vs viewpoint, engineering vs publication viewpoints. Queries: “How to organise multiple descriptions of one object-of-talk?”, “How are viewpoints, views and correspondences structured in FPF?”, “How do viewpoint libraries generalise ISO 42010 for non-architectural descriptions?” | Builds on: C.2.1 (U.EpistemeSlotGraph; DescribedEntity/Viewpoint/View slots), A.6.2 (U.EffectFreeEpistemicMorphing), A.6.3 (U.EpistemicViewing), A.6.4 (U.EpistemicRetargeting), A.7 (Strict Distinction; I/D/S vs Surface), E.10.D1 (Context), E.10.D2 (I/D/S discipline). Used by: E.17 (MVPK — publication as a specialisation of multi-view describing for morphisms), E.17.1 (U.ViewpointBundleLibrary), E.17.2 (TEVB), E.18:5.12 (E.TGA engineering viewpoint families), domain-specific description schemes (architecture, safety cases, governance, research). |
| E.17.1 | **U.ViewpointBundleLibrary — Reusable Viewpoint Bundles** | Stable | Keywords: viewpoint family, viewpoint library, ViewFamilyId, reusable bundles, engineering/management/research packs, ISO 42010 viewpoint libraries. Queries: “How to define reusable viewpoint bundles in FPF?”, “What is a Viewpoint library?”, “How do we reuse the same viewpoint family across EoIClasses and contexts?” | Builds on: E.17.0 (U.MultiViewDescribing), C.2.1 (U.EpistemeSlotGraph; ViewpointSlot/ViewSlot), A.6.2–A.6.4 (episteme morphisms), A.7 (Strict Distinction; I/D/S vs Surface), E.7 (Archetypal Grounding), E.10/E.10.D1/D2 (LEX-BUNDLE & Context/I-D-S discipline). Used by: E.17.2 (TEVB — Typical Engineering Viewpoints Bundle), E.18:5.12 (E.TGA engineering viewpoint families), future domain-specific viewpoint packs (architecture, governance, safety, research). |
| E.17.2 | **TEVB — Typical Engineering Viewpoints Bundle** | Stable | Keywords: engineering viewpoints, holon, Functional/Procedural/Role-Enactor/Module-Interface views, EoIClass = U.Holon, ISO 42010 mapping, E.TGA bindings. Queries: “What are canonical engineering viewpoints over a holon?”, “How does TEVB relate to E.TGA and MVPK?”, “How do ISO 42010 architecture viewpoints map onto FPF engineering viewpoints?” | Builds on: E.17.0 (U.MultiViewDescribing), E.17.1 (U.ViewpointBundleLibrary), C.2.1 (U.EpistemeSlotGraph; DescribedEntity/Viewpoint/View slots), A.1 (Holon; U.System/U.Episteme as typical EoI), A.6.2–A.6.4 (episteme morphisms), A.7/E.10.D2 (Strict Distinction & I/D/S discipline). Used by: E.18:5.12 (E.TGA engineering viewpoint families), E.17 (MVPK — publication of engineering morphisms via EngineeringVPId/PublicationVPId correspondences), engineering description/spec patterns and future ISO-aligned architecture description species. |
| E.17 | **Multi‑View Publication Kit (for Morphisms)** | Stable | Keywords: publication, U.View/U.EpistemeView, multi-view, viewpoints, PublicationScope (USM), PlainView/TechCard/InteropCard/AssuranceLane, functorial views, reindexing (PromoteView[s→t]), Publication characteristics (PC.Number, PC.EvidenceBinding, PC.ComparatorSetRef, PC.CharacteristicSpaceRef), CHR/UNM/CG-Spec anchoring, UTS, pin discipline, D/S→Surface (no I→D/D→S). Queries: “How to publish any morphism across Plain/Tech/Interop/Assurance views without changing semantics?”, “How do MVPK faces relate to U.View/U.EpistemeView and U.Viewpoint/PublicationVPId?”, “How to pin numeric claims and evidence lanes on publication faces so they stay functorial and audit-ready?” | Builds on: A.7/E.10.D2 (Strict Distinction & I/D/S discipline; Surface orthogonality), A.6.2–A.6.3 (U.EffectFreeEpistemicMorphing, U.EpistemicViewing), C.2.1 (U.EpistemeSlotGraph; View/Viewpoint slots), E.17.0 (U.MultiViewDescribing), E.17.1 (U.ViewpointBundleLibrary), E.17.2 (TEVB), E.8 (Authoring conventions), E.10 (LEX-BUNDLE incl. L-SURF), Part F/G (UTS, CG-Spec, CHR pins, UNM). Used by / Coordinates with: E.18 (E.TGA — publication of morphisms via MVPK faces), Part G (SoTA pack shipping surfaces, EvidenceGraph views), tooling that emits human-readable cards/lanes over D/S-epistemes about morphisms. |
| E.18 | **Transduction Graph Architecture (E.TGA)** | Stable | *Keywords:* transduction graph, **nodes=morphisms**, **edge=U.Transfer** (single-edge kind), **OperationalGate(profile)**, **CV⇒GF** (ConstraintValidity → GateFit), **MVPK** faces, **SquareLaw**, **UNM single-writer**, **CSLC normalize-then-compare**, **Set-return selection**, **PathSlice/Sentinel refresh**, **DesignRunTag**. *Queries:* “What is E.TGA?”, “How do gates/bridges publish crossings?”, “How to model flows of morphisms?” | **Builds on:** E.17 (MVPK), E.8, E.10, A.7. **Coordinates with:** A.20–A.26 (Flow/GateProfilization/Profiles/Sentinels), F.9 (Bridges & CL), G.11 (Refresh). |
| E.19 | **Pattern Quality Gates: Review & Refresh Profiles** | Stable | *Keywords:* pattern review, quality gates, admission, refresh, staleness, profile-based checks, PQG, PCP, suite-level review (PCP‑SUITE), planned baseline & P2W seam (PCP‑P2W), `SlotFillingsPlanItem`, MVPK projections, guard vs gate separation. *Queries:* "How to review a new FPF pattern before admitting it?", "How to refresh stale patterns in FPF?", "What are PQG/PCP in FPF?", "How to review a MechSuiteDescription (suite obligations, contract pins, protocols)?", "How to review SlotFillingsPlanItem / planned slot filling and its MVPK projections?" | **Builds on:** E.8, E.10, E.9, E.15. **Coordinates with:** F.8 (Mint/Reuse), F.18 (Naming protocol), F.9 (Bridges & CL), F.15 (Harness), E.17 (MVPK), A.6.7 (MechSuiteDescription), A.15.3 (SlotFillingsPlanItem), G.11 (Refresh). **Constrains:** Admission/refresh decisions for patterns intended for the canonical corpus. |
| E.20 | **Mechanism Introduction Protocol (MIP)** | Draft | *Keywords:* mechanism introduction, authoring protocol, owner routing, MIP-run manifest, canonical card-first, no dangling `…IntensionRef`, suite boundary hygiene, P2W seam, SlotKind lexicon discipline, alias docking, typed RSCR triggers, regression envelope, PQG profiles. *Queries:* "How to introduce a new mechanism in FPF?", "How to avoid dangling IntensionRefs in suites?", "How to route mechanism changes by semantic owner?", "How to evolve mechanism suites without drift?" | **Builds on:** E.8, E.9, E.10, E.15, E.19. **Coordinates with:** A.6.1, A.6.7, A.15.3, F.18, E.18, G.Core, G.2, `G.x:Ext.*`. **Constrains:** Any change-set that introduces or revises mechanisms, suites, planned baselines, wiring modules, or citeable tokens. |

**Part F — The Unification Suite (U‑Suite): Concept‑Sets, SenseCells & Contextual Role Assignment**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| F.0.1 | **Contextual Lexicon Principles** | Stable | *Keywords:* local meaning, context, semantic boundary, bridge, congruence, lexicon, U.BoundedContext. *Queries:* "How does FPF handle ambiguity?", "What is the principle of local meaning?", "How do different contexts communicate?". | **Builds on:** A.1.1. **Prerequisite for:** All patterns in Part F. |
| **Cluster F.I — context of meaning & Raw Material** | | | | |
| F.1 | **Domain‑Family Landscape Survey** | Stable | Keywords: domain‑family survey, context map, canon, scope notes, versioning, authoritative source. | **Builds on:** E.10.D1, F.0.1, A.7. **Prerequisite for:** F.2, F.3, F.4, F.9. |
| F.2 | **Term Harvesting & Normalisation** | Stable | *Keywords:* term harvesting, lexical unit, normalization, provenance, surface terms. *Queries:* "How to extract terminology from a standard?", "What is a local lexical unit?", "How to handle synonyms within one domain?". | **Builds on:** F.1. **Prerequisite for:** F.3. |
| F.3 | **Intra‑Context Sense Clustering** | Stable | *Keywords:* sense clustering, disambiguation, Local-Sense, SenseCell, counter-examples. *Queries:* "How to group similar terms within a single domain?", "What is a SenseCell?", "How to handle words with multiple meanings in one context?". | **Builds on:** F.2. **Prerequisite for:** F.4, F.7, F.9. |
| **Cluster F.II — Concept-Sets & Role Assignment/Description (definition, naming, decision)** | | | | |
| F.4 | **Role Description (RCS + RoleStateGraph + Checklists)** | Stable | *Keywords:* role template, status template, invariants, RoleStateGraph (RSG), Role Characterisation Space (RCS). *Queries:* "How to define a role in FPF?", "What is a Role Description?", "How to specify the states of a role?". | **Builds on:** F.3, A.2.1. **Prerequisite for:** F.6, F.8. |
| F.5 | **Naming Discipline for U.Types & Roles** | Stable | *Keywords:* naming conventions, lexical rules, morphology, twin registers, U.Type naming. *Queries:* "What are the rules for naming roles in FPF?", "How to create clear and consistent names for concepts?". | **Builds on:** F.4, E.10. |
| F.6 | **Role Assignment & Enactment Cycle (Six-Step)** | Stable | *Keywords:* role assignment, enactment, conceptual moves, asserting status. *Queries:* "What is the process for assigning a role?", "How is a role enacted in FPF?", "What are the six steps of role assignment?". | **Builds on:** F.4, A.2.1, A.15. |
| F.7 | **Concept‑Set Table Construction** | Stable | *Keywords:* concept-set, table, row, columns, differences, comparisons. *Queries:* "How do I create a concept-set table?", "How do I compare concepts across contexts?". | **Builds on:** F.3, F.9. **Coordinates with:** A.6.9. **Prerequisite for:** F.8. |
| F.8 | **Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)** | Stable | *Keywords:* decision lattice, type explosion, reuse, minting new types, parsimony. *Queries:* "When should I create a new U.Type?", "How to avoid creating too many roles?", "Decision guide for new concepts.". | **Builds on:** F.4, F.7. |
| **Cluster F.III — Cross‑Context Alignment & Applied Bindings** | | | | |
| F.9 | **Alignment & Bridge across Contexts** | Stable | *Keywords:* bridge, alignment, mapping, cross-context, CL, loss notes, direction. *Queries:* "How do I bridge concepts across contexts?", "How do I express alignment safely?". | **Builds on:** F.3. **Coordinates with:** A.6.9. **Prerequisite for:** F.7, F.10. |
| F.10 | **Status Families Mapping (Evidence • Standard • Requirement)** | Stable | *Keywords:* status, evidence, standard, requirement, polarity, applicability windows. *Queries:* "How to map different types of status like 'evidence' and 'requirement'?", "How does FPF handle compliance?". | **Builds on:** F.9, B.3. |
| F.11 | **Method Quartet Harmonisation** | Stable | *Keywords:* Method, MethodDescription, Work, Actuation, Role–Method–Work alignment. *Queries:* "How to align the concepts of 'method' and 'work' across domains?", "What is the method quartet?". | **Builds on:** F.9, A.15. |
| F.12 | **Service Acceptance Binding** | Stable | *Keywords:* Service Level Objective (SLO), Service Level Agreement (SLA), acceptance criteria, binding, observation. *Queries:* "How to bind an SLO to actual work?", "How is service acceptance modeled in FPF?". | **Builds on:** F.9, A.2.3, KD-CAL. |
| **Cluster F.IV — Lexical Development Cycle, Growth Control, Tests & Examples** | | | | |
| F.13 | **Lexical Continuity & Deprecation** | Stable | *Keywords:* evolution, deprecation, renaming, splitting terms, merging terms. *Queries:* "How to manage changes to terminology over time?", "What is the process for renaming a concept?". | **Builds on:** F.5. |
| F.14 | **Anti‑Explosion Control (Roles & Statuses)** | Stable | *Keywords:* vocabulary growth, guard-rails, separation-of-duties, bundles, reuse. *Queries:* "How to prevent having too many roles and statuses?", "What are the strategies for controlling vocabulary size?". | **Builds on:** F.4, F.8. |
| F.15 | **SCR/RSCR Harness for Unification** | Stable | *Keywords:* static checks, regression tests, acceptance tests, validation, SenseCell testing. *Queries:* "How is the unification process validated?", "What are SCR/RSCR tests in FPF?". | **Builds on:** All of F.1-F.14. |
| F.16 | **Worked‑Example Template (Cross‑Domain)** | Stable | *Keywords:* didactic template, example, pedagogy, cross-domain illustration. *Queries:* "What is the standard format for a worked example in FPF?", "How to show a concept applied across different fields?". | **Builds on:** All of F.1-F.12. |
| F.17 | **Unified Term Sheet (UTS)** | Stable | *Keywords:* Unified Term Sheet, UTS, summary table, glossary, publication, human-readable output. *Queries:* "What is the final output of the FPF unification process?", "Where can I find a summary of all unified terms?". | **Builds on:** F.1-F.12. |
| F.18 | **Local-First Unification Naming Protocol** | Stable | *Keywords:* naming protocol, Name Card, local meaning, context-anchored naming. *Queries:* "What is the formal protocol for naming concepts?", "What is a Name Card in FPF?". | **Builds on:** F.1-F.5. | 

**Part G – Discipline SoTA Patterns Kit**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| G.Core | Part G Core Invariants | Draft | *Keywords:* Part‑G invariants, delegation-first core, RSCR trigger kinds, default ownership index, ID continuity, core linkage. *Queries:* "How to universalize Part G without drift?", "How to make RSCR triggers id-based?" | **Builds on:** E.8/E.10/E.19, A.6.7, A.15.3, A.19, G.0, A.19.CHR. Used by: all `G.0…G.13`. |
| G.0 | **CG-Spec — Frame Standard & Comparability Governance** | Stable | *Keywords:* CG-Spec, CG-Frame, legality gate, ComparatorSet, ScaleComplianceProfile (SCP), MinimalEvidence, Γ-fold, Φ(CL), Φ_plane, CL-routing, ReferencePlane, edition pins, RSCRTriggerKindId. *Queries:* "What is CG-Spec in FPF?", "How does CG-Spec constrain lawful comparison and aggregation?", "What must be pinned for CG-Spec reproducibility?" | **Builds on:** G.Core, A.19 (CN-Spec), A.10, A.17–A.19 / C.16 (MM-CHR legality), A.18 (CSLC), B.3, Part F (Bridges/UTS), E.10, E.5.2. **Prerequisite for:** G.1–G.6. |
| G.1 | **CG-Frame-Ready Generator**| Stable | *Keywords:* generator chassis, six-card kit (M1–M6), `CGKitId` manifest, `SoTA_SetId`, `VariantPoolId`, `ShortlistId`, `CGFrameLibraryId`, `RefreshReadinessCardId`, UTS/Name Cards, RSCR wiring (typed trigger ids), edition pins, set-return portfolios, shipping/refresh boundaries. *Queries:* "How to author a CG-Frame generator kit?", "What is the six-card chassis M1–M6 in Part G?", "How to wire harvesting (G.2), selection (G.5), and refresh (G.11) without shadow specs?" | **Builds on:** G.Core, E.8, E.10, E.19. **Uses:** A.10, A.15.3, A.19 (CN-Spec), G.0 (CG-Spec), G.2, G.3, G.4, G.5, G.10, G.11; (via Extensions) C.17 (Creativity-CHR), C.18 (NQD-CAL), C.19 (E/E-LOG). **Produces:** `CGKitId` + reusable CG-Frame kit surfaces and wiring stubs (UTS/RSCR-ready). |
| G.2 | **SoTA Harvester & Synthesis** | Stable | *Keywords:* SoTA harvest, synthesis, `SoTA Synthesis Pack@CG-Frame`, `SoTA_Set@CG-Frame`, `SoTAPaletteDescription`, `Tradition`, ClaimSheets, CorpusLedger, PRISMA Flow Record, BridgeMatrix, describedEntity, micro-examples, hand-off manifests, RSCRTriggerKindId. *Queries:* "How does FPF harvest and synthesize SoTA for a CG-Frame?", "What is a SoTA Synthesis Pack@CG-Frame?", "How to keep competing Traditions plural but comparable via bridges?", "How to make SoTA harvest refreshable with pinned editions and typed RSCR causes?" | **Builds on:** G.Core, E.8, E.10, E.19, A.10, B.3, F.9, F.17, G.0, G.6. **Used by:** G.1, G.3–G.5, G.10, G.11. **Relates to:** G.13. |
| G.3 | **CHR Authoring: Characteristics - Scales - Levels - Coordinates** | Stable | *Keywords:* CHR authoring, characteristics, scales, levels, coordinates, CSLC legality, typed measurement, CHR Pack@CG-Frame, ReferencePlane, Φ/CL policy pins, edition pins, RSCRTriggerKindId. *Queries:* "How do I author CHR packs (typed characteristics and scales) for a CG-Frame?", "How to keep measurement lawful (CSLC) and refreshable (RSCR)?" | **Builds on:** G.Core, G.2, G.0, A.17–A.19, A.18 (CSLC), C.16 (MM-CHR), A.19.CHR, A.15.3, G.6, F.17. **Prerequisite for:** G.4. **Used by:** G.4, G.5, G.10, G.11. |
| G.4 | **CAL Authoring: Calculi - Acceptance - Evidence** | Stable | *Keywords:* CAL authoring, operators, acceptance clauses, evidence profiles, tri-state admissibility, Γ-fold hooks, Φ/Ψ/Φ_plane policy pins, legality gates, edition pins, RSCRTriggerKindId. *Queries:* "How to author CAL operators and acceptance clauses for CG-Frames?", "How to keep acceptance/evidence wiring auditable and refreshable?" | **Builds on:** G.Core, G.3, G.0, B.3 (Trust), A.18 (CSLC), G.6. **Prerequisite for:** G.5. **Used by:** G.5, G.8–G.10, G.11. |
| G.5 | **Multi-Method Dispatcher & MethodFamily Registry** | Stable | *Keywords:* dispatcher, selector, MethodFamily registry, GeneratorFamily registry, TaskSignature, set-return selection, portfolio (`Archive`/`Pareto`), dominance regime, parity harness, UTS publication, evidence pins (PathId/PathSliceId), typed RSCRTriggerKindId. *Queries:* "How does FPF dispatch among competing MethodFamilies without scalarising?", "How are portfolios and parity runs made auditable and refreshable?" | **Builds on:** G.Core, G.0, A.19 (CN-Spec), G.2, G.3, G.4, G.6. **Coordinates with:** G.7–G.11, C.18 (NQD-CAL), C.19 (E/E-LOG), C.23 (Method-SoS-LOG), A.15.3. **Used by:** G.1, G.8–G.12, G.10, G.11. |
| G.6 | **Evidence Graph & Provenance Ledger** | Stable | *Keywords:* EvidenceGraph, provenance, PathId, PathSliceId, lane tags (TA/VA/LA), SCR/RSCR, GateCrossing, CrossingSurface, UTS PathCard, TriggerAliasMap, Γ-fold pinning. *Queries:* "How does FPF trace claims to evidence?", "What is an EvidenceGraph?", "How do PathId/PathSliceId support audit and refresh?" | **Builds on:** G.Core, A.10, B.3, G.4, F.9, F.15, F.17, E.18, A.21, E.10, E.5.2. **Used by:** G.5, G.8, G.9, G.10, G.11. |
| G.7 | **Cross-Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)** | Stable | *Keywords:* bridge calibration, BridgeCard, BridgeCalibrationTable (BCT), RegressionSet, SentinelSet, BridgeSentinel, Congruence Level (CL/CL^k/CL^plane), loss notes, waivers, ReferencePlane, Φ(CL)/Ψ(CL^k)/Φ_plane policy pins, PathSliceId, GateCrossing, UTS, RSCRTriggerKindId. *Queries:* "How to calibrate cross-Tradition bridges in Part G?", "What is BCT and how is it used?", "How do Bridge Sentinels trigger RSCR?" | **Builds on:** G.Core, G.2, F.9, F.3, F.7, B.3, G.6, E.18, A.21, E.10, C.21. **Prerequisite for:** G.5. **Used by:** G.9–G.11, G.10, G.12. |
| G.8 | **SoS-LOG Bundles & Maturity Ladders** | Stable | *Keywords:* SoS-LOG, rule ids, admissibility ledger, tri-state `{pass|degrade|abstain}`, maturity ladder (poset/ordinal), selector-facing bundle, evidence path pins (`PathId/PathSliceId`), Bridge/CL/Φ policy pins, portfolio/archive telemetry, RSCRTriggerKindId. *Queries:* "How to package SoS-LOG rules for the selector?", "How to publish a maturity ladder as a citable card?", "How to keep thresholds out of LOG and pin evidence paths?" | **Builds on:** G.Core, C.23, G.4, G.6, G.5, C.22. **Coordinates with:** G.7, G.10, G.11, F.8, F.9, E.18, E.10, E.5.2. |
| G.9 | **Parity / Benchmark Harness** | Stable | *Keywords:* parity, benchmark, harness, `ParityPlan@Context`, `ParityReport@Context`, pinned editions, freshness windows, `ComparatorSpecRef.edition`, baseline binding (`BaselineBindingRef`), EvidenceTrace (`EvidenceGraphId`, `PathId`, `PathSliceId`), GateCrossing visibility, set-return outcomes (portfolio/archive), RSCR parity tests, cross-tradition parity via Bridge/CL/Φ pins. *Queries:* "What is a parity run in FPF?", "How to run a reproducible parity benchmark (pins, windows, editions)?", "How to publish parity outcomes without hidden scalarisation?" | **Builds on:** G.Core, G.5, G.6, G.4, F.15, E.18, A.21, A.27, E.5.2, E.10. **Uses:** G.0, A.19, F.9. **Publishes to:** G.10, G.11. **Optional wiring:** G.7, C.18/C.19, C.23. |
| G.10 | **SoTA Pack Shipping (pack-boundary owner; `SoTA-Pack(Core)`)** | Stable | *Keywords:* shipping, SoTA-Pack(Core), pack boundary, publication surface, `AuditPins`, `MOOManifest`, `UTS` publication, `PathId`/`PathSliceId`, `CrossingSurface`, edition pins, telemetry pins, RSCR wiring, parity pins, notation-independent pack. *Queries:* "How does FPF ship a SoTA pack?", "What is SoTA-Pack(Core) in Part G?", "How do AuditPins and MOOManifest support replay and audit?", "How are crossing surfaces exposed during shipping?" | **Builds on:** G.Core, F.17–F.18, E.5.2, E.18, A.10, A.15.3. **Consumes/cites:** G.2–G.9, optional G.12–G.13. **Used by:** selector-facing consumers (via G.5), refresh orchestration (G.11). |
| G.11 | **Telemetry-Driven Refresh & Decay Orchestrator** | Stable | *Keywords:* telemetry, refresh, decay, RSCR, PathSlice, Bridge Sentinels, edition-aware, epistemic debt, deprecation, edition bumps, re-shipping. *Queries:* "How does FPF keep SoTA packs up-to-date?", "What triggers refresh / RSCR reruns?", "How are deprecations and edition bumps governed?". | **Builds on:** G.Core, G.6, G.7, G.5, G.8, G.9, G.10, B.3.4, E.18. **Coordinates with:** G.12, C.18/C.19, C.23, F.15. |
| G.12 | **DHC Dashboards — Discipline-Health Time-Series (lawful telemetry, generation-first)** | Stable | *Keywords:* dashboard, DHC, discipline health, time-series, lawful telemetry, view-only slices, PathId/PathSliceId, edition pins, UTS twins, RSCR/refresh wiring. *Queries:* "How to build DHC dashboards in FPF?", "How to publish lawful DHC time-series with evidence and edition pins?", "How to wire dashboard telemetry into RSCR refresh?" | **Builds on:** G.Core, C.21, G.6, G.11, A.19, G.0, F.17/F.18, E.5.2, E.10. **Coordinates with:** G.5 (portfolio/set outputs), G.7 (crossings/CL/Φ_plane pins), G.8 (maturity ladder panel), G.10 (shipping inclusion), C.18/C.19 (QD/OEE telemetry), G.2 (SoTA palette hooks). |
| G.13 | **External Interop Hooks for SoTA Discipline Packs (conceptual; normative when used)** | Draft | *Keywords:* interop, external index, claim mapper, mapping policy, plane map, embedding spec, `ExternalIndexCard@Context`, `ClaimMapperCard@Context`, `InteropSurface@Context`, CHR-typed SoS features, edition pins, UTS twins, RSCRTriggerKindId, telemetry pin. *Queries:* "How does FPF integrate external scholarly indexes into Part G?", "What is an ExternalIndexCard / ClaimMapperCard / InteropSurface in FPF?", "How to make interop refreshable with RSCR trigger kinds and edition pins?" | **Builds on:** G.Core, G.2–G.7, G.9–G.12, A.19, A.18, G.0, F.17, E.5.2, E.18. |

**Part H – Glossary & Definitional Pattern Index**

| § | ID & Title |  Status | Concise reminder |
| :--- | :--- | :--- | :--- |
| H.1 | **Alphabetic Glossary** | stub | Every `U.Type`, relation & operator with four‑register naming. |
| H.2 | **Definitional Pattern Catalogue** | stub | One‑page micro‑stubs of every definitional pattern for quick lookup. |
| H.3 | **Cross‑Reference Maps** | stub | Bidirectional links: Part A ↔ Part C ↔ Part B terms. |

**Part I – Annexes & Extended Tutorials**

| § | ID & Title | Status | Concise reminder |
| :--- | :--- | :--- | :--- |
| I.1 | **Deprecated Aliases** | stub | Legacy names kept for backward compatibility. |
| I.2 | **Detailed Walk‑throughs** | stub | Step‑by‑step modelling of a pump + proof + dev‑ops pipeline. |
| I.3 | **Change‑Log (auto‑generated)** | stub | Version history keyed to DRR ids. |
| I.4 | **External Standards Mappings** | stub | Trace tables to ISO 15926, BORO, CCO, Constructor‑Theory terms. |

**Part J – Indexes & Navigation Aids**

| § | ID & Title | Status | Concise reminder |
| :--- | :--- | :--- | :--- |
| J.1 | **Concept‑to‑Pattern Index** | stub | Quick jump from idea (“boundary”) to pattern (§, id). |
| J.2 | **Pattern‑to‑Example Index** | stub | Table listing every archetypal grounding vignette. |
| J.3 | **Principle‑Trace Index** | stub | Maps each Pillar / C‑rule / P‑rule to concrete clauses. |

**Part K - Lexical Debt**

| § | ID & Title | Status | Concise content reminder — “what belongs here” |
| :--- | :--- | :--- | :--- |
| K.1 | **Mandatory Replacement of Measurement Terms** | stub | Retires "axis/dimension" in favor of "Characteristic" and aligns other measurement terms. |
| K.2 | **Migration Debt from A.2.6 (USM)** | stub | Specifies the required edits across the FPF to align with the new Unified Scope Mechanism (USM). |

# **Preface** (non-normative)

## FPF is a first principle based architecture decisions for transdisciplinary SoTA methods of evolving holons: systems, epistemes, communities.

FPF is designed to serve three primary roles: the Engineer, who builds reliable systems; the Researcher, who searches for and grows trustworthy knowledge; the Manager, who organizes the collective thinking process of the Engineers and Researchers. Therefore FPF stands on a deliberately cross‑disciplinary scaffold. What follows traces the ideas that most visibly shaped its kernel, holonic constructive algebra, transdisciplinary thinking methods (described by patterns) with conceptual standards of publication/presentation results of this thinking.

Format of architecture decisions for transdisciplinary thinking architecture: similar to ADR (architecture decision records). **First Principles Framework (FPF)** proposes: a **pattern language** that is _generative_ rather than prescriptive—a toolkit for constructing thought. Each pattern follows the **Alexanderian quartet** (problem context - problem - solution - checklist - consequences - rationale, plus dependences); Patterns interlock to form an **operating system for thought** that is designed to **evolve** (Open‑Ended Evolution, **A.4**).

## Creativity in Open-Ended Evolution and Assurance*

Most engineering and management standards, methodologies and frameworks pick a side. They either optimise for **assurance** — audits, evidence, safety gates — or they celebrate open-ended evolution/agility based on **creativity** — ideas, leaps, pivots. **First Principles Framework (FPF)** is built to do both at once. It gives you a disciplined way to collectiverly generate and mature novel ideas with trust.

**On the imagination rail,** FPF is equally deliberate. It does not treat creativity as a black box or a personality trait. It provides a **named choreography for creative work**:

* **Abduct first.** Start with the *“what could be true?”* move—the **Abductive Loop**—to propose bold candidate explanations or designs before you overfit to today’s data. **Search widely, then focus.** Use an **open‑ended search** style to illuminate “adjacent possibles,” then apply an **explore–exploit governor** to decide when to roam for surprises and when to double‑down on promising directions. **Shape → Evidence → Operate.** Turn a promising sketch into a concrete shape, collect the right evidence to test it, and run it for real. Then loop.

FPF also **measures creative quality**. It distinguishes novelty for its own sake from *valuable* novelty. Work is scored along simple, universal characteristics—*Is it new?* *Is it useful?* *Does it fit the constraints?*—so that teams can compare options without collapsing into taste or hierarchy.

**On the assurance rail,** FPF makes trust a first‑class concern. Claims are anchored to evidence; formality can scale from plain checks to machine‑verified proofs; confidence is computed, not intuited. Meaning is kept local to an explicit frame of reference so “the same word” can’t quietly shift under your feet. The result is a reasoning trail that explains *why* a decision is justified—clear enough to audit, conservative enough for safety, and evolvable over time. One of important questions is *“What does ‘good’ look like?”* to pass/fail decision be against declared acceptance criteria. Created portfolio/collection of candidates scored **Novelty, Use‑Value, Surprise, Constraint‑Fit** on a Pareto fronties. And then we can evolve our holons-of-interest in small, auditable steps; record rationale for changes.  Run **open‑ended** searches early, then **govern** the switch from exploring to refining.   

*In a lab:* a puzzling anomaly isn’t “noise”; it is a **prompt**. You generate alternate explanations, explore them widely, then pick a direction with a clear **explore–exploit** rule. Each candidate must face a **fit‑for‑purpose** test; only those with evidence advance.
*In a product team:* concept sketches are not meetings in disguise; they are first‑class artifacts that move through **Explore → Shape → Evidence → Operate**. Creativity is expected; untested cleverness is not.
*In operations:* procedures are safe by design, yet the framework leaves Context for **abductive fixes** when reality throws a curve ball—*provided* they are later folded back into the evidence trail.

Assurance without imagination calcifies. Imagination without assurance drifts. FPF’s Standard is to **separate the moves cleanly**—so you can be genuinely inventive without losing your audit trail—and to **reconnect them on purpose**—so good ideas survive contact with the world. The framework’s creative patterns make *generation* systematic; its assurance patterns make *selection* and *adoption* reliable. That is how a team becomes both safe and original.

**Synthesis.** FPF treats creativity as a governed search and assurance as a repeatable reckoning. Together they form an **engine for changing collective's mind responsibly**—and then changing physical world.

FPF also adopts an explicit **Bitter‑Lesson Preference** and a **Scaling‑Law Lens** for all open‑ended search and portfolio‑selection work:
* **BLP default (policy).** When a domain‑specific heuristic competes with a **general, scale‑amenable** search/learning method, **prefer the general method** unless (i) a declared **deontic constraint** forbids it, or (ii) a **scale‑probe** (two or more points along declared Scale Variables) shows the heuristic **dominates in the relevant scale window** for this context.
* **Scale‑savvy exploration.** In open‑ended generation, **declare the Scale Variables (S)** that govern improvement (e.g., parameterisation breadth, data exposure, iteration budget, temporal/spatial resolution) and the expected **elasticities**; early exploration **samples along scale‑paths** to estimate diminishing‑returns regimes.
* **Strategy read‑out.** Portfolios and SoTA packs are **reported as sets** with **scale‑aware fronts** (utility × novelty × constraint‑fit × **scale‑elasticity** classes), not as single winners at frozen budgets; exploitation phases **inherit** the declared scale policy.  *(Formalisation: C.18.1 SLL; C.19.1 BLP.)*

## Navigating Uncertainty: Building Closed Worlds within an Open World *(non-normative)*

A fundamental challenge in any rigorous thinking is how to handle incomplete information. To build reliable systems and make trustworthy claims, we must make decisive judgments based on what we know, while remaining aware of the vast ocean of what we don't. This tension is formally captured by two opposing assumptions about the world: the Open-World Assumption and the Closed-World Assumption. FPF does not force a choice between them; instead, it provides a principled architecture for using both where they are most appropriate.

The distinction is best understood through a simple analogy:

*   **The Open-World Assumption (OWA): Absence of proof is not proof of absence.**
    If a name is not on a party guest list, we cannot conclude they are not coming. The list might simply be incomplete. This is the assumption of science, exploration, and the internet. It is a world of unbounded possibility, where new facts can always be discovered.

*   **The Closed-World Assumption (CWA): What is not known to be true is considered false.**
    If a name is not on a flight manifest, the airline and the security services will conclude they are not on the plane. For safety and operations, the list is assumed to be complete and authoritative. This is the assumption of databases, legal Standards, and safety-critical engineering. It is a world of bounded certainty, where we need to make reliable decisions based on a defined set of facts.

FPF is a hybrid system, architected to operate within the reality of an open world while enabling the construction of the reliable, locally-closed worlds necessary for engineering.

**How FPF Embraces the Open World?**
The framework is fundamentally designed to acknowledge that our knowledge is never complete. This OWA stance is embedded in its core principles:

*   **Open-Ended Evolution (P-10):** FPF is built on the premise that any holon—a system, a theory, a method—is perpetually incomplete and can be improved. New evidence can always emerge.
*   **Open-Ended Kernel (A.5):** The architecture of a minimal kernel of patterns in FPF alexandrian/architectural pattern language is an admission that the core cannot and should not attempt to describe everything. The world is too rich for any single, final ontology.
*   **The Abductive Loop (B.5.2):** The very first step of the reasoning cycle is to generate a new hypothesis. This act is a formal recognition that our current model is insufficient to explain an anomaly—a clear OWA posture.  It operationalised by **B.5.2.1** via **C.17–C.19**.

**How FPF Constructs and Manages Closed Worlds?**
While the universe is open, engineering requires us to build systems that are safe, predictable, and auditable. To do this, we must be able to draw a line and declare that, *for a specific purpose*, our knowledge *within that line* is complete. FPF provides the formal tools to build and govern these "islands of CWA":

*   **`U.BoundedContext` (A.1.1):** This is the primary mechanism for establishing a local CWA. Within a Bounded Context, a specific set of models, rules, and invariants is declared to be authoritative. Any statement that violates an invariant *within that context* is considered false.
*   **`U.Boundary` (A.1):** The boundary of a holon is the physical or conceptual wall of the CWA island. It makes the distinction between the managed "inside" and the unmanaged "outside" explicit, turning an abstract assumption into a concrete architectural feature.
*   **Conformance Checklists:** Each pattern's checklist acts as a set of CWA rules. A model that fails a check is not "of unknown status"; it is formally **non-conformant**.
*   **Assurance Levels (B.3.3):** The assurance calculus makes a decisive CWA judgment on trust. A claim without an explicit evidence anchor is not "of unknown reliability"; it is assigned **`AssuranceLevel: L0 (Unsubstantiated)`**. For the purpose of making decisions, it is not trusted.

In essence, FPF does not attempt the impossible task of transforming the open world into a closed one. It provides the architectural discipline to draw a firm line in the sand, make a reliable decision based on what's inside that line, and always remain aware of the open, unbounded world that lies beyond it.

## FPF as an Evolutionary Architecture for Thought

A method of thinking is itself a system. Like any system, it can be designed with ad-hoc, brittle connections that fail under pressure, or it can be architected for resilience, clarity, and growth. The First Principles Framework is not merely a collection of concepts or a static ontology; it is a formal **architecture for a method of trans-disciplinary thinking**. Its very structure—a collection of interconnected Architectural and Definitional Patterns presented as a series of an architecture/design records — is a deliberate choice that mirrors its function.

This concept is directly analogous to the modern practice of **Evolutionary Architecture** in software engineering. An evolutionary architecture is one designed to support incremental, guided change across multiple dimensions. It acknowledges that the systems we build are never "finished" and must be able to adapt to new requirements and a changing environment without catastrophic rewrites. The architecture itself provides the stable pathways and guiding principles—the "fitness functions"—that allow the system to evolve gracefully.

FPF applies this same architectural thinking to the dynamic of reasoning itself. It provides a set of load-bearing patterns and constitutional principles that act as the fitness functions for our thoughts. By building our reasoning within this architecture, we are not just seeking a correct answer in the moment; we seeking a collection/portfolio of answers at Pareto frontier in multi-criterial optimisation. This is SoTA answers that regularily need to re-check due to moving this Pareto frontier due to progress in science and engineering. Open-endedness and evolvability is The Rule.

The value of this architectural approach lies in its ability to explicitly protect and sustain the critical **characteristics of rigorous thought**, holding them from the natural degradation they suffer in complex, long-running projects. Where traditional critical thinking identifies failures in these characteristics, FPF provides the mechanisms to build them in by design. Open-ended creative generativity is explicitly instrumented.

Part of FPF architecture for open-ended evolution is counterintuitive. E.g., to determine SoTA systems, knowledge, communities, methods, disciplines and other entities, you need to compare them. Therefore FPF has measurement and comparability theory that starts all thinking with designing of a Comparability Governance frame (CG-frame). To discuss dynamics of holon change, FPF talks about holon's characteristics that are measurable within CG-frames and trajectories in characteristic spaces. 

## Architectural Characteristic of Thought

| Architectural Characteristic of Thought | What it protects / why it matters | The FPF Mechanisms that Preserve It |
| :--- | :--- | :--- |
| **Auditability & Traceability** | The unbreakable chain from a claim back to its evidence. This is the quality of being able to answer "Why is this true?" at any point. | **`Evidence Graph Referring (A.10)`**, the **`Design-Rationale Record (DRR) Method (E.9)`**, and the entire **`Trust & Assurance Calculus (B.3)`**. The architecture makes untraceable claims a modeling violation. |
| **Evolvability** | The capacity of a model or system to adapt to new information or requirements without losing its conceptual integrity. | The **`Open-Ended Evolution Principle (P-10)`**, the **`Canonical Evolution Loop (B.4)`**, and the **`DRR Process (E.9)`**. Change is not a bug; it is a formally managed, first-class feature of the architecture. |
| **Creativity (Generative Novelty & Value)** | The ability to reliably generate, select, and mature novel hypotheses/designs that are both *new* and *fit to purpose*—exploration without losing auditability or safety. | **`Creativity‑CHR (C.17)`** for measurable **Novelty / Use‑Value / Surprise / Constraint‑Fit**; **`NQD‑CAL (C.18)`** for open‑ended, illumination‑style search; **`E/E‑LOG (C.19)`** to govern explore↔exploit policies; **`Creative Abduction with NQD (B.5.2.1)`** / **`Abductive Loop (B.5.2)`** to structure hypothesis generation; **`Design‑Rationale Record (E.9)`** to capture decisions so creativity stays auditable. |
| **Composability & Modularity** | The ability to construct complex, reliable ideas from simpler, independently verifiable components. | The **`Open-Ended Kernel (A.5)`**, **`Universal Γ (B.1)`**, plus **Boundary‑Inheritance Standard (BIC)** and the **Cut‑Stable Boundary Axiom** for safe structural cuts, and the **Method Interface Standard (MIC)** for typed method I/O and conservation constraints. Together they make composition predictable and auditable.  |
| **Falsifiability** | The quality that every claim is structured so it can be rigorously tested and potentially proven false. | **`Conformance Checklists`** embedded in every pattern and the **`Trust & Assurance Calculus (B.3)`**. Every normative artifact must declare success/failure criteria and null tests. |
| **Cross-Scale Coherence** | The guarantee that the same fundamental logic applies to a single component, an integrated system, and a system‑of‑systems. | **`Cross-Scale Consistency (A.9)`**, **Universal Γ (B.1)** with proof obligations for context/time reasoning (Proof Kit), and declared Γ‑fold policies over WLNK/COMM/LOC/MONO + time policy (no free‑hand averages). These preserve invariants across zoom levels and eras.  |
| **Design–Run Separation (Temporal Integrity)** | Prevents “design/run chimeras”, keeps assumptions/versioned specs separate from runtime evidence; enables reproducible state over time. | **A.4 design–run split** (used across CHR/creativity), **KD‑CAL CC‑KD‑08** (no episteme mutation in Work), **Γ_time** rules (T‑1..T‑3), **DRR (E.9)** for rationale/versioning, **Canonical Evolution Loop (B.4)** for orderly change.  |
| **Lexical & Representation Discipline** | Guards against category errors and notation lock‑in; keeps language unambiguous and tool‑neutral across contexts. | **Strict Distinction** (didactic distillation of SD), **LEX‑BUNDLE (E.10)**, and **Guard‑Rails E.5.\*** (DevOps Lexical Firewall, Notational Independence, Unidirectional Dependency, Bias‑Audit). All meanings live in a **`U.BoundedContext`** and cross only via Bridges. |
| **Measurement Typing & Units** | Ensures metrics are correctly typed (ordinal/interval/ratio), unitful, and safe to operate on; forbids “ordinal averages”. | **A.17/A.18** measurement discipline + **MM‑CHR (C.16)** templates; **KD‑CAL CC‑KD‑12** (units/envelopes/windows). |
| **Order/Time‑Safe Orchestration** | Separates structure from control‑flow and time; prevents hidden order/time bugs in authored models. | **Γ_ctx** (NC‑1..3) and **Γ_time** (T‑1..T‑3) laws; **CT2R‑LOG** “no order/time in parts”; **E.14** “no order/time in structure” for authoring conformance. |
| **Trust Calibration & Cross‑Context Integrity** | Keeps claims honest when moved across Contexts; reduces over‑optimism via weakest‑link and CL penalties. | **Trust & Assurance Calculus (B.3)** (F‑G‑R characteristics), **Bridges with CL** (KD‑CAL **CC‑KD‑07**), and creativity rules that lower **R** (not scale) when crossing contexts.  |
| **Agency & Accountability (SoD)** | Makes “who acts” explicit; enforces Separation‑of‑Duties so evidence isn’t self‑authored. | **A.2 Role suite** & **A.15 run‑alignment** (roles vs evidence/work), SoD gates in creativity flows (“fails SoD — same author as reviewer”). |
| **Scope Safety & Encapsulation** | Prevents scope‑creep and category bleed; each claim applies only within its declared Context/context and exits only via governed bridges. | **Γ_ctx (NC‑1..3)** and **`U.BoundedContext`** for hard context walls; **Bridges with CL** (KD‑CAL **CC‑KD‑07**) for governed crossings; **CG‑frame (A.19)** to declare scope of comparability. |
| **Reproducibility & Deterministic Replay** | Ability to re‑obtain the same result given the same inputs, model version, and time policy; enables trustworthy debugging and audit. | **A.4 Design–Run split**, **Γ_time (T‑1..T‑3)**, **CT2R‑LOG** (“no order/time in parts”), **E.14** (“no order/time in structure”), **DRR (E.9)** for versioned rationale, **Evidence Graph Referring (A.10)**. |
| **Change‑Impact Predictability (Blast‑Radius Control)** | Changes have bounded, knowable effects; reviewers can see which CG‑frames, bridges, and claims are touched. | **Canonical Evolution Loop (B.4)** with explicit deltas, **DRR (E.9)** change graph and decision record, **Evidence Graph Referring (A.10)** for provenance links, **Trust & Assurance Calculus (B.3)** to update risk post‑change, **CG‑frame (A.19)** to localize roll‑ups. |
| **Exploration Health (Portfolio Coverage)** | Avoids local maxima and groupthink; measures how widely we explore. | **Creativity‑CHR (C.17)** **`Diversity_P`** + coverage maps (illumination), **NQD‑CAL (C.18)** **`IlluminationSummary`**, **E/E‑LOG (C.19)** **`explore_share`/policy. |
| **Constraint Safety & Ethical Assurance** | Ensures non‑negotiable constraints (safety/ethics/standards) gate enactment; prevents “novelty theft”. | **`ConstraintFit` (C.17 §5.4)** as eligibility, **D‑cluster Bias‑Audit & Ethical Assurance (D.5)**; attribution tracked via **`AttributionIntegrity`**. |
| **Didactic Clarity & Working‑Model Primacy** | Keeps the human‑readable canon primary; assurance flows downward; readers can reason without tool lock‑in. | **E.12 Didactic Primacy & Cognitive Ergonomics**, **E.14 Human‑Centric Working‑Model** (conformance checklist), **E.7** Tell‑Show‑Show.  |
| **Typed Reasoning (Kinds & Intent/Extent)** | Prevents category confusions; enables typed, context‑local reasoning and safe Cross‑context mappings. | **Kind‑CAL (C.3)** — `U.Kind` & `SubkindOf`, **KindSignature & Extension**, **KindBridge & CL^k** for Cross‑context mapping.  |
| **Comparability & Roll‑up Integrity (CG‑frames)** | Makes “same number” meaningful across teams; preserves invariants in aggregation. | **CG‑frame (A.19)** comparability modes and explicit Γ‑fold declarations (WLNK/COMM/LOC/MONO + time policy); integrates with **Bridges with CL** for Cross‑context moves; benefits include safe roll‑ups and RSG‑ready gates. |

Therefore, FPF should be understood not as a passive library of terms, but as an **engineered method for thinking**. Its patterns are the architectural decisions that shape this method. Its ultimate value is not in any single model it can produce, but in the enduring quality of the reasoning process it sustains—a discipline that is auditable, evolvable, and coherent by design.

## Beyond Cognitive Biases: FPF as a Generative Architecture for Thought

The modern discipline of critical thinking has rightly focused on identifying and mitigating a long list of cognitive biases—the predictable glitches in our intuitive reasoning, from confirmation bias to the availability heuristic. The practice of "bias hunting" is a valuable diagnostic tool for improving our intellectual hygiene. However, it suffers from a fundamental limitation: it is primarily **corrective, not constructive**. It teaches us how to find flaws in existing arguments but offers little guidance on how to build a robust, complex argument from first principles.

This reactive approach is like trying to improve road safety by handing drivers a list of 50 common mistakes. While helpful, it is an incomplete solution. It relies on the driver's constant vigilance to avoid an ever-growing catalog of potential errors—a cognitive "whack-a-mole" that is both exhausting and ultimately fallible.

The First Principles Framework (FPF) proposes a different, complementary approach. It is not concerned with correcting the driver's psychology, but with **designing a safer car and establishing the rules of the road**. FPF is a **generative architecture for thought**. Its primary purpose is not to diagnose errors, but to provide a structural scaffold that makes entire classes of errors difficult or impossible to commit in the first place.

This architectural approach shifts the focus from the internal, fallible state of the thinker to the external, verifiable structure of their thoughts. Where the study of cognitive biases offers a map of mental pitfalls, FPF provides the engineering blueprints for building a bridge over them. The following table illustrates how FPF's architectural solutions provide structural protection against common cognitive failure modes—many of which are deeper and more systemic than those on the classic lists of biases.

| Cognitive Failure Mode | The Conventional Approach (Diagnostic) | The FPF Solution (Architectural & Generative) |
| :--- | :--- | :--- |
| **Conflation of Plan and Reality** | Reminds us to be aware of the **Planning Fallacy** or **Confirmation Bias**, where we seek evidence that our plan is working and ignore contradictory data. | **`Temporal Duality (A.4)`** and the strict distinction between `design-time` artifacts (`MethodDescription`, `WorkPlan`) and `run-time` artifacts (`Work`). This is not a psychological reminder; it is a **category error** to mix them. The architecture enforces the separation. |
| **Ambiguity and Equivocation** | Warns against using vague terms or shifting the meaning of a word mid-argument. | **`Lexical Discipline (E.10)`** and **`U.BoundedContext (A.1.1)`**. FPF bans overloaded terms like "process" from its core and requires that all domain terms be explicitly projected onto precise FPF concepts within a bounded context. Ambiguity is architecturally constrained, not just advised against. |
| **Causality Collapse & Lack of Accountability** | Points out the **Fundamental Attribution Error** or describes situations where causes are poorly understood. | **`External Transformer Principle (A.12)`**. FPF makes it an architectural invariant that every change **must** be attributed to an external agent (`System` in a `U.RoleAssignment`). "It configured itself" is not a cognitive bias; it is a **modeling violation**. Causality is non-negotiable. |
| **Inconsistent Aggregation & Scope Neglect** | Highlights biases where we incorrectly generalize from parts to a whole or ignore the scale of a problem. | **`Cross-Scale Consistency (A.9)`** and the **`Universal Algebra of Aggregation (Γ)`** with its **Invariant Quintet (B.1)**. FPF provides a formal, conservative algebra (e.g., the Weakest-Link bound) for aggregation, making naive or optimistic roll-ups a **provable error** in the model. |
| **Creative Mode Collapse (Premature Convergence)** | Advises teams to “brainstorm more,” add ideation checklists, or warn against fixation—creativity is audited post‑hoc. | **`Creative Abduction (B.5.2)`** bound to **`NQD‑CAL (C.18)`** and governed by **`E/E‑LOG (C.19)`** keeps hypothesis generation formally open (illumination‑style emitters, exploration quotas, selection lenses), while **`Creativity‑CHR (C.17)`** scores outputs on `Novelty`, `Use‑Value`, `Surprise`, and `ConstraintFit` inside a `U.BoundedContext`. Premature convergence becomes a **policy/modeling violation** (insufficient exploration or missing lenses), not a soft reminder.  |

FPF does not make a thinker immune to cognitive biases. Rather, it provides a disciplined, external environment for reasoning that channels cognitive effort productively. It provides the **`Canonical Reasoning Cycle (B.5)`**—a constructive path from a novel idea (Abduction) to a validated conclusion (Induction)—rather than just a set of warnings about wrong turns. **Creative ideation** is first‑class: **B.5.2.1** together with **C.17–C.19** replaces ad‑hoc brainstorming with measurable **Novelty–Quality–Diversity** search, complementing the assurance calculus.

In this way, FPF is not a replacement for critical thinking and creative thinking but its **engineering reinforcement**. It provides the architectural integrity, shared vocabulary, and formal discipline necessary to move from merely avoiding mistakes and generate ad hoc ideas to reliably generating trustworthy and auditable insights.

## Thinking Through Writing: The FPF Discipline of Conceptual Work

A core challenge of any rigorous intellectual effort is that thought itself is intangible. While many frameworks focus on managing data, process, or team activities, FPF uniquely focuses on architecting the *act of reasoning itself*. It achieves this by providing a discipline of "thinking through writing"—a method for giving thought a concrete, shareable, and auditable form. The diverse formats found within the framework—the Cards, Tables, Records, and Specifications—are the instruments for this discipline.

At its heart, FPF requires what might be metaphorically called "pencil and paper." To engage with the framework is to externalize one's reasoning, moving it from the fleeting space of internal cognition to a persistent medium where it can be inspected, challenged, and refined. This "writing" is not a by-product of thinking; it *is* the thinking. The act of filling out a **Role Description Card** or constructing a **Concept-Set Table** is not mere documentation; it is the cognitive work of making distinctions, declaring invariants, and justifying relationships. These forms give shape and persistence to thought.

This discipline is operationalized through a rich vocabulary of conceptual forms, each tailored for a specific cognitive task. *Cards* serve to define and scope individual concepts: a `Context Card` (F.1) fixes the semantic boundaries of a domain, while a `Role Description Card` (F.4) specifies the invariants of a particular behavioral role or status. *Tables* are used to compare and synthesize knowledge across these boundaries, with the `Unified Term Sheet (UTS)` (F.17) providing the canonical, human-readable summary of how concepts align. *Records*, such as the `Design-Rationale Record (DRR)` (E.9), create a durable, auditable history of *why* a decision was made, capturing the context and trade-offs. Finally, *Standards* and *Specifications* make rules explicit, from the high-level principles to the detailed `Conformance Checklists` that conclude every pattern. Each form is a distinct instrument in the FPF toolkit, designed to isolate and clarify a specific aspect of a complex problem.

It is critical, however, to understand the precise nature of this "writing." The FPF constitution is built on a deliberate separation of concerns that grants teams maximum freedom in their operational practices.

*   **FPF is Not a Tooling or Notation Mandate.** The "pencil and paper" are a metaphor. FPF is fundamentally agnostic to the medium. Whether a team uses a physical whiteboard, a shared text document, a wiki, a version-controlled set of Markdown files, or a sophisticated modeling tool is an implementation detail that lies outside the conceptual core. The framework's value resides in the *structure of the thought* that these forms demand, not in any specific rendering. This is the essence of the **Notational Independence** guard-rail (E.5.2).

*   **FPF is Not a Team Workflow or an organisational process policy.** The framework does not prescribe how a team should run its meetings, manage its repositories, or version its files. It is not a substitute for methodologies like Agile or for organisational information policies. Rather, FPF provides the **conceptual content** that these processes act upon. A team can use its existing Agile workflow to manage the creation of a **Design-Rationale Record (DRR)**, and its existing artefact-management conventions to manage the storage of an **Unified Term Sheet (UTS)**. FPF provides the *what*—the structure of a sound argument—not the *how* of team logistics.

The purpose of this discipline is to augment both individual and collective cognition. For the individual, the written artifact acts as an extension of working memory, making it possible to hold and manipulate far more complex models than one could in their head alone. For the team, these shared, tangible artifacts create a common conceptual space. They become the stable ground upon which collective reasoning can occur—a shared object that can be debated, annotated, and iteratively improved.

This flexibility is by design. The conceptual Standard of a **Role Description Card** is fixed by FPF, but its physical implementation is a project-level decision. One team might manage their cards in a simple spreadsheet, another in a relational database, and a third in a formal ontology. All can be fully FPF-conformant because they honor the conceptual structure, regardless of the underlying data-handling choices.

Ultimately, the diverse forms within FPF are not bureaucratic artifacts to be produced; they are conceptual instruments to be used. They provide the minimal necessary structure to turn fleeting insights into durable, shareable, and contestable knowledge. They are the grammar that allows a team to write its thoughts, and then, together, to edit them towards truth.

## Descriptive Ontologies vs. A Thinking-Oriented Architecture

The First Principles Framework (FPF) shares a goal with classical upper ontologies (e.g., **Basic Formal Ontology (BFO)**, **DOLCE**): to provide a universal, unified language that cuts across disciplinary silos. Yet they pursue this from fundamentally different starting points. Understanding this distinction is key to grasping FPF’s unique purpose.

A classical upper ontology aims to create a logically consistent **inventory of what exists**. Its primary task is descriptive metaphysics: partitioning reality into fundamental categories (like *continuants* vs. *occurrents*, *objects* vs. *processes*) and defining their relations. The result is a rigorous, hierarchical map optimized for data integration and preventing category errors. It tells you, with formal precision, that an *engine* is not a *process of running*, and that a *hole* is a *quality*, not an *object*.

FPF, by contrast, is a **thinking-oriented architecture**. Its primary task is not to describe the world but to **orchestrate the process of reasoning about the world**. It is less a map and more a compass and checklist, guiding an agent's attention toward the decisive aspects of a problem—objectives, trust, emergence, and dynamics—before any taxonomy is imposed. This resolves a core tension: descriptive ontologies become static encyclopedias, while FPF's generative patterns interlink into an evolvable language for action.

The following contrasts highlight this shift:

| Characteristic | Classical Upper Ontology | FPF's Thinking Architecture |
| :--- | :--- | :--- |
| **Core Task** | Logically consistent inventory of entity types. | Generative scaffold for reasoning and decision-making. |
| **Primary Question** | “What is this?” | “How do we reason about this, and why does it matter?” |
| **Guiding Artefact** | Taxonomy & logical axioms. | **Patterns** (context ▲ problem ▲ solution + CC). |
| **Validation Mode** | Consistency in formal reasoners. | Satisfying **Conformance Checklist** for goals, trust, emergence. |
| **Change Driver** | Domain evolution → new classes. | Cognitive evolution → new reasoning patterns. |
| **Cross-Disciplinarity** | Challenging: each domain = new branch. | Built-in: patterns span ≥3 domains (C-1 Universality). |
| **Physical Grounding** | Optional; often abstract. | Mandatory: material Transformer anchor (e.g., in Pattern D.1 Mereology). |

## The "Bitter Lesson" trajectory — compute, data, and freedom over hand‑tuned rules (FPF stance)
Empirical progress since 2015 supports the “Bitter Lesson” (Sutton, 2019): systems that leverage *more data*, *more compute*, and *more freedom* (less hand‑coded domain procedure) tend to outperform bespoke rule‑engineered solutions. Scaling‑law work (e.g., 2020–2022) shows that broader models benefit from compute/data scaling; instruction‑following and tool‑use methods (2019–2024) let general models adapt across tasks without per‑task re‑engineering (e.g., ReAct‑style tool use, self‑reflection/Reflexion, autonomous open‑world exploration such as Voyager/Auto‑GPT‑class agents).

 FPF separates *goals and constraints* from *procedures*. We prefer **Rule‑of‑Constraints (RoC)** — explicit prohibitions, budgets, and safety envelopes — over **Instruction‑of‑Procedure (IoP)** — detailed step‑by‑step scripts. RoC keeps the **design–run separation** intact: designers declare *what must not happen* and *what budgets apply*; agents have freedom of choose *how* to act within those bounds at run‑time. 

**Implications for architecture (normative hooks inside FPF):**
- **Express behavior as goals, constraints, and budgets.** Prefer RoC to IoP. When you must prescribe a procedure (regulatory/safety), document the exception in the Design‑Rationale Record and pair it with run‑time monitors (see *Observability‑first templates*).
- **Autonomy budgets.** For each agent/holon, declare allowed tools, call‑rates, cost/time ceilings, and risk thresholds. Enforce via policy/telemetry cells; record usage in the **Comparability Governance (CG) frame** so that uplift/regret can be compared over runs.
- **Agentic tool use.** Orchestrate function calls via agentic planning/reflective loops instead of fixed pipelines: the agent can choose order, retry strategies, and escalation paths (cf. ReAct‑style tool use, self‑reflection, autonomous exploration in 2022–2024 SoTA). This keeps logic in prompts/policies, not in brittle DAGs.
- **Compute and data elasticity.** Keep **bench/test packs** versioned; enable periodic model refresh without rewriting logic (Chinchilla‑style scaling insight, 2022). Treat data > code when feasible; ensure refresh does not break **parity/comparability** by pinning to the CG‑frame.
- **Feedback‑in‑the‑loop.** Build preference/critique channels (human‑, AI‑, or environment‑in‑the‑loop), shadow modes, and safe A/B gating. Use these to continuously adjust prompts/policies rather than continuously fine‑tuning bespoke sub‑models.
- **Safety first.** Encode **rules‑as‑prohibitions** (create **Constitution-based framework**) and **risk budgets** as RoC; keep them small, explicit, and testable. Combine with design‑run separation to prevent prompt drift from violating safety envelopes.

A **Rule‑of‑Constraints (RoC)** is a compact, versioned policy bundle: *(a)* scope (holon/agent + tools), *(b)* budgets (cost/time/call‑rate), *(c)* prohibitions (red lines), *(d)* escalation (who/what to consult), *(e)* telemetry (metrics to log into the CG‑frame). RoC is enforced at run‑time but never prescribes the exact procedure.

**Why not just add more rules?** Because micro‑ontologies and brittle flow‑charts do not generalize. FPF uses rules to define *boundaries* and *measurement frames* while giving agents freedom to search within them using general models. The inner loop remains empirical: **measure → reflect → adjust RoC/prompts → run**.

**Expected outcomes.** Faster iteration (minutes‑to‑change via prompt/policy edits), resilience to model refresh, lower authoring cost, and higher autonomy at comparable risk thanks to budgets + telemetry + CG‑framed comparability.

## From Flat Documents to High-Dimensional Truth: The Multi-View Architecture

Classical semiotics gave us the Semantic Triangle: Symbol, Concept, Object. It was a useful approximation for a paper-based world where a blueprint was physically distinct from the machine it described. For contemporary systems engineering, computational discovery, and AI-augmented management, that Triangle is a flatland map for a multidimensional territory. It collapses distinctions we now need to keep sharp: it confuses the view with the viewpoint, the carrier with the content, and the projection with the reality.

First Principles Framework (FPF) replaces this flat geometry with a topological architecture for knowledge. A complex `U.System`—whether a nuclear plant, a corporate strategy, or a causal model—cannot be captured by a single “truth document”. It is described by a family of connected epistemes (`U.Episteme`), each rigorous, each partial, and each obtained from the others by law-governed morphisms rather than copy-and-paste edits.

The Episteme as a Slot Graph, Not a Point
In FPF, an episteme is not a static node. It is a structured **Episteme Slot Graph** (`U.EpistemeSlotGraph`, C.2.1). It has explicit slots for what it describes (`DescribedEntity`), where it is grounded (`GroundingHolon`), and through which lens it is seen (`Viewpoint`). This moves us beyond the naive “map vs territory” debate into a disciplined treatment of epistemic morphisms:
* engineering views are not separate files to be synchronised manually; they are structure-preserving projections (`U.EpistemicViewing`, A.6.3) of a shared underlying `DescribedEntity`;  
* retargeting—moving from a physical description to a functional one, or from data to a model—is a formal, effect-free operation (`U.EpistemicRetargeting`, A.6.4) governed by bridges and invariants, not by “creative writing”.

Multi-View Describing vs Publication (MVPK)
Engineers and managers often mistake the act of publishing (making a PDF, updating a dashboard) for the act of describing. FPF enforces **Strict Distinction** here (A.7, E.10.D2). `U.MultiViewDescribing` arranges families of descriptions and specifications under engineering viewpoints; the **Multi-View Publication Kit** (MVPK, E.17) sits on top and treats publication as a typed, functorial projection from those morphisms to human-facing surfaces.

A “Safety Case” and a “System Architecture” are not competing documents; they are two valid views of the same holon, rendered under different viewpoints and onto different surfaces. When a manager looks at a red/green dashboard, they are looking at a `U.View` (an `U.EpistemeView`), mathematically derived from underlying Work and EvidenceGraph lanes via a declared `U.Viewpoint` and `PublicationScope`. As long as that correspondence is maintained, the report cannot drift away from the reality it summarises without tearing the audit trail.

Supporting State-of-the-Art (SoTA)
This multi-view architecture is designed for the age of the **Bitter Lesson**. Modern AI and solver-based workflows do not “think in documents”; they operate on latent representations, graph embeddings, and formal constraints. FPF’s multi-view kernel lets us treat a neuro-symbolic embedding, a solver model, and a human-readable specification as three views of the same episteme, linked by declared correspondences. It turns the “black box” of AI into a named component of a multi-view description, where we can rigorously ask: *under which viewpoint(s) is this output admissible, and over which ClaimScope (G)?*

By treating description as a graph of typed projections rather than a pile of files, FPF gives the Engineer tools to keep views coherent, the Researcher tools to trace provenance across viewpoints, and the Manager justified confidence that dashboards and reports are lawful views of the territory, not parallel worlds.

## Boundary Statements: Where Language Becomes a System Boundary

Most of the time we can think in fast, compressed speech. Teams say “it’s the same”, “we synced it”, “the service guarantees”, “this is compliant”, and everyone roughly knows what is meant. Nothing explodes—until that sentence crosses a boundary: it lands in an interface, a safety case, an evaluation protocol, a contract, or a dashboard used for a go/no‑go decision.

At the boundary, prose stops being “just communication” and starts behaving like a mechanism. Ambiguity becomes a latent defect: it forks viewpoints, hides obligations, and later gets “patched” by politics rather than evidence.

In post‑2015 engineering practice, boundary text is everywhere:

- API contracts (OpenAPI/Protobuf/gRPC), schema evolution, and data contracts;
- SLO/SLA language in SRE, incident retrospectives, and operational gating;
- ML governance artefacts: evaluation protocols, model cards, dataset sheets, reproducibility checklists;
- regulatory and safety assurance: “what is guaranteed”, “what is admissible”, “what evidence counts”.

FPF treats such boundary sentences as first‑class architectural objects. The **A.6 cluster** (*Signature Stack & Boundary Discipline*) is the place in the spec that deals with the edge‑cases of meaning: the situations where “normal prose” is too lossy, but a full formal spec is not yet available (or not yet worth the cost).

The key idea is simple: do not let one sentence do four jobs. When the same line simultaneously tries to define meaning, declare a runtime gate, assign a duty, and claim evidence, it becomes uncheckable. A.6 gives a lightweight routing discipline—captured as the **Boundary Norm Square** (A.6.B)—that keeps these roles separate:

- **L — laws & definitions** (truth‑conditional content you can inspect or reason over),
- **A — admissibility & gates** (what a mechanism admits at application time),
- **D — deontics & commitments** (who owes what, to whom, and under which scope),
- **E — work‑effects & evidence** (what must be observable on carriers so adjudication is possible).

Once boundary talk is routable, it becomes evolvable: different views can publish the *same* underlying boundary without creating parallel contracts, and changes can be narrated without silently rewriting meaning.

## Raising Semantic Precision: From Triggers to Math‑Backed Ontics

FPF does not assume people will speak in fully‑typed relational algebra on day one. Early thought is sketchy, and that is healthy. What matters is having a repeatable upgrade path—a way to go from “useful but ambiguous” to “auditable and reusable” when a statement starts carrying load.

That upgrade is often called “formalization” in everyday speech, but in FPF it is a **semantic precision upgrade**: a small workflow that turns compressed language into structure you can reason about. “Formalization” is only one internal step: choosing a stable mathematical substrate so the reasoning cannot collapse back into vibes.

A good precision upgrade tends to follow five moves:

1. **Notice the triggers.** Umbrella verbs (“sync/align/ground/depends”), pronouns (“it/this”), and metonymic endpoints (“the service”, “production”) are not sins; they are alarms that a richer ontic fragment is hiding underneath.
2. **Unpack the ontic fragment.** Make the local mini‑ontology explicit: which kinds, roles, scopes, viewpoints, time selections, and evidence objects are actually in play.
3. **Put a stable mathematical object under it.** Choose a structure with known behaviour—record types with named slots, typed n‑ary relations / hyperedges, partial orders, lattices, graphs, effect signatures—so future edits become well‑posed transformations rather than rewrites of prose.
4. **Refactor the ontology to fit the substrate.** Split bundled notions, make participant positions explicit, declare invariants, and introduce named change classes for “what changed?” (retarget vs revise vs rescope, etc.).
5. **Mint precise lexemes and guardrails.** Give the refined concepts specific names and keep them paired across registers (Tech/Plain twins via **LEX‑BUNDLE**, E.10). Add lexical firewalls so the umbrella words don’t silently re‑enter and collapse distinctions again.

In the spec this precision‑upgrade move is captured as a family recipe (**A.6.P**, Relational Precision Restoration) and then specialised for recurring boundary pain points (slot discipline, basedness declarations, service polysemy, cross‑context “same”, contract unpacking). The point is not to ban natural language; the point is to make natural language *upgradeable*.

A tiny example illustrates the intent:

Before (fast speech): “We synced the model with production.”  
After (precision‑restored): declare *which* relation kind holds between *which* endpoints, under *which* scope/time/viewpoint, with *which* admissible change classes—and publish a Plain gloss that maps back to the Tech token.

Once the relation has a kind, slots, qualifiers, and a change lexicon, you can do what modern SoTA engineering expects: evolve it safely, compare editions, automate checks, and still keep the story readable for humans.

## The “big storylines” unique to FPF (load‑bearing commitments)
1. **Holonic kernel with physical anchoring**  —  everything that composes is a `U.Holon`; every change is enacted by an **external transformer** (A.1; A.12).
2. **Role–Method–Work split with time duality** — prevents the endemic plan/reality conflation; only `U.Work` carries actuals (A.4; A.15.1–.2).
3. **Assurance as a first‑class calculus** — evidence roles, decay, and weakest‑link composition make “trust” computable and auditable (B.3; A.10).
4. **Algebra of aggregation (Γ) with cross‑scale invariants** — conservative composition that generalizes from pumps to proofs (B.1).
5. **Local meaning, global alignment** — `U.BoundedContext` islands and explicit Bridges with **congruence‑loss** turn “it depends” into a Standard (A.1.1; F.9).
6. **Publication Standard & guard‑rails** — Core ↔ Tooling ↔ Pedagogy split, notational independence, and Lexical Discipline prevent conceptual drift (E.5; E.10).
7. **Open‑ended evolution by design** — evolve not only solutions but also problem frames; work not only on holons‑of‑interest but also across the diversity of their environments.
8. **Creativity with Novelty and Quality Diversity optimisation** — DRR, evidence refresh, **and explicit creative search (NQD + E/E‑LOG)** keep the system alive without ossification (A.4; B.4; **C.18; C.19;** E.6; E.9; B.3.4).
9. **Semantic precision of boundary statements** — five moves (lexical, ontological, mathematical, adjusted ontological, ajusted lexical) to unpack precision on the statements "on the boundary" with multiple viewpoints (cluster A.6 and especially A.6.P and its specializations).

**What FPF is**: a **generative, testable architecture for open-ended evolutionary thinking** that any domain can inhabit.
**What FPF is not**: a repository of domain facts, a rule‑chaining engine, a methodology du jour, or a notation.

## Transdisciplinarity as a Meta‑Theory of Thinking

*Modern complexity lives at the junction of silos.*  A climate model borrows genetics to track pathogens; a venture‑capital pitch cites thermodynamic “runway.” Yet each field guards its own mathematics, and translation costs soar.  **FPF answers this tension by treating transdisciplinarity as a meta‑theory of thinking itself** — a language for designing reasoning, not another specialist dialect.

 An FPF **pattern** usially a principle, *theory about theories*: holonic Calculus abstracts part‑whole composition; Knowledge Dynamics captures changes in trust to knowledge about holons.  These patterns act as **generative scaffolds**: a biologist modelling adaptation, an engineer designing resilience, and a strategist planning pivot options all reach for the same invariant trio — *objective, feedback loop, trust metric*.  FPF names that trio explicitly (`U.Objective`, Canonical Evolution Loop, Unified Trust Model) and **requires universality** *(Principle C‑1: at least three heterogeneous domains)*.

The synthesis is physical, not metaphoric. *Constructive mereology* (Kit Fine) and *Constructor Theory* (Deutsch & Marletto) insist that every whole arises through a **material Transformer as transformer of matter and information**—a sensor grid that binds “crowd‑flow” to joules, a data pipeline tying employee action to market response. Part B formalises this anchor; without it, abstractions cannot cross scales.

Modern projects live at the junction of silos: software SREs speak of *incidents* and *SLOs*, manufacturing lines of *acceptance* and *tolerances*, scientists of *evidence* and *replication*. The same surface word often means different things across these local traditions, and unguarded reuse of labels silently corrupts designs, audits, and decisions. Part F provides a **local‑first** discipline for meaning that **keeps senses inside a `U.BoundedContext`** and requires any cross‑context reading to travel through an **explicit Bridge** with a declared **congruence level (CL)** and **loss notes**. In short: *translate across contexts; never collapse them*.  

Part F is the framework’s **publication surface for cross‑domain alignment**. It turns harvested terms into **SenseCells** (context‑scoped senses), relates them via **Bridges** (with kind, direction, CL, loss), bundles aligned senses into **Concept‑Sets**, and publishes the result as a single, human‑readable **Unified Term Sheet (UTS)**—*“one table that a careful mind can hold.”* This sheet is how engineers, managers, and researchers **talk precisely about the same things** while preserving local rigor.  Disciplines divide the world; trans-disciplinary theories that captured in FPF's patterns remind us it is one conversation.

Part G turns “state‑of‑the‑art” from a moving target into a **governed, selector‑ready portfolio**. It does this by (i) fixing *what may be compared and under which evidence minima*; (ii) generating and harvesting SoTA alternatives across rival traditions; (iii) authoring lawful measurements and calculi; (iv) registering method families and selecting among them **without semantic flattening**; and (v) shipping edition‑aware packs with telemetry so that refresh is principled rather than ad‑hoc. In short: **G formalises SoTA as an auditable, updatable object, not a leaderboard snapshot.**   

## FPF as a Culinary Architecture for Collective Thought: Why We Formalize “Obvious” Ideas

A thoughtful reader encountering concepts like *Open-Ended Evolution*, *Minimally Viable Examples*, or the *Explore-Exploit* trade-off within FPF might rightly observe: "These are not new ideas. They are foundational principles in fields from Agile development to strategic management." This observation is not only correct; it is central to understanding FPF's unique value.

FPF does not seek to invent the fundamental ingredients of rigorous thought. Its purpose is not to discover that evolution is effective or that empirical testing is valuable. Its mission is to provide a **transdisciplinary architectural synthesis** of these powerful, "obvious" ideas, transforming them from disconnected heuristics into a coherent, interoperable, and fully-governed "operating system for thought."

A useful analogy is the distinction between an individual cook following a recipe and a professional kitchen organized for the collective, high-quality production of diverse dishes in a dynamic environment:
*   **The fundamental concepts** (MVP, evolution, exploration/exploitation) are like **fundamental ingredients**: flour, eggs, salt, heat. They are universal and essential.
*   **A domain-specific methodology** (like Lean Startup or a specific scientific method) is like a **cookbook**: it provides excellent recipes for using those ingredients to create a specific dish, such as a software product or a research paper.
*   **The First Principles Framework (FPF)** is the **architecture of the kitchen itself**—the system established by Auguste Escoffier as the *brigade de cuisine*.

Escoffier did not invent the ingredients, nor did he create every recipe. He designed a **system** with defined roles (*Saucier, Pâtissier*), standardized techniques (*sauté, julienne*), and a clear workflow that could reliably produce a vast range of complex dishes to a consistently high standard. The architecture of the kitchen, not any single recipe, is what enables culinary excellence at scale.

FPF provides this same architectural layer for the process of thinking. It operationalizes these "obvious" ideas by giving them a formal place and a normative function within a larger, cohesive system.

| **Culinary Architecture** | **First Principles Framework (FPF)** | **The Value of the Architecture** |
| :--- | :--- | :--- |
| **Defined Roles** (e.g., *Pâtissier*) | **`U.Role` & `U.RoleAssignment` (A.2)** | Separates concerns and assigns clear, context-dependent responsibilities to agents. |
| **Standardized Techniques** (e.g., *sauté*) | **`U.Method` & `U.MethodDescription` (A.3)** | Provides a universal, representation-agnostic way to describe *how* an action is performed, from a physical process to a line of reasoning. |
| **Workflow & Composition** (plating a dish) | **Universal Algebra of Aggregation (Γ) (B.1)** | Guarantees that components (whether physical parts or logical premises) can be composed into a coherent whole in a predictable and auditable way. |
| **Trans-Culinary Applicability** | **Transdisciplinarity (C-1)** | The same architecture that "cooks" a `U.System` can be used to "cook" a `U.Episteme` or a personal development strategy, because the underlying principles of composition, evolution, and assurance are universal. |

Therefore, when one author applies the concept of "exploration vs. exploitation" by drawing from business literature and another by referencing FPF, they may arrive at similar practical advice. The difference is that the FPF user is operating within an architecture where that single concept is already connected to a rich, formal network of other principles. Their decision is implicitly wired into a system of Evidence Graph Referring, trust calculus, and open-ended evolution, making it more robust, auditable, and seamlessly composable with other rigorously-defined concepts.

FPF does not claim ownership of the timeless ingredients of good thinking. It provides the timeless architecture that enables a world-class kitchen for collective thought.

This naturally leads to a crucial question: if a skilled practitioner, without formal knowledge of FPF, can produce a solution of comparable quality, where does the framework's value truly lie?

The answer lies at the threshold of complexity. For a well-defined problem solved by a single, expert agent, well-honed heuristics and tacit knowledge often suffice. The solutions proposed by such an expert and by FPF may indeed appear indistinguishable, much like a master chef's personal recipe for a single dish is impeccable without needing a formal kitchen architecture. FPF shines not in delivering a superior single-shot response, but in sustaining and evolving answers over time in collective thinkibng environment through its built-in cycles of reasoning and refinement with auditable trace and knowledge hands-off standardisation. While an initial pass through these cycles may yield comparable quality with or without FPF — drawing on common sense, ubiquitous knowledge and ad hoc intuition — the framework's true value emerges in the long term, where its evolvability, auditability, and mechanisms for managing epistemic debt ensure that solutions adapt, compound, and scale without fragmentation or decay.

FPF's utility begins to scale exponentially when the problem itself crosses a **Pareto frontier of complexity**, where the "general cultural knowledge" of even a brilliant individual becomes suboptimal. This frontier is defined not by mere computational difficulty, but by the emergence of several non-computational dimensions:

*   **Compositional Complexity:** The need to integrate numerous, heterogeneous, and often conflicting components—be they physical parts, software modules, or logical premises—into a coherent and reliable whole.
*   **Collaborative Complexity:** The need to align the mental models and coordinate the work of a diverse team, ensuring that a shared understanding is maintained without stifling individual contribution.
*   **Temporal Complexity:** The need for a solution to live, adapt, and evolve over long periods, maintaining its conceptual integrity and remaining auditable for future generations of stakeholders.
*   **Assurance Complexity:** The need to provide explicit, auditable, and often formal proof that a solution is safe, reliable, and fair, especially when the cost of failure is high.
*   **Generative Complexity:** The need not to find a single correct answer, but to systematically explore a vast solution space, manage a portfolio of diverse options, and drive open-ended evolution.

An expert's intuition can find a single, excellent point on this multi-dimensional frontier. FPF provides the architectural discipline to navigate the entire frontier. It is the necessary scaffold for building solutions that are not only clever, but also composable, collaborative, evolvable, trustworthy, and perpetually creative at scale.

## Intellect Stack

*Complex problems fail more often from mis‑aligned competencies than from missing facts.* Inside one brain—or one team—model builders, testers, and decision makers can behave like separate departments. The **Intellect Stack** offers a **layered map of cognitive skills**, showing how FPF’s patterns combine into an “operating system for thought.”

The stack is **pedagogical, not prescriptive**: you may enter at any layer, but mastery grows when the layers reinforce one another. Each rung names a domain‑agnostic capability (`U.Capability`) and points to the patterns that realise it.

Conceptually, the Intellect Stack is formalized as a non-normative **Characterization (CHR) package**. This package defines types such as `U.IntellectLayer` (e.g., *Logician*, *Strategist*) and `U.Competency`, which are then linked to the kernel's `U.Capability` via a `hasCapability` mapping. This ensures that while the stack remains a flexible teaching tool, its structure is coherent and formally grounded.

| Layer                          | Core question                          | Key patterns & exemplary domains                                                                                                                            |
| ------------------------------ | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1 - Structure & Reality**    | *What exists and how is it bounded?*   | **Kind-CAL** for universal categories; **Sys‑CAL** for system boundaries. <br>Physics (control volumes), Software (static types), Ecology (trophic levels). |
| **2 - Knowledge & Reasoning**  | *Why should we trust this claim?*      | **KD‑CAL** (F‑G‑R characteristics), **Arg‑LOG** for formal argument. <br>AI (model validation), Evidence‑based policy.                                                 |
| **3 - Action & Execution**     | *How do we turn intent into change?*   | **Agent‑CHR**, **Method‑CAL**, **Resrc‑CAL**. <br>Robotics (action plans), DevOps (pipelines), Urban planning (resource flows).                             |
| **4 - Strategy & Rationality** | *Which option wins under uncertainty?* | **Decsn‑CAL**—`U.Decision`, causal models. <br>Finance (risk fronts), Military wargaming.                                                                   |
| **5 - Governance & Purpose**   | *Why act at all; what is permissible?* | **Norm‑CAL**—`U.Objective`, value conflicts. <br>Bioethics, Sustainability metrics.                                                                         |

Every layer remains **physically grounded**: an abstract *method* references a *material Transformer* (Pattern D.1) such as a laboratory rig or CI runner that proves the method can exist.  Without that anchor, the skill is rhetoric, not capability.

The stack mirrors software’s architecture layer stacks. **A.5 Open‑Ended Kernel & Extention Layering** lets new layers emerge via **Design Rationale Records (E.9)**, keeping the map alive.

A full description of the Intellect Stack and its layers resides in the Pedagogical Companion.

*“A stack without mastery is scaffolding; mastery without a stack is improvisation—FPF supplies the ladder that turns skills into intelligence.”*

## Purpose, Scope, and Explicit Non‑Goals

*A framework that aims at everything excels at nothing.* To keep **Cognitive Elegance (P‑1)** and **Pragmatic Utility (P‑7)** intact, FPF draws a deliberate line around what it serves—and what it refuses to be.

**Purpose – an operating system for thought**
FPF’s mission is to supply a **generative scaffold** that carries a raw idea—whether from a physicist, a product‑manager, or an AI agent—toward a reproducible, auditable impact on the physical world. It does so by offering:

* a **Kernel of first principles**—postulates that are universal (SCR in ≥ 3 heterogeneous domains per C‑1), falsifiable, and non‑derivable inside the framework;
* **patterns as principles and meta‑theories of thinking**, such as Systemic Calculus for composition and Knowledge Dynamics for epistemic evolution;
* **patterns with Conformance Checklists** that quantify objectives, trust, emergence, and evolution;
* **Design Rationale Records (DRRs)** that govern safe, auditable evolution of the Canon;
* a **Constitution**—the **Eleven Pillars (E.2)** plus the **Guard‑Rails (E.5.\*)**—that constrains all normative content.

**Scope – tool‑agnostic, normative patterns only**
This Core Specification defines:

1. **Universal concepts** (`U.Type`, `U.Objective`, `U.Decision`, …).
2. **Algebras of composition** (aggregation, role‑projection, metasystem transition).
3. **Invariants of change**—rules that safeguard cross‑scale consistency as systems evolve.

Everything here is **free of implementation detail**; verification lives in Tooling, guidance in Pedagogy. Physical grounding is mandatory: every abstraction must reference a *material Transformer* (Pattern D.1).

**Explicit Non‑Goals – enforced by guard‑rails**

| Non‑Goal                      | Rationale / Pattern link                                                                                                                       |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Domain encyclopaedia**      | FPF hosts no physics constants or finance taxonomies; import such knowledge via Type & Role Calculus (`D‑0`).                                  |
| **Single mathematical dogma** | Patterns are expressible in multiple formalisms; **Notational Independence** (`E.5.2`) forbids locking into OWL, JSON‑LD, or category theory. |
| **Prescribed tool stack**     | Implementation choices belong to the **Tooling Reference**; the Core never cites CI pipelines or file formats (**DevOps Lexical Firewall `E.5.1`**). |
| **Step‑by‑step tutorial**     | Pedagogical Companion carries worked examples and Intellect‑Stack exercises; the Core remains concise and normative.                           |

This boundary avoids the fate of “grand unifiers” that collapsed under their own encyclopaedic weight. FPF instead follows the lesson of Euclidean geometry and the TCP/IP suite: a **small set of powerful, generative rules** outlives any single domain fashion.

# Part A – Kernel Architecture Cluster

## A.0 - Onboarding Glossary (NQD & E/E‑LOG)
**One‑screen purpose (manager‑first).** This pattern gives newcomers a plain‑language starter kit for FPF’s *generative* engine so they can run a lawful **problem‑solving / search loop** on day one. It explains the few terms you must publish when you **generate, select, and ship portfolios** (not single “winners”), and points to the formal anchors you’ll use later. *(OEE is a Pillar; NQD/E/E‑LOG are the engine parts.)*

**Builds on.** E.2 (**P‑10 Open‑Ended Evolution; P‑2 Didactic Primacy**), A.5, C.17–C.19 - **Coordinates with.** E.7, E.8, E.10; F.17 (UTS); G.5, G.9–G.12 - **Constrains.** Any pattern/UTS row that **describes a generator, selector, or portfolio**.

**Keywords & queries.** *novelty, quality‑diversity (NQD), explore/exploit (E/E‑LOG), **portfolio (set)**, illumination map *(report‑only telemetry)*, parity run, comparability, ReferencePlane, CL^plane, **ParetoOnly** default*

### 1) Problem frame

Engineer‑managers meeting FPF for the first time need a **plain, on‑ramp vocabulary** for the framework’s *generative* engine so they can run an informed **problem‑solving/search loop** on day one—*before* formal specifications. Without that, Part G and Part F read as assurance/alignment only, and teams default to single “best” options. This **undercuts P‑10 Open‑Ended Evolution** and weakens adoption. 

### 2) Problem

In current practice:

* **Single‑winner bias.** Teams look for “the best” option and publish a leaderboard, suppressing **coverage & diversity** signals essential to search.
* **Metric confusion.** “Novelty” and “quality” are used informally; units/scales are omitted; ordinal values are averaged, breaking comparability.
* **Hidden policies.** Explore/exploit budgets and governor rules are implicit; results are irreproducible and **refresh‑unsafe** (no edition/policy pins).
* **Tool lock‑in.** Implementation terms (pipelines, file formats) leak into the Core, violating Guard‑Rails.

FPF needs a **short, normative glossary** that names the generative primitives in **Plain** register and ties each to its **formal anchor**—so portfolios, not single scores, become the default publication. 

### 3) Forces

| Force                         | Tension                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------- |
| **Readability vs Rigor**      | One‑liners for managers ↔ lawful definitions with editions and scale types.     |
| **Creativity vs Assurance**   | Open‑ended search (OEE/QD) ↔ conformance, parity, and publication discipline.   |
| **Comparability vs Locality** | Shared N‑U‑C‑D terms ↔ context‑local CG‑frames and bridges with CL.             |
| **Tool‑agnostic Core**        | Conceptual publication in UTS ↔ engineering teams’ urge to cite specific tools. |

### 4) Solution — **Normative onboarding glossary and publication hooks**

#### 4.1 Plain one‑liners (normative on‑ramp; formal anchors in C.17–C.19)

| Term                      | Plain definition (on‑ramp)                                                                                                                                   | See        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **Novelty (N)**           | *How unlike the known set in your declared **CharacteristicSpace**. **Compute lawfully** (declared `DescriptorMapRef` + `DistanceDefRef`; no ad‑hoc normalisation). | C.17, C.18 |
| **Use‑Value (U / ValueGain)** | *What it helps you achieve now under your **CG‑Frame**; tie to acceptance/tests; **publish units, scale kind, polarity, ReferencePlane**.                   | C.17, C.18 |
| **Constraint‑Fit (C)**    | *Satisfies must‑constraints (Resource/Risk/Ethics)*; legality via **CG‑Spec**; **unknowns propagate** (never coerce to zero).                                | C.18, G.4  |
| **Diversity_P (portfolio)** | *Adds a new niche to the **portfolio**; measured against the **active archive/grid**, not a single list; declare **ReferencePlane** for each head.          | C.17, C.18 |
| **E/E‑LOG**               | *Named, versioned **explore↔exploit** policy*; governs when to widen space vs refine candidates; **policy‑id is published**.                                   | C.19       |
| **ReferencePlane**        | *Where a value lives:* **world** (system), **concept** (definition), **episteme** (about a claim). **Plane‑crossings add CL^plane** (penalties to **R only**); cite policy‑id. | F.9, G.6   |
| **Scale Variables (S)**  | *The **monotone knobs** along which improvement is expected* (e.g., parameterisation breadth, data exposure, iteration budget, resolution). **Declare S** for any generator/selector claimed to scale. | C.18.1       |
| **Scale Elasticity (χ)** | *Qualitative class of improvement when moving along S* (e.g., **rising**, **knee**, **flat** in the declared window). Used as a **selection lens**; numeric laws live in domain contexts.              | C.18.1       |
| **BLP (Bitter‑Lesson Preference)**  | *Default policy that **prefers general, scale‑amenable methods** over domain‑specific heuristics, unless forbidden by deontics or overturned by a scale‑probe.*                                        | C.19.1, C.24 |
| **Iso‑Scale Parity**  | *Fair comparison across candidates at equalised **scale budgets** along S*; may also include **scale‑probes** (two points) to test elasticity.                                                         | G.9, C.18.1  |

*(Registers & forbidden forms per **LEX‑BUNDLE**; avoid “axis/dimension/validity/process” for measurement and scope.)*  

#### 4.2 Publication & telemetry duties (where these terms **show up**)

1. **UTS surface (Part F).** When a **UTS row describes a generator, selector, or portfolio**, it **MUST** surface **N, U, C, Diversity_P, E/E‑LOG `policy‑id`, `ReferencePlane`**, with **units/scale/polarity** typed under **MM‑CHR / CG‑Spec**, and lawful references to `DescriptorMapRef`/`DistanceDefRef`. *(Row schema: F.17; shipping via G.10.)*  
2. **Parity & edition pins (Part G).** When QD/OEE is in scope, **pin** `DescriptorMapRef.edition` and `DistanceDefRef.edition` (and, where applicable, `CharacteristicSpaceRef.edition`, `TransferRulesRef.edition`) and record `policy‑id` + `PathSliceId`. Treat **illumination/coverage as report‑only telemetry**; publish an **Illumination Map** where G‑kit mandates parity artefacts. **Declare S** (Scale Variables) and run at least one **scale‑probe** (two points along S) when claiming **scale‑amenability**. **Dominance policy defaults to `ParetoOnly`;** including illumination in dominance **MUST** cite a CAL policy‑id.
3. **Tell‑Show‑Show (E.7/E.8).** Any arhitectural pattern that claims generative behaviour **MUST** embed **both** a **U.System** and a **U.Episteme** illustration using this glossary (manager‑first didactics). 

#### 4.3 Minimal recipe (run this on day one)
1) Declare **CG‑Frame** (what “quality” means; lawful units/scales) and **ReferencePlane**.  
2) Pick 2–4 **Q components** + a simple **DescriptorMap** (≥2 dims) for N/D; publish **editions**.  
3) Choose an **E/E‑LOG policy** (explore↔exploit budget); record **policy‑id**.  
4) Call the selector under **G.5** with parity pins; **return a set** (Pareto/Archive), not a single score.  
5) **Publish to UTS** + **PathIds/PathSliceId**; **Illumination Map** is **report‑only telemetry** by default.

### 5) Archetypal Grounding
*Informative; manager‑first (E.7/E.8 Tell‑Show‑Show).*  <!-- exact heading per CC‑AG.1 -->

**Show‑A - SRE capacity plan (selector returns a set).**
*Frame.* We must raise service commitment headroom for Q4 without breaking latency SLOs.
*Portfolio.* `{cache‑expansion, read‑replicas, query‑shaping, circuit‑breaker tuning, schema‑denorm}`.
*Glossary in action.* `U = latency@p95 & error‑rate`, `C = budget ≤ $X, risk ≤ R`, `N = dissimilarity to current playbook`, `Diversity_P = adds a previously empty niche in our archive (e.g., “shifts load to edge”)`. E/E‑LOG starts **Explore‑heavy**, flips **Exploit‑heavy** once ≥ K distinct niches are lit. *(Publish UTS row + parity pins; illumination stays report‑only telemetry.)*  

**Show‑B - Policy search with QD archive (MAP‑Elites‑class).**
*Frame.* Robotics team explores gaits that trade stability vs energy use.
*Glossary in action.* `CharacteristicSpace = {step‑frequency, lateral‑stability}`, `ArchiveConfig = CVT grid`, `N` from descriptor distance, `U` = task reward, `Diversity_P` = coverage gain; **PortfolioMode=Archive**. Families include **MAP‑Elites (2015)**, **CMA‑ME/MAE (2020–)**, **Differentiable QD/MEGA (2022–)**, **QDax (2024)**; publish editions and policy‑ids; treat illumination as **report‑only telemetry**.  

*(Optional)* **Show‑C - OEE parity (POET/Enhanced‑POET).**
Co‑evolve `{environment, method}` portfolios; publish **coverage/regret** as telemetry metrics; pin `TransferRulesRef.edition`; return *sets*, not a single winner. 
  
**Show‑Epi - Evidence synthesis (U.Episteme).**
*Frame.* A living review compares rival **causal identification** methods (e.g., IV vs. DiD vs. RCT‑adjacent surrogates) across policy domains.
*Glossary in action.* `U = external‑validity gain @ F/G‑declared lanes`, `C = ethics & data‑licence constraints`, `N = dissimilarity in **ClaimGraph** transformations`, `D_P = coverage of identification niches in the archive`. `ReferencePlane = episteme`. Illumination/coverage stays **report‑only telemetry**; selection returns a **portfolio** of methods per niche. *(Publish UTS rows; cite Bridges + CL for cross‑domain reuse; edition‑pin Descriptor/Distance defs where QD applies.)*

### 6) Bias‑Annotation

**Scope.** Trans‑disciplinary; glossary applies to both **System** and **Episteme** work.
**Known risks & mitigations.**
*Over‑aggregation:* forbid mixed‑scale sums; use **CG‑frame** and **MM‑CHR**.
*Terminology drift:* enforce **LEX‑BUNDLE** registers; ban tool jargon in Core.
*Optimization monoculture:* require **portfolio** publication where G‑kit mandates parity; illumination stays **report‑only telemetry** unless a CAL policy promotes it (policy‑id cited).   

### 7) Conformance Checklist (SCR/RSCR stubs)

| ID          | Requirement                                                                                                                                                                               | Purpose                                                                         |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **CC‑A0‑1** | If a pattern/UTS row **describes a generator, selector, or portfolio**, it **MUST** surface **N, U, C, Diversity_P, `ReferencePlane`, and E/E‑LOG `policy‑id`**; **units/scale/polarity** **MUST** be declared. | Makes generative claims comparable and auditable (UTS as publication surface).  |
| **CC‑A0‑2** | When QD/OEE is in scope, **pin** editions: `DescriptorMapRef.edition`, `DistanceDefRef.edition` (and, where applicable, `CharacteristicSpaceRef.edition`, `TransferRulesRef.edition`); log `PathSliceId` and policy‑ids. | Enables lawful *parity/refresh*; edition‑aware telemetry.                       |
| **CC‑A0‑3** | **No mixed‑scale roll‑ups**; ordinal data **SHALL NOT** be averaged; any roll‑up **MUST** live under a declared **CG‑frame**.                                                             | Prevents illegal scoring; keeps comparisons lawful.                             |
| **CC‑A0‑4** | Where the G‑kit requires parity, **publish an Illumination Map** (coverage per niche); **single‑number leaderboards are non‑conformant** on the Core surface when a ParityReport is required. | Portfolio‑first publication; avoids single‑winner bias.                         |
| **CC‑A0‑5** | Keep **illumination/coverage** as **report‑only telemetry**; **dominance policy defaults to `ParetoOnly`**; any change is CAL‑authorised and cited by policy‑id.                                          | Separates fit from exploration; preserves auditability.                         |
| **CC‑A0‑6** | Apply **E.7/E.8**: include a **U.System** and a **U.Episteme** illustration when claiming generative behaviour; obey **E.10** register hygiene; use the exact subsection title **“Archetypal Grounding.”** | Locks didactic primacy; prevents jargon drift.                                  |
| **CC-A0-7** | **ReferencePlane declared** for every N/U/C/Diversity_P head and **CL^plane** penalties **route to R only**; **Φ_plane** policy-id published when planes differ.                            | Prevents plane/stance category errors; aligns with Bridge/**GateCrossing visibility** guards (Bridge+UTS+CL/Φ_plane). |
| **CC‑A0‑8** | **Diversity_P ≠ Illumination.** Diversity_P may enter dominance; **Illumination** remains **report‑only telemetry** unless explicitly promoted by CAL policy‑id.                                         | Matches QD triad semantics and parity defaults.                                 |
| **CC‑A0‑9** | If a generator/selector is claimed **scale‑amenable**, **declare S (Scale Variables)** and an **E/E‑LOG scale policy‑id**; otherwise mark **S = N/A**.                                      | Makes scale assumptions explicit and comparable across contexts.                 |
| **CC‑A0‑10** | For scale‑amenable claims, execute a **scale‑probe** (≥ 2 points along S) and report a **Scale Elasticity class** (*rising/knee/flat*) in the UTS row.                                      | Forces early strategy‑relevant evidence without over‑specifying numerics.        |
| **CC‑A0‑11** | Apply **Iso‑Scale Parity** in parity runs when S is declared; where infeasible, state the **loss notes** and treat results as **non‑parity** with an explicit penalty in **R**.             | Keeps comparisons fair and auditable under scale constraints.                    |
| **CC‑A0‑12** | **BLP default.** If a domain‑specific heuristic is selected over a general, scale‑amenable method, record a **BLP‑waiver** reason: *deontic*, *scale‑probe overturn*, or *context‑specific*. | Prevents silent violations of the Bitter Lesson; improves selector transparency. |

### 8) Consequences

**Benefits.**
• **Immediate usability** for engineer‑managers (plain one‑liners) with **formal anchors** for auditors.
• **Portfolio‑first** culture (sets & illumination) instead of brittle leaderboards.
• **Edition‑aware comparability**; parity/refresh is routine, not ad‑hoc.

**Trade‑offs & mitigations.**
• Slightly longer UTS rows → mitigated by consistent schema and copy‑paste snippets.
• Requires discipline on units/scales → mitigated by CG‑frame templates.

### 9) Rationale

This pattern **instantiates P‑10 Open‑Ended Evolution** by making *generation‑selection‑publication* **operational** at the on‑ramp: readers get just enough shared vocabulary to run *search as standard practice*. It aligns with **Didactic Primacy (P‑2)** and **LEX‑BUNDLE (E.10)** by keeping definitions *plain‑first* and scale‑lawful, and with **Patterns Layering (P‑5)** by pointing to C.17–C.19 for formal anchors without tool lock‑in. The post‑2015 line (MAP‑Elites → CMA‑ME/MAE → Differentiable QD/MEGA → QDax; POET/Enhanced‑POET/Darwinian Goedel Machine) normalised **quality‑diversity** and **open‑endedness** as first‑class search objectives; this glossary surfaces those ideas as **publication standards**, not tool recipes.  

### 10) Relations

**Builds on.** **E.2 Pillars** (P-10, P-2, P-6), **A.5** (Open-Ended Kernel), **B.5/B.5.2.1** (Abductive loops + NQD integration), **C.17–C.19** (Creativity-CHR, NQD-CAL, E/E-LOG).    

**Coordinates with.** **E.7/E.8** (Archetypal Grounding; Authoring template), **E.10** (LEX‑BUNDLE), **F.17** (UTS), **G.5/G.9–G.12** (set‑returning selectors, **iso‑scale** parity, shipping & refresh).
**Constrains.** Any generator/selector/portfolio publication on the Core surface: **N‑U‑C‑Diversity_P + policy‑ids; S/Scale‑probe where applicable; parity pins; lawful scales; portfolio‑first where mandated**. (Ties into UTS rows and parity artefacts.)
**Editor’s cross‑reference.** For agentic orchestration of scalable tool‑calls under **BLP**/**SLL**, see **C.24 (Agent‑Tools‑CAL)**.

### Editor’s note (implementation hint)

This pattern is an **on‑ramp**: it **does not replace** C.17–C.19. It binds Plain definitions to **publication/telemetry** expectations so newcomers can *use* NQD/E/E‑LOG immediately while experts follow the formal trails. 

### A.0:End


## A.1 - Holonic Foundation: Entity → Holon
> **Type:** Architectural (A)  
> **Status:** Stable  
> **Normativity:** Normative

> *“Name the thing without smuggling in its parts.”*

### A.1:1 - Problem Frame

The first epistemic act in any discipline is to **point**: “that thing, not the background.” Physics calls the pointed object a *system*, biology an *organism*, information science an *artifact*, philosophy an *entity*. Reusing any one of these across domains drags hidden assumptions and yields nonsense like *“What is the mass of a system of equations?”* or *“Where is the network interface of a moral theory?”*
FPF therefore starts from a **minimal, domain‑agnostic root** that makes such category errors impossible **by construction** and gives engineers and managers a clean, uniform handle for composition, boundaries and interfaces.

### A.1:2 - Problem

If FPF treats **system** as the universal root, two recurrent failure modes appear:

1. **Category Error** — physical affordances get projected onto abstract artifacts (ports on theories; kilogram‑mass of paradigms).
2. **Mereological Over‑reach** — part–whole calculus is applied to genuinely atomic entities (prime numbers, elementary charges), producing meaningless “sub‑parts.”

A robust kernel **separates identity from structure**: first say *what can be singled out*, then say *what has parts*.

### A.1:3 - Forces

| Force                         | Tension                                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Universality vs Intuition** | Precision of a new root term (*Holon*) ↔ practitioner expectation of familiar words (*System*, *Theory*).  |
| **Purity vs Pragmatism**      | Clean formalism ↔ immediate usability for engineers, scientists, managers.                                 |
| **Structure vs Identity**     | Need to talk about atoms with zero parts ↔ need full mereology for composites.                             |

### A.1:4 - Solution — A three‑tier root (Entity ⊃ Holon ⊃ {System, Episteme})

FPF adopts a **three‑tier root ontology** refining Koestler’s “holon,” with crisp boundaries and safe composition. 

#### A.1:4.1 - `U.Entity` — Primitive of Distinction
Anything that can be individuated and referenced. **No structural assumptions.** Use when you need to name “a something” without committing to having parts.

> **Naming note (mint vs reuse).** `U.Entity` and `U.Holon` are minted kernel terms: they reuse familiar words but intentionally diverge from domain‑specific ontologies and DDD “Entity”, so we can reason cross‑domain without importing hidden assumptions.

#### A.1:4.2 - `U.Holon` — Unit of Composition
A `U.Entity` that is *simultaneously* **(a)** a whole composed of parts and **(b)** a part within a larger whole. Formally, `U.Holon ⊑ U.Entity`.
Well‑formedness constraints:

* **WF‑A1‑1 (Single boundary).** A holon has **exactly one** `U.Boundary` that separates it from its environment.
* **WF‑A1‑2 (Γ domain).** The universal aggregation operator **Γ** is defined **only** on sets of `U.Holon` (never on bare `U.Entity`).
* **WF‑A1‑3 (Γ scope).** A Γ‑application is scoped to a declared context and a single declared temporal scope (design **or** run); order/time are routed to Γ\_ctx / Γ\_time (B.1.4).

These constraints make composition rules uniform across domains and prevent Γ from being misapplied.

#### A.1:4.3 - Interface primitives: `U.Boundary` & `U.Interaction`
Every holon is defined by **how** it is separated and **what** crosses the separation.

* **`U.Boundary`** — physical or conceptual surface delimiting the holon’s scope.
* **`U.Interaction`** — any flow of matter, energy, or information that crosses a boundary.
  **Canonical boundary kinds (with twin archetypes):**

| Kind          | Permitted exchanges             | `U.System` archetype               | `U.Episteme` archetype                                        |
| ------------- | ------------------------------- | ---------------------------------- | ------------------------------------------------------------- |
| **Open**      | Matter, energy, information     | Microservice exposing a public API | Public wiki editable by anyone                                |
| **Closed**    | Energy, information (no matter) | Sealed cooling loop in a server    | Version‑locked theory accepting new evidence but fixed axioms |
| **Permeable** | User‑filtered subset            | Cell membrane regulating ions      | Legal code allowing specific amendment classes only           |

This pair (`Boundary`, `Interaction`) makes interfaces explicit, reviewable, and testable across domains.

#### A.1:4.4 - Inside/Outside decision procedure
To decide whether an entity **E** is *inside* a holon **H**, apply:

1. **Dependency test:** removing **E** breaks a core invariant of **H**.
2. **Interaction test:** **E** participates in causal loops wholly within **H**’s boundary.
3. **Emergence test:** **E** contributes to a novel collective property warranting **H** as a single unit.
   Fail all three → **E** is *outside*. This practical triage prevents “scope creep” and forces explicit modeling of environment vs interior.

> **Collections vs collectives.** A set/collection of holons is not itself an acting unit. If a grouping is expected to act, model it as a `U.System` holon with its own boundary and attach roles/methods/work to that system (see CC‑A1.6; details in A.2 and A.15).

#### A.1:4.5 - Archetypal sub‑holons
FPF fixes two **archetypal** specializations to ground cross‑domain universality:

| Subtype                    | Essence                                                | Home pattern |
| -------------------------- | ------------------------------------------------------ | ---------------- |
| **`U.System ⊑ U.Holon`**   | Physical, operational holon obeying conservation laws. | **Sys‑CAL**      |
| **`U.Episteme ⊑ U.Holon`** | Knowledge holon (axioms, evidence, argument graph).    | **KD‑CAL**       |

> **Agency rule.** Behavioural roles and executed methods/work attach to `U.System` holons only; `U.Episteme` is passive content. Any change to an episteme is performed by an external system acting across a boundary (cf. CC‑A1.5 and A.2/A.15).

*Naming guideline:* keep “**System**” and “**Episteme**” for practitioner comfort; reserve **Holon** for meta‑level discourse and formal signatures.

### A.1:5 - Archetypal Grounding (System / Episteme)

| Holonic slot | **`U.System` — Water‑pump**            | **`U.Episteme` — Scientific theory**            |
| ------------ | -------------------------------------- | ----------------------------------------------- |
| **Identity** | Pump #37 stamped on the name‑plate     | “Newtonian Gravitation”, 1726 edition           |
| **Boundary** | Cast‑iron casing; inlet/outlet flanges | Axiomatic scope and vocabulary                  |
| **Parts**    | Motor, impeller, seals, housing        | Axioms, definitions, theorems, datasets         |
| **Whole**    | Operable assembly that moves fluid     | Coherent body of knowledge predicting phenomena |

Showing the **same structural slots** filled by a machine and a theory demonstrates the **substrate‑independent universality** of `U.Holon`. This is the didactic “Tell–Show–Show” anchor required by the Style‑Guide for architectural patterns. 

### A.1:6 - Bias-Annotation — Boundary-first modelling risks

This kernel distinction is intentionally **boundary‑first**: it treats “where the boundary is” as a modelling decision that shapes everything downstream. That framing is powerful, but it can also smuggle bias if boundary choices are made implicitly or for political convenience.

| Lens | Typical bias risk | Mitigation in this pattern |
|---|---|---|
| **Gov** | Boundary decisions become “org charts”, not defensible model choices. | Record boundary rationale in the working model and require the **Inside/Outside test** (A.1:4.4) for contested cases. |
| **Arch** | Over‑modularisation: every interaction becomes a “system” with hard edges. | Prefer **permeable boundaries** when the phenomenon is gradient‑like; keep the `U.Entity`/`U.Holon` split minimal and push dynamics into Roles (A.2) and Work (A.15). |
| **Onto/Epist** | Category error: treating knowledge artifacts as physical actors (or vice‑versa). | Keep `U.Episteme` passive; model transformations as actions of a `U.System` in role, acting via explicit carriers (see A.10). |
| **Prag** | “Holon” becomes jargon that slows teams down. | Use `U.System` / `U.Episteme` in day‑to‑day models; reserve “holon” for kernel‑level discourse (see naming guidance in A.1:4.5 and CC‑A1.8). |
| **Didactic** | Readers infer semantics from overloaded labels or inconsistent headings. | Keep canonical titles and the `U.*` prefixes explicit; avoid informal deontic language in normative clauses (E.8). |

### A.1:7 - Conformance Checklist (normative)

| ID          | Requirement                                                                                                                                                                    | Purpose / Notes                                                                                                        |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **CC‑A1.1** | Any modelled object that exhibits a part–whole structure **MUST** be typed as `U.Holon` or its subtype.                                                                        | Prevents applying Γ to atomic entities; makes aggregation well‑typed.                                                  |
| **CC‑A1.2** | Each `U.Holon` **MUST** reference exactly one `U.Boundary` and declare its boundary kind (*open / closed / permeable*).                                                        | Enables boundary inheritance and environmental Standards; aligns with the canonical boundary kinds introduced in A.1.  |
| **CC‑A1.3** | Domain patterns **MUST** explicitly subtype their root concept (`U.System`, `U.Episteme`, …) from `U.Holon`.                                                              | Ensures cross‑domain compatibility of aggregation and emergence patterns.                                              |
| **CC‑A1.4** | Inside/Outside decisions for any candidate part **SHALL** be justified by the three‑step test (Dependency → Interaction → Emergence) and recorded with the boundary reference. | Makes holon membership auditable and repeatable; uses A.1’s decision procedure.                                        |
| **CC‑A1.5** | Behavioural roles (**including** `TransformerRole`) **SHALL** attach only to `U.System` (the bearer), not to `U.Holon` in general and not to `U.Episteme`.                     | Preserves Strict Distinction and prevents category errors; episteme roles are classificatory only.                     |
| **CC‑A1.6** | Do **not** model acting groups as sets. If a grouping is expected to **act**, it **SHALL** be modelled as a **collective system** (with boundary, role, Method/Work).          | Distinguishes `MemberOf` (collection) from mereology; prepares for A.14 Portions/Phases.                               |
| **CC‑A1.7** | The universal aggregation operator **Γ** **SHALL** be applied **only** to sets of `U.Holon` within a single declared temporal scope (design **or** run) and context.           | Prevents “chimera” graphs; routes order/time to Γ\_ctx / Γ\_time (B.1.4).                                              |
| **CC‑A1.8** | Prose and diagrams **SHALL** follow the naming guideline: use **Holon** for meta‑level discourse; prefer **System / Episteme** in practitioner‑level statements.               | Reduces jargon friction; keeps signatures precise and text readable.                                                   |

> *Audit tip.* CC‑A1.5 is frequently violated when authors write “holon bearing TransformerRole”. Rewrite to “**system** bearing TransformerRole” or provide the explicit `U.RoleAssignment`. See A.2/A.15 for role mechanics.

### A.1:8 - Common Anti‑Patterns and How to Avoid Them — Manager’s quick checks

1. **“Ports on a theory.”** Treating a proof corpus as if it had physical connectors. *Fix:* model `U.Interaction` only across **boundaries**; for epistemes, interactions are **symbolic flows** via carriers and citations (see A.10), not power or mass.
2. **“Document edited itself.”** Assigning actions to an episteme. *Fix:* actions are executed by a **system bearing a role** (A.12/A.15); epistemes are transformed **via external transformers** acting on their **symbol carriers**.
3. **“Parts everywhere.”** Forcing a part–whole onto atomic entities (e.g., prime numbers). *Fix:* if no meaningful parts exist, stay at `U.Entity`; apply Γ only to `U.Holon`.
4. **“Scope ≡ section.”** Using “scope” as a text region rather than a modeled boundary. *Fix:* define a `U.Boundary` and state what crosses it (`U.Interaction`).

> **When in doubt:** first decide **what is a holon**, then state **its boundary**, then list **what crosses**. Roles and methods come *after* (see A.2 and A.15).

### A.1:9 - Consequences (informative)

| Benefits                                                                                                                                                         | Trade‑offs / Mitigations                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Eliminates category errors** across physical and abstract realms by cleanly separating identity (Entity), structure (Holon), and behaviour (Role/Method/Work). | Introduces the unfamiliar term **Holon**; mitigated by Tell‑Show‑Show pedagogy and dual archetypal examples (System/Episteme).  |
| **Unifies aggregation**: a single algebra Γ composes pumps, proofs, genomes, and teams under one roof.                                                           | Requires refactoring legacy “System‑only” language; addressed by A.2/A.3 role calculus and the Γ‑family in B.1.                 |
| **Predictable extension point**: CAL/LOG/CHR patterns add constraints without touching the core types.                                                      | Imposes discipline on boundary declarations; mitigated by boundary kinds and the Inside/Outside test.                           |

### A.1:10 - Rationale — Cross‑domain corroboration (post‑2015, informative)

The separation **Entity → Holon → {System, Episteme}** is not only ontologically clean; it is **empirically validated across domains since 2015**:

* **Compositional open systems.** Category‑theoretic treatments show that *boundaried* components compose safely (decorated cospans, open systems). This mirrors Γ’s reliance on declared boundaries. *(Fong & Spivak, 2019; Baez & Courser, 2017)*
* **Microservices & bounded contexts.** Modern software architecture stresses strong service boundaries and local reasoning as the route to evolvability—our `U.Boundary` and Inside/Outside test encode the same discipline. *(Newman, 2021; Vernon, 2022)*
* **FAIR & provenance.** Data/knowledge communities require explicit distinction between **content** and **carrier**, and auditable provenance—precisely the System/Episteme + SCR split used in A.1/A.10. *(Wilkinson et al., 2016; Boeckhout et al., 2018)*
* **Digital Twin / Thread.** Engineering practice since late‑2010s emphasises the run↔design seam and boundary‑consistent aggregation of subsystems—formalised in our Γ‑family and boundary inheritance rules. *(Grieves & Vickers, 2017; NIST DT/Thread reports 2019‑2021)*
* **Layered control of CPS.** Standard‑based, multi‑rate architectures justify explicit holon boundaries and scale transitions—feeding directly into B.2 Meta‑Holon Transition. *(Matni et al., 2024)*

These streams converge on one point: **make boundaries and composition first‑class** and separate **what a thing is** from **what it is doing here‑and‑now**—the heart of A.1/A.2.

### A.1:11 - SoTA-Echoing (post‑2015, informative)

This solution echoes several modern (post‑2015) research and engineering streams. We **adopt** their boundary‑and‑composition insights, but **reject** any requirement to commit to a single formalism (per Notational Independence).

| Stream | Representative sources | Adopt / Adapt / Reject | What we take (and what we diverge from) |
|---|---|---|---|
| Compositional open systems | Baez & Courser (2017); Fong & Spivak (2019) | **Adapt** | Take the idea that composition should be explicit and typed; diverge by keeping the Core notation‑independent (no category‑theory prerequisite). |
| Software boundaries and bounded contexts | Newman (2021); Vernon (2022) | **Adopt** | Take boundary‑scoped meaning and ownership as the default; diverge by lifting “bounded context” to a kernel boundary concept rather than a software‑only practice. |
| FAIR / provenance for epistemic artifacts | Wilkinson et al. (2016); Boeckhout et al. (2018) | **Adopt** | Take provenance and carrier/content separation; diverge by modelling knowledge artifacts as `U.Episteme` (passive) rather than agents. |
| Digital twin / digital thread | Grieves & Vickers (2017); NIST DT/Thread (2019–2021) | **Adapt** | Take the run↔design seam; diverge by requiring a boundary kind at the holon level. |
| Systems/control criteria for emergence | Matni et al. (2024) | **Adopt** | Take emergence as a criterion for systemhood; diverge by requiring explicit boundary declarations even when “obvious”. |

### A.1:12 - Relations

* **Builds / Grounds:**

  * **A.2 Role Taxonomy** — A.1 provides the substantial characteristic (`Holon`), A.2 introduces the functional characteristic (`Role` and `U.RoleAssignment`). Together they prevent role/type explosion and keep agency contextual.
  * **A.7 Strict Distinction (Clarity Lattice)** — A.1 supplies the *slots* (Entity/Holon/System/Episteme); A.7 guards their separation in prose and models, stopping Object ≠ Description ≠ Carrier conflations.
  * **A.14 Advanced Mereology: Portions & Phases** — A.1’s holon substrate is the target of A.14’s edge discipline (`ComponentOf`, `ConstituentOf`, `PortionOf`, `PhaseOf`); only mereological subtypes build holarchies.

* **Interacts with the Γ‑family (B‑cluster):**

  * **B.1 Universal Algebra of Aggregation** — Γ is defined **on holons** and respects CC‑A1.\*; Γ\_ctx/Γ\_time carry order and temporal composition, Γ\_work handles resource ledgers.
  * **B.2 Meta‑Holon Transition (MHT)** — uses A.1’s boundary and Inside/Outside rules to decide when aggregation yields a **new** whole with novel properties.
  * **B.3 Trust & Assurance Calculus** — evidence attaches to carriers (SCR/RSCR) of epistemes; assurance levels depend on A.1/A.10 alignment.
  * **B.4 Canonical Evolution Loop** — operationalises the **design↔run** seam at holon boundaries; observation itself is an external transformation across a boundary.

* **Specialised by patterns:** `U.System` (Sys‑CAL) and `U.Episteme` (KD‑CAL) are archetypal sub‑holons that supply domain‑specific invariants while inheriting A.1’s boundary and aggregation duties. 

*Without the holon, parts drift; without the role, purpose evaporates.* (Carry this epigraph with A.1 to cue the A.2 hand‑off.)

### A.1:End

## A.1.1 - `U.BoundedContext`: The Semantic Frame

> **Type:** Architectural (A)  
> **Status:** Stable  
> **Normativity:** Normative

*Make meaning local; make translation explicit.*

### A.1.1:1 - Problem Frame

Large systems of thought (and large engineered systems) break down when meaning is treated as globally uniform.
The same label (e.g., “role”, “service”, “ticket”, “evidence”) routinely carries incompatible senses across teams, disciplines, standards editions, and historical eras.

FPF needs a first-class mechanism that answers a simple question with precision:
**“In which semantic frame does this term, rule, or role-claim hold?”**

The `U.BoundedContext` is that mechanism. It makes “it depends” explicit and governable by naming *what it depends on*.

### A.1.1:2 - Problem

Absent an explicit, first-class semantic frame:

1. **Ambiguity becomes structural debt.** Integrations silently overwrite meanings (“process” becomes “procedure”; “role” becomes “permission”), and the resulting model cannot be audited.
2. **Pluralism looks like contradiction.** Two valid perspectives appear mutually exclusive because the frame of reference is implicit (e.g., Pluto as `PlanetRole` vs `DwarfPlanetRole`).
3. **Roles lose semantic footing.** A `U.Role` without a declared frame degenerates into a global label, violating the kernel’s insistence that roles are contextual masks (A.2, A.2.1).
4. **Local rules leak globally.** Team- or theory-specific invariants are mistaken for universal laws, producing incoherent cross-domain reasoning.

### A.1.1:3 - Forces

| Force | Tension |
| :--- | :--- |
| **Local coherence** | A context must be internally unambiguous ↔ real work crosses boundaries and needs translation. |
| **Pluralism** | Multiple valid frames must coexist ↔ readers demand apparent “one truth”. |
| **Governance cost** | Explicit boundaries and rules improve reliability ↔ too many contexts create overhead and fragmentation. |
| **Evolvability** | Contexts must change over time ↔ change must remain traceable and non-destructive to prior meaning. |
| **Familiarity** | Practitioners use domain-native vocabulary ↔ the kernel must stay universal and type-stable. |
| **Domain-family convenience** | People want “the domain” as a handle ↔ FPF requires specific, named semantic frames. |

#### A.1.1:3.1 - Prophylactic clarification — Domain family vs `U.BoundedContext`

To prevent a common category error, **Domain (as used colloquially)** and **`U.BoundedContext`** are **not synonyms** in FPF, and “Domain” is not a kernel type.
Per **E.10.D1 (D.CTX)**, **Domain is an informative family label** grouping multiple contexts; there is no “domain context”.

| Characteristic | **Domain family (informative)** (e.g., Healthcare, Physics, Workflow) | **`U.BoundedContext`** (e.g., `Hospital.OR_2025`, `Theory:QuantumMechanics`, `BPMN_2_0`) |
| :--- | :--- | :--- |
| **Nature** | An external field of practice/knowledge; a catalog handle. | An internal FPF holon: a named semantic frame with local vocabulary and local invariants. |
| **Role in FPF** | Groups contexts for survey, coverage, and stewardship discussions. | Localizes meaning and rules; provides a semantic firewall where words and obligations are coherent. |
| **Relationship** | One family hosts many legitimate perspectives/editions. | One context hosts one such perspective with explicit `Glossary`, `Invariants`, `Roles`, and optional `Bridges`. |

**Well-formedness constraint (didactic):** In any `U.RoleAssignment`, `context` is total and points to **exactly one** `U.BoundedContext` (cardinality **1..1**).
*Think “specific room” (e.g., `Hospital.OR_2025`), not “the whole building” (e.g., “Healthcare”).*

**Manager’s one-liner:** A **Domain family** is the *territory label*; a **Bounded Context** is a *purpose-made map* of one perspective on that territory.

### A.1.1:4 - Solution

FPF elevates **semantic framing** to a kernel primitive by introducing `U.BoundedContext` as a first-class holon of meaning.
Inspired by Domain-Driven Design (DDD) but generalized beyond software, a bounded context is not a mere namespace: it is **a governable model locale** with explicit vocabulary, rules, and role taxonomy.

#### A.1.1:4.1 - Term & Definition

* **Term:** `U.BoundedContext`
* **Definition:** A **`U.BoundedContext`** is a `U.Holon` that serves as an explicit **semantic frame of reference**. It declares a boundary within which a specific vocabulary, role taxonomy, and invariant set are coherent and authoritative. It is FPF’s kernel mechanism for localizing meaning and managing complexity by partitioning a larger conceptual space into smaller, coherent, independently governable **semantic locales** (Contexts).

**Mint vs reuse** (informative): The label "Bounded Context" is reused from DDD; `U.BoundedContext` is the FPF-defined kernel type (generalized beyond software). Cross-context sameness is never inferred from spelling; cross-context alignment is represented only via explicit `Bridge` artifacts (F.9; E.10.U9; see CC-A1.1.5).

#### A.1.1:4.2 - Core components (normative shape)

A `U.BoundedContext` is a composite holon whose *parts* constitute the context’s local “constitution”:

* **`Glossary` (Local Lexicon):** A set of `U.Lexeme` entries (Lang-CHR) defining the local vocabulary and its intended senses. This is where a context can state: “Inside here, `ticket` denotes `U.WorkItem`, not `U.TravelPermit`.”
* **`Invariants` (Local Rules):** A set of `U.ConstraintRule`s (Norm-CAL) that must hold for artifacts and processes operating in this context. These rules define the context’s local “physics”.
  * *Example (role compatibility):* “Within this context, a `holder` cannot simultaneously play `AuditorRole` and `DeveloperRole`.”
  * *Example (state transition):* “A `U.WorkItem` can transition from `InProgress` to `InReview`, never directly to `Done`.”
* **`Roles` (Local Taxonomy):** A partial order of `U.Role`s that are defined and valid only within this context. It specifies the “masks” available on this stage (A.2).
* **`Bridges` (Optional alignments):** A set of explicit cross-context relations (`U.Alignment`, formalized in F.9 / E.10.U9) describing how meaning translates when information crosses context boundaries, including loss/fit notes.
  * *Example (alignment):* “`AgileDevelopment:UserStory` is congruent (CL=1) to `FormalEngineering:Requirement` under the stated loss policy.”

#### A.1.1:4.3 - Context interactions with other kernel objects (normative)

* **As a `U.Holon`:** A `U.BoundedContext` has a defined `U.Boundary` and internal parts (`Glossary`, `Invariants`, …). However, **contexts do not form holarchies with each other**: per E.10.D1 (D.CTX), contexts have no is‑a or containment relations; cross-context relationships are expressed only via explicit `Bridges`.
* **As the semantic frame for `U.RoleAssignment`:** The `context` field of `U.RoleAssignment` identifies the unique semantic frame in which the holder-role assignment is interpreted (A.2.1).
* **As the scope carrier for rules and objectives:** `U.Objective`s and `U.ConstraintRule`s are typically authored and evaluated relative to a specific context’s invariants.
* **As a change target:** Context evolution (new invariants, revised glosses, deprecated roles) is modeled as a `U.Transformer` acting on the `U.BoundedContext` holon itself. Where time is merely stance (`design`/`run`), treat it as a TimeScope tag, not a new context (C‑7; D.CTX).

> *If meaning is local by design, then translation must be explicit by design.*

**Admissibility constraints (concept-level; non-deontic).**

* **BC‑1 (Holon nature).**  A `U.BoundedContext` is a `U.Holon` and declares a `U.Boundary`.
* **BC‑2 (Flat context map).** No `U.BoundedContext` is modeled as inheriting from, containing, or being contained by another `U.BoundedContext`; cross-context relations are represented only via explicit `Bridges` (E.10.D1 / E.10.U9).
* **BC‑3 (Role localization).** Every `U.Role` is defined in the `Roles` taxonomy of at least one `U.BoundedContext`; a "global role" is not a valid kernel object.
* **BC‑4 (Invariant scope).** Any invariant authored in a Context applies only to holons and processes operating within that Context; cross-context reuse is mediated by Bridges and re‑stated locally.
* **BC‑5 (Bridge explicitness).** Any interaction or semantic alignment between two Contexts is represented by an explicit `Bridge` artifact.
* **BC-6 (RoleAssignment context field).** A `U.RoleAssignment` references exactly one `U.BoundedContext` in its `context` field (cardinality 1..1).
* **BC‑7 (Domain is metadata).** "Domain" denotes only an informative family label grouping multiple contexts; it is not a kernel type and does not substitute for `U.BoundedContext` (E.10.D1).

### A.1.1:5 - Archetypal Grounding

The concept of a `U.BoundedContext` is universal and applies to both physical/operational domains and purely abstract/epistemic ones. Understanding these two archetypes clarifies its role as a fundamental FPF primitive.

| Archetype | Stewarding community | `U.BoundedContext` Example | Core Components Illustrated |
| :--- | :--- | :--- | :--- |
| **`U.System` Archetype** | A modern software engineering team | **`AgileProject:Phoenix`** | **`Glossary`**: Defines "Story Point," "Sprint," "Velocity." <br> **`Invariants`**: "Daily stand-up must not exceed 15 minutes." "A Story cannot move to 'Done' without a linked Test Case." <br> **`Roles`**: `ProductOwnerRole`, `ScrumMasterRole`, `DeveloperRole`. <br> **`Bridges`**: Maps `Velocity` metric to the `FinanceDept` context's `CostCenter:BudgetBurnRate`. |
| **`U.Episteme` Archetype** | A scientific community | **`Theory:SpecialRelativity`** | **`Glossary`**: Defines "Inertial Frame," "Lorentz Transformation," "Proper Time." <br> **`Invariants`**: "The speed of light in a vacuum is constant for all observers." "The laws of physics are the same in all inertial frames." <br> **`Roles`**: `Postulate#AxiomaticCoreRole`, `Experiment#EvidenceRole`. <br> **`Bridges`**: Maps its concept of "Spacetime" to the `GeneralRelativity` context's more complex concept of "Curved Spacetime." |

**Key takeaway from grounding:**
This illustrates that a `U.BoundedContext` is not an abstract container but a **holon with tangible content**. For the engineering team, it's their project's "operating system." For the scientific theory, it's the "intellectual constitution." In both cases, the context defines what is true, what is possible, and what words mean *locally*.

### A.1.1:6 - Bias-Annotation

This pattern is intentionally universal, but it can be misread through narrower lenses:

* **Software-centrism bias:** Readers may assume “bounded context” only applies to microservices/teams. *Mitigation:* the Episteme archetype is first-class; contexts apply equally to theories, standards, and scientific practices.
* **Boundary reification bias:** Authors may treat boundaries as “natural facts” rather than modelling choices. *Mitigation:* boundaries are declared for governance and clarity, and cross-context relations are handled via Bridges with explicit loss/fit.
* **English-label bias:** Examples often use English surface terms, which can hide multilingual drift. *Mitigation:* language/edition discipline in D.CTX governs when to split/merge contexts; multilingual labels are metadata when semantics are truly bound.

### A.1.1:7 - Conformance Checklist

To ensure `U.BoundedContext` is used consistently and rigorously, the following normative checks apply.

| ID | Requirement (Normative Predicate) | Purpose / Rationale |
| :--- | :--- | :--- |
| **CC-A1.1.1 (Holon Nature)** | A `U.BoundedContext` **MUST** be modeled as a `U.Holon` with a defined `U.Boundary`. | Reinforces that contexts are well-defined entities, not vague groupings. Enables reasoning about contexts themselves as systems. |
| **CC-A1.1.2 (Flat Context Map)** | A `U.BoundedContext` **MUST NOT** be modeled as inheriting from, containing, or being contained by another `U.BoundedContext`. Cross-context relations **MUST** be expressed only via explicit `Bridges` (E.10.D1 / E.10.U9). | Prevents semantic leakage and hidden globalism; keeps cross-context translation auditable and loss-aware. |
| **CC-A1.1.3 (Role Localization)** | Every `U.Role` **MUST** be defined within the `Roles` taxonomy of at least one `U.BoundedContext`. A "global role" is forbidden. | Ensures roles are never context-free; meaning remains local and checkable. |
| **CC-A1.1.4 (Invariant Scope)** | An invariant defined within a context **MUST** only apply to holons and processes operating *within* that context. | Prevents local rules from leaking into global reasoning; preserves modularity. |
| **CC-A1.1.5 (Bridge Explicitness)** | Any interaction or alignment between two `U.BoundedContext`s **MUST** be modeled as an explicit `Bridge` artifact. | Forbids implicit cross-context equivalences; makes dependencies visible and auditable. |
| **CC-A1.1.6 (RoleAssignment Context Binding)** | Every `U.RoleAssignment` **MUST** reference exactly one `U.BoundedContext` in its `context` field (cardinality 1..1). | Guarantees that each assignment is interpreted in one authoritative frame of meaning. |
| **CC-A1.1.7 (Domain family is informative)** | “Domain context” **MUST NOT** appear in normative prose; Domain labels **MAY** appear only as informative family metadata that groups multiple contexts (E.10.D1). | Prevents the domain/context conflation that breaks locality and auditability. |

### A.1.1:8 - Common Anti-Patterns and How to Avoid Them

These failure modes recur when applying `U.BoundedContext` in real programs and knowledge work.

| Anti-pattern | Symptom | Why it fails (force violated) | How to avoid / repair |
| :--- | :--- | :--- | :--- |
| **Domain-as-Context** | “Healthcare” or “Physics” is used where a specific context is required. | Violates Domain-family convenience vs precision; meaning stays ambiguous. | Use a specific context id (edition- and source-scoped), and keep the domain label as informative family metadata only. |
| **Implicit equivalence across contexts** | The same string in two contexts is treated as “obviously the same”. | Violates local coherence; creates silent semantic overwrites. | Publish an explicit Bridge with relation kind and loss/fit note (F.9 / E.10.U9). |
| **Context hierarchy / nesting** | Authors model “sub-contexts” as containment or is‑a between contexts. | Violates the flat context map discipline; leaks rules by inheritance. | Remove context-to-context containment; express relationships via Bridges only (E.10.D1). |
| **Time-as-Context** | “Design context” and “Runtime context” are created as separate contexts. | Violates evolvability and clarity; multiplies frames incorrectly. | Use TimeScope tags (`design`/`run`) on artifacts and sources; keep the semantic frame fixed (C‑7; D.CTX). |
| **Glossary-only context** | A context is defined by vocabulary but has no invariants or role taxonomy. | Violates governance intent; “local truth” remains implicit. | Add at least one invariant and a minimal local role taxonomy, even if initially coarse. |

### A.1.1:9 - Consequences

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Enables True Modularity:** By encapsulating models, FPF can support large, complex systems where different teams can work on their own bounded contexts in parallel with minimal interference. | **Modeling Overhead:** Requires architects to explicitly think about and define the boundaries of their models, which can feel like extra work initially. *Mitigation:* This upfront effort is a strategic investment that prevents the much higher cost of integration chaos and semantic ambiguity later in the project. |
| **Resolves Ambiguity and Paradox:** Provides a formal mechanism to manage synonyms, homonyms, and conflicting models (like the Pluto example). It transforms "it depends" into a precise, queryable structure. | **Bridge Maintenance:** As contexts evolve, the bridges between them must be maintained. *Mitigation:* FPF tooling should support "link integrity" checks to automatically flag broken or outdated bridges. |
| **Makes Rules Explicit:** The `Invariants` component of a context makes the local rules and invariants for a project or theory explicit, documented, and auditable. | - |
| **Foundation for Scalable Autonomy:** In multi-agent systems, each agent can operate within its own bounded context, communicating with others through well-defined bridges. This is a prerequisite for building robust, decentralized systems. | - |

### A.1.1:10 - Rationale

**Lineage and fit with Domain‑Driven Design (DDD).**  
FPF generalizes the proven DDD idea of a **Bounded Context** from software into a universal modeling primitive:

| DDD concept | FPF counterpart | Generalization in FPF |
| :--- | :--- | :--- |
| Bounded Context | **U.BoundedContext** (a holon) | Used for systems **and** knowledge; first‑class object with explicit Glossary, Invariants, local Roles, Bridges. |
| Ubiquitous Language | **Glossary** of the context | The shared vocabulary is an explicit component, not just narrative. |
| Context Map | **Bridges/Alignment** between contexts | Cross‑context relations are modeled explicitly rather than assumed globally. |

**Why this matters here.**  
`U.BoundedContext` gives `U.RoleAssignment` (A.2.1) its footing: role meanings are **local by design**, conflicts are checked **inside** the same context, and differences **across** contexts are handled by **explicit Bridges** instead of “global truth.”

The introduction of `U.BoundedContext` as a first-class holon is a direct implementation of several core FPF principles and is strongly supported by contemporary practice.

*   **Philosophical Grounding:** The idea that meaning is always local and context-dependent is a cornerstone of late 20th-century philosophy of language (e.g., Wittgenstein's "language-games"). FPF operationalizes this insight.
*   **Domain-Driven Design (DDD):** The concept is a direct borrowing and generalization from Eric Evans' seminal work on DDD, where the Bounded Context is the central strategic pattern for managing complexity in large-scale software. Its success over the past two decades in the software industry provides powerful empirical validation for its utility. FPF elevates it from a software design pattern to a universal ontological primitive.
*   **Architectural Necessity:** For FPF to fulfill its promise of being an "operating system for thought," it needs a mechanism analogous to an OS's "process separation." A `U.BoundedContext` is precisely that: a protected "memory space" for a model, preventing different models from corrupting each other.
*   **Enabler for Key Patterns:** The `Contextual Role Assignment` pattern (A.2.1) would be incoherent without a formal definition of "Context." This pattern provides that necessary foundation, making the entire role-based architecture sound.

In essence, `U.BoundedContext` is the architectural pattern that allows FPF to be both **universal** in its core principles and **specific** and **pluralistic** in its applications. It is the mechanism that tames complexity and makes large-scale, multi-paradigm modeling possible.

### A.1.1:11 - SoTA-Echoing (post-2015 practice alignment)

The `U.BoundedContext` concept aligns strongly with contemporary (post‑2015) practice in software architecture, socio-technical design, and knowledge/provenance disciplines. Where FPF differs, it does so to preserve kernel universality, explicit loss-aware translation, and auditability.

| Claim (A.1.1 need) | SoTA practice (post‑2015) | Primary source (post‑2015) | Alignment with A.1.1 | Adoption status |
| :--- | :--- | :--- | :--- | :--- |
| Meaning boundaries must be explicit to scale development. | Modern microservice architecture stresses clear service boundaries and local reasoning to keep systems evolvable. | Newman (2021), *Building Microservices* (2nd ed.). | A.1.1 adopts the boundary-first stance but generalizes it from “service boundaries” to a universal semantic holon with explicit local invariants and roles. | **Adopt/Adapt.** Adopt boundary discipline; adapt by making the semantic frame a first-class kernel object, not only a team convention. |
| Organizational boundaries and cognitive load shape semantic boundaries. | Socio-technical architecture practice encourages team-aligned boundaries and explicit interaction modes to prevent cognitive overload. | Skelton & Pais (2019), *Team Topologies*. | A.1.1 aligns by treating a context as governable by a stewarding community, but requires explicit Bridges when knowledge crosses boundaries (rather than relying on tacit coordination). | **Adopt.** Directly supports local autonomy; tighten with explicit cross-context translation artifacts. |
| Cross-domain data integration needs explicit contracts, not implicit “one truth”. | Data Mesh emphasizes domain-oriented data products and explicit interoperability contracts across domains. | Dehghani (2022), *Data Mesh* (book form of the 2019–2021 program). | A.1.1 matches the “data product boundary” move, but insists that interoperability is expressed as explicit Bridges with loss/fit notes, preserving pluralism instead of collapsing it. | **Adapt.** Adopt the decentralization intuition; adapt by requiring explicit semantic alignment artifacts rather than assuming shared enterprise semantics. |
| Knowledge and artifacts must carry machine-actionable semantics and provenance. | FAIR and modern research-object packaging push for explicit metadata, provenance, and reuse conditions. | Wilkinson et al. (2016), FAIR Principles; RO‑Crate community specs (2019→). | A.1.1 supports this by making local meaning explicit (Glossary + Invariants) and making cross-context translation explicit (Bridges), enabling auditable reuse without pretending to globalize semantics. | **Adopt/Adapt.** Adopt provenance and reuse intent; adapt by separating semantic frame (Context) from carriers and by making loss explicit on crossings. |

### A.1.1:12 - Relations

*   **Constitutes:** The foundational "semantic space" for patterns like `A.2 Role Taxonomy` and `A.13 The Agential Role`.
*   **Builds on:** `A.1 Holonic Foundation`, as a `U.BoundedContext` is itself a `U.Holon`.
*   **Constrained by:** `E.10.D1 D.CTX`, which fixes the lexical discipline for “Context”, forbids context hierarchies, and makes Domain family informative.
*   **Interacts with:**
    *   `Norm-CAL`: A context's `Invariants` are typically expressed as `U.ConstraintRule`s.
    *   `Lang-CHR`: A context's `Glossary` is a collection of `U.Lexeme`s.
    *   `Decsn-CAL`: Decisions and objectives are often scoped to a specific context.
    *   `F.9 Alignment & Bridge`: the canonical locus of cross-context relations and loss policies.
*   **Enables:** The resolution of conflicts as modeled in `D.3 Holonic Conflict Topology`, by showing that many conflicts are context-dependent.
    
### A.1.1:End


## A.2 - Role Taxonomy
> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative

*A holon’s essence tells us **what it is**; its roles tell us **what it is being, here and now**.*

### A.2:1 - Problem frame

Pattern A.1 established the **substantial** characteristic of the core (`Entity → Holon → {System, Episteme, …}`), cleanly separating identity from structure and aggregation. The present pattern introduces the **functional** characteristic: how a holon participates in purposes **within a bounded context** and for some interval. This extends the early sketch of A.2 and tightens its alignment with A.7 (Strict Distinction): roles are *not* parts and *not* behaviours; they are contextual **masks** that a holon wears while behaviours are handled by **Method**/**Work**. 

### A.2:2 - Problem

Without an explicit role calculus:

1. **Type explosion & conflation.** Each new purpose breeds a new “subtype” (`PumpAsCoolingLoop`, `PumpAsFuelLoop`, …), violating parsimony and fusing substance with function.
2. **Agency opacity.** It becomes unclear whether *any* system may act as a transformer/agent, or only pre-declared special kinds.
3. **Epistemic blindness.** Knowledge artefacts (papers, proofs) cannot be given roles, blocking modelling of citation, evidence, or design-time justification.

### A.2:3 - Forces

| Force                                | Tension                                                              |   |
| ------------------------------------ | -------------------------------------------------------------------- | - |
| **Identity vs Function**             | A holon’s make‑up ↔ its transient, contextual purpose.               |   |
| **Static vs Dynamic classification** | Fixed type lattice ↔ late‑binding of new roles.                      |   |
| **Universality vs Familiarity**      | One mechanism for pumps **and** papers ↔ domain‑specific role names. |   |
| **Simplicity vs Expressiveness**     | Minimal primitives ↔ multi‑role, multi‑holder scenarios.             |   |

### A.2:4 - Solution

We elevate **Role** to a first‑class semantic construct: a context‑bound *mask* (capability/obligation schema) worn by a holon. **Behaviour** and **resource deltas** live in **Method**/**Work**, not in the role itself.

#### A.2:4.1 - S‑level definitions (normative)

* **`U.Role`** — a **context-bound** capability/obligation schema that a holon **may bear (play)** for a time interval. A role has **no structural parts** (it does not participate in A.14 `partOf`) and **no resource deltas** of its own. Role refinement/bundling is expressed via in‑Context relations (`≤`, `⊥`, `⊗`) rather than mereology. *(A7 guard)*
* **`U.RoleAssignment`** — a first-class assignment record recording that a holon **bears (plays)** a role **in** a bounded context over an optional **Window**. Keep the signature aligned with **A.2.1 Role Assignment Standard**; governance metadata (authority/justification/provenance) is captured via `U.RoleAssigning` and the evidence graph (A.10).

```
U.RoleAssignment {
  holder        : U.Holon,
  role          : U.Role,
  context       : U.BoundedContext,
  window? : U.Window
  justification?: U.Episteme,  // why (standard, SOP, evidence)
  provenance?   : U.Method     // how assignment/verification was done (NOT the role's bound method set)
}
```

Short form (readable): `Holder#Role:Context@Window`.

> **Why a first-class assignment record?** It keeps identity (holon), function (role), context (semantics), and time (run-window) separate yet linked, preventing the substance/function conflation identified above. The early `playsRoleOf(Holon, Role, span)` relation in the draft is subsumed by `U.RoleAssignment` and extended with **Context** (and optional governance fields).

#### A.2:4.2 - Temporal & behavioural alignment

* **Method (intension) vs Work (occurrence).** A `U.Method` is a **design‑time, order‑sensitive capability**: what can be enacted, under which preconditions/invariants, with what admissibility/acceptance gates. A `U.Work` is the **dated, spatiotemporally bounded enactment** of such behaviour by a system bearing a role (A.15.1).
* **MethodDescription is representation (viewpoint), not “the method itself”.** `U.MethodDescription` is an `U.Episteme` that represents a method under an explicit **viewpoint**. Step‑graphs/scripts/workflows are one common viewpoint, but not universal. Other valid viewpoints include state‑machines, dynamical/solver/controller models, lab protocols, and quantum circuits/channels. A method itself **need not** admit a step decomposition; only a given description might.
* **Executable chain (who / what / how / when).** A **behavioural Role** is eligible/authorized for one or more Methods (design‑time, Context‑local). A Work is `isExecutionOf` a **specific MethodDescription version** (run‑time) and cites `performedBy = U.RoleAssignment`. Together, these anchors answer “what happened, by which method, under which role” without collapsing design‑time into run‑time.
* **Resource accounting lives in Work.** Only `U.Work` carries resource deltas (feeds Γ\_work); Roles/Methods/MethodDescriptions do not.

> **Lexical note (A.6.P trigger).** In the Role–Method–Work cluster, `bindsMethod` is a **technical token** meaning “Context‑local eligibility/authorization of a Role for a Method”. Do not use plain “bind/rebind” as umbrella prose for editing relationships; when describing edits, prefer explicit change classes (declare/withdraw/retarget/revise/rescope/retime/refreshWitnesses).

#### A.2:4.3 - Admissibility constraints (concept-level; non-deontic).

1. **Locality.** `role ∈ Roles(context)`. Outside its context, a role’s meaning is undefined.
2. **Structural‑mereology firewall.** No Role (nor Method/MethodDescription) may appear as a node in any A.14 `partOf` chain; holarchies are for substantial holons only. Role refinement/bundling (`≤`, `⊗`) and method relations (refinement, factorization, step/phase views) are **not** `partOf` and MUST NOT be rewritten into structural parthood.
3. **Multiplicity.** A holder may **bear** multiple roles concurrently; a role may be **borne** by many holders—subject to each context’s compatibility rules.
4. **Time anchoring.** `window` (if present) is non-empty and finite for run‑time claims; open‑ended assignments are allowed but must be traceably open‑ended from an assignment time (A.2.1). Design‑time bindings are timeless but **descriptions are versioned** via `U.MethodDescription` identity.
5. **Behavioural coherence.** For any `U.Work` window, the performer’s cited RoleAssignment and the executed MethodDescription must align in the **same Context**: `work.performedBy = RA`, `work.isExecutionOf = MD`, and `RA.role` is eligible/authorized for the Method represented by `MD`. *(No hidden role swaps; no implicit method drift.)*

#### A.2:4.4 - Taxonomic frame (within a context)

Within each `U.BoundedContext`, role names are organised as a **partial order** (refinements) plus an **incompatibility** relation (mutually exclusive roles). Typical **substrate‑neutral** anchors:

| Kernel Role       | Intent                                | System archetype              | Episteme archetype                       |   |
| ----------------- | ------------------------------------- | ----------------------------- | ---------------------------------------- | - |
| `TransformerRole` | Changes other holons via Method/Work. | Robot arm assembling casings. | Prover constructing a new lemma.         |   |
| `ObserverRole`    | Collects evidence / metrics.          | Sensor array on a test‑rig.   | Reviewer annotating an article.          |   |
| `SupervisorRole`  | Governs subordinate holons.           | PLC orchestrating a line.     | Meta‑analysis curator combining studies. |   |

> Domains refine these anchors: e.g., `CoolingCirculatorRole`, `CitationSourceRole`, `LemmaRole`.

### A.2:5 - Archetypal Grounding (Tell–Show–Show: System / Episteme)

**Tell.** A single holon can be the *same bearer* across time while taking on different, context‑bound roles. A role is a *mask* (capability/obligation schema) that explains *what it is being* in a given `U.BoundedContext`; behavioural facts and resource deltas remain in `U.Method` / `U.Work`.

**Show.**

**System case — Cooling loop**
`PumpUnit#3#HydraulicPump:Plant‑A@2025‑08‑08..open`
`HydraulicPumpRole ↦bindsMethod↦ CentrifugalPumpingMethod` (design‑time, Context‑local eligibility)
`CentrifugalPumpingMethod ↦isDescribedBy↦ centrifugal_pump_curve.ld@v7` (MethodDescription viewpoint; step‑graph OR dynamics, as appropriate)
`run‑2025‑08‑08 isExecutionOf centrifugal_pump_curve.ld@v7; performedBy PumpUnit#3#HydraulicPump:Plant‑A@2025‑08‑08..2025‑08‑08` (run‑time Work)
*(Behavioural/resource facts live in Work; method semantics live in the referenced MethodDescription viewpoint.)*

**Episteme case — Standard in design**
`RFC‑9110.pdf#ProtocolStandard:WorldWideWeb` justifies `MethodDescription` selection; the **system** bearing `TransformerRole` is the design service that executed the selection work. The episteme did **not** act.

**Collective vs set (safety pitfall)**
A **set** `{Alice, Bob, 3.14}` has no behaviour; a **team** is a **system** with boundary, coordination **Method**, and supervision **Work**; only the latter can bear agentic roles.

### A.2:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** (A‑cluster).

* **Architecture bias (Arch):** treating roles as structural parts can smuggle function into mereology and break holarchies.  
  *Mitigation:* keep `partOf` chains role‑free; roles are not constituents (see CC‑A2.1).
* **Onto/Epist bias (Onto/Epist):** anthropomorphising epistemes collapses evidence into agency.  
  *Mitigation:* epistemes can justify/authorize; only systems perform methods and work (CC‑A2.2).
* **Pragmatic bias (Prag):** over‑contextualising can fragment reuse and create naming drift.  
  *Mitigation:* require explicit `:Context` binding and explicit bridges instead of silent equivalence (CC‑A2.4).
* **Didactic bias (Did):** metaphors (“mask”) may be misread as informal.  
  *Mitigation:* bind obligations to CC items; avoid imperative prose outside CC.

### A.2:7 - Authoring guidance (for engineers and leads)

* **Name roles for intent, not mechanics.** Prefer `CoolingCirculatorRole` over `ChannelFluidWithCentrifugalProfile`.
* **Pin the context early.** If two teams disagree, split contexts and (optionally) define an alignment bridge; do not over‑generalise the role.
* **Document the enactment chain.** For any operational claim, be ready to point to: `RoleAssigning → RoleAssignment → (Role ↦bindsMethod↦ Method) ↔ MethodDescription → Work`. (Readers’ dictionary: *workflow/script/state‑machine/dynamical model/quantum circuit → MethodDescription; run/job/operation → Work.*)

### A.2:8 - Conformance Checklist (CC‑A2.\*)

|                      ID | Requirement                                                                                                                                                                                                                                                                          | Practical test (manager‑oriented)                                                                                                                                                             |
| ----------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|             **CC‑A2.1** | A **Role** SHALL NOT be a mereological part of any holon; roles are never constituents of holarchies.                                                                                                                                                                                | If a diagram shows `Role →(part‑of)→ Holon`, the model **fails**. Replace the edge with `playsRoleOf(Holon, Role, span)` (A.14 governs parts).                                                |
|             **CC‑A2.2** | Only a **System** can bear **behavioural** roles (e.g., `TransformerRole`, `AgentialRole`) and thus bind **Method**/**Work**; an **Episteme** MAY bear **non‑behavioural** roles (e.g., `ReferenceRole`, `ConstraintSourceRole`) only.                                               | Lint the model: any `U.Episteme` that `bindsMethod` or is a `performedBy` target **fails**; move behaviour to a system bearing the role and act on episteme **carriers** (A.7, A.12, A.15).   |
|             **CC‑A2.3** | Every **behavioural Role** that is used for Work SHALL `bindsMethod ≥ 1`; behavioural roles with no bound method are **abstract** placeholders and non‑executable.                                                                                                                     | If a behavioural role participates in `Work` without some `Method ⟷ MethodDescription` chain, flag “unbound role” and add a binding (A.15).                                                   |
|             **CC‑A2.4** | Every **role reference** in normative text SHALL be **context‑indexed** by a declared **Bounded Context** (local to the pattern or glossary). Local shorthand **“Transformer”** is permitted only if the pattern’s Glossary **re‑binds** it to “**System bearing TransformerRole**”. | If prose says “Transformer updates the spec”, the pattern MUST define the local alias and its target; otherwise rewrite to the canonical long form (E.10, A.7).                               |
|             **CC‑A2.5** | Each `U.RoleAssignment` SHALL carry an explicit `window` **or** be traceably open‑ended from an assignment time (e.g., via `U.RoleAssigning`). Open intervals are allowed but must be explicit. | Search for RoleAssignments with neither `window` nor a traceable assignment time; add `@t₀..t₁` (or open bound) and/or an issuing RoleAssigning Work. |
|             **CC‑A2.6** | If two roles are declared **incompatible inside the same context**, a bearer SHALL NOT hold them over **overlapping** spans.                                                                                                                                                         | Check the context’s role‑compatibility grid; if overlaps exist, either split the Work by `PhaseOf` or change staffing (A.14; B.1.4/Γ\_time).                                                  |
|             **CC‑A2.7** | For any **Work** item, `performedBy` MUST reference the **concrete RoleAssignment** of the performer, and its window MUST cover the Work’s window. | Assert `performedBy(Work) = RA` and `RA.window ⊇ window(Work)`; split Work or update assignments if the performer changes mid‑window (A.2.1, A.15). |
|             **CC‑A2.8** | Every **Method** bound to a role SHALL be `isDescribedBy ≥ 1` **MethodDescription** (`U.Episteme`) and every **Work** SHALL be `isExecutionOf` exactly one **MethodDescription** version.                                                                                                          | If a Work lacks `isExecutionOf`, or a Method lacks `MethodDescription`, the audit fails (A.15; A.10 evidencing hook).                                                                                |
|            **CC‑A2.8b** | When a claim relies on **step/phase/serial/parallel** semantics, the referenced **MethodDescription** SHALL declare an appropriate viewpoint and its ordering/coordination rules; do not infer “steps” from `U.Method` by default.                                                    | If prose says “step 3”, “submethod”, or “phase”, but the cited MethodDescription is not a workflow/script/step‑graph viewpoint (or lacks ordering rules), flag it; rewrite in the declared viewpoint or mint an additional view. |
|             **CC‑A2.9** | **Evidence** for claims about roles and execution MUST anchor to **symbol carriers** (SCR/RSCR); self‑evidence is forbidden.                                                                                                                                                         | A role effectiveness claim without SCR/RSCR or with cyclic provenance fails (A.10).                                                                                                           |
|            **CC‑A2.10** | When a Role assignment implies **order** or **temporal** structure, the pattern SHALL defer to **Γ\_ctx**/**Γ\_time** rather than overloading role edges.                                                                                                                               | If argument order matters, use Γ\_ctx folds and record OrderSpec; version/evolution goes via Γ\_time (B.1.3 §4.5).                                                                            |
|            **CC‑A2.11** | Use of legacy nouns “creator/actor/agent” in Core text is prohibited unless they are explicitly typed as **roles** with bearers; the term **“Transformer”** is a local alias, **not** a type.                                                                                        | Scan for bare nouns; replace with “system bearing TransformerRole” or define an alias in the Glossary (A.7 canonical rewrites; E.10 registers).                                               |
| **CC‑A2.12 (advisory)** | A reified **RoleAssigning** object SHOULD capture `context`, `window`, optional `authority`, `justification (U.Episteme)`, and `provenance (U.Method)`. | Recommended for governance‑heavy domains; it improves explainability without changing Core semantics. |

> **Note.** CC‑A2.2 aligns with **A.7 Role‑domain guards** (“behavioural roles’ domain = system; epistemes bear non‑behavioural roles only”).

### A.2:9 - Common Anti-Patterns and How to Avoid Them

1. **“Transformer as system subtype.”**
   ✗ *“`U.TransformerSystem` builds pumps.”*
   ✓ *“`RobotArm R‑45#Transformer:Plant‑A` executed Work W.”* (Role is a mask; behaviour is Method/Work.)

2. **“Role as part.”**
   ✗ *“The pump’s role is one of its components.”*
   ✓ Roles are **never** parts; components are substantial. Keep all `partOf` chains role‑free.

3. **“Episteme acts by itself.”**
   ✗ *“The PDF enforced the SOP.”*
   ✓ An **episteme** can hold roles like `ProtocolStandard` **in context**, but only a **system** performs the Method/Work that uses it.

4. **“Context leakage.”**
   ✗ *“Pluto is Planet and DwarfPlanet.”* (in one tacit space)
   ✓ *“`Pluto#Planet:Early20thCenturyAstronomy`; `Pluto#DwarfPlanet:IAU_2006_Definition`.”* No contradiction—different bounded contexts. (Illustrative of `U.RoleAssignment` semantics carried forward from the A.2.1.)

5. **“Method = workflow (step list) by default.”**
   ✗ *“The method is the ordered list of steps 1..n.”*
   ✓ A **Method** is a design‑time capability; “steps” (or their absence) are a property of a **MethodDescription viewpoint**. A Work executes a specific MethodDescription; use a workflow/script view when step semantics matter, and use other views (dynamics/solver/circuit/channel) when steps are not meaningful.


### A.2:10 - Consequences

| Benefit                     | Why it matters                                                                                                       | Trade‑off / Mitigation                                                                       |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Category‑error immunity** | Clear firewall between **identity** (holarchies) and **function** (roles) prevents mixing “parts” with “masks”.      | Slight modelling overhead; templates provide checklists (A.7, A.14).                         |
| **Operational clarity**     | Who did what, when, under which mask, and **by which MethodDescription** becomes audit‑ready (RoleAssignment + `performedBy` + `isExecutionOf` + method‑binding). | Requires spans on Role assignments; mitigated by default “open‑ended” spans in drafts.       |
| **Epistemic hygiene**       | Knowledge holons contribute as **evidence** or **constraints**, never as doers.                                      | Authors must rewrite anthropomorphic prose; canonical rewrites help.                         |
| **Cross-context pluralism** | Same bearer can hold different roles across contexts without contradiction; differences are explicit in the assignment. | Requires declaring the **bounded context**; E.10 eases the ceremony with registers/aliases.  |
| **Γ‑coherence**             | Order/time/aggregation stay in Γ‑operators, not overloaded into “role" edges.                                        | Authors learn when to call Γ\_ctx/Γ\_time; the Part B on‑ramp is short.                      |

### A.2:11 - Rationale (post‑2015 cross‑domain corroboration)

*Why insist on roles as contextual masks and externalised transformers?*

1. **Constructor Theory (2015–2022).** Post‑2015 work by Deutsch & Marletto re‑centres physics on **possible tasks and constructors** rather than objects, mirroring FPF’s **TransformerRole**: behaviour is attached to “who can realise a task,” not to substance per se. Our separation of **SubstantialHolon** vs **Role** and the insistence on **external** transformers directly echo this shift. *(Conceptual alignment noted in A.2 Solution and A.12 intent.)* 
2. **Layered Control Architectures (Matni–Ames–Doyle, 2024).** The modern control stack cleanly **externalises** regulators and planners relative to plants. FPF’s obligatory “system bearing TransformerRole” (A.7, A.12) is isomorphic to that separation, keeping supervision and actuation **outside** the controlled holon. 
3. **Active‑Inference / Agency spectrum (2017–2023).** Contemporary models treat agency as **graded** and **contextual** (percept‑act loops tuned by free‑energy bounds). A.13 adopts exactly this: **AgentialRole** is a role worn by a holon, with graded measurements via **Agency‑CHR**, not a static type.
4. **Basal Cognition & multi‑scale organisation (2019–2024).** Fields & Levin argue for **cross‑scale** control and information flows; FPF encodes this via Γ‑flavours and the **Meta‑Holon Transition** triggers, ensuring Role assignments compose across scales without collapsing identity into function.
5. **Knowledge ecosystems & safety cases (2018–2025).** Modern assurance relies on **traceable evidence** and conservative integration (no “truth averaging”): our A.10 anchors (SCR/RSCR) and Γ\_epist’s **weakest‑link** fold implement that discipline and forbid self‑evidence. 

> Summing up: post‑2015 science and engineering converge on **roles as contextual capabilities**, **externalised control**, and **traceable evidence**. A.2 codifies these insights in a substrate‑neutral way, keeping the Core small yet powerful.

### A.2:12 - SoTA-Echoing (post‑2015 alignment, informative)

| Claim (A.2 need) | SoTA practice (post‑2015) | Primary source (post‑2015) | Alignment with A.2 | Adoption status |
| --- | --- | --- | --- | --- |
| Roles are context‑dependent, anti‑rigid descriptors rather than structural parts. | Conceptual modeling distinguishes substantial types from role types; roles depend on context/relational situations. | Guizzardi (2019), *Ontological Foundations for Conceptual Modeling*; recent OntoUML/UFO literature. | Maps to `U.Role` as context‑bound schema; keeps `partOf` free of roles. | **Adopt.** |
| Meaning boundaries must be explicit; reuse across boundaries must be declared, not assumed. | Modern DDD and socio‑technical architecture emphasise explicit bounded contexts and explicit translation/alignment. | Vernon (2016), *Domain‑Driven Design Distilled*; Newman (2021), *Building Microservices*. | Matches `role ∈ Roles(context)` and CC‑A2.4 context binding + explicit bridge discipline. | **Adopt/Adapt.** Adopt boundaries; adapt reuse via FPF Bridges + CL. |
| Agency should not be attributed to artifacts; treat evidence/provenance as first‑class. | Safety/assurance and governance treat documents as evidence and constraints; provenance is required for claims. | ISO 26262:2018; NIST SP 800‑53 Rev. 5 (2020). | Supports “episteme as justification” and CC‑A2.2/CC‑A2.9 evidence binding. | **Adopt.** |
| “Agency” is graded and mediated by active systems + policies. | Cognitive/agentic modeling treats agency as spectrum, mediated by control loops and policies. | Friston et al. (2017), Active Inference; basal cognition surveys (2018+). | Supports separating role labels from behavioural work; aligns with A.13/A.15. | **Adopt (with scope).** Keep obligations in CC. |

> **Note.** Prefer citing a maintained SoTA synthesis pack for roles/contexts if your Context has one.

### A.2:13 - Relations

* **Builds on:**
