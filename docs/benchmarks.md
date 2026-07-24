<!-- fingerprint:753af57276549eb8ae4ac1b88673a69f -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-24 10:30 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.505794e-01 | 99.90% |
| PSO | 500 | 9.941152e-19 | 100.00% |
| GLUE | 500 | 2.966970e-01 | 99.99% |
| Sobol | 500 | 1.498132e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
