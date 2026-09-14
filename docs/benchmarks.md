<!-- fingerprint:6c912c589d40d15c9a0370cc96c897ca -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-14 09:51 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.937763e-01 | 100.00% |
| PSO | 500 | 1.395794e-17 | 100.00% |
| GLUE | 500 | 1.154156e+00 | 99.02% |
| Sobol | 500 | 1.037889e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
