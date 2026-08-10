<!-- fingerprint:52c3aedf1f2abb37bc0197af8e1ed114 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-10 10:11 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.120552e+01 | 100.00% |
| PSO | 500 | 5.867232e-24 | 100.00% |
| GLUE | 500 | 2.044943e-01 | 99.94% |
| Sobol | 500 | 1.932974e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
