---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__002_use-this-when.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:0 — Use This When"
line_start: 88701
line_end: 88726
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.REL"
  - "E.10"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "actual performing U.System"
  - "assignment coverage"
  - "exact U.RoleAssignment"
  - "performedUnderAssignment"
  - "separate assertion and evidence"
  - "world-side attribution"
---

### F.6:0 - Use This When

**Plain name.** Check who performed this work under which role assignment.

Use this pattern when deciding whether one exact dated Work individual `W : U.Work` was performed under one exact obtaining assignment occurrence `RA : U.RoleAssignment`. When it was, the direct world-side relation `performedUnderAssignment(W, RA)` obtains. A separate attribution assertion or record may designate `W` and `RA` and state that the relation obtains.

Typical moments include:

- a work record says "Alice reviewed", "Robot-7 inspected", or "the operations team approved", but the exact assignment episode is missing;
- a method description names a work-facing role and the project must connect performed work to the system that held that role;
- source wording says `RoleEnactment`, "played the role", or `Holder#Role:Context@Window`, and the direct work-to-assignment relation must be recovered;
- a report, standard, dashboard, access label, or other episteme is described with role language even though it did not perform the work;
- a role label is reused under another role taxonomy or reference scheme and local attribution would be unsafe without an explicit bridge.

**Primary EntityOfConcern.** One obtaining direct `performedUnderAssignment` relation occurrence between one exact `U.Work` occurrence and one exact `U.RoleAssignment` occurrence.

**Primary working reader.** An engineer, operator, method author, manager, or FPF author deciding whether a performed-work attribution is grounded strongly enough for the next use.

**First useful move.** Name the Work occurrence and the assignment occurrence that may participate in the attribution relation. Recover the assignment's holder system, role value, role-taxonomy episteme, effective reference scheme, and assignment window before deciding whether `performedUnderAssignment(W, RA)` obtains.

**What goes wrong if missed.** Assignment is treated as proof that work happened; a work log names a person but not the assignment episode; a context-like word hides the role taxonomy and interpretation scheme; or an episteme is made the performer because it described, constrained, or evidenced the work.

**What this buys.** Work attribution becomes a direct, inspectable relation while role state, capability, method fit, evidence, source use, result, publication, and cross-scheme correspondence remain with their own governing patterns.

**Not this pattern when.** Use `A.2` for the role value, `A.2.1` for the assignment occurrence, `A.2.5` for a current role-state predicate, `A.2.2` for capability, and `A.15.1` for the work occurrence. Use `A.10`, `A.15.4`, `E.17`, or another direct pattern when the current claim is evidence use, source reliance, publication, status, gate, or decision. Use `A.6.5` when "role" means a relation position rather than a work-facing `U.Role`.

