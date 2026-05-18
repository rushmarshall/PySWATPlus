<!-- fingerprint:b1d1a4126c0c0f1069cb4b2cfef9a666 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-18 11:10 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.144928e+00 | 99.97% |
| PSO | 500 | 5.177809e-25 | 100.00% |
| GLUE | 500 | 1.296417e+00 | 97.03% |
| Sobol | 500 | 1.311552e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
