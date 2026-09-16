<!-- fingerprint:2cb471504b2117f8fc81927978585ed6 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-16 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.637887e-01 | 100.00% |
| PSO | 500 | 4.717983e-20 | 100.00% |
| GLUE | 500 | 6.262160e-01 | 100.00% |
| Sobol | 500 | 3.165432e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
