<!-- fingerprint:b6d05eb40787787231a9ff04c1f24fad -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-30 10:33 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.633411e-02 | 99.98% |
| PSO | 500 | 8.900207e-19 | 100.00% |
| GLUE | 500 | 3.405318e-01 | 99.98% |
| Sobol | 500 | 2.672098e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
