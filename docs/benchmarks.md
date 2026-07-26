<!-- fingerprint:a80d223ad68c452de4f0049d993a8d73 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-26 10:21 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.582443e+00 | 95.23% |
| PSO | 500 | 6.905178e-20 | 100.00% |
| GLUE | 500 | 4.969860e-01 | 99.78% |
| Sobol | 500 | 1.249096e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
