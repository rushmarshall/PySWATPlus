<!-- fingerprint:4da75b2ed8e4796f5a906dd496dcb7f0 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-22 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.367629e-02 | 99.99% |
| PSO | 500 | 2.398768e-21 | 100.00% |
| GLUE | 500 | 8.197804e-01 | 100.00% |
| Sobol | 500 | 9.328816e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
