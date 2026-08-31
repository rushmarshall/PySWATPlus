<!-- fingerprint:8c56bd575255a8398e9f5b278a00c087 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-31 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.983707e-01 | 100.00% |
| PSO | 500 | 3.789583e-19 | 100.00% |
| GLUE | 500 | 2.634778e-01 | 99.90% |
| Sobol | 500 | 1.421162e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
