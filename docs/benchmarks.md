<!-- fingerprint:2b1ca75a1ebddb5a49d73bce7d5dd6d6 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-04 10:29 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.165971e-01 | 100.00% |
| PSO | 500 | 5.342442e-19 | 100.00% |
| GLUE | 500 | 2.127166e+00 | 99.95% |
| Sobol | 500 | 2.539597e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
