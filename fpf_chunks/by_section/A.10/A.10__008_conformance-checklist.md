---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
section_id: "A.10:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__008_conformance-checklist.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "A.10 — Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
  - "A.10:6 — Conformance Checklist"
line_start: 22894
line_end: 22906
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.PROD"
  - "A.19"
  - "A.2-family"
  - "A.2.4"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.10.ROLE"
  - "E.17"
  - "F.6"
  - "G.11"
  - "G.4"
keywords:
  - "RelianceDisposition"
  - "actual-use relation"
  - "bounded use"
  - "carrier"
  - "claim/result episteme"
  - "currentness"
  - "dated work"
  - "direct relation"
  - "evidence-provenance path"
  - "relied-on claim"
  - "rival explanation"
  - "source publication"
  - "unsupported overread"
---

### A.10:6 - Conformance Checklist

1. **Claim:** the exact relied-on C.2.1 episteme and proposition/local result are named.
2. **Result rule:** every measurement, formal, causal, diagnostic, conformance, comparison, selection, acceptance, gate, permission, commitment, system-role-kind classification, system-role-assignment occurrence or state, relation among system-role kinds, or decision result identifies the pattern that defines or tests it; any other technical *role* use is first routed through E.10.ROLE.
3. **Carrier/source:** the selected source episteme and edition, any material publication occurrence, form, carrier, or face, the copy/transform chain, and direct provenance or citation relations are recoverable.
4. **Work:** whenever production, interpretation, transformation, evaluation, or reliance is asserted as dated `U.Work`, point to its complete A.15.1/F.6 basis. Add direct relations, A.6.1 bindings, and resource-use facts only when the receiving claim uses them. Ordinary source-finding action need not be admitted as `U.Work`.
5. **MethodDescription boundary:** the description contains only generic method claims; it supplies no actual participants, occurrence, use, proof/test event, or result.
6. **Result boundary:** domain result, result episteme, carrier, provenance entry, outcome, and later action remain distinct.
7. **Graph boundary:** every asserted edge names an independently established direct relation; no edge establishes work, participation, production, result, currentness, reliance, or representation by graph membership.
8. **Time/currentness:** edition, window, supersession, revocation, source order, and G.11 result are explicit when they affect use.
9. **Reliance:** bounded use, unsupported attempted use, local `RelianceDisposition`, rival explanation, and reopen trigger are present; B.3 opens only when an actual named assurance claim is current.
10. **Contest/privacy:** the affected party can challenge the claim and disposition, while sensitive carrier access is minimized without erasing recoverability.

