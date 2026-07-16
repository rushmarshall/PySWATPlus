<!-- fingerprint:4fe9db8fb49930cd1b43f21a620a65aa -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-16 10:25 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.055319e-01 | 99.97% |
| PSO | 500 | 9.614749e-21 | 100.00% |
| GLUE | 500 | 2.525549e-01 | 99.79% |
| Sobol | 500 | 1.269326e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
