<!-- fingerprint:ecd6afa751f5f2f6098390348e22dd7d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-25 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.087571e-01 | 100.00% |
| PSO | 500 | 7.195197e-23 | 100.00% |
| GLUE | 500 | 8.971899e-01 | 100.00% |
| Sobol | 500 | 9.237038e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
