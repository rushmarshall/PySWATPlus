<!-- fingerprint:343195db3d4376f4f3e84084b497d8d3 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-15 09:52 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.694783e-01 | 100.00% |
| PSO | 500 | 2.112307e-17 | 100.00% |
| GLUE | 500 | 7.636562e-01 | 99.99% |
| Sobol | 500 | 3.220089e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
