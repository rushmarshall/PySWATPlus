<!-- fingerprint:6ad2cd3d08396a276c2f5a8302463820 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-19 09:55 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.463209e-01 | 100.00% |
| PSO | 500 | 1.047248e-20 | 100.00% |
| GLUE | 500 | 1.737147e+00 | 99.15% |
| Sobol | 500 | 1.492951e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
