---
chunk_kind: "child"
pattern_id: "A.3.3.TR"
pattern_title: "Construct a Rule for State Change"
section_id: "A.3.3.TR:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.TR/A.3.3.TR__012_sota-echoing.md"
commit_sha: "acc387fc7a206495eabe07f1953849217f291715"
heading_path:
  - "A.3.3.TR — Construct a Rule for State Change"
  - "A.3.3.TR:11 — SoTA-Echoing"
line_start: 10069
line_end: 10082
dependencies:
  - "A.22.CGUS"
  - "A.3.3"
  - "A.3.3.CC"
  - "B.5.FM"
  - "B.5.MPC"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### A.3.3.TR:11 - SoTA-Echoing

**Working question and selected answer.** How can a reader construct a rule when several local operations or physical interactions jointly determine the change? The selected best-known line keeps their state relations available, combines jointly applicable relations, and retains alternative actions until the question or model selects among them. A serious alternative is a directly executable update procedure with a fixed order. That procedure is cheaper to apply when its order and effects already describe the required behavior; :1 therefore permits direct use of a suitable existing rule.

For the interference question in :5.1, choosing one execution order loses the alternative histories that can defeat the total. Retaining saved values and local instruction positions costs additional description and exploration, but a single lost-increment history already answers whether failure is possible. For the load question in :5.2, retaining the connection force makes that result calculable; eliminating it is useful when only motion is needed. The selected trade-off is to keep the relations and alternatives that can change the requested answer, and to stop at a sufficient result. **Adapt:** :4.1–:4.3 construct those contributions, :4.4 derives the consequence, and :4.5–:4.6 limit stronger claims and additional work.

**Discrete operations and proof.** Lamport's [Specifying Systems](https://lamport.azurewebsites.net/tla/book-02-08-08.pdf), chapters 2–3 and §5.7, supplies before/after actions, unchanged values and the distinction between reachable invariance and an inductive assertion. **Adopt** these constructions in :4.2–:4.4 and :5.1. TLA's stuttering and fairness conventions serve their stated modeling purposes; choose progress assumptions for the use in :4.5.

**Constrained interaction.** Tong's [Classical Dynamics, §2.3](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html) compares generalized coordinates and constraint-force treatment. **Adapt** the latter in :4.2 and :5.2 to retain the exchanged force when it is needed. Reduced coordinates offer a serious simpler alternative for motion alone. The cart derivation is an authored Newtonian case with its idealizations stated; another physical theory must supply its own relations.

**Coupled equations and events.** The [Modelica Language Specification 3.7, chapter 8](https://specification.modelica.org/maint/3.7/equations.html) supplies simultaneously satisfied equations, event semantics and consistent initialization. Its [DAE representation](https://specification.modelica.org/maint/3.7/modelica-dae-representation.html) separates continuous evolution and event processing: halt at a detected event, resolve its relations and restart integration. **Adapt:** :4.2–:4.3 keep joint relations distinct from evaluation order; :4.3.1 and :5.4 teach the continuous/event passage. Modelica supplies one explicit instantaneous-event convention; actual delays enter the model when consequential.

The joint Method is a conceptual synthesis whose comparison is supported by these constructions and their stated uses. Reopen the choice if a competing construction retains the same consequential continuations or interaction result at lower effort, or if an observed missing interaction, intermediate effect or event defeats the selected rule. Further Methods develop efficient exploration, proof, differential-equation solution and protocol design when the constructed rule requires that work.

