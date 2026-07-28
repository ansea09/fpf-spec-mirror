---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent (Promise Content)"
section_id: "A.2.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__004_problem-frame.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "A.2.3 — U.PromiseContent (Promise Content)"
  - "A.2.3:1 — Problem frame"
line_start: 3210
line_end: 3223
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8"
  - "A.2.9"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "A.6.8"
  - "A.6.C"
  - "A.7"
  - "C.2.1"
  - "E.10"
  - "F.12"
  - "F.9"
  - "U.Capability"
  - "U.ClaimScope"
  - "U.Episteme"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Work"
  - "U.WorkPlan"
  - "U.WorkScope"
keywords:
  - "SLA"
  - "SLO"
  - "Work evidence"
  - "acceptanceSpec"
  - "accessSpec"
  - "claim scope (G)"
  - "promise content"
  - "provider/consumer roles"
---

### A.2.3:1 - Problem frame

Across domains the word **service** is used for many different things: a server or **provider**, an **API**, a **procedure**, a **run**, a **department**, even a **product bundle**. Such polysemy is productive in everyday speech but toxic in a normative model.

FPF therefore reserves **`U.PromiseContent`** for one kernel meaning: a consumer-facing **promise content** clause. When "service" denotes something else, recover the current referent: a provider or access point as `U.System`, provider participation as `U.RoleAssignment`, an access description as `U.MethodDescription`, performed delivery as `U.Work`, or the named direct relation governed by its own pattern. Normative prose uses an explicit facet head phrase per **A.6.8 (RPR-SERV)**.

This keeps the kernel minimal while keeping the prose readable to non‑mathematicians: the canonical symbol is `U.PromiseContent`, and the head kind in normative text is always *promise content*.

**Modularity note.** A.2.3 defines the promise-content episteme and `PromiseContentUse`. Role assignment, access specification, delivery work, actual operation application and result binding, result-episteme identity, affected-subject change, A.10 evidence relations, evaluation, commitment, delivery, acceptance, speech act, and publication remain with their direct governing patterns. A.6.8 restores which service facet the wording denotes; it does not replace the named participants and their direct relations with a locally minted service-situation relation. A.6.C governs the Contract Bundle lens when contract, SLA, or guarantee wording must be unpacked.

**Plain reading.** Promise content says what a consumer may rely on. A system holding the provider role through a named `U.RoleAssignment` occurrence performs delivery work by enacting a `U.Method`; a `U.MethodDescription` describes that method. `PromiseContentUse` obtains between the delivery-work occurrence and the selected promise-content edition during the named interval. Exact work-participation, affected-referent, actual-change, delivery, and acceptance relations state what happened. A separately performed evaluation applies the declared operation or method; its actual result binding states the evaluation value. If another use needs a verdict episteme, C.2.1 governs that episteme and A.15.PROD governs any current entity-identity-inception claim. Evidence relations support the relied-on assertions. No universal work-result relation is presumed.

**Lexical note (L-SERV and RPR-SERV).** Bare *service* does not determine one FPF referent. When that word carries a relied-on claim, use A.6.8 to select the service facet: for example, a promise-content episteme and an access-point system have different kinds and participate in different relations. E.10 `L-SERV` triggers that recovery; after the facet is known, its direct governing pattern applies.

