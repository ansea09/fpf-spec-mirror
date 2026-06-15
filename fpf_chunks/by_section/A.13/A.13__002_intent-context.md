---
chunk_kind: "child"
pattern_id: "A.13"
pattern_title: "The Agential Role & Agency Spectrum"
section_id: "A.13:1"
section_title: "Intent & Context"
source_path: "FPF-Spec.md"
output_path: "by_section/A.13/A.13__002_intent-context.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.13 — The Agential Role & Agency Spectrum"
  - "A.13:1 — Intent & Context"
line_start: 20181
line_end: 20191
dependencies:
  - "A.12"
  - "A.2"
  - "A.2.1"
  - "C.9"
  - "E.16"
keywords:
  - "agency as role"
  - "agency spectrum"
  - "autonomy grading"
  - "contextual role assignment"
  - "substrate-neutral autonomy"
---

### A.13:1 - Intent & Context

The concept of "agency"—the capacity of an entity to act purposefully—is central to engineering, biology, and AI, yet it remains one of the most overloaded and ambiguous terms. Without a precise, falsifiable, and substrate-neutral definition, models of autonomous systems risk descending into "self-magic," where actions have no clear cause and accountability is lost.

This pattern builds directly upon the foundations laid in the FPF Kernel to provide that definition. A.1 established that only a **`U.System`** can be the bearer (`holder`) of behavioral roles.  A.2.1 defined the universal `U.RoleAssignment` (`Holder#Role:Context`) as the canonical way to assign roles. A.3 and A.12 defined the `TransformerRole` and the principle of the external agent.

The intent of this pattern is to:
1.  Formally define **agency** not as an intrinsic *type* of holon, but as a **contextual Role Assignment**.
2.  Introduce a measurable, multi-dimensional **spectrum of agency** via a dedicated Characterization (`Agency-CHR`), moving beyond a simple binary "agent/not-agent" switch.
3.  Provide a clear, **didactic grading system** that allows engineers and managers to assess and communicate the Agency Grade of any system in a consistent, evidence-backed manner.

