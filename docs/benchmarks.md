<!-- fingerprint:e77b28a62ea562802cf197e9fc063331 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-24 10:20 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.823989e-01 | 100.00% |
| PSO | 500 | 7.004352e-19 | 100.00% |
| GLUE | 500 | 3.108863e-01 | 99.82% |
| Sobol | 500 | 3.894898e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
