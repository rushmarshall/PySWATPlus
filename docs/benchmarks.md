<!-- fingerprint:75a610090497441df602fc76d7123985 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-28 11:03 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.462074e-01 | 99.96% |
| PSO | 500 | 2.213977e-16 | 100.00% |
| GLUE | 500 | 4.185472e-01 | 99.99% |
| Sobol | 500 | 4.618452e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
