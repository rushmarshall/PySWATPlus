<!-- fingerprint:3c51f6aff70a4b27e54575b385ebe3f4 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-17 10:12 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.074555e+00 | 99.96% |
| PSO | 500 | 5.076106e-18 | 100.00% |
| GLUE | 500 | 6.931378e-01 | 99.98% |
| Sobol | 500 | 1.923851e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
