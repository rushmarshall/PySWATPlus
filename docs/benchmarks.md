<!-- fingerprint:95369dacbb5b897bbcb2b035fb66b387 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-09 10:48 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.027734e+00 | 100.00% |
| PSO | 500 | 7.743944e-24 | 100.00% |
| GLUE | 500 | 1.376493e+00 | 99.98% |
| Sobol | 500 | 4.662570e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
