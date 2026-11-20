<!-- fingerprint:5043d6682cc6ec794d9cf6565da8ee11 -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-20 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.719462e-02 | 100.00% |
| PSO | 500 | 3.245482e-16 | 99.96% |
| GLUE | 500 | 1.105127e+00 | 99.71% |
| Sobol | 500 | 2.636004e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
