---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "SystemRoleKindDescription — Describing an Exact System-Role Kind"
section_id: "F.4:6"
section_title: "Reasoning Primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__008_reasoning-primitives.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "F.4 — SystemRoleKindDescription — Describing an Exact System-Role Kind"
  - "F.4:6 — Reasoning Primitives"
line_start: 91885
line_end: 91916
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
  - "A.6.RSIR"
  - "A.7"
  - "C.2.1"
  - "C.3"
  - "C.3.2"
  - "E.10.D2"
  - "E.10.ROLE"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.5"
  - "F.9"
keywords:
  - "classification criterion"
  - "description episteme"
  - "effective scheme"
  - "local kind"
  - "non-inference boundary"
  - "system-role-kind description"
---

### F.4:6 - Reasoning Primitives

Use these schemas as thinking checks.

```text
SystemRoleKindDescription D describes local system-role kind K
  -> D is a C.2.1 episteme about K; D is not K or a classification judgment.
```

```text
Candidate system X satisfies the current KindSignature of K
  -> this may support a classification judgment about X and K;
     it creates neither an assignment nor performed Work.
```

```text
Assignment A relates admitted holder system X to K
  -> A is an occurrence of an exact species under U.SystemRoleAssignment;
     D establishes neither A nor X's system admission.
```

```text
D cites capability requirement CapReq or Method requirement MReq
  -> apply A.2.2 or the direct Method pattern; the citation proves neither result.
```

```text
Source says “episteme X has role Y”
  -> use E.10.ROLE to recover the direct episteme-use relation or ordinary wording
     before considering any system-role kind or assignment.
```

