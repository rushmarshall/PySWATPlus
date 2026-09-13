<!-- fingerprint:d0ec5281b60022e8cce9f438c88416e9 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-13 10:05 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.780126e-01 | 99.98% |
| PSO | 500 | 2.959059e-23 | 100.00% |
| GLUE | 500 | 4.718499e-01 | 99.99% |
| Sobol | 500 | 5.463438e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
