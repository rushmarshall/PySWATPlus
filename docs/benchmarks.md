<!-- fingerprint:89e638d8c629fa360054a7d54f007617 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-13 10:44 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.045063e+01 | 99.94% |
| PSO | 500 | 1.769428e-22 | 100.00% |
| GLUE | 500 | 8.097864e-01 | 99.96% |
| Sobol | 500 | 1.292236e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
