---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local‑First Unification Naming Protocol"
section_id: "F.18:18"
section_title: "Worked examples (compact)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__019_worked-examples-compact.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "F.18 — Local‑First Unification Naming Protocol"
  - "F.18:18 — Worked examples (compact)"
line_start: 68075
line_end: 68140
dependencies:
  - "A.19.SUPPORT-VIEW"
  - "A.6.P"
  - "E.10"
  - "E.10.SEMIO"
  - "F.0.1"
  - "F.1-F.17"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:18 - Worked examples (compact)

> Each example shows **how the Protocol steers naming** so engineers and managers can communicate without hidden Cross‑context leaks.
> **Card hygiene shown explicitly:** each example **states the Kind and the Purpose/use‑domain** and **chooses Tech/Plain labels from a small NQD‑frontier** (seed set diversified by traditions, novelty/familiarity, and lexical form; see Part G patterns).
> **Head-term diversity:** each example **MUST** also state the **distinct head-term families** represented in its NQD candidate set (lexical “roots” such as *Recipe*, *Run*, *Episode*, not prepositional/morphological variants). This prevents faking Diversity_P with near-clones of one head.

#### F.18:18.1 - Example 1 — *MethodDescription* vs *Work* (recipe vs run)

* **Context harvest:**
  *BPMN 2.0 (2011):* “Process model” (recipe) and “Activity instance” (run).
  *PROV‑O (2013):* `prov:Plan` vs `prov:Activity`.
  *ITIL:* “Work instruction” vs “Change implementation record.”
* **Kind:** `U.MethodDescription` (design‑time record) **and** `U.Work` (run‑time occurrence).
* **Purpose / use‑domain:** planning/scheduling vocabulary across BPMN, PROV‑O, ITIL; separates *design recipe* from *execution episode* for governance and telemetry.
* **NQD‑front (seed candidates):**
  *design‑time:* *Procedure*, *ProcessModel*, *MethodSpec*, *WorkflowDefinition*, *Recipe*, *MethodScript*
  *run‑time:* *Run*, *Execution*, *Enactment*, *ActivityInstance*, *Job*, *Episode*
* **Head-term families used (DesignRunTag):**
  *design-time heads:* {Procedure, ProcessModel, MethodSpec, WorkflowDefinition, Recipe, MethodScript}
  *run-time heads:* {Run, Execution, Enactment, ActivityInstance, Job, Episode}
* **Chosen from frontier (Unified Tech / Plain):**
  `U.MethodDescription` / “recipe”; `U.Work` / “run”.
  *Discarded highlights:* **Procedure** (collides with governance “procedure/policy”); **Execution** (overloaded in CS/security);
* **Anti-pattern (for illustration only, non-conformant).**
 > *Bad CandidateSet (lexically narrow):* {“Reference plane”, “Plane of reference”, “Planar reference”, “Ref. plane v2”}.
 > All four are one **head-term family** (*plane*). Even if Diversity_P over raw strings looks high (four labels), **head-term diversity is 1**, so this set **fails** the F.18 diversity intent. A conformant Card would either: (a) add labels with other heads (e.g., *Layer*, *Track*, *Band*), or (b) explicitly record why other heads are rejected (AliasRisk, domain idiom) and accept low lexical Diversity_P with a rationale.
* **Enactment** (speech‑act nuance).
* **Bridges:** recipe↔run **related**, not identical; loss note “control‑flow vs. execution.”
* **Why it matters:** Managers can schedule **Work** while authors improve the **MethodDescription**—no category errors. The NQD‑front preserves tradition‑diverse, lexically stable options until a reasoned choice is made. (F.11/F.16; F.17 rows.)

#### F.18:18.2 - Example 2 — *Service* (promise) vs *SpeechAct* (utterance) vs *Commitment* (deontic)

* **Context harvest:**
  *IT service canon:* “SLA/OLA clause”, “ticket approved”.
  *Speech‑act theory:* “performative utterance”.
  *Org governance:* “approval signature”.
* **Kind:** `U.PromiseContent` (promise), `U.SpeechAct` (utterance), `U.Commitment` (deontic bond).
* **Purpose / use‑domain:** ops/governance vocabulary connecting ITSM, organizational policy, and pragmatics; separates saying, binding, and promising.
* **NQD‑front (seed candidates):**
  *promise:* *Service*, *Offering*, *Provision*, *CapabilityOffer*
  *utterance:* *SpeechAct*, *Performative*, *Utterance*, *Declaration*
  *deontic bond:* *Commitment*, *Obligation*, *Binding*, *Duty*
* **Chosen from frontier (Unified Tech / Plain):**
  `U.PromiseContent` / “service (promise)”; `U.SpeechAct` / “utterance”; `U.Commitment` / “commitment”.
  *Discarded highlights:* **Offering** (business‑model connotations); **Declaration** (too narrow for performatives); **Obligation** (legalese; narrower than commitment envelope).
* **Ontology note (informative):**
  `U.SpeechAct` and `U.Commitment` are defined normatively in Part A (A.2.9 and A.2.8 respectively). This F.18 card is a lexical/NQD anchor, not the ontology definition site.

* **Bridges:** utterance **institutes** commitment; commitment **binds** promise content; no synonymy claimed.
* **Why it matters:** Status tracking becomes intelligible without pretending that a “service” acts; the NQD‑front yields neutral, cross‑tradition readable labels. (F.12; F.17 blocks D/R.)

#### F.18:18.3 - Example 3 — *Characteristic* names without process-phase bias

* **Context harvest:**
  *Quality canon:* “maturity level”; *Performance canon:* “throughput”.
 **Kind:** `U.Characteristic` (measurement names).
* **Purpose / use‑domain:** CHR‑compatible measurements for planning and performance; bridgeable across engineering and management.
* **NQD‑front (seed candidates):**
  *readiness (ordinal):* *MaturityLevel*, *ReadinessLevel*, *PhaseReadiness*, *TRL*, *ReadinessScore*
  *throughput (ratio):* *Throughput*, *Rate*, *ProcessingRate*, *OpsPerSecond*, *FlowRate*
* **Chosen from frontier (Unified Tech / Plain):**
  `U.ReadinessLevel` / “readiness level” (ordinal); `U.Throughput` / “throughput” (ratio).
  *Discarded highlights:* **TRL** (tied to a specific scale/tradition); **Rate/OpsPerSecond** (over‑specific units baked in).
* **Narrative:** Dynamics are shown as **movement in state-space**, not via process-phase-laden names such as “pre-production process”.
* **Why it matters:** Prevents process phase/time from leaking into labels; the NQD-front ensures neutrality and recognizability. (A-series CHR rationale; F.17 §4-§6.)

