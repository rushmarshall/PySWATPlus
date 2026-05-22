<!-- fingerprint:51e8c878dd0d0f97c8bc3871d89411d2 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-22 10:42 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.016885e-01 | 99.99% |
| PSO | 500 | 4.804057e-21 | 100.00% |
| GLUE | 500 | 8.545897e-01 | 100.00% |
| Sobol | 500 | 2.822565e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
