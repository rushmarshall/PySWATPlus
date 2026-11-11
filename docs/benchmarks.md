<!-- fingerprint:110095e862335b030b4e1a4cc496e8dc -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-11 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 9.789246e-01 | 99.99% |
| PSO | 500 | 1.785874e-20 | 100.00% |
| GLUE | 500 | 1.341623e+00 | 99.96% |
| Sobol | 500 | 9.797700e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
