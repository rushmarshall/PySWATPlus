<!-- fingerprint:ad50bc908449ce1f4d6431def5e789b0 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-10 10:43 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.590144e-01 | 99.48% |
| PSO | 500 | 2.193618e-18 | 100.00% |
| GLUE | 500 | 2.061863e+00 | 99.99% |
| Sobol | 500 | 1.006098e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
