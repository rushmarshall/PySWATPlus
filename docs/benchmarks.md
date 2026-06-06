<!-- fingerprint:60c4b328b94426774870502599ac2faa -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-06 10:28 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.833122e-01 | 95.68% |
| PSO | 500 | 1.293029e-21 | 100.00% |
| GLUE | 500 | 2.258197e-01 | 99.40% |
| Sobol | 500 | 4.698283e-02 | 99.63% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
