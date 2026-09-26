<!-- fingerprint:07a92a7a71da99d0a8049abcead0f70d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-26 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.820247e-01 | 100.00% |
| PSO | 500 | 7.349580e-22 | 99.99% |
| GLUE | 500 | 1.764889e-01 | 100.00% |
| Sobol | 500 | 1.244411e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
