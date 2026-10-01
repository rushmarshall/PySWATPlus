<!-- fingerprint:9586d67ca4994750d9bbf6a43e18983c -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-01 09:53 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.412114e-01 | 99.99% |
| PSO | 500 | 1.062291e-21 | 100.00% |
| GLUE | 500 | 2.042603e-01 | 99.92% |
| Sobol | 500 | 7.410110e-02 | 99.64% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
