<!-- fingerprint:64af05e68b790a01998c329689bee33f -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-16 09:53 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 9.365243e-01 | 99.90% |
| PSO | 500 | 9.890264e-20 | 100.00% |
| GLUE | 500 | 6.904970e-01 | 100.00% |
| Sobol | 500 | 2.329659e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
