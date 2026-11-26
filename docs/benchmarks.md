<!-- fingerprint:184093e6a51cad83ddf64a4d277c0ebe -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-26 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.503801e-02 | 100.00% |
| PSO | 500 | 8.814879e-23 | 100.00% |
| GLUE | 500 | 5.916232e-01 | 99.73% |
| Sobol | 500 | 2.746941e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
