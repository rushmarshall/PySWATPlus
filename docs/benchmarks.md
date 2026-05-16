<!-- fingerprint:bb5454f4cf013dbc8e70687a4fb26f90 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-16 10:11 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.144175e-02 | 99.87% |
| PSO | 500 | 7.075433e-17 | 99.99% |
| GLUE | 500 | 1.705726e-01 | 99.98% |
| Sobol | 500 | 3.215931e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
