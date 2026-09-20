<!-- fingerprint:f0785d23bebad9eed6f25d26cc0eb550 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-20 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.401463e+00 | 99.99% |
| PSO | 500 | 2.704786e-22 | 100.00% |
| GLUE | 500 | 2.628089e-01 | 77.05% |
| Sobol | 500 | 1.391446e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
