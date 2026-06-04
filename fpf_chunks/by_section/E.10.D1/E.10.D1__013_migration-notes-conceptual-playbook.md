---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Lexical Discipline for “Context” (D.CTX)"
section_id: "E.10.D1:12"
section_title: "Migration Notes (conceptual playbook)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__013_migration-notes-conceptual-playbook.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.10.D1 — Lexical Discipline for “Context” (D.CTX)"
  - "E.10.D1:12 — Migration Notes (conceptual playbook)"
line_start: 59765
line_end: 59774
dependencies:
  - "A.4"
  - "A.7"
  - "E.10.U1"
  - "E.10.U2"
  - "E.10.U4"
  - "E.10.U7"
  - "E.10.U9"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.9"
keywords:
  - "U.BoundedContext"
  - "anchor"
  - "context"
  - "domain"
  - "frame"
---

### E.10.D1:12 - Migration Notes (conceptual playbook)

1. **Rename headings.** Replace any “Context” section title with **Problem Frame**.
2. **Delete “anchor”.** Replace with **SenseCell** or **Concept‑Set** references.
3. **Split domain vs context.** Where “domain context” appears, rewrite as **Domain family** + explicit list of `U.BoundedContext`s.
4. **Audit references.** Ensure every semantic reference is `ContextId:LocalLabel` or `SenseCell(ContextId, …)` or Concept‑Set column.
5. **Flatten contexts.** Remove any inheritance among contexts; move relations to **E.10.U9**.
6. **Tag time.** Replace “design or runtime context” with **TimeScope tags**.
7. **Language/edition pass.** Split or merge Contexts per **D‑CTX‑7**; document rationale.

