<!-- fingerprint:47bae5f1e212c22cadf9d6e5e352e9b0 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-11 09:59 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.561876e-01 | 99.99% |
| PSO | 500 | 5.572258e-18 | 100.00% |
| GLUE | 500 | 6.311271e-01 | 98.95% |
| Sobol | 500 | 1.728114e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
