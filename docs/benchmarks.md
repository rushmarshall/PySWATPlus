<!-- fingerprint:33d5e41e3e63c289535e3e74ca8f276b -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-16 11:33 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.968004e-01 | 100.00% |
| PSO | 500 | 9.132023e-20 | 100.00% |
| GLUE | 500 | 3.282544e-01 | 99.32% |
| Sobol | 500 | 6.636145e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
