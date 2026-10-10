<!-- fingerprint:8e4eec2da937154097612bde7bb9ddf6 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-10 09:51 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.386749e-01 | 100.00% |
| PSO | 500 | 2.832418e-20 | 100.00% |
| GLUE | 500 | 9.292978e-02 | 100.00% |
| Sobol | 500 | 1.315217e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
