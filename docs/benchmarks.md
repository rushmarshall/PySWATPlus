<!-- fingerprint:9b884cc71d0003d6808e81081a7fdf7a -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-17 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.430659e-01 | 100.00% |
| PSO | 500 | 6.295857e-24 | 100.00% |
| GLUE | 500 | 2.185858e+00 | 98.86% |
| Sobol | 500 | 1.139257e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
