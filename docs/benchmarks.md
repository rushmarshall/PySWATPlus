<!-- fingerprint:7f38ef640251a5ecea94221f68edc28c -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-26 10:05 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.920297e-02 | 99.29% |
| PSO | 500 | 1.403693e-21 | 100.00% |
| GLUE | 500 | 2.294825e-01 | 99.99% |
| Sobol | 500 | 3.710159e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
