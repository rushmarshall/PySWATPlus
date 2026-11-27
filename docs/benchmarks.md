<!-- fingerprint:7987ae3cb0fa9197b278802edd0a5668 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-27 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.081874e-01 | 100.00% |
| PSO | 500 | 6.568886e-21 | 100.00% |
| GLUE | 500 | 3.164276e-01 | 99.99% |
| Sobol | 500 | 3.140588e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
