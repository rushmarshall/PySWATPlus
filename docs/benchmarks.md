<!-- fingerprint:9776781fda09714800fcaaa71d56cd0c -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-10 10:12 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.602597e-01 | 100.00% |
| PSO | 500 | 4.481868e-22 | 100.00% |
| GLUE | 500 | 2.594966e+00 | 100.00% |
| Sobol | 500 | 1.062261e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
