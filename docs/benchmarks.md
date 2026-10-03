<!-- fingerprint:befc8fe9400dea5fa9de082592decf32 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-03 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.286961e-01 | 99.96% |
| PSO | 500 | 4.296827e-18 | 98.11% |
| GLUE | 500 | 2.324589e-01 | 100.00% |
| Sobol | 500 | 2.370558e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
