<!-- fingerprint:b9a65a37c3534cb723c8445348870b49 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-20 10:42 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.314838e-04 | 93.17% |
| PSO | 500 | 1.245189e-23 | 100.00% |
| GLUE | 500 | 4.432907e-01 | 99.98% |
| Sobol | 500 | 2.484327e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
