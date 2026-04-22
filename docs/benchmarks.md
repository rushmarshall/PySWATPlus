<!-- fingerprint:526cfb999b1ff14f315dc269f18e3d15 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-22 10:13 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.875329e-01 | 99.99% |
| PSO | 500 | 1.269566e-20 | 100.00% |
| GLUE | 500 | 6.008951e-02 | 95.13% |
| Sobol | 500 | 2.295777e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
