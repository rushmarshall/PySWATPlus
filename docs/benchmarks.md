<!-- fingerprint:d6988ac854a43b14eded182e4f944736 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-19 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.294863e-01 | 100.00% |
| PSO | 500 | 9.295020e-20 | 100.00% |
| GLUE | 500 | 3.383467e+00 | 100.00% |
| Sobol | 500 | 2.544130e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
