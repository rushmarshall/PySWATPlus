<!-- fingerprint:d133064d1e88d9649bc644da1a67d4ba -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-15 10:35 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.809754e-01 | 100.00% |
| PSO | 500 | 2.974409e-22 | 100.00% |
| GLUE | 500 | 5.633195e-01 | 72.02% |
| Sobol | 500 | 2.737012e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
