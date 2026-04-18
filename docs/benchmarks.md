<!-- fingerprint:42ba9de5c454de0a8022f89e81766e24 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-18 10:02 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.699871e-01 | 99.82% |
| PSO | 500 | 1.195972e-18 | 100.00% |
| GLUE | 500 | 3.595408e-01 | 99.94% |
| Sobol | 500 | 8.896544e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
