<!-- fingerprint:98f881279c30b195cda233afe5291dfe -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-09 10:48 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.731195e+00 | 99.77% |
| PSO | 500 | 1.707429e-17 | 100.00% |
| GLUE | 500 | 2.676926e-02 | 99.96% |
| Sobol | 500 | 3.536321e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
