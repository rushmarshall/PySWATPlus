<!-- fingerprint:58580c089d153a8c95e8e8a4b7a2520c -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-26 10:43 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.163206e-01 | 100.00% |
| PSO | 500 | 2.291600e-19 | 100.00% |
| GLUE | 500 | 6.296389e-01 | 100.00% |
| Sobol | 500 | 9.564948e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
