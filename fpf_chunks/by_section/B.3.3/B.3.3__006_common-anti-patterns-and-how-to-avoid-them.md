---
chunk_kind: "child"
pattern_id: "B.3.3"
pattern_title: "Assurance Subtypes & Levels"
section_id: "B.3.3:5"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.3/B.3.3__006_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "B.3.3 — Assurance Subtypes & Levels"
  - "B.3.3:5 — Common Anti-Patterns and How to Avoid Them"
line_start: 37438
line_end: 37445
dependencies:
  - "A.10"
  - "A.19"
  - "A.4"
  - "B.3"
  - "B.4"
  - "C.16"
  - "C.2.1"
  - "D.4"
  - "U.Episteme"
keywords:
  - "L0-L2"
  - "LA"
  - "TA"
  - "VA"
  - "assurance levels"
  - "typing"
  - "validation"
  - "verification"
---

### B.3.3:5 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It |
| :--- | :--- | :--- |
| **The "Tested but Unbridged" Mess** | "Our code has 100% test coverage, but we still have integration bugs and nobody understands what the code does." | **CC-B3.3.2** makes Concept-Bridge Assurance (CBA) mandatory for L1. You cannot claim your work is "Substantiated" without first ensuring your terms and concepts are clear, context-scoped, and consistently bridged. |
| **The "Perfect Blueprint, Flawed Reality"** | "The design was formally proven to be perfect, but the physical product failed catastrophically in the field." | **CC-B3.3.3** mandates Validation Assurance (LA) for safety-critical systems at L2. A perfect blueprint (`FV=4`) is not enough; you must also provide empirical evidence (`EV>0`) that it works in the real world. |
| **The "Paper Compliance" Shell Game** | "We have thousands of documents and links, so we must be at a high assurance level." | The computed `AssuranceLevel` is not based on the *quantity* of evidence but on its *type* and *quality* (via FV/EV scores). You cannot reach L2 without strong formal verification (VA), no matter how much validation (LA) you do. |

