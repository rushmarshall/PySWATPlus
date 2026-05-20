<!-- fingerprint:5ae365b5ef5f9feab500a5cb13c8c942 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-20 10:43 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 7.613838e-02 | 99.94% |
| PSO | 500 | 2.903694e-19 | 100.00% |
| GLUE | 500 | 1.110398e-01 | 99.99% |
| Sobol | 500 | 3.404745e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
