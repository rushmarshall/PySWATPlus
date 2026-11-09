<!-- fingerprint:53da16ce90ade5b22810c93495bc50e7 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-09 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 9.342288e-02 | 99.83% |
| PSO | 500 | 4.782776e-22 | 100.00% |
| GLUE | 500 | 3.708739e-01 | 99.40% |
| Sobol | 500 | 4.277312e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
