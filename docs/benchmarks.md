<!-- fingerprint:9209609c04e0271a3917eda85de3d6f4 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-08 10:31 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.180119e+00 | 100.00% |
| PSO | 500 | 7.427935e-21 | 100.00% |
| GLUE | 500 | 1.898202e-01 | 99.07% |
| Sobol | 500 | 3.111540e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
