<!-- fingerprint:82823f4c23f90952a5df358a26c4b742 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-24 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.967686e-01 | 100.00% |
| PSO | 500 | 6.131527e-22 | 100.00% |
| GLUE | 500 | 2.461462e-01 | 100.00% |
| Sobol | 500 | 7.705405e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
