<!-- fingerprint:97bf941f3b3e9d0b084c610b9161a54f -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-17 10:00 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.767555e-01 | 100.00% |
| PSO | 500 | 5.662290e-23 | 100.00% |
| GLUE | 500 | 1.882465e-01 | 99.99% |
| Sobol | 500 | 3.496718e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
