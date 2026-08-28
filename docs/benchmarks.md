<!-- fingerprint:a10d2463ac7713b281331380248d76e8 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-28 13:41 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.302462e-01 | 100.00% |
| PSO | 500 | 1.424067e-19 | 100.00% |
| GLUE | 500 | 1.066351e-01 | 99.94% |
| Sobol | 500 | 1.929897e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
