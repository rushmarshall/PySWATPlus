<!-- fingerprint:278bf966c8de183c1de553615961fcb8 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-09 10:10 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.540993e-01 | 100.00% |
| PSO | 500 | 6.209062e-21 | 100.00% |
| GLUE | 500 | 1.182418e+00 | 98.83% |
| Sobol | 500 | 2.855958e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
