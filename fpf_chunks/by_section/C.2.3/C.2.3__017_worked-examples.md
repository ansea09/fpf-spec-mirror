---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Formality of an Episteme"
section_id: "C.2.3:16"
section_title: "Worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__017_worked-examples.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.2.3 — Formality of an Episteme"
  - "C.2.3:16 — Worked examples"
line_start: 52410
line_end: 52437
dependencies:
  - "A.16"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.19.2"
  - "C.2"
  - "C.2.2"
  - "C.2.4"
  - "C.2.7"
  - "C.2.LS"
  - "C.39"
  - "F.9"
keywords:
  - "Formality assessment"
  - "expression properties"
  - "language-state separation"
  - "local ordinal scale"
  - "partial order"
  - "proof"
  - "specification"
---

### C.2.3:16 - Worked examples

#### C.2.3:16.1 - Research hypothesis

A short note proposes a scaling law with stable terms and acceptance conditions in prose. That can be enough to decide which measurement to attempt. Writing the relation with explicit variables, units and parameter conditions enables a quantitative comparison. The expression becomes more determinate in those respects; the fit to observations remains a separate question. A poor fit is not repaired by making the same formula typographically more formal.

#### C.2.3:16.2 - Interface specification

An interface specification declares preconditions, postconditions and invariants with their types and interpretation. It can be used to compare designs before an implementation exists. A faithful executable reference model adds the ability to run scenarios. A running implementation that omits the postcondition does not dominate that specification: the two expressions supply different contributions. To claim conformance, connect the implementation behavior to the required postcondition and supply the needed argument or test.

#### C.2.3:16.3 - Safety controller

A controller and plant model express discrete transitions, continuous evolution and the obligations connecting them. A proof of an invariant in higher-order logic can satisfy a requirement for an explicitly derived invariant under those assumptions. A checked dependent-type development can satisfy the same requirement. Choose between adequate options by compatibility, available proofs and application cost through C.19.2; there is no general requirement to replace HOL with a supposedly higher foundation. If the plant-assumption evidence is weak, retain that limitation even when the derivation is fully checked.

#### C.2.3:16.4 - Decision policy

A policy says in controlled prose that a request exceeding a thirty-minute planned-duration ceiling fails the budget condition. To evaluate that condition automatically, introduce a Plan variable p, define plannedMinutes(p) in nonnegative real minutes and state `meetsBudget(p) iff plannedMinutes(p) <= 30`. The expression now gives the needed domain, unit and predicate. Its evaluation can answer the budget question; it supplies neither the other eligibility conditions nor permission to proceed.

If “duration” later means elapsed duration rather than planned duration, retaining the formula's printed shape is insufficient. The input interpretation and therefore the condition have changed. Return to the affected policy meaning and uses.

#### C.2.3:16.5 - Proof-bearing algorithm

An algorithm's dependent type states a length-preservation property, and its term expresses a derivation under the chosen type theory. Inspect the property and term, then recover the required checking result. A separate HOL proof of the same stated property may be equally sufficient for the recipient. If a new task instead requires reasoning about higher equalities or a specific univalent construction, it changes the apparatus requirement. That new requirement does not retrospectively make the earlier sufficient derivation less rigorous.

#### C.2.3:16.6 - Executable ML recipe

A training-and-evaluation recipe declares the inputs, parameters, operations and output interpretation needed to repeat a run. This supplies executable meaning. It does not express a proof of generalization merely because the harness is sophisticated. If the receiving use needs an empirical performance estimate, obtain the corresponding observations and inference. If it needs a formal property of the procedure, state and derive that property under a suitable model. The two continuations repair different gaps.

