<!-- fingerprint:42356b712adcd2b8606a572d3257d5eb -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-23 10:13 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.600150e-01 | 100.00% |
| PSO | 500 | 2.076499e-19 | 99.99% |
| GLUE | 500 | 2.676359e-01 | 62.44% |
| Sobol | 500 | 1.569469e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
