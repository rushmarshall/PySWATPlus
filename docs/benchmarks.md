<!-- fingerprint:a4ec48f20e1cbea3b669d1659b73676a -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-20 09:52 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.548245e-02 | 100.00% |
| PSO | 500 | 5.609327e-15 | 99.98% |
| GLUE | 500 | 7.885278e-01 | 100.00% |
| Sobol | 500 | 4.942958e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
