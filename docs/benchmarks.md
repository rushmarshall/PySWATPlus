<!-- fingerprint:2e019c6610cbcaa7e935c147141dba3f -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-28 10:33 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.820659e-01 | 99.99% |
| PSO | 500 | 2.523612e-22 | 100.00% |
| GLUE | 500 | 1.039584e+00 | 99.97% |
| Sobol | 500 | 3.405651e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
