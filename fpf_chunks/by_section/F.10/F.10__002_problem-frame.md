---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping: Evidence, Standard, and Requirement Status"
section_id: "F.10:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__002_problem-frame.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "F.10 — Status Families Mapping: Evidence, Standard, and Requirement Status"
  - "F.10:1 — Problem frame"
line_start: 90302
line_end: 90317
dependencies:
  - "A.2.4"
  - "B.3"
  - "F.1"
  - "F.18"
  - "F.3"
  - "F.9"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:1 - Problem frame

Use this pattern when a project uses status words such as "observed", "measured", "validated", "approved", "deprecated", "satisfied", "violated", "waived", "pending", "current", or "ready" and needs to know what kind of status is being claimed, what it qualifies, and whether it can be compared or reused in another bounded context.

Use it especially when evidence, standards, and requirements are being mixed: a dashboard says a service is ready, a standard says a method is approved, a measurement says a requirement is satisfied, a model card says a model is validated, or a requirement register says a clause is waived.

**Primary EntityOfConcern.** The primary `EntityOfConcern` is the status-use statement and the status-family mapping that make one status value usable in one bounded context. The pattern governs the relation among status cell, target, target kind, scope, window, source or provenance constraint, and intended status use. It does not make an episteme hold a role and does not treat a visible status display as gate passage, permission, assurance, evidence, or performed work by itself.

**First useful move.** Write the smallest status-use statement: status family, bounded context, status value, target, target kind, scope, window when current, source or provenance constraint, intended use, and stronger use not carried by this relation.

**What goes wrong if missed.** A single word such as "validated" starts doing the work of evidence, standard approval, requirement satisfaction, gate passage, release readiness, and assurance at once. Cross-context dashboards compare labels without bridge loss. A report or standard is treated as if it had a status role. A design-time approval is read as run-time compliance.

**What this buys.** Status words stay local, typed, and comparable. Evidence status says what has evidential standing for a claim. Standard status says what a canon or standard-governed context sanctions. Requirement status says what is happening to an obligation or clause. Cross-context movement becomes an explicit bridge claim instead of a synonym guess.

**Not this pattern when.** If the current claim is full evidence provenance, use `A.10`. If the current claim is only an episteme being used as evidence or status before full status-family mapping is needed, use `A.2.4`. If the current claim is assurance, use `B.3`. If the current claim is causal use, use `C.28`. If the current claim is a source, publication face, view, explanation, or specification-use question, use `E.17`, `E.17.0`, `E.17.2`, `E.17.EFP`, `E.10.D2`, or the direct publication-use pattern. If the current claim is a system or acting holon holding a work-facing role, use `A.2` and `A.2.1`. If the current claim is performed work, use `A.15.1`.

