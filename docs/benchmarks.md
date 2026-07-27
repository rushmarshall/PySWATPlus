<!-- fingerprint:669cda688f15a5b8e2bbe01e48e4381e -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-27 10:54 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.764583e+00 | 100.00% |
| PSO | 500 | 2.512173e-20 | 100.00% |
| GLUE | 500 | 4.622464e-02 | 99.66% |
| Sobol | 500 | 4.365138e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
