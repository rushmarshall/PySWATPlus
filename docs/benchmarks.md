<!-- fingerprint:d6ef66e81dca790eae51a97cbe52bf32 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-05 10:30 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.319498e-01 | 99.99% |
| PSO | 500 | 3.419584e-19 | 100.00% |
| GLUE | 500 | 3.587769e-02 | 99.98% |
| Sobol | 500 | 7.062764e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
