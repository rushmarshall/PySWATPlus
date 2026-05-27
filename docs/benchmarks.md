<!-- fingerprint:debcfdcd30d0322b19a98137a2d4f5f3 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-27 11:01 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.719566e-01 | 99.98% |
| PSO | 500 | 3.282420e-20 | 100.00% |
| GLUE | 500 | 1.241430e-01 | 100.00% |
| Sobol | 500 | 6.495965e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
