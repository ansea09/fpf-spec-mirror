---
chunk_kind: "child"
pattern_id: "C.29.SC"
pattern_title: "Derive a Consequence from a Symmetry"
section_id: "C.29.SC:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.SC/C.29.SC__012_sota-echoing.md"
commit_sha: "bbfb5347013400e9a895fa4b0f66992e931c0ece"
heading_path:
  - "C.29.SC — Derive a Consequence from a Symmetry"
  - "C.29.SC:11 — SoTA-Echoing"
line_start: 65019
line_end: 65030
dependencies:
  - "A.3.3.TR"
  - "C.29.1"
  - "C.29.2"
  - "C.29.AV"
keywords:
---

### C.29.SC:11 - SoTA-Echoing

The selected approach defines the structure and input-output action before using symmetry. It supports direct algebra for a small problem and provides the premise for more specialized group, optimization or numerical constructions.

[Bronstein, Bruna, Cohen and Veličković, *Geometric Deep Learning*, draft chapter 3, §§3.1-3.2](https://geometricdeeplearning.com/book/algebraicpriors.html) develops symmetries as invertible structure-preserving maps and distinguishes invariant and equivariant outputs. Adopt that explicit action and output discipline. Whether a transformation preserves a label or target still comes from the modeled task. Architecture construction and learning-performance claims need the corresponding further Methods and evidence.

[Tong, *Classical Dynamics*, §2.4](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html) derives conserved quantities from continuous symmetries of a Lagrangian using its equations of motion. The useful contribution is the extra argument connecting symmetry with time evolution. The simple oscillator calculation above performs that connection directly; it does not substitute for the wider Noether construction.

[Hairer, *Geometric Numerical Integration*, lecture 2, §1](https://www.unige.ch/~hairer/poly_geoint/week2.pdf) supplies the symplectic Euler formulas and their Hamiltonian conditions. The direct comparison above shows why a requested invariant must be examined under the actual numerical update. A different model or requested accuracy can favor a different scheme.

C.29.1 supplies the general result-transfer comparison. The fixed-point and selection constructions here make one specific consequence available without a full group-theory survey. Revisit the use when its structure, output meaning, uniqueness premise or transformation law changes.

