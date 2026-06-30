---
chunk_kind: "child"
pattern_id: "F.3"
pattern_title: "Intra‑Context Sense Clustering"
section_id: "F.3:12"
section_title: "Worked examples (all intra‑Context)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.3/F.3__013_worked-examples-all-intra-context.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "F.3 — Intra‑Context Sense Clustering"
  - "F.3:12 — Worked examples (all intra‑Context)"
line_start: 81511
line_end: 81596
dependencies:
  - "A.11"
  - "A.7"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "Local-Sense"
  - "SenseCell"
  - "counter-examples"
  - "disambiguation"
  - "sense clustering"
---

### F.3:12 - Worked examples (all **intra‑Context**)

#### F.3:12.1 - BPMN 2.0 (workflow Context)

**Card A — “process (graph)”**

* **Label**: Tech **process** - Plain **workflow graph**
* **Sense line**: A BPMN **graph of flow nodes and sequence flows** **specifying orchestration among participants** *(design‑time)*.
* **Inside**: *process*, *process model*, *business process* (when used as diagram).
* **Counter‑example**: *“This process took 5 minutes”* ← **runtime** occurrence, **not** this sense.

**Card B — “event (node‑type)”**

* **Label**: Tech **event (node)** - Plain **event symbol**
* **Sense line**: A **node-type** that marks starts, ends, and intermediates; typed by trigger and result.
* **Inside**: *start event*, *message event*, *end event*.
* **Counter‑example**: *“The outage event happened at 13:05”* ← narrative occurrence, **not** the node‑type.

> **Outcome:** “Process uptime” is rejected as a BPMN sense; Execution belongs to another Context.

#### F.3:12.2 - PROV‑O (provenance Context)

**Card C — “activity (run)”**

* **Label**: Tech **activity** - Plain **time‑bounded execution**
* **Sense line**: An **occurrence** that **uses** and **generates** entities; linked to agents; has start/end.
* **Inside**: *activity*, *execution* (when PROV authors use it).
* **Counter‑example**: *“Sorting algorithm”* ← capability/method, **not** an occurrence.

**Card D — “agent (provenance)”**

* **Label**: Tech **agent** - Plain **provenance actor**
* **Sense line**: Thing that bears **responsibility** for an activity’s effects (person, org, software).
* **Inside**: *agent*.
* **Counter‑example**: *“RBAC role”* ← access status, **not** a PROV agent.

#### F.3:12.3 - ITIL 4 (services Context)

**Card E — “service‑level objective”**

* **Label**: Tech **SLO** - Plain **service target**
* **Sense line**: A **target value/range** for a **service characteristic** used to define acceptable service.
* **Inside**: *service‑level objective*, *SLO*.
* **Counter‑example**: *“Actual availability 99.5%”* ← observation, **not** the target.

**Card F — “incident”**

* **Label**: Tech **incident** - Plain **service disruption**
* **Sense line**: An **unplanned interruption** or reduction in quality of a service.
* **Inside**: *incident*.
* **Counter‑example**: *“Fault in plant sensor”* ← Sys‑CAL fault; different Context.

#### F.3:12.4 - SOSA/SSN (sensing Context)

**Card G — “observation (act)”**

* **Label**: Tech **observation** - Plain **measurement act**
* **Sense line**: An **act** applying a **Procedure** to a **FeatureOfInterest** to yield a **Result** for a property.
* **Inside**: *observation*.
* **Counter‑example**: *“Temperature is 20 °C”* ← **result value**, not the act.

#### F.3:12.5 - OWL 2 (types Context)

**Card H — “subclass‑of”**

* **Label**: Tech **subclass‑of** (⊑) - Plain **is‑a (class)**
* **Sense line**: A **class inclusion**: every instance of **C** is an instance of **D**.
* **Inside**: *SubClassOf*, *is‑a* (when authors use it for classes).
* **Counter‑example**: *rdf\:type* (instance‑of) — not class inclusion.

**Card I — “equivalent‑class”**

* **Label**: Tech **equivalent‑class** - Plain **same class extension**
* **Sense line**: Mutual class identity by extension; two labels for **the same** set of instances.
* **Inside**: *EquivalentClasses*.
* **Counter‑example**: *owl\:sameAs* (individual identity), different predicate.

#### F.3:12.6 - IEC 61131‑3 (control‑runtime Context)

**Card J — “task (runtime)”**

* **Label**: Tech **task** - Plain **program runner**
* **Sense line**: A **cyclic or event‑driven** execution unit that **invokes programs** on schedule or trigger.
* **Inside**: *task*.
* **Counter‑example**: *“Control algorithm”* ← design/method, not the runtime task.

