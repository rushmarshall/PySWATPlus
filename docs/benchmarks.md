<!-- fingerprint:db6bad9da45751ec53071914f3725436 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-02 11:13 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.325958e-01 | 99.97% |
| PSO | 500 | 2.459212e-20 | 100.00% |
| GLUE | 500 | 1.511901e-01 | 99.99% |
| Sobol | 500 | 1.631431e-06 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
