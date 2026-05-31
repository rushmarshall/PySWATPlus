<!-- fingerprint:f798fef478fa08a453a9401540d1c47c -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-31 10:28 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.814518e-01 | 100.00% |
| PSO | 500 | 1.651126e-24 | 100.00% |
| GLUE | 500 | 8.875545e-02 | 99.90% |
| Sobol | 500 | 5.381647e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
