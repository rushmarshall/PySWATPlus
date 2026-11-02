<!-- fingerprint:e51b2eca8303214fad4c63f429896193 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-02 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.182000e-03 | 99.98% |
| PSO | 500 | 5.498752e-22 | 100.00% |
| GLUE | 500 | 2.240143e-01 | 100.00% |
| Sobol | 500 | 5.424674e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
