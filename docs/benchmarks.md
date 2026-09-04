<!-- fingerprint:45943bc3fb03cef8c9b8a224b9e5f5d2 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-04 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.576951e+00 | 99.89% |
| PSO | 500 | 1.548090e-20 | 100.00% |
| GLUE | 500 | 1.144005e+00 | 99.98% |
| Sobol | 500 | 2.432517e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
