<!-- fingerprint:1bc88397421fec2f4e364a17b11ce9a0 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-14 09:51 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.604305e-01 | 99.99% |
| PSO | 500 | 8.770608e-20 | 100.00% |
| GLUE | 500 | 6.341012e-02 | 99.84% |
| Sobol | 500 | 1.565156e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
