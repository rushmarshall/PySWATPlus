<!-- fingerprint:bc989453b36b23ec2bdc6412fda1bfbf -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-29 10:26 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.108169e+00 | 99.95% |
| PSO | 500 | 1.031538e-17 | 100.00% |
| GLUE | 500 | 1.826715e-01 | 99.85% |
| Sobol | 500 | 6.835757e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
