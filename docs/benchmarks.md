<!-- fingerprint:ec5d63589fc78d7cb4335e071bb17fa2 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-12 10:15 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.907715e-02 | 100.00% |
| PSO | 500 | 5.722886e-22 | 100.00% |
| GLUE | 500 | 7.957963e-01 | 99.90% |
| Sobol | 500 | 2.020585e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
