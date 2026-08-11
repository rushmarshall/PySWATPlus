<!-- fingerprint:de58cbf5fbf4f56f25e04bd49fc93716 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-11 10:07 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.895523e-02 | 100.00% |
| PSO | 500 | 3.307447e-17 | 100.00% |
| GLUE | 500 | 2.993546e-01 | 100.00% |
| Sobol | 500 | 1.777464e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
