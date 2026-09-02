<!-- fingerprint:eaa624b10c2974861c6d2405411abdc9 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-02 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.068177e-01 | 100.00% |
| PSO | 500 | 1.579237e-24 | 100.00% |
| GLUE | 500 | 1.034889e-01 | 99.71% |
| Sobol | 500 | 2.169350e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
