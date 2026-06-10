<!-- fingerprint:81ef3a1030ff91ad18c8301fe0d64fb7 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-10 11:04 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 9.638570e-02 | 100.00% |
| PSO | 500 | 2.790582e-22 | 100.00% |
| GLUE | 500 | 1.100806e+00 | 99.94% |
| Sobol | 500 | 1.538893e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
