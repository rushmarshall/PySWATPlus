<!-- fingerprint:93e44b735d8515d411379434f9ba0ece -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-01 10:19 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.176015e-01 | 99.99% |
| PSO | 500 | 6.734235e-21 | 100.00% |
| GLUE | 500 | 1.362295e+00 | 100.00% |
| Sobol | 500 | 1.214609e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
