<!-- fingerprint:9448cdb8af1dd21c24d40371a90d4b98 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-29 11:28 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.155933e-02 | 100.00% |
| PSO | 500 | 2.881518e-20 | 100.00% |
| GLUE | 500 | 1.478380e+00 | 100.00% |
| Sobol | 500 | 1.899825e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
