---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants (UNM)"
section_id: "A.19.UNM:11"
section_title: "SoTA-Echoing — preserve the answer needed after normalization"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__013_sota-echoing-preserve-the-answer-needed-after-normalization.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants (UNM)"
  - "A.19.UNM:11 — SoTA-Echoing — preserve the answer needed after normalization"
line_start: 35064
line_end: 35075
dependencies:
keywords:
  - "CV→NCV"
  - "NormalizationFixSpec"
  - "NormalizationInvariant[*]"
  - "NormalizationMethodId"
  - "NormalizationMethodInstanceId"
  - "fail-closed tri-state guard (pass"
  - "normalization"
  - "validity window (no implicit “latest”)"
  - "≡_UNM"
---

### A.19.UNM:11 - SoTA-Echoing — preserve the answer needed after normalization

**Practice question.** May a receiver answer its original query from normalized values after the transformation merges inputs? The selected best-known line checks whether that query is constant on each fiber of the declared function. A serious alternative keeps only bounded normalized values and uses a representative or inverse-transform interface for later queries. The latter is convenient when the receiver deliberately accepts the lost distinctions; it is insufficient for recovering an exact original-input answer that differs within a fiber.

The [Lean reference on quotients](https://lean-lang.org/doc/reference/latest/The-Type-System/Quotients/) supplies the mathematical line: lifting a function requires equal results for equivalent representatives. It also describes canonical-representative implementations as a useful alternative representation. **Adopt** the query-constancy criterion in §4.0, UNM-L2 and §4.4. **Reject** the inference that choosing a representative recovers an original-input query: the representative defines a choice, and recovery still needs constancy. These are mathematical conditions; using Lean or constructing a proof-assistant artifact is not required by UNM.

The [scikit-learn 1.9 MinMaxScaler documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html) supplies a concrete current preprocessing alternative and its declared trade-off. Optional clipping keeps held-out values in the chosen range, while its documentation warns that inverse transformation may not restore the original data and that clipping can distort the test distribution. **Adapt** this explicit loss disclosure as a receiving-use check, rather than banning bounded preprocessing or treating the software interface as evidence of invertibility.

For example, a declared clipped transform n(x)=min(1,max(0,x/100)) sends 120 and 150 to 1. The query “was x above 130?” gives different answers, so it cannot be recovered from that NCV or its class representative. Keep the original value, refine the output with the needed distinction, or return the unresolved answer allowed by the receiving rule. This is the same test used by the finite-domain example in §5 and the Result branch checklist; separately inherited partial operations also retain their availability check.

At comparable effort, both choices use the same declared transform and query. One counterexample within a fiber can settle failure cheaply; a positive exact-recovery claim needs a constancy argument over the admitted domain, not just sampled successes. Keeping additional input information has a storage/handling cost, while clipping can be appropriate for a model that only needs its bounded input. The chosen rule makes that trade-off explicit and leaves ordinary transformed-value use cheap. Reopen when the receiver changes its query, the transformation or domain changes, or a proposed smaller representation retains the required answer with a sound argument. Neither software documentation nor the quotient theorem supplies measurement legitimacy, evidence sufficiency or assurance for a particular application.

