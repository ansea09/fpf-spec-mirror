---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
section_id: "F.8:7"
section_title: "Micro‑examples (didactic triad)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__008_micro-examples-didactic-triad.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "F.8 — Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
  - "F.8:7 — Micro‑examples (didactic triad)"
line_start: 71456
line_end: 71480
dependencies:
  - "A.11"
  - "A.7"
  - "A.8"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "decision lattice"
  - "minting new types"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:7 - Micro‑examples (didactic triad)

#### F.8:7.1 - For engineers — “Do we need a new **Execution** label?”

* **Need.** “We want to refer to **what actually happened** in both provenance logs and PLC runtime.”
* **senseFamily.** Execution - **stance.** run.
* **Contexts.** `PROV‑O` (Activity), `IEC 61131‑3` (task run).
* **Row?** F.7 has **execution-occurrence** at **assignment/enactment-eligibility**, CL = 2.
* **Decision.** **Reuse** that row’s label at **Assignment-eligibility**; **no** new U.Type; define Role Descriptions **anchored to each Context** as needed.

#### F.8:7.2 - For managers — “Can we call them all **actors**?”

* **Need.** A single everyday word in the spec to denote “the responsible party”.
* **senseFamily.** Role (behavioural mask in prose).
* **Contexts.** `BPMN 2.0` (Participant), `PROV‑O` (Agent).
* **Row?** **Naming‑only** row “actor”, CL = 2.
* **Decision.** **Reuse** “actor” **in prose only**; keep Context‑loyal labels in formal sections. No Role Description minted unless tied to one context.

#### F.8:7.3 - For researchers — “New **U.Type** for ‘Work Scope’?”

* **Need.** Kernel notion capturing **feasible performance region** across systems.
* **Test A.8.** Appears in **control** (reachable sets), **services** (operating envelope), **measurement** (confidence bands): **≥ 3 families?**
* **Reduction test.** Can it be expressed as a **row** + existing `U.Relation` + KD‑CAL constructs?
* **Decision.** If **not reducible** and **cross‑family stable**, propose **new U.Type** with minimal definition; otherwise, prefer a **row** or a **pattern**.

