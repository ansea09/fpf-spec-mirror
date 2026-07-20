---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:5"
section_title: "Quadrant specifications"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__007_quadrant-specifications.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:5 — Quadrant specifications"
line_start: 9595
line_end: 9699
dependencies:
  - "A.10"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26.1"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.8"
  - "F.18"
  - "U.Commitment"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.Signature"
  - "U.SpeechAct"
keywords:
  - "(MUST"
  - "(ii) claim that evidence carriers exist (that is E-)"
  - "(ii) encode runtime entry predicates (those are A-)"
  - "(they are not obligations"
  - "Keeps modalities separated and audit-ready"
  - "L/A/D/E claim classification"
  - "MAY"
  - "MUST"
  - "MUST NOT"
  - "MUST NOT hide a gate predicate (that is A-)"
  - "SHALL"
  - "SHOULD"
  - "SHOULD NOT"
  - "The key words MUST"
  - "accountable commitments"
  - "admissible use"
  - "alone select neither branch"
  - "and MAY"
  - "and MUST NOT cite D-*"
  - "and SHALL are to be interpreted as in RFC 2119/8174. Lower-case must"
  - "and should in explanatory prose is descriptive"
  - "as if it were an agent obligation"
  - "as if it were an agent obligation. (It is a gate predicate"
  - "as operators"
  - "atomic claims"
  - "boundary norm square"
  - "claim IDs"
  - "laws vs entry predicates vs deontic results vs evidence"
  - "may"
  - "non-admissible use"
  - "not a duty.)"
  - "not normative"
  - "or (iii) assert evidence existence or measurement outcomes (those are E-*)"
  - "or (iii) assign responsibility or enforcement (that is D-*)"
  - "or MAY) as operators inside the law or definition itself"
  - "strong or weak permission results"
  - "they describe adjudicable effects and evidence)"
  - "triangle decomposition"
  - "“commits to”)"
  - "“is admissible”"
  - "“is blocked”"
  - "”) used as operators inside L- or A- predicates (should be D- that references L-/A-)"
---

### A.6.B:5 — Quadrant specifications

This section is the normative “API” of the square: what each quadrant is for, how it is written, and what it must not contain.

#### A.6.B:5.1 — Quadrant L: Laws & Definitions

**Intent.** State truth‑conditional content: definitions, invariants, typing and well-formedness constraints, equational laws.

**Adjudication.** In‑description: can be checked by inspection, proof, type validation, or model reasoning.

**Canonical form.** `Definition:` / `Invariant:` / predicate‑style constraints using “is / iff / for all”.

**Prohibitions.**

* An `L-*` statement **MUST NOT** contain RFC deontic keywords (**MUST, SHALL, SHOULD, or MAY**) as operators inside the law or definition itself.
* An `L-*` statement **MUST NOT** encode runtime gate predicates (those are `A-*`).
* An `L-*` statement **MUST NOT** assert evidence availability or measurement outcomes (those are `E-*`).

**A.7 EntityOfConcern binding.** `L-*` claims are **Descriptions**: they specify semantics of the signature or mechanism description, not work.

**Typical dependence.** `A-*` and `E-*` claims may reference `L-*` IDs for vocabulary, metric definitions, and invariants needed for interpretation.

#### A.6.B:5.2 — Quadrant A: Admissibility & Gates

**Intent.** Specify when a mechanism application is admissible: runtime entry predicates, validity gates, and applicability checks that require context or execution environment. An `A-*` predicate may test a current grant or conflict result as one condition, but it does not institute permission, resolve conflict, or become a grant.

**Common mistake #0 — Applicability ≠ Admissibility (informative).** Signature `Applicability` scopes *intended use and bounded context*; it is not a runtime entry gate. Runtime entry checks and admissibility predicates belong in `U.Mechanism.AdmissibilityConditions` as `A-*`. If your prose reads like “clients must satisfy the applicability”, you almost certainly want a `D-*` duty + an `A-*` gate (linked by ID) instead.

**Adjudication.** In‑work: evaluated at mechanism entry (or operationally at the point the mechanism is applied).

**Canonical form.** Predicate style, e.g.:

* “A request is admissible iff …”
* `admissible(x) iff P(x)` (conceptual form; no particular syntax is required)

**Prohibitions.**

* An `A-*` statement **MUST NOT** be placed in `U.Signature.Laws`.
* An `A-*` statement **MUST NOT** use RFC deontic keywords as if it were an agent obligation. (It is a gate predicate, not a duty.)
* An `A-*` statement **MUST NOT** claim that evidence exists (that is `E-*`) or that someone must enforce the gate (that is `D-*`).

**A.7 EntityOfConcern binding.** `A-*` claims are **Descriptions** of a mechanism gate. They are not “what a client must do”; they are “what the mechanism admits”.

**Required references (explicit).** If an `A-*` predicate relies on defined terms or invariants, it **SHOULD** reference the relevant `L-*` IDs (or at minimum the signature that defines them).

#### A.6.B:5.3 — Quadrant D: Deontics & Commitments

