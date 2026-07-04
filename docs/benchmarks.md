<!-- fingerprint:286cbd8555d0cb741314e3a6f14f37d7 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-04 10:28 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.240347e-02 | 100.00% |
| PSO | 500 | 2.421026e-24 | 100.00% |
| GLUE | 500 | 3.230194e-01 | 99.99% |
| Sobol | 500 | 1.227264e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
