<!-- fingerprint:fe2ccaded1b2516f9781440fd4f1e913 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-12 10:02 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.343847e-02 | 100.00% |
| PSO | 500 | 2.063974e-20 | 100.00% |
| GLUE | 500 | 9.320631e-01 | 99.99% |
| Sobol | 500 | 2.992962e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
