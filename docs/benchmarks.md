<!-- fingerprint:481899446c43636706b9e943eb8903e2 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-30 10:45 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.444695e-01 | 99.34% |
| PSO | 500 | 2.775635e-19 | 100.00% |
| GLUE | 500 | 6.757899e-01 | 99.94% |
| Sobol | 500 | 2.986369e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
