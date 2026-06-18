<!-- fingerprint:c09139bd2b708c5bf117403d447fb88b -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-18 11:10 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.022103e-01 | 99.89% |
| PSO | 500 | 2.436013e-19 | 100.00% |
| GLUE | 500 | 4.487941e-01 | 99.95% |
| Sobol | 500 | 2.101543e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
