<!-- fingerprint:1393ca17dd08e386e530822c2fa0275e -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-04 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.284379e+00 | 97.90% |
| PSO | 500 | 7.580925e-19 | 100.00% |
| GLUE | 500 | 1.460877e+00 | 99.89% |
| Sobol | 500 | 4.264121e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
