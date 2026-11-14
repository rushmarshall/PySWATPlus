<!-- fingerprint:ffea5d6d3932e985c8fee297aa8f55cb -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-11-14 09:50 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 8.711792e-03 | 100.00% |
| PSO | 500 | 5.194792e-23 | 100.00% |
| GLUE | 500 | 3.746518e-01 | 99.99% |
| Sobol | 500 | 2.176984e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
