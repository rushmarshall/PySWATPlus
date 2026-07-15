<!-- fingerprint:dff630772bc9f61300fffcc218bcc8e9 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-15 10:23 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.237141e-01 | 100.00% |
| PSO | 500 | 2.973755e-23 | 100.00% |
| GLUE | 500 | 1.763569e-01 | 100.00% |
| Sobol | 500 | 2.551565e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
