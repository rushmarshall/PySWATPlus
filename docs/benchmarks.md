<!-- fingerprint:7f2d6643cb4fcd5112bda1a8c39911fd -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-24 10:14 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.480673e-01 | 100.00% |
| PSO | 500 | 2.540211e-17 | 100.00% |
| GLUE | 500 | 6.601241e-01 | 97.91% |
| Sobol | 500 | 3.332546e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
