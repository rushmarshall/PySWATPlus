<!-- fingerprint:1ffd9c23128b54aa9ae48cb1d5bc0168 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-29 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.885570e-01 | 99.97% |
| PSO | 500 | 3.022026e-17 | 99.86% |
| GLUE | 500 | 9.278584e-02 | 100.00% |
| Sobol | 500 | 2.224218e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
