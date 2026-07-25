---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext Semantic Frame"
section_id: "A.1.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__002_use-this-when.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.1.1 — U.BoundedContext Semantic Frame"
  - "A.1.1:0 — Use This When"
line_start: 1734
line_end: 1758
dependencies:
  - "A.1"
  - "A.15"
  - "A.6.5"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.24"
  - "E.24.PUB"
  - "F.0.1"
  - "F.18"
  - "F.9"
  - "U.Holon"
keywords:
---

### A.1.1:0 - Use This When

Use this pattern when a term, role, rule, invariant, unit, status, or admissible inference is meaningful only inside a named semantic frame.

Typical moments:

- the same word means different things in engineering, finance, legal, scientific, or operations work;
- a role assignment needs the context that defines the role and its incompatibilities;
- an invariant is local to one standard, team, theory, regulation, product line, or edition;
- two contexts need a bridge relation rather than an assumed global equivalence;
- a "domain" label is too broad to decide local vocabulary or rules.

**First useful move.** Name the `U.BoundedContext` that governs the current meaning, then state the local vocabulary, local invariants, role taxonomy when role assignments are current, episteme-use/status relations when epistemic-use or status claims are current, and bridge relations that matter for the claim.

**What goes wrong if missed.** "Owner", "ticket", "service", "evidence", "role", "done", and "valid" become global labels. Integration work then appears to be about matching words, while the real problem is unspoken semantic frames.

**What this buys.** FPF can keep plural meanings without contradiction: each meaning is local, and cross-context use becomes an explicit bridge relation with stated fit and loss.

**Not this pattern when.**

- If the question is only naming a durable term, use `F.18`.
- If the question is role-method-work alignment after the context is known, use `A.15`.
- If the question is episteme description context, use `C.2.1` with `BoundedContextRef`.
- If the question is a broad field such as healthcare, physics, finance, or architecture, treat it as an informative domain family unless a specific bounded context is named.

