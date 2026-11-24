<!-- fingerprint:61dcafb7c3174efb1c93241e56c6231a -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-24 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.683639e-02 | 99.99% |
| PSO | 500 | 1.264229e-18 | 100.00% |
| GLUE | 500 | 5.598844e-01 | 99.99% |
| Sobol | 500 | 1.410437e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
