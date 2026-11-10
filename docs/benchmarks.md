<!-- fingerprint:5fcf5ef2a97eac98f2c068dea2e9c209 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-10 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.484669e-02 | 99.92% |
| PSO | 500 | 5.041101e-20 | 100.00% |
| GLUE | 500 | 5.375057e-01 | 98.82% |
| Sobol | 500 | 8.272125e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
