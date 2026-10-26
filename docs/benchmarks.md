<!-- fingerprint:cc076ed9746b7af2cd78d93ba13cfd8d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-26 10:00 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.000261e+00 | 100.00% |
| PSO | 500 | 1.499072e-18 | 100.00% |
| GLUE | 500 | 1.101808e+00 | 99.88% |
| Sobol | 500 | 1.524247e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
