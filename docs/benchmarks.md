<!-- fingerprint:d62e0e504901bd0e3c060a1ee2d99915 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-15 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.007423e-02 | 99.92% |
| PSO | 500 | 7.399340e-21 | 100.00% |
| GLUE | 500 | 3.480409e-01 | 100.00% |
| Sobol | 500 | 7.425505e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
