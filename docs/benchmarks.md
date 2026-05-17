<!-- fingerprint:d827060bb840358974be7c0b17ba832e -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-17 10:14 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.671886e-02 | 99.99% |
| PSO | 500 | 4.936336e-22 | 100.00% |
| GLUE | 500 | 1.051308e+00 | 99.97% |
| Sobol | 500 | 4.374194e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
