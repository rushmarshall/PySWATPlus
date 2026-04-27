<!-- fingerprint:eced2bf878c9c3dfbb7cb99a61107fc5 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-27 10:28 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.017557e-01 | 99.98% |
| PSO | 500 | 9.566523e-17 | 99.98% |
| GLUE | 500 | 1.527524e-01 | 99.80% |
| Sobol | 500 | 1.791445e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
