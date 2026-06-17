---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description - Description Episteme for U.Role"
section_id: "F.4:6"
section_title: "Reasoning Primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__008_reasoning-primitives.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "F.4 — Role Description - Description Episteme for U.Role"
  - "F.4:6 — Reasoning Primitives"
line_start: 72982
line_end: 73010
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.3"
  - "F.6"
  - "F.8"
  - "F.9"
keywords:
  - "Role Characterisation Space (RCS)"
  - "RoleStateGraph (RSG)"
  - "invariants"
  - "role template"
  - "status template"
---

### F.4:6 - Reasoning Primitives

Use these judgement schemas as thinking checks.

```text
RoleDescription RD describes Role R in Context C
  -> RD is a description episteme about R, not R itself.
```

```text
RoleDescription RD admits holder kind HK for Role R
  -> A RoleAssignment may use a holder of HK only if A.2.1 and neighboring checks admit it.
```

```text
RoleDescription RD lists capability requirement CapReq
  -> capability claim is governed by A.2.2, not by RD.
```

```text
RoleDescription RD lists method requirement MReq
  -> method or method-description claim is governed by A.15, A.3.1, or A.3.2.
```

```text
Source says "X has role Y" and X is an episteme
  -> recover direct episteme-use relation before considering U.Role.
```

