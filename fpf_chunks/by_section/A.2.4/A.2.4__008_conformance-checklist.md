---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__008_conformance-checklist.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:7 — Conformance Checklist"
line_start: 3640
line_end: 3656
dependencies:
  - "A.10"
  - "A.2"
  - "A.2.1"
  - "A.2.4"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.17.EFP"
  - "F.10"
  - "G.6"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "claim"
  - "episteme"
  - "evidence-use"
  - "provenance"
  - "source-use"
  - "status-use"
---

### A.2.4:7 - Conformance Checklist

| Check | Pass condition |
| --- | --- |
| `CC-A2.4-1` Episteme boundary | The evidence or status bearer is identified as `U.Episteme`, publication face, claim, status bearer, or another direct-pattern bearer; no episteme is placed in `U.RoleAssignment` merely because it is used. |
| `CC-A2.4-2` Target relation | Evidence use names the target claim or effect when claim-bound; status use names the status bearer, status value, and target when needed. |
| `CC-A2.4-3` Grounding and scope | Claim grounding holon, claim scope, status scope, or use scope is named when changing it would change the relation or admissible use. |
| `CC-A2.4-4` Polarity and value | Evidence polarity or status value is explicit when the use depends on it. |
| `CC-A2.4-5` Time and freshness | Relevance window, theory-version fence, freshness policy, status window, or source-currentness relation is explicit when the use is time-sensitive. |
| `CC-A2.4-6` Provenance | External producing work, source, publication, proof check, measurement, method description, register, or evidence-provenance relation is named when it decides admissible use. |
| `CC-A2.4-7` Assurance boundary | Assurance, readiness, safety, compliance, release confidence, trust, `F`, `G`, `R`, or `CL` claims go to `B.3`; A.2.4 only supplies typed evidence-use or status-use relation positions. |
| `CC-A2.4-8` Causal boundary | Causal-use and counterfactual claims go to `C.28`; A.2.4 does not mint causal evidence kinds. |
| `CC-A2.4-9` Work boundary | The producing work remains `U.Work`; the episteme use remains evidence-use or status-use. |
| `CC-A2.4-10` Publication boundary | Publication face, source citation, generated explanation, credential view, or dashboard display is not treated as evidence-use or status-use until the relation is recoverable. |
| `CC-A2.4-11` No evidence/status role ontology drift | Live prose does not teach `U.EvidenceRole`, status role for epistemes, episteme role holder, or evidence-role assignment through `U.RoleAssignment`. |
| `CC-A2.4-12` Direct governing pattern | The statement names the direct pattern that owns the current use: `A.10`, `B.3`, `C.2.1`, `C.28`, `F.10`, `G.6`, `E.17`, `E.10.D2`, or another governing pattern named by value. |

