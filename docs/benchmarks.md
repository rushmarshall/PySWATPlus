<!-- fingerprint:1e8c59a8bdc2ebb6ed26810b894eed17 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-09 13:53 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.037427e-03 | 100.00% |
| PSO | 500 | 8.063899e-20 | 100.00% |
| GLUE | 500 | 3.182625e-01 | 100.00% |
| Sobol | 500 | 2.842769e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
