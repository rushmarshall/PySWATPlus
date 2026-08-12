<!-- fingerprint:fa44573164c4fbcf5205bdad3c8edf5d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-12 10:10 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.496926e-01 | 100.00% |
| PSO | 500 | 4.653144e-20 | 100.00% |
| GLUE | 500 | 1.857534e-01 | 100.00% |
| Sobol | 500 | 1.785024e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
