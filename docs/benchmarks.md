<!-- fingerprint:61f75bc278a28c1fba25379b29a59ddd -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-05 10:57 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.242974e-01 | 100.00% |
| PSO | 500 | 1.617355e-22 | 100.00% |
| GLUE | 500 | 2.382641e-02 | 99.99% |
| Sobol | 500 | 2.348935e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