**Intent.** State governance through one of two D branches: accountable obligations, recommendations-as-duty, prohibitions, commitments, publication duties, operational duties, or contractual commitments under `A.2.8`; or the exact strong/weak permission, exercise, non-violation, or conflict result under `A.2.8.PER`. Only the commitment branch requires an accountable role assignment, role value, or admitted acting system as its subject.

**Adjudication.** In‑description (governance is stated in the spec); compliance may be audited via `E-*`.

**Canonical form.** In the `U.Commitment` branch, a `D-*` statement **MUST** have an accountable subject (role assignment, `U.Role`, or admitted acting system). In the permission branch, it **MUST** cite the exact `A.2.8.PER` object and preserve that object's own participant/reference contract: beneficiary/action for a grant or weak finding, actual work plus grant occurrence for exercise, checked actual work for non-violation, or the exact grant and conflicting norm for conflict. Commitment-branch examples:

* “Client implementers **MUST** satisfy `A-…`.”
* “Operators **SHALL** retain carriers …”
* “Provider **SHALL** meet `E-…` under exclusions …”

**Canonical payload (recommended; lintable).** When a `D-*` claim states an accountable obligation, recommendation-as-duty, or prohibition and is intended to be lintable and reusable, it **SHOULD** be representable as a `U.Commitment` record (A.2.8). A `D-*` statement that instead asserts strong permission, weak non-prohibition/non-violation, actual permission exercise, or permission conflict cites the exact `A.2.8.PER` result and does not force it through `U.Commitment.modality`. Default commitment fields to make explicit:

* `id` (often the `D-*` claim ID),
* `subject` (accountable role assignment or party; never an episteme),
* `modality` (the exact A.2.8 `DeonticModalityToken`: `MUST | MUST_NOT | SHOULD | SHOULD_NOT`),
* `scope` + `validityWindow`,
* `referents` (by ID; e.g., `SVC-*`, `L-*`, `A-*`, `E-*`, `MethodDescriptionRef(...)`),
* optional `adjudication.evidenceRefs` when the commitment is meant to be auditable,
* optional `source` when authority or provenance matters.

**Prohibitions.**

* A commitment-branch `D-*` statement **MUST NOT** use “the system, service, interface, or specification” as the grammatical subject unless the accountable role assignment or admitted acting system is explicitly named. A permission-branch `D-*` statement **MUST NOT** acquire a commitment subject; it **MUST** preserve the exact selected `A.2.8.PER` object's participants and references. Use `A.6.C` when contract, promise, utterance, or agreement-like boundary language is live.
* A `D-*` statement **MUST NOT** restate `L-*` or `A-*` predicates in new words when an ID exists; it **SHOULD** reference the ID.
* A `D-*` statement **MUST NOT** pretend that deontic results are laws. A commitment is an accountable-agent relation, and a permission result retains its direct `A.2.8.PER` relation/finding kind; neither is a truth-conditional invariant.

**A.7 EntityOfConcern binding.** A commitment-branch `D-*` claim is about the accountable role assignment or admitted acting system and its duty, or about a carrier-retention/exposure duty. A permission-branch `D-*` claim is about the exact `A.2.8.PER` relation or finding with its direct participants and references. Both remain written as **Descriptions**.

**Required references (explicit).**

* If a `D-*` statement imposes compliance with a gate, it **MUST** reference the relevant `A-*` ID(s).
* If a `D-*` statement is meant to be auditable, it **SHOULD** reference the `E-*` claim(s) that provide evidence and the carrier classes involved.

#### A.6.B:5.4 — Quadrant E: Work‑Effects & Evidence

**Intent.** State what happens in work and how it can be evidenced: observed effects, emitted events, traces, logs, and metrics, produced reports, measurement outcomes.

**Adjudication.** In‑work: checked by running or operating and inspecting carriers produced in work.

**Canonical form.** An `E-*` statement **SHOULD** include the minimum fields needed for adjudication:

1. **Observation and measurement conditions** (when, where, and how observed; workload, window, and triggers)
2. **Evidence carrier or record reference** under `A.7`, `A.10`, or `G.6` as applicable for the evidence relation or source basis
3. **Viewpoint and consumer** (who uses this evidence and why; ties to `viewpointRef` discipline)

**Prohibitions.**

* `E-*` statements **SHOULD NOT** use RFC deontic keywords (they are not obligations; they describe adjudicable effects and evidence).
* An `E-*` statement **MUST NOT** hide a gate predicate; gate predicates are `A-*`.
* An `E-*` statement **MUST NOT** assign agency (“the interface guarantees …”); if enforceability or commitment is intended, express it as `D-*` referencing the `E-*`.

**A.7 EntityOfConcern binding.** `E-*` claims are primarily **carrier-referenced**: they assert what carriers exist and how they relate to observed work.

**Required references (explicit).**

* If the effect or evidence claim is conditioned on a gate decision, the `E-*` statement **SHOULD** reference the relevant `A-*` ID(s).
* If the evidence is interpreted using metric definitions or invariants, the `E-*` statement **SHOULD** reference relevant `L-*` ID(s).

