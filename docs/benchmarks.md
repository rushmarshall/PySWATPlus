<!-- fingerprint:ae5917fb108fef3545c4929e4e89bec3 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-18 10:12 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.020000e+00 | 99.96% |
| PSO | 500 | 4.870700e-13 | 99.97% |
| GLUE | 500 | 1.430886e+00 | 99.22% |
| Sobol | 500 | 1.113676e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
