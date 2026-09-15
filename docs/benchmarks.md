<!-- fingerprint:314852ddf5e696395351fd484b92150f -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-15 09:51 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.029210e+00 | 100.00% |
| PSO | 500 | 1.087305e-22 | 100.00% |
| GLUE | 500 | 3.425361e-01 | 94.50% |
| Sobol | 500 | 4.798547e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
