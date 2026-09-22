---
chunk_kind: "child"
pattern_id: "C.29.BB"
pattern_title: "Construct a Balance across a Boundary"
section_id: "C.29.BB:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.BB/C.29.BB__012_sota-echoing.md"
commit_sha: "acc387fc7a206495eabe07f1953849217f291715"
heading_path:
  - "C.29.BB — Construct a Balance across a Boundary"
  - "C.29.BB:11 — SoTA-Echoing"
line_start: 65413
line_end: 65426
dependencies:
  - "A.3.3.TR"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
  - "E.18.2"
keywords:
---

### C.29.BB:11 - SoTA-Echoing

[OpenStax, University Physics Volume 1, §14.5](https://openstax.org/books/university-physics-volume-1/pages/14-5-fluid-dynamics) derives fluid continuity from mass flow and uses constant density to pass to volume flow. Adopt the need for a physical quantity basis; adapt the simple equal-flow case by retaining changing storage in the selected region.

[Sonin, On Choosing and Using Control Volumes (2001), Methods 1–6](https://ocw.mit.edu/courses/2-25-advanced-fluid-mechanics-fall-2013/1657c64b3737c8d35e5905ea21702c6b_MIT2_25F13_On_Choo_and_Usi.pdf) compares fixed and moving boundaries for the same piston-driven flow. The constructions obtain the same exit speed while changing accumulation and crossing terms; a boundary through the piston makes one formulation require a density-discontinuity treatment. Use this established control-volume Method when its continuum quantities and mathematical preparation fit the question. The finite construction in :4 also serves event counts and partitioned computational updates.

[Ketcheson, LeVeque and del Razo, Riemann Problems and Jupyter Solutions, “Finite volume methods”](https://www.clawpack.org/riemann_book/html/Approximate_solvers.html#Finite-volume-methods) obtains aggregate conservation by weighting cell averages and canceling neighboring fluxes. Adopt compatible interface transfer in a numerical update. The book's approximate-solver construction supplies additional transport and approximation methods beyond this balance test.

For the changed tank question, compare two adequate accounts with the same supplied interval amounts and elementary arithmetic. Direct accounting at the tank boundary uses the line's 15 L departure and 13 L arrival to obtain 43 L. Accounting over tanks plus line gives 45 L; recovering the tank amount then needs the line's final 2 L store. Choose the account whose needed quantities are available. Applying only the outside exchange to A+B gives the wrong 45 L answer because it omits the line's increase. If an applicable balance already answers the question, another account adds no benefit.

The boundary-revision procedure and the tank and job continuations are a conceptual synthesis of additive accounting, physical storage and computational conservation. Detailed continuum transport, chemical reaction accounting and stochastic queue models need their own subject Methods.

Reconsider the quantity, boundary or balance form when membership changes, needed storage information is unavailable, boundary motion changes the crossing law, or a cheaper adequate construction becomes available.

