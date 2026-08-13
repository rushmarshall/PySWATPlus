<!-- fingerprint:80f6f157860c5c4f56bf247670cc667d -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-13 10:10 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.128419e-01 | 100.00% |
| PSO | 500 | 6.802873e-19 | 100.00% |
| GLUE | 500 | 2.100533e-01 | 100.00% |
| Sobol | 500 | 2.117612e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
