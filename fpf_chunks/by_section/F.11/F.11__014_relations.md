---
chunk_kind: "child"
pattern_id: "F.11"
pattern_title: "Method Quartet Harmonisation"
section_id: "F.11:13"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/F.11/F.11__014_relations.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "F.11 — Method Quartet Harmonisation"
  - "F.11:13 — Relations"
line_start: 65555
line_end: 65569
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.10"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.9"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Work"
keywords:
  - "Actuation"
  - "Method"
  - "MethodDescription"
  - "Role–Method–Work alignment"
  - "Work"
---

### F.11:13 - Relations

**Builds on:**
E.10.D1 **D.CTX** (Context ≡ `U.BoundedContext`); A.3/**A.3.1**/**A.3.2**/**A.15** (Method/Spec/Work foundations); Sys‑CAL (Actuation semantics); KD‑CAL (Observation); F.1–F.3 (Contexts → SenseCells); F.10 (Status families & Windows).

**Constrains:**

* **F.4 Role Description:** Roles or Statuses **must** point to the right box (e.g., *Approved* → MethodDescription; *Observed* → Work).
* **F.5 Naming:** Enforce distinct Tech/Plain labels for Method/Spec/Work or Actuation where homonyms threaten.
* **F.7/F.9 Bridges:** All Cross‑context assertions among quartet terms **must** go through explicit Bridges with **kind/CL/Loss**.

**Used by.**
Part C patterns (Sys‑CAL, KD‑CAL, Method‑CAL, Kind-CAL, LCA‑CAL) when describing examples, proofs, and cross‑disciplinary mappings.


