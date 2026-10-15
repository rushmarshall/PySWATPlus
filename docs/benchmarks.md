<!-- fingerprint:ad6534d7979e54840e2aa93db5bf0174 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-15 09:51 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.828249e-03 | 99.67% |
| PSO | 500 | 2.564738e-18 | 100.00% |
| GLUE | 500 | 1.075472e-01 | 99.98% |
| Sobol | 500 | 2.090069e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
