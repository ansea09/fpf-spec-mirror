---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:11"
section_title: "SoTA‑Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__013_sota-echoing.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:11 — SoTA‑Echoing"
line_start: 21948
line_end: 21956
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.21"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "E.10"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
keywords:
  - "EntityOfConcern ≠ Description episteme"
  - "MethodDescription ≠ Method ≠ Capability ≠ Work"
  - "category error"
  - "system-role kind and assignment ≠ Work"
---

### A.7:11 - SoTA‑Echoing

* **Digital twins (ISO 23247-1/-2, 2021).** The public previews of [Part 1, §§3.2.2–3.2.5](https://gso-sims-preview-doc-aws.s3-eu-west-1.amazonaws.com/iso-23247-1-2021-en.html) distinguish observable manufacturing elements from synchronized digital representations; [Part 2, §§3.5/5.2.3–5.2.4](https://cdn.standards.iteh.ai/samples/78743/024341895c784ad18c5f6361d5ae074e/ISO-23247-2-2021.pdf) distinguishes implementing and management systems and permits a digital-twin entity to denote a system or systems. **Adapt:** distinguish the representation from its implementing System, and identify the FPF kind from the actual referent.
* **Observability (OpenTelemetry).** [Semantic Conventions 1.44.0](https://opentelemetry.io/docs/specs/semconv/) defines attribute meanings; the [Specification Overview 1.60.0](https://opentelemetry.io/docs/specs/otel/overview/) and [exporter description](https://opentelemetry.io/docs/concepts/components/#exporters) distinguish export components and their data mappings. **Adapt:** keep semantic definitions and transport or representation mappings distinct. Publication-face and publication-form orthogonality is the FPF use of that distinction.
* **Active inference.** In [*Active Inference: A Process Theory* (2017), §§2–2.2](https://discovery.ucl.ac.uk/id/eprint/1530701/1/Friston_Active_Inference_Process_Theory.pdf), Friston, FitzGerald, Rigoli, Schwartenbeck and Pezzulo distinguish a generative model, policies, the generative process, and the action/observation cycle. **Adopt** this historical model/action distinction for A.7's referent recovery; identify the model and acting System under their own FPF rules.
* **Constructor theory.** [Deutsch's *Constructor Theory*, arXiv:1210.7439v2 (17 January 2013), §§1.1/2.14/2.15](https://arxiv.org/abs/1210.7439v2) distinguishes tasks and constructors and also treats information and knowledge as abstract constructors. [Marletto's *Constructor theory of life* (2015), §3.1](https://www.constructortheory.org/wp-content/uploads/2016/03/ct-life.pdf) retains embodied knowledge's constructor role; her [*Constructor Theory of Thermodynamics* (2016)](https://www.constructortheory.org/wp-content/uploads/2016/07/THD-ArXiv-Final.pdf) concerns thermodynamic work and work media. **Adapt** the historical task/realization distinction. A.7 uses that distinction without assigning these source meanings of knowledge or thermodynamic work to `U.Episteme` or `U.Work`.
* **Quality-diversity (MAP-Elites).** In [*Illuminating search spaces by mapping elites* (2015), §3/Fig. 2](https://arxiv.org/pdf/1504.04909), Mouret and Clune describe storing candidate solutions by feature-space cell and retaining the best found for an occupied cell. The returned feature-performance map differs from the run producing it; default parent selection chooses one elite. **Adopt and adapt** this historical archive/execution distinction and collection-valued output example; govern any FPF typed-space or order claim by its own rule.
* **Formal verification and quantities.** [*LiquidHaskell: Experience with Refinement Types in the Real World* (2014)](https://goto.ucsd.edu/~nvazou/real_world_liquid.pdf), by Vazou, Seidel and Jhala, presents logical refinement predicates and contracts. Koenig and Leino's [*Programming Language Features for Refinement*, KRML 248 (2015)](https://leino.science/papers/krml248.pdf), together with the [Dafny Reference Manual's refinement section](https://dafny.org/dafny/DafnyRef/DafnyRef#sec-refinement), describes restricted program refinement. [uom 0.38.0](https://docs.rs/uom/0.38.0/uom/#design) supplies dimension-safe quantities with declared units and conversions. **Adapt** these distinct practices to motivate the specification-use boundary: the claiming specification, formality, refinement, measurement-criterion, and publication patterns govern the applicable check, law, and pins.

