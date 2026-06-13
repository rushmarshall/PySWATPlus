<!-- fingerprint:2579d8a0a781b88ffe5160cdc88f3b0c -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-13 10:36 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.013261e+01 | 100.00% |
| PSO | 500 | 3.197367e-24 | 100.00% |
| GLUE | 500 | 5.505522e-01 | 100.00% |
| Sobol | 500 | 5.429167e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
