---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge & CL^k — Cross‑context Mapping of Kinds"
section_id: "C.3.3:6"
section_title: "Norms & Invariants (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__007_norms-invariants-normative.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "C.3.3 — KindBridge & CL^k — Cross‑context Mapping of Kinds"
  - "C.3.3:6 — Norms & Invariants (normative)"
line_start: 45433
line_end: 45473
dependencies:
  - "A.2.6"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
  - "F.9"
keywords:
  - "CL^k"
  - "KindBridge direct relation"
  - "R penalty"
  - "bridge assertion episteme"
  - "loss"
  - "target judgment"
---

### C.3.3:6 - Norms & Invariants (normative)

> The following formalize the **KB‑01…KB‑12** rules announced in C.3.

#### C.3.3:6.1 - Direct relation subject and scope

**KB-01 (Participants and obtaining).** A `KindBridge` relation occurrence has exactly two direct participants: one source local kind and one target local kind. It obtains only under the named source and target reference-scheme editions when the directional correspondence predicate holds for the paired kind interpretations within declared definedness. Order preservation or collapse is not an obtaining condition for one pair relation; it is asserted separately over the relevant KindBridge and `U.SubkindOf` occurrences. The `KindSignature` epistemes used to evaluate the correspondence, their formality values, mapping expression, bridge assertion, evidence, `CL^k`, and loss notes are not relation participants.

**KB-02 (No Scope).** A KindBridge MUST NOT map Claim or Work scope G. Scope translation uses the USM Bridge + CL channel (A.2.6, Part B). `U.ContextSlice` values appear in bridge applicability and target judgments, not as scope stored on either kind.

**No blended score.** Congruence for Scope (CL) and for Kind (`CL^k`) MUST NOT be aggregated into a single interoperability score in guards; each channel is assessed and penalized separately. See Annex C.3.A §5 (E-06).

#### C.3.3:6.2 - Settlement, assertion, and identity

**KB-03 (Direct settlement).** The C.3.3 direct relation settlement SHALL make recoverable:

1. the exact source-kind and target-kind participants, direction, and source/target reference-scheme editions;
2. the directional mapping obtaining predicate and its definedness area, with no implicit `latest`; and
3. the occurrence-identity rule: when explicit identity is needed, source kind, target kind, direction, and both reference-scheme editions distinguish the occurrence.

A separate C.2.1 bridge-assertion episteme SHALL name the paired source and target `KindSignature` editions used to evaluate the predicate and, for the receiving use, state the mapping-rule expression, the status of each selected obtaining `U.SubkindOf` relation as preserved, collapsed, not preserved, or unknown, plus any current `CL^k`, loss notes, evidence, admitted use, and assertion polarity. Another assertion, mapping expression, card, row, signature edition, or publication edition does not create another relation occurrence. A changed assertion, signature, or mapping-rule edition prompts reevaluation of obtaining; it does not reidentify a continuing relation when the participants, direction, and scheme editions remain fixed and the same relation still obtains. A changed participant, direction, or scheme edition is another proposed occurrence and must establish obtaining independently.

**KB-04 (Determinism and local evaluation).** With fixed scheme versions and mapping-rule edition, the asserted bridge use MUST be reproducible. Independently, with fixed candidate, target `KindSignature` edition, TargetSlice, and target-declaration dependencies, evaluate reproducible `J(candidate, targetKind, targetSignatureEdition, TargetSlice)` in the target context. A source judgment or bridge assertion may support reliance but MUST NOT be copied into the target result. Preserve `unknown` only for a target judgment whose own declared evaluation cannot settle; an unsettled or inadmissible bridge use and the guard's refusal remain separate receiving predicates.

#### C.3.3:6.3 - Order & Monotonicity

**KB-05 (Monotone order).** If a bridge assertion states that source order fact `SubkindOfObtains(k1, k2; sourceRS)` is preserved, it SHALL designate exact target kinds `k1'` and `k2'`, the respective obtaining `KindBridge` relations from `k1` to `k1'` and from `k2` to `k2'`, and the basis on which `SubkindOfObtains(k1', k2'; targetRS)` holds. Identify a target `R_sub : U.SubkindOf` occurrence only when a receiving use needs occurrence identity.
**KB-06 (No inversions).** A bridge assertion MUST NOT state preservation when the mapped target order is inverted. If `SubkindOfObtains(k2', k1'; targetRS)` holds for distinct mapped kinds, state non-preservation and the exact loss. If the required target order cannot be settled, state `unknown`; do not turn non-settlement into either preservation or inversion.
**KB-07 (Collapse semantics).** A bridge assertion may classify selected source subkind distinctions as collapsed when several source kinds correspond to one target kind. The assertion SHALL designate the affected obtaining `U.SubkindOf` relations and state the lost properties; the direct bridge relation does not alter either local order.

#### C.3.3:6.4 - Congruence & Assurance

**KB-08 (Anchor reuse and AT neutrality).** `CL^k` reuses the ordinal anchor semantics of CL but assesses the declared bridge use over kind intent and order. The bridge-assertion episteme labels it kind-congruence. Neither the obtaining KindBridge relation nor its assertion computes or alters KindAT; AT is editorial and independent of `CL^k`.
**KB-09 (Effect on R only).** When a receiving claim relies on an obtaining KindBridge relation and on `J(candidate, targetKind, targetSignatureEdition, TargetSlice)`, apply the bridge-assertion episteme's monotone `Ψ(CL^k)` consequence to R alongside any independent scope-bridge penalty. Do not alter F or G. An `unknown` target judgment remains `unknown` even when the guard declines use.
**KB‑10 (Chaining).** For a chain of bridges, **effective `CL^k` = min** of the links (weakest‑link).

#### C.3.3:6.5 - Loss Notes & Definedness

**KB-11 (Loss notes).** The bridge-assertion episteme SHALL state which `KindSignature` invariants are not preserved, which obtaining source `U.SubkindOf` relations are collapsed or not preserved, and any higher-equality caveats. These claims do not rewrite the source or target kinds.
**KB-12 (Definedness and guard use).** The bridge obtaining predicate and assertion SHALL state the definedness area. Outside it, a receiving guard declines that cross-context bridge use. The independently evaluated target classification retains its own `true`, `false`, or `unknown` value; bridge inapplicability neither rewrites it nor denies that another bridge could obtain.

