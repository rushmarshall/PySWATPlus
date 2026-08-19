<!-- fingerprint:5300bd3ac2acba7a43b84c2eacc82b98 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-19 09:56 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.701950e-01 | 99.47% |
| PSO | 500 | 3.145455e-16 | 100.00% |
| GLUE | 500 | 2.808727e-01 | 100.00% |
| Sobol | 500 | 1.099639e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
