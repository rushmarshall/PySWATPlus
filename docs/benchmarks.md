<!-- fingerprint:ed373359a2d3ad2e78b138861be498b5 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-05-25 11:11 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 2.737639e-02 | 100.00% |
| PSO | 500 | 7.442803e-21 | 100.00% |
| GLUE | 500 | 3.373023e-02 | 99.94% |
| Sobol | 500 | 5.968604e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
