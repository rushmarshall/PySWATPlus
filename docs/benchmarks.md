<!-- fingerprint:bcae7a30066c37ca4a2d0fe08bc8c576 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-24 10:42 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.716316e-01 | 100.00% |
| PSO | 500 | 1.466730e-20 | 100.00% |
| GLUE | 500 | 7.005926e-01 | 100.00% |
| Sobol | 500 | 3.012935e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
