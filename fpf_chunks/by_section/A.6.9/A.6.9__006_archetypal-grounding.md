---
chunk_kind: "child"
pattern_id: "A.6.9"
pattern_title: "U.CrossContextSamenessDisambiguation - Repairing cross-context “same / equivalent / align” via explicit Bridges (RPR‑XCTX)"
section_id: "A.6.9:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.9/A.6.9__006_archetypal-grounding.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.6.9 — U.CrossContextSamenessDisambiguation - Repairing cross-context “same / equivalent / align” via explicit Bridges (RPR‑XCTX)"
  - "A.6.9:5 — Archetypal Grounding"
line_start: 16748
line_end: 16815
dependencies:
  - "A.6.6"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.3.3"
  - "E.10"
  - "E.10.D1"
  - "E.10.U9"
  - "E.17"
  - "E.19"
  - "F.0.1"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "CL"
  - "SenseCells"
  - "alignment"
  - "bridge"
  - "cross-context sameness"
  - "direction"
  - "loss notes"
  - "mapping"
  - "substitution licence"
  - "weakest-link"
---

### A.6.9:5 - Archetypal Grounding

#### A.6.9:5.1 - System archetype: identity “sameness” across products

**Tell (ambiguous):**
“An IAM *User* is the same as a CRM *Customer*.”

**Show A (Bridge Card repair):**

```
BridgeId: β-IAM→CRM-UserCustomer (edition-pinned)
Cells: “User”@IAM ↔ “Customer”@CRM
senseFamily: Role
kind: ⋂
dir: IAM↔CRM
CL: 2 (Translatable) — high overlap; service accounts and leads/prospects are counterexamples
Loss:
  - CRM “Customer” includes leads/prospects with no IAM account
  - IAM “User” includes service accounts and disabled identities not treated as customers
Counter-example: “svc-billing@” is a User@IAM but not a Customer@CRM
scope: Naming-only
Didactic hook: “Overlap only: share labels; do not substitute without guards/refinement.”
```

**Effect:** dashboards and prose may share labels (Naming‑only). Workflow substitution is *not* implied globally; it is gated by scope and guards.

**Show B (change narration, later evidence):**
After hard constraints are added (e.g., “human‑verified email”, “not a service account”), a team wants higher-licence reuse in the ticketing integration.

*Do not write:* “Now they are equivalent / now the mapping is fixed.”
*Write:*

0. Keep the broad Bridge **as‑is** (Naming‑only, overlap): it remains the correct “shared label” relation for the unguarded endpoints.
1. `refreshWitnesses(β-IAM→CRM-UserCustomer, witnessRefs→witnessRefs ∪ {TicketingIntegrationTestSuite_v3})`
2. `declareBridge(β-IAM→CRM-HumanVerifiedUser→VerifiedCustomer, HumanVerifiedUser@IAM, VerifiedCustomer@CRM, …slots…)` (new Bridge id or new edition family)
3. In that new Bridge: state `kind=⊑` (if inclusion is now true for the refined endpoints), `dir=IAM→CRM`, keep `CL=2`, restate Loss (remaining exclusions), and provide a crisp counter‑example for where substitution would still break.
4. `rescope(β-IAM→CRM-HumanVerifiedUser→VerifiedCustomer, Naming‑only → Role Assignment & Enactment‑eligible)` with DRR explaining why `CL=2` suffices for the refined endpoints.

Direction remains IAM→CRM; if the inverse is required, declare a separate Bridge with its own loss/counterexamples.

#### A.6.9:5.2 - Episteme archetype: schema/ontology alignment between knowledge graphs (class-level)

**Tell (ambiguous):**
“`Person` in KG‑A is equivalent to `Person` in KG‑B.”

**Show A (Bridge Card repair):**

```
BridgeId: β-KGA↔KGB-Person (edition-pinned)
Cells: Person@KG-A ↔ Person@KG-B
senseFamily: Type-structure
kind: ⋂
dir: A↔B
CL: 2 (Translatable) — overlap is high but invariants differ
Loss:
  - KG-A “Person” includes fictional characters; KG-B excludes them
  - KG-B requires a stable external identifier; KG-A does not
Counter-example: “Sherlock Holmes” ∈ Person@KG-A but ∉ Person@KG-B
scope: Naming-only
Didactic hook: “Shared label does not grant type-structure or substitution; the sets only overlap until invariants and membership rules are aligned.”
```

**Show B (strengthening attempt and rejection):**
A reviewer proposes Type‑structure reuse (“treat them as the same class across graphs”). Under A.6.9, this triggers a required invariant check:

* Since Type‑structure reuse requires CL=3 and matched invariants, the proposal is rejected unless the invariants are aligned and the counterexample class is eliminated (e.g., by refining `Person@KG-A` into `FictionalPerson` vs `RealPerson`).
* The correct change narrative is: `changeBridgeKind` (if kind changes), `adjustCL` only if the counterexample disappears and invariants are shown, else keep CL=2 and Naming‑only scope.

