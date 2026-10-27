<!-- fingerprint:923552a27c489801def9332b3c12cec3 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-27 09:54 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.030459e+00 | 100.00% |
| PSO | 500 | 1.003658e-19 | 100.00% |
| GLUE | 500 | 1.015874e-01 | 98.20% |
| Sobol | 500 | 3.801079e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
