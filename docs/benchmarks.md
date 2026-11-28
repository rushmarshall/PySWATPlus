<!-- fingerprint:6d14e128f4a14e487bd1a2971c87e76b -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-28 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.003330e+01 | 99.99% |
| PSO | 500 | 1.715224e-19 | 100.00% |
| GLUE | 500 | 9.182790e-01 | 99.62% |
| Sobol | 500 | 1.430953e-02 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
