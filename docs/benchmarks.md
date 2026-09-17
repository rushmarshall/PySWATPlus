<!-- fingerprint:b317a3da19361caf66b0fe4de5cbb58a -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-17 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.016454e-01 | 100.00% |
| PSO | 500 | 8.849856e-18 | 100.00% |
| GLUE | 500 | 4.150649e-01 | 99.78% |
| Sobol | 500 | 2.243007e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
