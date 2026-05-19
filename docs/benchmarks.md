<!-- fingerprint:48d5c0bf5a83e52bb00ff73e4259bdc2 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-19 10:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.089728e-01 | 100.00% |
| PSO | 500 | 2.743971e-21 | 100.00% |
| GLUE | 500 | 4.895897e-02 | 99.96% |
| Sobol | 500 | 1.743010e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
