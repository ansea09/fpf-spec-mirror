---
chunk_kind: "child"
pattern_id: "A.6.RSIR"
pattern_title: "Relation, Signature, Interface, Role, and Slot Precision Restoration"
section_id: "A.6.RSIR:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIR/A.6.RSIR__002_use-this-when.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.6.RSIR — Relation, Signature, Interface, Role, and Slot Precision Restoration"
  - "A.6.RSIR:0 — Use This When"
line_start: 14647
line_end: 14664
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.0"
  - "A.6.5"
  - "A.6.A"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "C.2.P"
  - "C.2.P.DR"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "F.10"
  - "F.18"
  - "F.19"
  - "G.6"
keywords:
  - "API"
  - "affordance"
  - "capability"
  - "concern"
  - "endpoint"
  - "field"
  - "function"
  - "interest"
  - "interface wording"
  - "method"
  - "parameter"
  - "port"
  - "protocol"
  - "relation-signature-interface-role-slot recovery"
  - "role wording"
  - "shadow ontology"
  - "slot wording"
---

### A.6.RSIR:0 - Use This When

**Plain name.** Relation-signature-interface-role-slot recovery.

Use this pattern when relation, signature, interface, role, role-holder grammar such as `Holder#Role:Context`, assignment, enactment, slot, field, parameter, argument, endpoint, port, API, protocol, capability, affordance, method, function, concern, interest, Markov-blanket, computational-boundary, or active-inference-boundary wording hides which FPF object or claim kind is current.

**Primary EntityOfConcern.** The EntityOfConcern is the RSIR wording-use situation: a source or FPF-governed phrase whose local project concern may point to a relation, relation slot, signature, interface claim, role value, role assignment, role description, port, boundary claim bundle, or plain source label.

**Primary working reader.** The first reader is an FPF pattern author, reviewer, or practitioner repairing a phrase before selecting the direct governing pattern. The downstream reader is the engineer, manager, analyst, or steward who needs the repaired phrase to preserve useful project language without minting a shadow ontology.

**First useful move.** Recover the project concern first, then recover the current governed EntityOfConcern or claim kind. Apply the direct governing pattern as soon as it is clear. Keep a reduced-use source label only when no governed value is being asserted.

**What goes wrong if missed.** The same phrase becomes several ontologies. "Interface" becomes API, signature, port, compatibility evidence, and module boundary. "Role" becomes work role, argument position, evidence status, and access badge. "Parameter" becomes SlotKind, ValueKind, RefKind, and field at once. "Function" becomes capability, method, work, mathematical function, and architecture structure.

**What this buys.** The reader gets one small recovery move before the direct pattern is applied. The repair preserves useful engineering words while preventing a lexical cue from minting a new root kind or hiding a relation slot.

**Not this pattern when.** Do not use `A.6.RSIR` after the direct governing pattern is already clear. Do not use it for general relation repair after `A.6.P` is selected, for slot discipline after `A.6.5` is selected, for function-like repair after `A.6.F` is selected, for module-interface repair after `A.6.M` is selected, for transformation wording after `A.3.4.P` is selected, or for publication and description repair after `E.17`, `C.2.1`, or `C.2.P.DR` is selected.

