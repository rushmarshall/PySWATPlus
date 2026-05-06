<!-- fingerprint:c3e453046c9743c19d3ecf85bb0fa3ea -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-06 10:29 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.316817e-01 | 100.00% |
| PSO | 500 | 2.975505e-19 | 100.00% |
| GLUE | 500 | 4.261745e-01 | 99.98% |
| Sobol | 500 | 3.913401e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
