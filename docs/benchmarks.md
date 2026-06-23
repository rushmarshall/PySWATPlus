<!-- fingerprint:0ccd4ef8fe84b7374f2d0b96af821055 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-23 10:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.489738e-01 | 99.98% |
| PSO | 500 | 5.116229e-21 | 100.00% |
| GLUE | 500 | 2.196068e-01 | 22.56% |
| Sobol | 500 | 2.239968e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
