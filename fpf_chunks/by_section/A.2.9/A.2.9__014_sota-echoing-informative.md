---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct — Communicative Work and Its Intended Use"
section_id: "A.2.9:11"
section_title: "SoTA-Echoing (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__014_sota-echoing-informative.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.2.9 — U.SpeechAct — Communicative Work and Its Intended Use"
  - "A.2.9:11 — SoTA-Echoing (informative)"
line_start: 9010
line_end: 9018
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.2.9"
  - "A.6.C"
  - "A.7"
  - "F.6"
  - "U.Method"
  - "U.Work"
keywords:
  - "A.13-qualified actual performer"
  - "containment"
  - "enacted Method"
  - "evidence carrier"
  - "independently admitted speech-act Work"
  - "institutional target and effect"
  - "named receiving use"
  - "optional SpeechActRecord"
  - "publication relation"
  - "response versus achievement"
  - "same obtaining assignment"
  - "separate later performedUnderAssignment"
  - "smallest repair or stop"
  - "time"
  - "utterance description"
---

### A.2.9:11 — SoTA-Echoing (informative)

> **Informative.** Alignment notes; not normative requirements.

* **ISO 24617‑2:2020 / multi-dimensional communicative functions.** Modern dialogue‑act standards treat communicative behavior as potentially multi‑functional. A.2.9 mirrors this with an `actTypes` **set** on one communicative Work and permits shared carriers across several acts only when their world-side histories establish distinct occurrences.
* **Commitment-based semantics for communication (multi-agent/protocol practice, 2015+).** A pragmatic way to avoid mental-state modeling is to track communication by its **social/institutional effects**, especially on commitments, permissions, and protocol states. A.2.9 reflects this via separate `institutes.commitments` and `institutes.permissions` links to `U.Commitment` and `GrantedPermissionRelation@Context` without modeling sincerity or intention.
* **Illocutionary pluralism in multiparty discourse (2015+).** One utterance can perform multiple recognizable functions. A.2.9 avoids the “single force” trap by allowing several recognized functions on one act, while several acts sharing an utterance or carrier still require distinct occurrence grounds.
* **Purpose-relative grounding evidence and structured interaction.** Clark and Brennan's (1991) purpose-relative grounding principle is a historical anchor: evidence of understanding must be sufficient for the current purpose. Studies of grounding gaps in human–LLM dialogue (Shaikh et al., 2024, 2025) reinforce the risk of presumed shared understanding, while one structured-interface study (Do et al., 2024) shows that interaction structure can help in its tested setting. Section 5.1 applies that line by naming the receiving use and evidence first, then changing the wording, representation, prerequisite, medium or interaction that blocks it. A reply, silence or favourable outcome alone does not fix meaning, prove achievement or establish causal contribution. For the named receiving use, reconsider the affected evidence threshold or interaction choice when new evidence, changed participants, a changed medium or a failed source transfer invalidates its basis.

