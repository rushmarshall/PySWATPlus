<!-- fingerprint:ed73c671c2f58ea775a30cbf33741e46 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-23 09:53 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.726292e-01 | 99.99% |
| PSO | 500 | 2.741810e-21 | 100.00% |
| GLUE | 500 | 2.355875e-01 | 99.95% |
| Sobol | 500 | 7.228864e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
