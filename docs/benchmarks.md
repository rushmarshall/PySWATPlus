<!-- fingerprint:79d669f2a17ca0efc5c13ec1739dc345 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-05 10:40 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.391639e-03 | 100.00% |
| PSO | 500 | 1.714993e-18 | 100.00% |
| GLUE | 500 | 7.613852e-01 | 99.78% |
| Sobol | 500 | 1.498096e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
