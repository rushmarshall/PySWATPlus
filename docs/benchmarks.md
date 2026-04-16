<!-- fingerprint:85e59a3a40476569370e11623035898f -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-16 10:12 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.457305e-01 | 96.29% |
| PSO | 500 | 1.723196e-22 | 100.00% |
| GLUE | 500 | 4.033817e-01 | 99.95% |
| Sobol | 500 | 8.573084e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
