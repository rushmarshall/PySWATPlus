<!-- fingerprint:ada65e4705dc5c84a0b77a232bdcd079 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-20 09:57 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.172053e-01 | 99.95% |
| PSO | 500 | 5.468977e-19 | 100.00% |
| GLUE | 500 | 1.566998e+00 | 99.99% |
| Sobol | 500 | 1.616808e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
