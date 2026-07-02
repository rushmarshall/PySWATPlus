<!-- fingerprint:29ab5b1ce4f8ab715182d57d1cd97840 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-02 10:40 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 5.225905e-02 | 99.99% |
| PSO | 500 | 1.148450e-17 | 100.00% |
| GLUE | 500 | 4.803638e-01 | 100.00% |
| Sobol | 500 | 1.082333e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
