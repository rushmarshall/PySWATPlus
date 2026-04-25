<!-- fingerprint:88d85720c84c853a11903c4743103a91 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-04-25 10:04 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 9.592942e-02 | 99.97% |
| PSO | 500 | 1.316403e-19 | 100.00% |
| GLUE | 500 | 7.437256e-01 | 99.92% |
| Sobol | 500 | 2.504055e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
