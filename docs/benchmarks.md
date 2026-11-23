<!-- fingerprint:6e3828945d27dc1554707cd25b46007e -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-23 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 4.774158e-01 | 100.00% |
| PSO | 500 | 2.349242e-21 | 100.00% |
| GLUE | 500 | 8.965684e-01 | 99.96% |
| Sobol | 500 | 8.817618e-05 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
