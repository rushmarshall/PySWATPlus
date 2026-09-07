<!-- fingerprint:8eefda5bdb9fe0e39722a26556018d1b -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-07 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.847061e-02 | 99.99% |
| PSO | 500 | 5.504572e-18 | 100.00% |
| GLUE | 500 | 1.201190e-01 | 98.96% |
| Sobol | 500 | 7.273502e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
