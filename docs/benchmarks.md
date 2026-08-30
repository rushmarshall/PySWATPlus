<!-- fingerprint:95bba579c7736ffe8751d9cbeec912a9 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-30 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.037847e+01 | 100.00% |
| PSO | 500 | 2.036489e-21 | 100.00% |
| GLUE | 500 | 9.023123e-01 | 100.00% |
| Sobol | 500 | 1.014353e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
