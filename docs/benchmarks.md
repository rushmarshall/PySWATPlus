<!-- fingerprint:813cdbf4b72eb99d285e3b397ca4af4e -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-07-21 10:33 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 1.939366e-02 | 99.96% |
| PSO | 500 | 9.460665e-21 | 100.00% |
| GLUE | 500 | 3.088081e-01 | 99.97% |
| Sobol | 500 | 2.160794e-03 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
