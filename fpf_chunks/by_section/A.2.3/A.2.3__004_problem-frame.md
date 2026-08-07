---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent (Promise Content)"
section_id: "A.2.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__004_problem-frame.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "A.2.3 — U.PromiseContent (Promise Content)"
  - "A.2.3:1 — Problem frame"
line_start: 3676
line_end: 3689
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
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
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

FPF therefore reserves **`U.PromiseContent`** for one kernel meaning: a consumer-facing **promise content** clause. When *service* denotes something else, use **A.6.P:4.11a** to recover whether it denotes code or another episteme, a Method, Work/run, provider participation, an exact bearer or access-providing arrangement, permission, status, or a direct relation. A product label chooses none of these readings, and bare *service* has no default system reading. After recovery, name the referent or relation. Apply A.1/A.1.SCR only when the recovered referent is an entity and the claim depends on its being a system.

This keeps the kernel minimal while keeping the prose readable to non‑mathematicians: the canonical symbol is `U.PromiseContent`, and the head kind in normative text is always *promise content*.

**Modularity note.** A.2.3 defines the promise-content episteme and `PromiseContentUse`. It does not redefine role assignment, access specification, delivery work, actual operation application and result binding, result-episteme identity, affected-subject change, A.10 evidence relations, evaluation, commitment, delivery, acceptance, speech-act, or publication claims; use the patterns that define or constrain those claims. A.6.P:4.11a recovers which concrete service/access referent or relation the wording denotes; it does not replace the named participants and their direct relations with a locally minted service-situation relation. A.6.C governs the Contract Bundle lens when contract, SLA, or guarantee wording must be unpacked.

**Plain reading.** Promise content says what a consumer may rely on. A system holding the provider role through a named `U.RoleAssignment` occurrence performs delivery work by enacting a `U.Method`; a `U.MethodDescription` describes that method. `PromiseContentUse` obtains between the delivery-work occurrence and the selected promise-content edition during the named interval. Exact work-participation, affected-referent, actual-change, delivery, and acceptance relations state what happened. A separately performed evaluation applies the declared operation or method; its actual result binding states the evaluation value. If another use needs a verdict episteme, C.2.1 governs that episteme and A.15.PROD governs any current entity-identity-inception claim. Evidence relations support the relied-on assertions. No universal work-result relation is presumed.

**Lexical note (L-SERV and A.6.P:4.11a).** Bare *service* does not determine one FPF referent. When that word carries a relied-on claim, use A.6.P:4.11a to recover the concrete referent or relation: for example, a promise-content episteme and an access-point system have different kinds and participate in different relations. E.10 `L-SERV` triggers that recovery. After recovery, name the referent or relation and use the pattern that defines or constrains the current claim. Resolve the defining or constraining `ClaimGraph` only when this claim or a named later use depends on a particular rule edition; the pattern id then serves as its locator.

