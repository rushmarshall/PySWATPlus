<!-- fingerprint:4e6ecd8ce4693ec00d16d101027e45d6 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-11 10:11 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.024464e+00 | 100.00% |
| PSO | 500 | 2.510769e-20 | 100.00% |
| GLUE | 500 | 4.660753e-01 | 99.74% |
| Sobol | 500 | 1.015563e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
