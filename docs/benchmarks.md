<!-- fingerprint:70d5c826b253701faface884941aafc6 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-19 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.503234e-01 | 99.99% |
| PSO | 500 | 1.733180e-20 | 100.00% |
| GLUE | 500 | 5.467121e-03 | 100.00% |
| Sobol | 500 | 9.055975e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
