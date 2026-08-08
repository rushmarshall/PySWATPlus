<!-- fingerprint:7a13e629053199379a075aec8f15ad6f -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-08 09:58 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.317938e-01 | 99.61% |
| PSO | 500 | 2.399975e-19 | 100.00% |
| GLUE | 500 | 6.332826e-01 | 60.75% |
| Sobol | 500 | 2.766769e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
