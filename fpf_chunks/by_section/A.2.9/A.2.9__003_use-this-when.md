---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Object)"
section_id: "A.2.9:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__003_use-this-when.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Object)"
  - "A.2.9:0 — Use This When"
line_start: 5642
line_end: 5673
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.6.C"
  - "A.7"
  - "U.Work"
keywords:
  - "act≠utterance≠carrier"
  - "approval/authorization/publication/revocation"
  - "communicative work"
  - "institutes"
  - "judgement context"
  - "provenance"
  - "speech act"
  - "window/freshness"
---

### A.2.9:0 - Use This When

Use this pattern when a communicative event must be modeled as performed work: an approval, authorization, revocation, notice, declaration, publication, or similar act whose occurrence changes what a project can claim or do.

**What goes wrong if missed.** A document, interface, ticket, message, or log is treated as if it performed the act; approval, utterance content, evidence carrier, commitment, and performed work collapse into one governance phrase.

**What this buys.** Communicative acts become inspectable `U.Work` occurrences with performer, context, time window, affected referents, and evidence links while utterance descriptions and carriers stay separate.

Typical moments:

- a release, gate, or work step depends on whether a named approval or authorization was performed;
- a publication, notice, or revocation changes status in a bounded context;
- a commitment must cite the act that instituted it, rather than only pointing at a document;
- a message, ticket, signed record, or API call log is being mistaken for the act itself.

**Primary EntityOfConcern.** The EntityOfConcern is `U.SpeechAct`: a communicative work occurrence performed by an accountable role-assignment in a bounded context. The utterance content is a description episteme; the file, message, ticket, or log is a carrier or evidence record.

**First useful move.** Name the performer, judgement context, time window, act type, affected referents, and any instituted effects by reference. Add utterance or carrier references only when they are needed for observation, audit, or source return.

**Not this pattern when.** If the question is only what a document says, use A.7/C.2/E.17. If the question is who is accountable under a deontic relation, use A.2.8. If the question is evidence, use A.10/G.6. If the work has no communicative effect, use A.15.1 directly.

> **Type:** Definitional (D)
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A → **A.2 Roles & Agency Kernel**
> **Refines:** A.2 (Role Taxonomy)
> **Builds on:** A.2.1 (RoleAssignment), A.2.6 (`Γ_time` and windows), A.7 (EntityOfConcern, Description episteme, and carrier), A.10 (SCR/RSCR carrier discipline), A.15.1 (`U.Work`)
> **Purpose (one line):** Provide a minimal, lintable kernel object for **communicative enactments** (approvals, authorizations, revocations, notices, declarations, publications) as **`U.Work`**, explicitly separating the **act** from its **utterance descriptions** and **evidence carriers**, so governance and gate checks can cite `SpeechActRef` without deontic ambiguity or episteme-as-agent mistakes.

> FPF already treats communicative acts as observable events used in role-state checklists and grounding (“presence of act: AuthorizationSpeechAct exists…”, and `U.SpeechAct` is listed as observable evidence for state assertions).
> The spec’s micro-examples and conformance gates distinguish **communicative Work** (“performed a SpeechAct”) from **operational Work** (“executed Work”) while keeping both inside `U.Work` (cf. CC‑A15‑10 GateSplit).
> F.18 can name `U.SpeechAct` in the promise/utterance/commitment triad; A.2.9 keeps the ontology and conformance discipline in Part A where communicative work, utterance description, and evidence carrier can be kept distinct.

