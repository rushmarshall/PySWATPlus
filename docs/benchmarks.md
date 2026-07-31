<!-- fingerprint:97c6c82e32f6d1c198b37bbac8023574 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-31 10:40 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.314428e-01 | 99.99% |
| PSO | 500 | 1.545227e-18 | 100.00% |
| GLUE | 500 | 6.882010e-01 | 99.92% |
| Sobol | 500 | 4.786387e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
