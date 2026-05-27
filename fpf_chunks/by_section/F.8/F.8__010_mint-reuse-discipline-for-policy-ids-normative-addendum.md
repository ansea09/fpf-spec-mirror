---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
section_id: "F.8:8.1"
section_title: "Mint/Reuse discipline for policy-ids (normative addendum)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__010_mint-reuse-discipline-for-policy-ids-normative-addendum.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "F.8 — Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
  - "F.8:8.1 — Mint/Reuse discipline for policy-ids (normative addendum)"
line_start: 67787
line_end: 67809
dependencies:
  - "A.11"
  - "A.7"
  - "A.8"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "decision lattice"
  - "minting new types"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:8.1 - Mint/Reuse discipline for **policy-ids** (normative addendum)

FPF treats **policy-ids** (e.g., `Φ(CL)`, `Φ_plane`, `Ψ(CL^k)`, `Aut-Guard`, `EmitterPolicyRef`, `InsertionPolicyRef`, Acceptance clause ids) as **first-class, versioned tokens**. They are not “just strings”, and they are not governed by tier ladders or implied authority.

**PolicySpecRef.** A **resolvable reference** to the normative definition of a policy-id (“what does this policy-id mean?”). At minimum it:
* identifies the policy-id,
* pins an immutable edition (or equivalent digest), and
* can be located from the same publication bundle (MVPK / UTS / EvidenceGraph anchors).

**MintDecisionRef.** A **resolvable reference** to the decision record that introduced (minted) a policy-id into a declared namespace/registry. For **normative** policy-ids this is typically a **DRR id** (E.9) or an equivalent change decision record. For **purely local, non-exported** policy-ids it MAY be a Gate `DecisionLog` entry (A.21) if that local-only scope is explicit.

**PolicyIdRef (canonical bundle).**
`PolicyIdRef := { policy_id, PolicySpecRef, MintDecisionRef? }`.

**Rules.**
1. **No silent policy-id minting.** If a publication introduces a *new* policy-id (not previously present in the declared namespace/registry), it **MUST** surface a `PolicyIdRef` whose:
   * `PolicySpecRef` is edition-pinned, and
   * `MintDecisionRef` is resolvable from the publication’s DRR/DecisionLog links.
2. **Reuse is reference-only.** If a publication **reuses** an existing policy-id, it **MUST** surface a `PolicySpecRef` (and **SHOULD** preserve the prior mint decision link where available). It **MUST NOT** restate policy semantics *as if* minting a new policy-id.
3. **GateCrossing checkability.** Any GateCrossing/CrossingBundle that surfaces policy-ids **MUST** include `PolicyIdRef` (or an equivalent “policy-id + resolvable refs” structure) so GateChecks can verify resolvability and pin consistency (E.18/A.21/G.6:7.5.8).
4. **Authority is policy, not tiers.** “Who may mint” vs “who may reuse” is expressed by the referenced **policy specs** and **mint decisions** (and enforced by the active GateProfile/GateChecks), not by fixed tier labels.


