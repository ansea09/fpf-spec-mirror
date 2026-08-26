---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "Gate Decisions from Independent Check Results"
section_id: "A.21:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__002_use-this-when.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "A.21 — Gate Decisions from Independent Check Results"
  - "A.21:0 — Use this when"
line_start: 33723
line_end: 33746
dependencies:
  - "A.10"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.20"
  - "B.3"
  - "C.3.2"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.19"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
---

### A.21:0 - Use this when

Use A.21 when a named gate must decide whether one bounded action or transition may proceed under an applicable profile rule. Identify every check that the rule requires, including the subject and criterion of each check.

**First useful move.** Name the action being decided, the profile rule that applies, and every required check result. Map each check result under that rule, then let the worst mapped value win.

**Quick worked case.** `WorkshopEntryGate-4` decides whether `CalibrationCycle-17` may start before 16:00. `WorkshopEntryProfile-E5` requires two checks: `CalibrationCertificate-44` for `TorqueWrench-12` is current under `CalibrationRule-E3`, and `WorkshopEnclosure-2` is closed under `EnclosureRule-E2`. Both checks are evaluated and satisfied, so each maps to `pass`; the gate returns `pass` and the cycle may start before 16:00. Recheck if the instrument, certificate edition, enclosure state, profile edition, or time window changes.

If the state of `WorkshopEnclosure-2` is unknown, that check remains `unknown`. `WorkshopEntryProfile-E5` maps the uncertainty to `block`, not to `abstain`, so the cycle stays on hold until the enclosure is checked. A different policy may accept a bounded uncertainty only through an explicit rule that names the subject, tolerance, consequence, and validity window.

**Short boundary.** A gate decision is neither work-entry readiness nor performed Work. Use `A.15.5` for the ordinary readiness question. If Work later occurs, identify it through the A.15 family; do not treat the gate, plan item, or prospective claim as that later Work.

**What goes wrong if missed.** A green display is mistaken for permission, an unknown required check disappears as a neutral value, two different check subjects are merged by label, or a new path slice is treated as authority to weaken policy.

**What this buys.** The practitioner can recover what was decided, which rule applied, which facts supported the decision, what action follows, and when the decision must be made again.

**Not this pattern when.**

- Use `A.20` for one internal-constraint result.
- Use `A.15.5` for full-kit or work-entry readiness without a gate decision.
- Use `E.18` for transformation-flow positions, paths, slices, and structural crossings.
- Use the pattern that defines the policy, safety rule, regulatory rule, evidence claim, channel condition, or system-role claim for the truth of that check.
- Use `E.17` only when the decision is published through a form or carrier.

