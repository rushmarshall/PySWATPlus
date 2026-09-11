<!-- fingerprint:5bc012391b71650b4cf7abc95c276606 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-11 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.809545e-01 | 99.99% |
| PSO | 500 | 4.705152e-19 | 100.00% |
| GLUE | 500 | 7.700448e-01 | 99.77% |
| Sobol | 500 | 5.407015e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
