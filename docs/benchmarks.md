<!-- fingerprint:fb6cc9c9fc084bc15aeaad87e8ef8040 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-03 11:26 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.121214e-01 | 99.96% |
| PSO | 500 | 1.551218e-18 | 100.00% |
| GLUE | 500 | 1.633245e+00 | 98.51% |
| Sobol | 500 | 3.189845e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
