<!-- fingerprint:415e4b815d73c119b2248ce673fe4d9a -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-23 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.015071e-01 | 100.00% |
| PSO | 500 | 1.811366e-23 | 100.00% |
| GLUE | 500 | 1.222289e+00 | 99.59% |
| Sobol | 500 | 5.988262e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
