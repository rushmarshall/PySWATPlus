<!-- fingerprint:33015f82f861c4a9b05e3908d68bf36d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-29 10:40 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.005416e-01 | 100.00% |
| PSO | 500 | 2.566090e-20 | 100.00% |
| GLUE | 500 | 1.949668e-01 | 100.00% |
| Sobol | 500 | 1.722220e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
