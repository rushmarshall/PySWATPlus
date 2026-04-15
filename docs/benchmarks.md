<!-- fingerprint:2a0d58a3428e6832a2d659b35fdf0ae7 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-15 10:12 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.358043e+00 | 99.98% |
| PSO | 500 | 1.152541e-17 | 100.00% |
| GLUE | 500 | 5.301359e-01 | 99.97% |
| Sobol | 500 | 4.132995e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
