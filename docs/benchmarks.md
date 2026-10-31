<!-- fingerprint:2c857d4b4a13944adf137dda963ae567 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-31 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.326376e-01 | 96.20% |
| PSO | 500 | 1.476292e-19 | 100.00% |
| GLUE | 500 | 2.077433e-02 | 99.92% |
| Sobol | 500 | 2.820560e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
