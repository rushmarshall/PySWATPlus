<!-- fingerprint:a44f04cda9aa964ca60e0033a3c83b44 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-10 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.776241e-01 | 99.98% |
| PSO | 500 | 5.083014e-24 | 100.00% |
| GLUE | 500 | 1.171560e-01 | 99.73% |
| Sobol | 500 | 1.723432e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
