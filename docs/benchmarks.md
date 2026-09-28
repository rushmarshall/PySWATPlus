<!-- fingerprint:915e141db31ca3f38aa87ed8f34b0abd -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-09-28 09:57 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.128644e-01 | 100.00% |
| PSO | 500 | 2.504111e-20 | 100.00% |
| GLUE | 500 | 1.205327e-01 | 99.99% |
| Sobol | 500 | 3.929611e-04 | 99.62% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
