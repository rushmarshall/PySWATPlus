<!-- fingerprint:ec58c61fb2d7cc1a81b89d43c9693978 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-01 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.709970e-02 | 99.32% |
| PSO | 500 | 5.148223e-22 | 100.00% |
| GLUE | 500 | 3.243968e-01 | 99.24% |
| Sobol | 500 | 1.513638e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
