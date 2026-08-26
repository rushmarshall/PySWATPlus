<!-- fingerprint:9f1f783a621c7024a218155783e094d6 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-26 10:00 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.195786e+00 | 99.94% |
| PSO | 500 | 2.122452e-23 | 100.00% |
| GLUE | 500 | 5.526099e-02 | 99.02% |
| Sobol | 500 | 1.278751e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
