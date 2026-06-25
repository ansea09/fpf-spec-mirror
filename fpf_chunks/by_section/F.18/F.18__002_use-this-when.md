---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__002_use-this-when.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:0 — Use This When"
line_start: 84429
line_end: 84441
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.RSIR"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1"
  - "F.1-F.17"
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

Use `F.18` when a name must become stable, public, Core-facing, reusable across contexts, or durable enough that later work can cite it without guessing. Typical cases:

- a local expression becomes a durable name for a role, relation, slot, method, work, characteristic, status value, architecture element, or other already governed value;
- two teams use different words for the same candidate sense and need one reusable term plus preserved local wording;
- one tempting head word is useful in one context but misleading in another;
- a role-derived, method-derived, status-like, evidence-like, interface-like, or slot-like name risks creating a second ontology by wording alone.

First useful move: recover the governed object or governed value before choosing the name. Ask: what already-governed value is being named, in which bounded context, by which governing pattern, for which use, and with which local sense? Only then decide whether a `NameCard` and, when public or cross-context use is current, a `UnifiedTermRow` are needed.

Do not use `F.18` for one-off wording repair. If the phrase is local and not becoming a reusable name, use `E.10`, `E.10.ARCH`, `A.6.P`, `A.6.RSIR`, `C.2.P`, or the governing pattern for the object being named.

