<!-- fingerprint:70026b5ec193abf614c53baf862d461b -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-09 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.919873e-01 | 100.00% |
| PSO | 500 | 2.398234e-19 | 100.00% |
| GLUE | 500 | 6.479563e-01 | 100.00% |
| Sobol | 500 | 9.479293e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
