---
chunk_kind: "child"
pattern_id: "A.6.8"
pattern_title: "Service Polysemy Unpacking (RPR‑SERV)"
section_id: "A.6.8:7"
section_title: "Conformance Checklist (CC‑A.6.8)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.8/A.6.8__008_conformance-checklist-cc-a-6-8.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.6.8 — Service Polysemy Unpacking (RPR‑SERV)"
  - "A.6.8:7 — Conformance Checklist (CC‑A.6.8)"
line_start: 20052
line_end: 20094
dependencies:
  - "A.15"
  - "A.2.3"
  - "A.2.8"
  - "A.2.9"
  - "A.6.5"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "C.26.1"
  - "C.26.3"
  - "E.10"
  - "E.15"
  - "F.17"
  - "F.18"
  - "F.8"
  - "U.Commitment"
  - "U.PromiseContent"
  - "U.SpeechAct"
  - "U.Work"
keywords:
  - "API read/export"
  - "boundary exchange"
  - "interface semantics"
  - "promise content"
  - "provider principal"
  - "service polysemy"
  - "service situation"
  - "service/cell analogy"
  - "viability envelope"
---

### A.6.8:7 - Conformance Checklist (CC‑A.6.8)

0. **CC‑A.6.8‑0 — UTS/LEX block exists for the service cluster.**
   Any document that applies this pattern (or that introduces normative “service” language) SHALL publish:
   (a) a local **UTS block** (F.17), and
   (b) paired **LEX‑BUNDLE entries** (E.10) for the Tech/Plain twins and PTG stances used here.
   +   Minimum cluster coverage SHALL include: `service`/`services`, `service provider`, `server`, `microservice`/`microservices` **when present in the source prose**, plus the chosen facet head phrases. If the document uses “API service / service interface / service access” or SLA/SLO/service‑level language, the local UTS/LEX block SHALL include those lexical forms as well.
   Each SenseCell SHALL cite ContextName@Edition; cited contexts SHOULD not be “FPF only”.
   Any newly introduced facet head phrase SHALL have an explicit Mint/Reuse decision (F.8) and SHOULD have a Name Card rationale (F.18).

1. **CC‑A.6.8‑1 — Unqualified “service” (and cluster stand-ins) is unsupported in normative prose.**
   A conforming boundary/spec text SHALL NOT use **service** as an unqualified head noun, and SHALL NOT use **server** or bare **service provider** as untyped stand‑ins for the same collapsed bundle.
   Every such occurrence SHALL be rewritten to a facet head phrase (promise content, promised work-kind, service provider role or principal, service delivery system, service access point, service access spec, service commitment, service promise act, or service delivery work) or replaced with the correct underlying EntityOfConcern or project-side FPF kind (team, ticket, workflow, system, etc.).
   The facet head phrases in §4.3 are **canonical**; using **service** as the family-name modifier inside those phrases is valid and does not itself trigger further unpacking. Any local shorthand that drops the modifier is valid only under SERV-LEX-3.
   *Exception:* direct quotations may retain the original lexical form, but the surrounding normative prose SHALL immediately provide an unpacking rewrite.

2. **CC‑A.6.8‑2 — `U.PromiseContent` is referred to as a “promise content” in prose.**
   When the intended referent is `U.PromiseContent`, authors SHALL use “promise content” (or “service promise clause”) as the head phrase and SHALL NOT rely on the bare word “service”.

3. **CC‑A.6.8‑3 — Addressability implies `accessPointRef` (system), not clause.**
   Any statement implying invocation/connection/deployment/restart SHALL target a service access point (`SystemRef`) and/or delivery work, never a promise content (`U.PromiseContent`).

4. **CC‑A.6.8‑4 — Deontic language requires a commitment.**
   Any normative “must/shall/guarantee/SLA” statement about service delivery SHALL introduce (or reference) a `U.Commitment` and attach the deontic force to that commitment/holder.
   In addition, a conforming text SHALL NOT use a service access point / server as the grammatical subject of an RFC‑keyword sentence; the subject is the accountable provider principal (or role assignment), with access‑point conditions stated as predicates/evidence.

5. **CC‑A.6.8‑5 — Performative verbs require a speech act.**
   Any statement using “promise/offer/accept/agree/announce/publish” about the service SHALL reference a `U.SpeechAct` (promise act) and SHALL NOT collapse it into the clause.

6. **CC‑A.6.8‑6 — Actuals require work + evidence.**
   Any claim about runtime state, telemetry, or incidents SHALL be stated as `U.Work` plus carrier/evidence references; it SHALL NOT be stated as a property of the promise content.

7. **CC‑A.6.8‑7 — Bundle lens is used when multiple facets are in play.**
   When a passage simultaneously discusses two or more facets (e.g., clause + endpoint + SLA + incident), the author SHOULD provide a `serviceSituation(…)` record (or equivalent explicit slot binding) so readers can track the linkage without guesswork.
   When a `serviceSituation(…)` record is provided, it SHALL satisfy SERV‑INV‑1, SERV‑INV‑2, and SERV‑WF‑1 from §4.2.
   When a `serviceSituation(…)` record is provided and it includes `commitmentRef` and/or `promiseActRef`, it SHALL also satisfy SERV‑WF‑2.

8. **CC‑A.6.8‑8 — Commitments and promises have an accountable principal.**
   Any statement that introduces a **service commitment** or **service promise act** SHALL name (directly or via role assignment) the **service provider principal** who is the holder/authorizer. A conforming text SHALL NOT attribute commitments/promises to a bare access point/server unless the Context explicitly models it as an agent with standing (and that modelling is declared).

9. **CC‑A.6.8‑9 — “How it works” claims belong under method or system, not under the clause.**
   Any statement about implementation, mechanism, workflow, runbook, or process SHALL name **service delivery system**, **service delivery method**, or **access spec** as applicable. It SHALL NOT be stated as a property of the promise content.

