<!-- fingerprint:7a9a42c521f45919de4310903b07f4f7 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-23 10:34 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.579502e-01 | 100.00% |
| PSO | 500 | 3.858544e-21 | 100.00% |
| GLUE | 500 | 6.922642e-02 | 100.00% |
| Sobol | 500 | 1.251963e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
