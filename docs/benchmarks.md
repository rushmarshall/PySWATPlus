<!-- fingerprint:2e4fc67207ca6f1c8c8ab7a92b745ff1 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-25 09:57 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 9.054816e-02 | 100.00% |
| PSO | 500 | 1.256966e-19 | 100.00% |
| GLUE | 500 | 1.580028e+00 | 99.99% |
| Sobol | 500 | 9.988661e-06 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
