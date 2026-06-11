<!-- fingerprint:1036de499e75eac25d53f1dbcececdfe -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-11 11:15 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.105098e+00 | 99.97% |
| PSO | 500 | 9.706660e-21 | 100.00% |
| GLUE | 500 | 8.942830e-01 | 79.14% |
| Sobol | 500 | 4.778423e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
