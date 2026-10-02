<!-- fingerprint:95a0a839a79bc9a55aed493645319b49 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-02 09:52 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.495122e-01 | 100.00% |
| PSO | 500 | 9.789527e-20 | 100.00% |
| GLUE | 500 | 3.294247e-01 | 0.00% |
| Sobol | 500 | 2.246577e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
