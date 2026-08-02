<!-- fingerprint:a6b470b9df5908660585ec78209a2257 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-02 10:19 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.158565e-01 | 99.99% |
| PSO | 500 | 1.362493e-19 | 99.99% |
| GLUE | 500 | 1.456153e-01 | 99.72% |
| Sobol | 500 | 1.317916e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
