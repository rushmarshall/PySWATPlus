<!-- fingerprint:546791ea7f401a2008878cf879a54046 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-22 10:33 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.378722e-01 | 99.39% |
| PSO | 500 | 1.347647e-22 | 100.00% |
| GLUE | 500 | 2.397724e-05 | 100.00% |
| Sobol | 500 | 1.105456e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
