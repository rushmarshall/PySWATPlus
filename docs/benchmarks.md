<!-- fingerprint:93404bfb81fea6407827fe9f2c6bae52 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-07 10:43 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.349955e-03 | 100.00% |
| PSO | 500 | 3.526116e-19 | 100.00% |
| GLUE | 500 | 6.161202e-01 | 93.22% |
| Sobol | 500 | 1.505995e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
