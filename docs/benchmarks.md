<!-- fingerprint:e20769c8cb2bf2e91950c46b8a9b8d8d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-28 10:40 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.326400e-01 | 100.00% |
| PSO | 500 | 2.422591e-18 | 100.00% |
| GLUE | 500 | 8.119293e-01 | 99.71% |
| Sobol | 500 | 3.169990e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
