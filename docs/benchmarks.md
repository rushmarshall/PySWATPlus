<!-- fingerprint:5e82a572bf7096b974c789a78d7313c9 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-13 10:38 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.114635e+00 | 99.97% |
| PSO | 500 | 1.313625e-18 | 99.91% |
| GLUE | 500 | 9.772709e-01 | 100.00% |
| Sobol | 500 | 1.287195e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
