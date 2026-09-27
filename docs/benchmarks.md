<!-- fingerprint:b357fd8da2d76bcacf1d560cfbe30963 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-27 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.206385e+00 | 100.00% |
| PSO | 500 | 1.891869e-16 | 100.00% |
| GLUE | 500 | 3.864269e-01 | 99.72% |
| Sobol | 500 | 1.849959e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
