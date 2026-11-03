<!-- fingerprint:d745ad56ae74774e0372ccbc66dc87cd -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-03 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.234792e-01 | 100.00% |
| PSO | 500 | 5.451445e-21 | 100.00% |
| GLUE | 500 | 1.104663e-01 | 99.99% |
| Sobol | 500 | 4.510335e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
