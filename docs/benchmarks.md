<!-- fingerprint:1a221fe93610fed3049074712ec759a6 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-06 11:16 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.963738e-01 | 91.73% |
| PSO | 500 | 2.090036e-20 | 100.00% |
| GLUE | 500 | 3.733407e+00 | 100.00% |
| Sobol | 500 | 8.410799e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
