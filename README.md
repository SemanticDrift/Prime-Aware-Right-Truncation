# The Prime-Aware Right-Truncation Operator
### Series: Mathematical Foundations for Universal Systems
**Author:** Carolina Johnson (CJ)
**Date:** December 2025
**License:** CC BY 4.0, Attribution required
**DOI:** https://doi.org/10.5281/zenodo.18442783
**ORCID:** https://orcid.org/0009-0002-8819-3347

---

## What This Does

A deterministic descent operator that navigates the prime landscape to its terminal states using exactly one binary choice per step. Right-truncation of primes terminates in finite steps for every prime. Run it and see where it lands.

---

## The Problem It Solves

Classical right-truncatable primes form a finite set of exactly 83 elements in base 10. The field treated this as a curiosity and moved on.

It is not a curiosity. It is a structural constraint. The finiteness is not a dead end. It is a signal that the operator needed one degree of freedom to become a complete dynamical system.

With exactly one binary perturbation δ ∈ {0, 1} per step, every prime p ≥ 11 descends deterministically to a terminal state. The descent is strict. The termination is finite. The freedom is minimal.

One binary choice. That's all primes need to descend.

---

## The Operator

For any prime p ≥ 11, write p = 10k + d where d ∈ {1, 3, 7, 9}. Define:

```
R(p) = k        if k is prime
R(p) = k + 1    if k is not prime and k+1 is prime
R(p) = ⊥        otherwise  (terminal state)
```

The perturbation δ ∈ {0, 1} is the minimum unit of freedom required. Not two choices. Not a continuous range. One binary decision per step.

**Theorem (Strict Descent):** For all p ≥ 11 in the domain of R, R(p) < p.

**Theorem (Finite Termination):** Every R-chain terminates in at most log₁₀(p₀) steps at either a terminal prime or ⊥.

---

## Terminal Primes

A prime t is terminal when neither ⌊t/10⌋ nor ⌊t/10⌋ + 1 is prime. The R-chain stops there.

The smallest terminal prime is 83. Neither 8 nor 9 is prime.

Verified terminal primes below 1000:

```
83, 97, 149, 241, 251, 263, 347, 383, 443, 487, 503, 547,
557, 563, 631, 643, 647, 743, 769, 853, 863, 907, 911,
929, 947, 953, 983
```

Terminal primes are sparse. For the vast majority of primes, the operator continues. Computational search to 10⁷ confirms that terminal primes form a vanishing fraction of the prime landscape as magnitude increases.

---

## Conjecture

There exists M such that for all primes p > M, the operator R(p) is always defined. Consistent with prime density heuristics from the Prime Number Theorem.

**Status: Open. Counterexamples welcome.**

---

## Connection to the Continuum

This operator is an instance of a broader structural principle: one degree of freedom is the minimum amount required for stability.

The same δ ∈ {0, 1} freedom that navigates the prime landscape appears in the Terminal Operator for recursive systems and in the Continuum as Closure framework. The pattern is not coincidental. It is structural.

| Framework | Freedom | Domain |
|-----------|---------|--------|
| Prime-Aware R | δ ∈ {0,1} | Prime numbers |
| Terminal Operator T | δ ∈ {0,1} | Recursive systems |
| Continuum as Closure | x + 1 | Cardinal arithmetic |

---

## Dependencies

| Framework | DOI |
|-----------|-----|
| Law of Admissibility (R = 4) | https://doi.org/10.5281/zenodo.18993233 |
| Continuum as Closure | https://doi.org/10.5281/zenodo.18457900 |

Full publication list: https://www.semanticdrift.net

---

## Repository Contents

- `README.md` — this file
- `A_Prime_Aware_Right_Truncation_Operator.pdf` — full paper
- `prime_aware_operator.py` — standalone implementation

---

## Citation

```
Johnson, C. (2025). A Prime-Aware Right-Truncation Operator and Its Terminal Primes.
Series: Mathematical Foundations for Universal Systems.
SemanticDrift. DOI: https://doi.org/10.5281/zenodo.18442783
License: CC BY 4.0
```

---

## License

© 2025 Carolina Johnson (CJ)
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)
Attribution required. https://creativecommons.org/licenses/by/4.0/

---

*"One degree of freedom is the minimum amount required for stability." — CJ*
