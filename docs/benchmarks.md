<!-- fingerprint:1ac44ee92ac2f170864025310d32d6e0 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-08 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.490857e-01 | 100.00% |
| PSO | 500 | 2.316138e-20 | 100.00% |
| GLUE | 500 | 3.749319e-01 | 100.00% |
| Sobol | 500 | 1.437889e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
