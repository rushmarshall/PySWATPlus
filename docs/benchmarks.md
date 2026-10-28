<!-- fingerprint:c533196bbae7c5fa696be67946e910dd -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-28 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.483595e-01 | 100.00% |
| PSO | 500 | 5.074733e-19 | 100.00% |
| GLUE | 500 | 2.217617e-01 | 100.00% |
| Sobol | 500 | 4.769284e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
