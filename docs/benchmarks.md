<!-- fingerprint:26864121768a6cbad8bcee42a31f23f5 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-01 10:13 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.130896e-01 | 99.98% |
| PSO | 500 | 1.470443e-19 | 100.00% |
| GLUE | 500 | 2.613959e-01 | 100.00% |
| Sobol | 500 | 1.485960e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
