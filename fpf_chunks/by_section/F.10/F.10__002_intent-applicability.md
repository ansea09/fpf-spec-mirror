---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping (Evidence • Standard • Requirement)"
section_id: "F.10:1"
section_title: "Intent & applicability"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__002_intent-applicability.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "F.10 — Status Families Mapping (Evidence • Standard • Requirement)"
  - "F.10:1 — Intent & applicability"
line_start: 72918
line_end: 72931
dependencies:
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:1 - Intent & applicability

**Intent.** Provide a **simple, Context‑first way** to express and compare **status meanings** across disciplines **without collapsing modalities** (*epistemic* vs *deontic*). We focus on three pervasive **status families**:

1. **EvidenceStatus** (what the world **shows**) — epistemic modality.
2. **StandardStatus** (what a canon **sanctions**) — deontic (curatorial) modality.
3. **RequirementStatus** (what an obligation is **doing**) — deontic (compliance) modality.

Each status meaning is **local to a Context** (`U.BoundedContext`). Cross‑context relationships appear **only** via **Bridges** (F.9) with a declared **kind** and **CL** (congruence level).

**Applicability.** Whenever models mix observations, standards, and obligations: service acceptance from uptime measurements; safety proofs against normative checklists; ML model “validated” vs “approved for use”.

**Non‑goals.** No workflows, no tool states, no editorial lifecycles. This pattern defines **conceptual meaning and safe reasoning moves**, not procedures.

