<!-- fingerprint:8ae8d0ad9449d261bac20ea3be6ba388 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-21 09:52 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.315866e-02 | 100.00% |
| PSO | 500 | 4.131954e-21 | 100.00% |
| GLUE | 500 | 3.776684e-01 | 100.00% |
| Sobol | 500 | 2.153117e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
