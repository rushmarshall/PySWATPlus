<!-- fingerprint:4e8244bfe4babc7e7e3fb9f0967bf9c6 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-30 09:53 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.047506e-01 | 99.78% |
| PSO | 500 | 2.210446e-21 | 100.00% |
| GLUE | 500 | 1.763183e+00 | 100.00% |
| Sobol | 500 | 9.743572e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
