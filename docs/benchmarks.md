<!-- fingerprint:da812aaa19210a5b360bc3783c732269 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-14 10:33 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.305994e-01 | 100.00% |
| PSO | 500 | 8.855725e-21 | 100.00% |
| GLUE | 500 | 6.647644e-01 | 100.00% |
| Sobol | 500 | 3.010384e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
