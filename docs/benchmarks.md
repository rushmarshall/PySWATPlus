<!-- fingerprint:0566a840786cd61b13f66d5bfa7ab30e -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-01 10:54 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.098084e-01 | 99.17% |
| PSO | 500 | 1.680862e-24 | 100.00% |
| GLUE | 500 | 1.761143e-01 | 99.91% |
| Sobol | 500 | 1.155913e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
