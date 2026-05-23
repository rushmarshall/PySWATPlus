<!-- fingerprint:04483909ef9f1e4c51cd3c6031ba347d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-23 10:16 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.771541e-01 | 99.99% |
| PSO | 500 | 1.610328e-17 | 100.00% |
| GLUE | 500 | 7.708862e-01 | 100.00% |
| Sobol | 500 | 2.097057e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
