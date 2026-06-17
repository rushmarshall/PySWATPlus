<!-- fingerprint:4c987ef0e4f3e4a4545aa55cd387a79a -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-17 11:22 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 9.734048e-02 | 100.00% |
| PSO | 500 | 1.109248e-20 | 100.00% |
| GLUE | 500 | 3.487710e-01 | 96.53% |
| Sobol | 500 | 8.934930e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
