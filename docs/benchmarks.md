<!-- fingerprint:3c2a12d87ff9870f782d9d76fda92a7d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-30 10:24 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.956597e-01 | 97.66% |
| PSO | 500 | 8.368007e-18 | 100.00% |
| GLUE | 500 | 2.054420e-01 | 99.55% |
| Sobol | 500 | 5.516862e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
