<!-- fingerprint:57eeee34be157a7c4fe5fab196a16dbb -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-07 10:34 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.447559e+00 | 88.77% |
| PSO | 500 | 1.026089e-20 | 100.00% |
| GLUE | 500 | 5.644705e-02 | 99.99% |
| Sobol | 500 | 3.347278e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
