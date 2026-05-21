<!-- fingerprint:1cc7e4f334ff5d6ee1d072e8070acfdb -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-21 10:53 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.786793e-02 | 100.00% |
| PSO | 500 | 5.407537e-21 | 100.00% |
| GLUE | 500 | 2.424078e-01 | 100.00% |
| Sobol | 500 | 3.623705e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
