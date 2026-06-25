<!-- fingerprint:bb3c2074f7af6f7f17a2c34d6f7a066d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-25 10:41 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.414690e-01 | 99.81% |
| PSO | 500 | 6.164708e-21 | 100.00% |
| GLUE | 500 | 6.561725e-01 | 99.98% |
| Sobol | 500 | 1.384629e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
