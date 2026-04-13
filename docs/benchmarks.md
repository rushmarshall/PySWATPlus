<!-- fingerprint:c3f185875b98b540a7f6fd46442bacef -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-13 10:21 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.779810e-01 | 98.17% |
| PSO | 500 | 2.381234e-20 | 100.00% |
| GLUE | 500 | 4.661506e-01 | 100.00% |
| Sobol | 500 | 9.062633e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
