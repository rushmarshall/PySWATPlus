<!-- fingerprint:8e031d99dced62d6e7e8e51874ece289 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-13 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.411555e+00 | 99.96% |
| PSO | 500 | 2.121627e-19 | 100.00% |
| GLUE | 500 | 6.174204e-01 | 100.00% |
| Sobol | 500 | 8.481239e-06 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
