---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U.Types & Roles"
section_id: "F.5:5"
section_title: "Normative rules — Role Descriptions (context‑local labels)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__006_normative-rules-role-descriptions-context-local-labels.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "F.5 — Naming Discipline for U.Types & Roles"
  - "F.5:5 — Normative rules — Role Descriptions (context‑local labels)"
line_start: 69069
line_end: 69094
dependencies:
  - "A.11"
  - "A.7"
  - "D.CTX"
  - "E.10"
  - "E.10.D1"
  - "E.10.D2"
  - "F.0.1"
  - "F.1"
  - "F.13"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "U.Type naming"
  - "lexical rules"
  - "morphology"
  - "naming conventions"
  - "twin registers"
---

### F.5:5 - Normative rules — Role Descriptions (context‑local labels)

Let **T** be a Role Description in Context **C** with SenseCell `sense(T)=⟨C,σ⟩`.

**R‑RD‑1 (Two registers).** Provide **both**:
`Tech(T)` = the **Context‑idiomatic** phrase (exact canon wording if possible).
`Plain(T)` = a brief, neutral explanation *that does not broaden meaning*.
*Symbolic alias* is optional and purely informative.

**R‑RD‑2 (No Context tags in labels).** Do **not** embed the Context name in the label (avoid “(BPMN)” in the label itself). Context is already carried by the **SenseCell**; keep labels clean.

**R‑RD‑3 (senseFamily‑aware morphology).**
— **Role** names are **countable nouns** for masks (e.g., *Participant*, *Operator*, *Reviewer*). Avoid verbs and gerunds. Add the suffix **“Role”** **only** if the Context idiom risks confusion with a substance or a status (e.g., *“Reviewer Role”* in a Context that also has a *“Reviewer Status”*).
— **Status** names are **state nouns** or **adjectival‑noun collocations** (e.g., *Approved*, *Compliant*, *In‑Service*, *Access Role* (RBAC)). If a family of levels exists, encode the **level** (`Assurance L1`, `Readiness L2`) rather than inventing decorative adjectives.

**R‑RD‑4 (Local idiom first).** Prefer the **canon’s term of art** even if it sounds narrower than a cross‑discipline cliché. The Plain label handles pedagogy; the Tech label honours the Context.

**R‑RD‑5 (Minimal generality).** Choose the **narrowest label** whose invariants you actually assert. Do **not** “upgrade” *Task* to *Activity* or *Process* just to sound universal.

**R‑RD‑6 (No permissions by stealth).** Role labels **must not** imply entitlement (*“Privileged Operator”* is a Status+Role mashup). Keep deontics in **Status** names in the **deontics Context**.

**R‑RD‑7 (Edition‑neutral labels).** Do **not** bake edition/profile into labels. Edition lives in the **Context**; the card binds to a SenseCell that already encodes edition where needed.

**R‑RD‑8 (Short and stable).** Favour **1–3 words**. Avoid rhetorical adjectives (*“robust, optimal, best‑practice”*).


