<!-- fingerprint:e765db6acf04aee4aa798384dcb07555 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-01 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.464046e-02 | 100.00% |
| PSO | 500 | 1.662621e-21 | 100.00% |
| GLUE | 500 | 5.699363e-01 | 100.00% |
| Sobol | 500 | 5.431899e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
