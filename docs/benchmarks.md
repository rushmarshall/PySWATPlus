<!-- fingerprint:765ac92449ae4475a5ff01ce885e3186 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-03 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.052255e-02 | 99.92% |
| PSO | 500 | 1.693800e-19 | 100.00% |
| GLUE | 500 | 1.092076e-01 | 99.61% |
| Sobol | 500 | 8.973801e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
