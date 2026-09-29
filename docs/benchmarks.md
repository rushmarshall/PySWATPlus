<!-- fingerprint:9c66cd3f555937167cacd63dc5c2950e -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-29 09:52 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.588794e-01 | 99.91% |
| PSO | 500 | 9.044834e-21 | 100.00% |
| GLUE | 500 | 1.900634e-01 | 100.00% |
| Sobol | 500 | 3.935451e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
