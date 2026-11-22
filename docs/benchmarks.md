<!-- fingerprint:a6284b9c68b8982a6726b36fa3891fed -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-22 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.293690e+00 | 99.98% |
| PSO | 500 | 3.032187e-19 | 100.00% |
| GLUE | 500 | 3.145339e-01 | 43.21% |
| Sobol | 500 | 1.979871e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
