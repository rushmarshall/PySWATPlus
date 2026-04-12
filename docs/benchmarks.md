<!-- fingerprint:53a5e024e086d37f7f196e18f3324fda -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-12 10:02 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.357681e-01 | 99.97% |
| PSO | 500 | 4.725309e-25 | 100.00% |
| GLUE | 500 | 2.260680e+00 | 100.00% |
| Sobol | 500 | 6.939908e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
