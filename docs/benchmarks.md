<!-- fingerprint:3b38c3567c660843536a73b37b13510e -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-01 11:40 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.207009e-02 | 100.00% |
| PSO | 500 | 2.340749e-20 | 100.00% |
| GLUE | 500 | 8.077124e-02 | 99.13% |
| Sobol | 500 | 8.461911e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
