<!-- fingerprint:e4b9651529302c2d9ca4ec8d81c3624e -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-06 09:52 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.796431e-02 | 100.00% |
| PSO | 500 | 1.238402e-20 | 99.99% |
| GLUE | 500 | 2.534488e-01 | 99.54% |
| Sobol | 500 | 2.964411e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
