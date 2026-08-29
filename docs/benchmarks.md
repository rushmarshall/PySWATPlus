<!-- fingerprint:dfa4340fdc2b8eeaf20a099838574e53 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-08-29 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 6.465135e-01 | 99.91% |
| PSO | 500 | 1.737906e-19 | 100.00% |
| GLUE | 500 | 4.256535e-02 | 99.68% |
| Sobol | 500 | 4.589056e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
