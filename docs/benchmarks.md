<!-- fingerprint:e2a0a36d83086fea983c1f53363af79d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-14 10:43 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.819634e-03 | 100.00% |
| PSO | 500 | 2.137087e-18 | 100.00% |
| GLUE | 500 | 8.901187e-01 | 100.00% |
| Sobol | 500 | 6.440402e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
