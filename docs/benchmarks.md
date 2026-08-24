<!-- fingerprint:7a20d8752a4a0a7e6258e9b3cd336422 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-24 10:03 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.052772e-02 | 100.00% |
| PSO | 500 | 1.902356e-18 | 100.00% |
| GLUE | 500 | 1.236293e+00 | 99.80% |
| Sobol | 500 | 9.130341e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
