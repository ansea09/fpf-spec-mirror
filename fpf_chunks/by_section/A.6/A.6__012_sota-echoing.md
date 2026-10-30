---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack: Classify and Place Boundary Claims"
section_id: "A.6:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__012_sota-echoing.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.6 — Signature Stack: Classify and Place Boundary Claims"
  - "A.6:11 — SoTA-Echoing"
line_start: 14157
line_end: 14180
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.8.PER"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.5"
  - "A.6.6"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
keywords:
  - "Confuses deontics with mathematical admissibility"
  - "Rewrite as declarative predicate"
  - "Work versus non-Work effect"
  - "acceptance"
  - "actual occurrence"
  - "and evidence"
  - "atomic L/A/D/E claims"
  - "delivery"
  - "in invariants"
  - "publication face"
  - "reference predicates by ID or canonical location from CC when needed"
  - "separate result"
  - "signature and mechanism declarations"
  - "six-way authority-word branch"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:11 - SoTA-Echoing

> **Informative.** The sources below supply distinct techniques for declaration, substitution, interaction and observation. The L/A/D/E organization is FPF's authoring choice for keeping their boundary claims and dependencies recoverable. Historical foundations retain their stated scope; current documentation is identified where used.

* **Algebraic effects and handlers / effect systems.** [Leijen (2017)](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/algeff.pdf) and [Hillerström and Lindley (2018)](https://www.pure.ed.ac.uk/ws/files/76099718/shallow_effect_handlers.pdf) distinguish declared operations, effect typing and handler semantics. A common interface permits different handlers, so behavior preservation needs the operation's semantic contract. [OCaml 5.4, §12.24](https://ocaml.org/manual/5.4/effects.html) also distinguishes runtime protocol enforcement from static effect safety. A.6 uses the declaration/realization distinction; provider duties and SLA claims require their separate FPF grounds.

* **Contracts and behavioral substitution.** [Meyer, *Applying “Design by Contract”* (1992)](https://www.kth.se/social/files/59526bfb56be5b4f17000807/meyer-92-contracts.pdf), pp. 40–42 and 46–49, develops preconditions, postconditions, invariants and optional runtime monitoring. [Liskov and Wing, *A Behavioral Notion of Subtyping* (1994)](https://www.cs.columbia.edu/~wing/publications/LiskovWing94.pdf), §§1–2 and 5.2, adds preservation of invariant and history properties under a stated abstraction. These historical foundations supply concrete preservation questions for §4.7. Their formal conclusions apply under their computational assumptions; an API replacement also needs its actual interaction and receiving-use conditions.

* **Session types for protocol boundaries.** [Scalas and Yoshida (2019)](https://www.doc.ic.ac.uk/~ascalas/papers/scalas-yoshida-popl19.pdf) connects global protocols, participant types and process properties under explicit conditions. [Hou, Yoshida and Kuhn (2026)](https://mrg.cs.ox.ac.uk/publications/less_is_more_revisited_association_with_global_protocols_and_multiparty_sessions/main.pdf) revisits the association and liveness reasoning. This helps compare changed message order, choice and retry behavior. Safety, deadlock-freedom and liveness have different conditions; a protocol theorem supplies only its stated property. A.6 separately locates admission, duties and actual-result claims.

* **Categorical optics, lenses, and bidirectional transformations.** Lenses supply useful construction expressions with coherence laws. FPF uses that lesson only for explicit A.6.3 construction or C.29 representation: a projection expression, publication face, and `U.View` remain different objects, while any cross-context reuse stays explicit.

* **Views and viewpoints.** [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html), particularly its concepts in §5, distinguishes an architecture, its description, viewpoints, views and correspondences. That supports organizing an API description around concerns and relating its parts. FPF's particular stack and face rules are additional choices. Query and projection operations can construct candidate epistemes and make omissions inspectable; E.17.0 supplies the separate FPF test against the exact viewpoint episteme.

* **DDD bounded contexts and microservice contract-language practice.** Architecture practice keeps meaning local and makes crossings explicit. A.6’s stack and L/A/D/E claim-classification discipline provide a precise placement scheme for what belongs to the context boundary claim set, what belongs at the entry gate, what belongs to governance duties, and what belongs to observability evidence.

* **Observability as evidence discipline.** [OpenTelemetry Trace API](https://opentelemetry.io/docs/specs/otel/trace/api/) and [Trace SDK](https://opentelemetry.io/docs/specs/otel/trace/sdk/) distinguish span identity, recording and export; sampling or dropped records can limit available observations. The [Metrics Data Model](https://opentelemetry.io/docs/specs/otel/metrics/data-model/) makes aggregation explicit. These are current specification contributions, not proof of a particular payment result. [Google SRE, *Monitoring Distributed Systems* (2016)](https://sre.google/sre-book/monitoring-distributed-systems/) supplies a historical practical distinction between a successful transport response and correct service content. A.10 connects the chosen observations to the exact claim and use; retention and exposure prescriptions belong to their own D claims.

* **Zero Trust, dynamic authorization, and policy as code.** Authorization practice separates policy, API, or schema text from a decision over subject, requested policy operation or work class, affected resource or work target, context, policy or gate version, decision source, and evidence. [Cedar's authorization semantics](https://docs.cedarpolicy.com/auth/authorization.html) separates a request's principal, action, resource and context from policies and entity data, policy evaluation, and the combined `Allow` or `Deny` response with diagnostics. The historical architecture in [NIST SP 800-207 (2020), §2.1 and §3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) also distinguishes the policy decision from administration and enforcement, using policy and observable state as inputs. An institutional grant used by an FPF gate retains its own obtaining conditions. A.6 keeps the corresponding L/A/D/E claims connected; use A.15.4 when appearance leaves an action prerequisite unrecovered, and A.15 for enactment alignment.

* **Relation-based authorization and consistent evaluation.** The historical Zanzibar design, described by [Pang et al. (2019), §§2.1–2.3 and 2.4.4](https://www.usenix.org/system/files/atc19-pang.pdf), combines relation tuples with configured rules to determine effective permissions. Its access checks use a consistent snapshot constrained by the relevant content version. This supplies a concrete reason to recover the decision's inputs and currentness conditions when reusing an authorization result after an access relation or protected content changes. The relation definitions, stored tuples, evaluation and returned decision make different contributions to that judgement.

* **Markov blankets and active inference as probabilistic boundary views only after restoration.** Markov-blanket thinking can help pick observables and diagnose boundary-condition failures, but the source phrase must be restored before it carries an A.6 boundary claim. It may name accepted local Markov dynamics, a mathematical or probabilistic lens, a holon delimitation or crossing relation, an interface, an interface module, a physical component, a boundary description, or an agency-threshold claim. A.6 uses the phrase only after the boundary claim set is recovered; it does not replace deontics, invariants, admissibility gates, or the subject pattern of the physical or mathematical claim.

