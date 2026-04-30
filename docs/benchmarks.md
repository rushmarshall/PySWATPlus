<!-- fingerprint:dc1953e5c446dd710e1afb1e64bd5bda -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-30 10:25 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 9.730138e-01 | 99.15% |
| PSO | 500 | 5.735796e-21 | 100.00% |
| GLUE | 500 | 1.954546e-03 | 100.00% |
| Sobol | 500 | 2.406129e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
