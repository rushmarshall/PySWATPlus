<!-- fingerprint:f5cb68028f6489766bc261517c28df1f -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-08 11:25 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.846948e-01 | 6.60% |
| PSO | 500 | 1.400161e-21 | 100.00% |
| GLUE | 500 | 1.470562e+00 | 100.00% |
| Sobol | 500 | 1.124087e-01 | 99.66% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
