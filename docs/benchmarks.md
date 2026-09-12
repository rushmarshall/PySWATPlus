<!-- fingerprint:c907b31e2bfed23e8641f3a2d333e630 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-12 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.221212e+00 | 99.29% |
| PSO | 500 | 2.318463e-19 | 100.00% |
| GLUE | 500 | 7.251097e-01 | 100.00% |
| Sobol | 500 | 4.811544e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
