<!-- fingerprint:ab171f87eaa2c31116525be6bde28e63 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-06-15 11:43 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.130748e-01 | 100.00% |
| PSO | 500 | 3.864542e-20 | 100.00% |
| GLUE | 500 | 1.090492e+00 | 99.89% |
| Sobol | 500 | 2.057729e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
