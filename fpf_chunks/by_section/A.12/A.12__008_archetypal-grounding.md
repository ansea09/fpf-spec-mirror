---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "External Transformer & Reflexive Split"
section_id: "A.12:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__008_archetypal-grounding.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.12 — External Transformer & Reflexive Split"
  - "A.12:5 — Archetypal Grounding"
line_start: 19006
line_end: 19018
dependencies:
  - "A.3"
  - "B.2.5"
  - "U.Interaction"
keywords:
  - "agency"
  - "causality"
  - "control loop"
  - "external agent"
  - "self-modification"
---

### A.12:5 - Archetypal Grounding

The principle of external causality and the Reflexive Split pattern are universal. They apply equally to physical systems, epistemes, and socio-technical organizations.

| Scenario | Naive Description ("Self-Magic") | FPF Model with Reflexive Split | `Agent` & `Target` |
| :--- | :--- | :--- | :--- |
| **System Archetype** | "The robot calibrates itself." | The robot is modeled as a composite holon containing two subsystems: <br> 1. **`CalibrationController`** (`U.System`) <br> 2. **`SensorSuite`** (`U.System`) <br> They interact across an internal data bus (`U.Boundary`). | **Agent:** `CalibrationController#TransformerRole:RobotInternals` <br> **Target:** `SensorSuite` |
| **Episteme Archetype** | "The document automatically updates its cross-references." | The "document" is a system comprising: <br> 1. **`UpdateScript`** (a `U.System` that executes code) <br> 2. **`DocumentFile.xml`** (a `U.System` acting as a symbol carrier) <br> They interact via the file system (`U.Boundary`). | **Agent:** `UpdateScript#TransformerRole:DocumentSystem` <br> **Target:** `DocumentFile.xml` (the carrier of the `U.Episteme`) |
| **Socio-Technical Archetype** | "The team reviews its own performance." | The team is modeled as a collective `U.System` that enacts two roles at different times: <br> 1. **`ExecutionTeam`** (doing the sprint work) <br> 2. **`ReviewTeam`** (conducting the retrospective) <br> The "boundary" is the formal separation created by the retrospective ceremony. | **Agent:** `Team#ReviewerRole:RetrospectiveContext` <br> **Target:** The `U.Work` logs and evidence carriers produced by the `Team#ExecutionRole`. |

**Key takeaway from grounding:**
These examples demonstrate that there is *no such thing as self-action* in a well-formed model. Every action, even an internal one, can and must be decomposed into an external interaction between a distinct agent and a distinct target. This makes the causal chain explicit and auditable in all domains.

