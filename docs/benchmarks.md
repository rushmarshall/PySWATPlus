<!-- fingerprint:dbeafbd94ec54b3d398b0ae2ac291edd -->
# Calibration Algorithm Benchmarks

*Last updated: 2026-10-24 09:49 UTC*

Synthetic benchmark on the **Rosenbrock** test function f(x,y) = (1−x)² + 100·(y−x²)²  with random starting points.

| Algorithm | Iterations | Best Objective | Convergence Rate |
|-----------|-----------|----------------|------------------|
| DDS | 500 | 3.798902e-01 | 100.00% |
| PSO | 500 | 1.418100e-25 | 100.00% |
| GLUE | 500 | 4.535986e-01 | 92.65% |
| Sobol | 500 | 5.874301e-02 | 99.64% |

![Convergence plot](benchmark-convergence.png)

*Convergence rate = fraction of total improvement achieved in the first 20% of iterations.*
