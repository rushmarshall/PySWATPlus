<!-- fingerprint:5d363f9e14f09b41ff1d5ce3d14e74af -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-05 09:59 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.606902e-01 | 99.49% |
| PSO | 500 | 4.347847e-21 | 100.00% |
| GLUE | 500 | 8.516524e-02 | 99.94% |
| Sobol | 500 | 5.140600e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
