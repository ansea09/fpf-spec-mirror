---
chunk_kind: "child"
pattern_id: "F.3"
pattern_title: "Intra‑Context Sense Clustering"
section_id: "F.3:6"
section_title: "Solution — how to think the clustering (notation‑free)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.3/F.3__007_solution-how-to-think-the-clustering-notation-free.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "F.3 — Intra‑Context Sense Clustering"
  - "F.3:6 — Solution — how to think the clustering (notation‑free)"
line_start: 70047
line_end: 70071
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

### F.3:6 - Solution — how to think the clustering (notation‑free)

> What follows are **mental moves**, not steps for a team. Use them as probes until the Context’s usage partitions itself naturally.

**6.1 Consolidate aliases into one Local‑Sense.**
If Units differ only by **orthography, abbreviation, or canon‑blessed synonymy** and are **used interchangeably** in the Context’s own sentences, treat them as **one Local‑Sense**.
*Example (ITIL):* *service‑level‑objective* and *SLO* → one Local‑Sense.

**6.2 Split on incompatible selectional frames.**
If the same head pairs with **different kinds of arguments** or plays **different roles** in the canon’s statements (and those roles cannot both be true at once), split.
*Example (BPMN):* *event* as **node type** vs as **occurrence narrative** in a tutorial → two Local‑Senses; adopt the **node type** sense if that is the normative layer.

**6.3 Split on entailments that pull apart.**
If paraphrases lead to **different entailments** (e.g., one implies temporality, another structural position), you have two senses.
*Example (PROV):* *activity* implies **time‑bounded use/generate**; it cannot be the same sense as a **static capability**.

**6.4 Prefer sense minimality.**
If two candidate Local‑Senses never lead to **different conclusions** in the Context’s own use, merge them. If they sometimes do, split them—and record a **counter‑example** to keep the boundary crisp.

**6.5 Keep Tech label idiomatic; Plain label helpful.**
Tech label stays as the canon speaks; Plain label conveys the **function** of the sense to a careful newcomer. Neither label may **broaden** the sense beyond usage.

**6.6 Name only as much as you will use.**
If a fine-grained split has **no downstream consequence** (Role Descriptions, tables, bridges), prefer the coarser Local-Sense.

