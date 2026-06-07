<!-- fingerprint:84cd611016b2f78bc870868c677a79e9 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-07 10:35 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.768039e-01 | 99.99% |
| PSO | 500 | 3.188965e-22 | 100.00% |
| GLUE | 500 | 4.866457e-01 | 98.61% |
| Sobol | 500 | 9.797991e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
