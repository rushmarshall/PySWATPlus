<!-- fingerprint:0e9880f8d7bebc1d8f3f3ec64321e367 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-18 09:48 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.195473e-02 | 100.00% |
| PSO | 500 | 3.165064e-19 | 100.00% |
| GLUE | 500 | 3.308254e-01 | 98.53% |
| Sobol | 500 | 1.573545e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
