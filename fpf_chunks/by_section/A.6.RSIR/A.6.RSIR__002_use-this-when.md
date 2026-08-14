---
chunk_kind: "child"
pattern_id: "A.6.RSIR"
pattern_title: "Relation, Signature, Interface, Role, and Slot Precision Restoration"
section_id: "A.6.RSIR:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIR/A.6.RSIR__002_use-this-when.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.6.RSIR — Relation, Signature, Interface, Role, and Slot Precision Restoration"
  - "A.6.RSIR:0 — Use This When"
line_start: 17044
line_end: 17061
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.3.4.P"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.A"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.17"
  - "F.10"
  - "F.18"
  - "F.19"
  - "G.6"
keywords:
  - "API"
  - "RelationSignature"
  - "SlotSpec"
  - "ambiguous role wording"
  - "direct relation participant"
  - "interface"
  - "operation declaration and binding"
  - "participant meaning"
  - "port"
  - "reduced-use source label"
  - "relation-signature-interface-role-slot recovery"
  - "representation position"
  - "system-role assignment"
  - "system-role kind"
---

### A.6.RSIR:0 - Use This When

**Plain name.** Relation-signature-interface-role-slot recovery.

Use this pattern when relation, signature, interface, assignment, enactment, slot, field, parameter, argument, endpoint, port, API, protocol, connector, capability, affordance, method, function, concern, interest, Markov-blanket, computational-boundary, or active-inference-boundary wording hides which FPF object or claim kind is current. When the unresolved starting cue is bare claim-bearing *role*, start with `E.10.ROLE`; return here only if the recovered branch concerns direct participation, a declaration, an interface, an operation, or a representation position.

**Primary EntityOfConcern.** The EntityOfConcern is one encountered use of an ambiguous engineering phrase together with the claim that this use is intended to carry. RSIR recovers the direct governed object, direct relation and participant meaning, actual participant, declaration-local `SlotSpec` or operation declaration, exact operation application and binding, assertion- or description-side designation, representation position and correspondence, or claim before selecting its subject pattern. The phrase remains wording in an episteme or in speech; it is not the world-side object, occurrence, value, or relation named by the recovered claim.

**Primary working reader.** The first reader is an FPF pattern author, reviewer, or practitioner repairing a phrase before selecting the subject pattern. The downstream reader is the engineer, manager, analyst, or steward who needs the repaired phrase to preserve useful project language without minting a shadow ontology.

**First useful move.** Recover the project concern first, then recover the current governed EntityOfConcern or claim kind. Apply the subject pattern as soon as it is clear. Keep a reduced-use source label only when no governed value is being asserted.

**What goes wrong if missed.** The same word is used for differently defined objects without saying which claim is current. For example, `interface` may denote an API description, reusable signature, functional port, compatibility claim, or module-boundary relation. Bare *role* may point to a system-role kind, one assignment, direct-relation participation, a declaration-local `SlotKind`, a representation position, use of an episteme, another object, or ordinary wording. A later reader then cannot recover which relation obtains, which participant is meant, which declaration is current, whether an exact operation application binds an actual value, or which representation correspondence is intended.

**What this buys.** The reader gets one small recovery move before the direct pattern is applied. The repair preserves useful engineering words while preventing a lexical cue from minting a new root kind or collapsing direct participation, reusable declaration, assertion or description, exact operation application and binding, and representation correspondence.

**Not this pattern when.** Do not use `A.6.RSIR` after the subject pattern is already clear. Do not use it for general relation repair after `A.6.P` is selected, for slot discipline after `A.6.5` is selected, for function-like repair after `A.6.F` is selected, for module-interface repair after `A.6.M` is selected, for transformation wording after `A.3.4.P` is selected, or for publication and description repair after `E.17`, `C.2.1`, or `C.2.P.DR` is selected.

