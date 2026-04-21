<!-- fingerprint:798ccf416289befdca6e91e95ecc70b8 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-21 10:13 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.279958e-02 | 99.98% |
| PSO | 500 | 1.764400e-16 | 100.00% |
| GLUE | 500 | 3.046142e-01 | 57.46% |
| Sobol | 500 | 1.169394e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
