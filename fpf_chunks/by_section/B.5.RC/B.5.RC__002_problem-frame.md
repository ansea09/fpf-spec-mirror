---
chunk_kind: "child"
pattern_id: "B.5.RC"
pattern_title: "Recover a Construction from Its Description"
section_id: "B.5.RC:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.RC/B.5.RC__002_problem-frame.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "B.5.RC — Recover a Construction from Its Description"
  - "B.5.RC:1 — Problem frame"
line_start: 41814
line_end: 41823
dependencies:
  - "A.6.3.RT"
  - "B.5"
  - "B.5.RA"
  - "C.29.1"
  - "C.29.2"
  - "C.39"
keywords:
---

### B.5.RC:1 - Problem frame

Use this pattern when a description points to a result you need, but you cannot yet recover how to obtain it from what is available. You may be reading a mathematical construction, an assembly method or a way to transform data. The difficulty is in the connection between starting material, allowed operations and the required result.

Here, a **construction** is a way of obtaining an object by applying operations to given objects. In a mathematical construction, those operations form mathematical objects. In an assembly method, they may produce a design or a physical assembly; identify which result the description promises. The relevant practice supplies the operations and their application conditions.

**First useful move:** name the result needed for the next use, then find the operation that could produce it and what that operation requires. Follow those requirements back to available starting material. Work a small instance forward to recover the missing connection.

This method needs access to the description and enough subject knowledge to interpret its objects and rules. Use an adequate known construction directly. If the task is to invent a method where no usable account is available, use C.39 for that development; a missing operation discovered here can become its input.

