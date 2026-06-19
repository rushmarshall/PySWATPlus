<!-- fingerprint:72bad9bc4dbf29b7f50e76fa117685be -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-19 11:13 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.970862e-01 | 99.99% |
| PSO | 500 | 1.586993e-20 | 100.00% |
| GLUE | 500 | 1.605043e-01 | 99.98% |
| Sobol | 500 | 2.498568e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
