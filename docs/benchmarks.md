<!-- fingerprint:0d901fc822eb762f836e5ab7811d7025 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-12 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.173898e-01 | 100.00% |
| PSO | 500 | 3.646742e-21 | 100.00% |
| GLUE | 500 | 6.747435e-03 | 99.86% |
| Sobol | 500 | 2.644511e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
