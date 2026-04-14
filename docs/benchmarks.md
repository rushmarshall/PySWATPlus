<!-- fingerprint:e34ce43b86738f488a6dba7be8b37341 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-14 10:12 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.533280e-01 | 99.99% |
| PSO | 500 | 5.573673e-22 | 100.00% |
| GLUE | 500 | 2.675496e-01 | 99.98% |
| Sobol | 500 | 5.607227e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
