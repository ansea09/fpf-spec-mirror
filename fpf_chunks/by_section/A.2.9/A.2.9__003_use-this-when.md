---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
section_id: "A.2.9:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__003_use-this-when.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
  - "A.2.9:0 — Use This When"
line_start: 6794
line_end: 6825
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.6.C"
  - "A.7"
  - "U.Method"
  - "U.Work"
keywords:
  - "actual communicative occurrence"
  - "admitted speech-act Work kind"
  - "authority-grounding assignment"
  - "evidence carrier"
  - "institutional target and effect"
  - "optional SpeechActRecord"
  - "performing U.System"
  - "publication relation"
  - "utterance description"
---

### A.2.9:0 - Use This When

Use this pattern when a communicative event must be modeled as performed work: an approval, authorization, revocation, notice, declaration, publication, or similar act whose occurrence changes what a project can claim or do.

**What goes wrong if missed.** A document, interface, ticket, message, or log is treated as if it performed the act; approval, utterance content, evidence carrier, commitment, and performed work collapse into one governance phrase.

**What this buys.** Actual communicative Work occurrences become inspectable without collapsing them into a claim-bearing `SpeechActRecord`, an utterance description, or an evidence carrier.

Typical moments:

- a release, gate, or work step depends on whether a named approval or authorization was performed;
- a publication, notice, or revocation may have an institutional effect only under an exact current policy or procedure, while the communicative act and any resulting effect retain distinct intervals;
- a commitment must cite the act that instituted it, rather than only pointing at a document;
- a message, ticket, signed record, or API call log is being mistaken for the act itself.

**Primary EntityOfConcern.** The EntityOfConcern is one actual speech-act occurrence admitted under the kind `U.SpeechAct`: communicative Work performed by an admitted accountable `U.System` under an exact obtaining `U.RoleAssignment` and enacting an exact `U.Method`. The assignment independently supplies the role, role-taxonomy episteme, effective reference scheme, authority ground, and covering extent; it does not act. Speech-act recognition separately uses an exact recognition-taxonomy episteme and effective reference scheme, plus a current policy or procedure only when classification or institutional force depends on it. A `SpeechActRecord`, MethodDescription, utterance-description episteme, channel, and file, message, ticket, or log carrier are separate objects.

**First useful move.** Name the actual occurrence, performer system, exact obtaining assignment, and exact enacted Method. Recover the assignment's role taxonomy and scheme; then name the act's time window, recognition-taxonomy episteme and effective scheme, satisfied act type, optional channel, and any current policy or procedure. Keep the optional MethodDescription, utterance subject, policy-selected institutional target, and independently established effect separate. Create a `SpeechActRecord` only when a receiving use needs a persistent claim about that occurrence; add utterance or carrier references only when observation, audit, or source return needs them.

**Not this pattern when.** If the question is only what a document says, use A.7/C.2/E.17. If the question is who is accountable under a deontic relation, use A.2.8. If the question is evidence, use A.10/G.6. If the work has no communicative effect, use A.15.1 directly.

> **Type:** Definitional (D)
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A → **A.2 Roles & Agency Kernel**
> **Refines:** A.2 (Role Taxonomy)
> **Builds on:** A.2.1 (RoleAssignment), A.2.6 (`Γ_time` and windows), A.7 (EntityOfConcern, Description episteme, and carrier), A.10 (SCR/RSCR carrier discipline), A.15.1 (`U.Work`)
> **Purpose (one line):** Admit communicative enactments under the `U.SpeechAct` kind, identify each actual Work occurrence, and provide a minimal optional `SpeechActRecord` for claims about it while keeping the act, record, utterance description, and evidence carrier separate.

> FPF already treats communicative acts as observable events used in role-state checklists and grounding (“presence of act: AuthorizationSpeechAct exists…”); those checks cite actual occurrences admitted under `U.SpeechAct`, not the kind itself.
> The spec’s micro-examples and conformance gates distinguish **communicative Work** (“performed a SpeechAct”) from **operational Work** (“executed Work”) while keeping both inside `U.Work` (cf. CC‑A15‑10 GateSplit).
> F.18 can name `U.SpeechAct` in the promise/utterance/commitment triad; A.2.9 keeps the ontology and conformance discipline in Part A where communicative work, utterance description, and evidence carrier can be kept distinct.

