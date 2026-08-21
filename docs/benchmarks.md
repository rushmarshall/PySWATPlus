<!-- fingerprint:997681b724fe67903920dc30447540d2 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-21 09:57 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.357154e-01 | 99.95% |
| PSO | 500 | 2.733350e-21 | 100.00% |
| GLUE | 500 | 3.883958e-01 | 99.86% |
| Sobol | 500 | 2.099447e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
