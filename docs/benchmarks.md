<!-- fingerprint:83ced1b24b115441f6cd12f94a1a7ef8 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-17 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.325590e+00 | 99.92% |
| PSO | 500 | 2.308110e-19 | 100.00% |
| GLUE | 500 | 4.482710e-01 | 100.00% |
| Sobol | 500 | 1.610470e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
