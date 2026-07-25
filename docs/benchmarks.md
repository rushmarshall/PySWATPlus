<!-- fingerprint:ff16c02417c8e10b9d6dca0e4034b4c7 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-25 10:16 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.109154e-01 | 100.00% |
| PSO | 500 | 2.437645e-19 | 100.00% |
| GLUE | 500 | 6.324992e-01 | 99.73% |
| Sobol | 500 | 7.596105e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
