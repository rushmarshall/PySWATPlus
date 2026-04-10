<!-- fingerprint:c29c59e2ce6f93120411e9f4ef20b43c -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-10 10:10 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.279788e-01 | 100.00% |
| PSO | 500 | 1.153551e-21 | 100.00% |
| GLUE | 500 | 6.345759e-01 | 99.96% |
| Sobol | 500 | 6.726310e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
