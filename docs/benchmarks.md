<!-- fingerprint:8f50ffbbb3ec6c890b2af1a05e246b9b -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-17 10:22 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.016853e-01 | 99.97% |
| PSO | 500 | 8.634723e-18 | 100.00% |
| GLUE | 500 | 3.776955e-01 | 98.35% |
| Sobol | 500 | 1.390207e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
