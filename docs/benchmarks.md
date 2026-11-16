<!-- fingerprint:ac59b7a6d393e7cf0421fb3bb0cafd8a -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-16 09:52 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.400039e-02 | 100.00% |
| PSO | 500 | 3.623888e-18 | 100.00% |
| GLUE | 500 | 7.923070e-02 | 99.87% |
| Sobol | 500 | 1.578391e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
