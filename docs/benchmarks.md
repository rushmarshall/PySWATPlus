<!-- fingerprint:9dcaeaa3b0d5f429b8263b9b20dfdbf8 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-19 10:16 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.188451e-01 | 100.00% |
| PSO | 500 | 2.328419e-21 | 100.00% |
| GLUE | 500 | 3.983929e-01 | 99.99% |
| Sobol | 500 | 7.702354e-02 | 99.64% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
