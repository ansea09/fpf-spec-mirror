---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__002_use-this-when.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:0 — Use This When"
line_start: 99571
line_end: 99589
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.PUB"
  - "F.0.1"
  - "F.1"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:0 - Use This When

Use `F.18` when a name must become stable, public, Core-facing, reusable under more than one named source, practice, or reference scheme, or durable enough that later work can cite it without guessing. Typical cases:

- a local expression becomes a durable name for a system-role kind, relation, slot, method, work, characteristic, status value, architecture element, or other already governed value;
- two teams use different words for the same candidate sense and need one reusable term plus preserved local wording;
- one tempting head word is useful under one recovered local meaning but misleading under another;
- a system-role-derived, method-derived, status-like, evidence-like, interface-like, or slot-like name risks creating a second ontology by wording alone.

**First useful move.**

1. Recover the exact value and the pattern containing its defining or testing rule.
2. Decide whether ordinary local wording is enough or later use really needs a durable name.
3. If a durable name is needed, compare the plausible names and record one Tech label, one Plain explanation, the selection reason, and the reopen condition in a `NameCard`.

If bare claim-bearing *role* still hides the object, use `E.10.ROLE`; if relation, slot, interface, port, or signature wording hides it, use section 5.6. Open section 4.4 only for a genuinely public, Core-facing, durable-across-context, or cross-context use. A public row is a later result, never part of the first naming move.

Do not use `F.18` for one-off wording repair. If the phrase is local and not becoming a reusable name, use `E.10`, `E.10.ARCH`, `A.6.P`, `A.6.RSIR`, `C.2.P`, or the pattern containing the rule for the object being named. In particular, say in ordinary words whether one exact Bridge is suitable for one named use; do not create a `NameCard`, public claim kind, or durable CamelCase head merely to abbreviate that C.2.1 claim. Reopen F.18 for that claim only when an independent later use actually needs a reusable name beyond the local statement.

